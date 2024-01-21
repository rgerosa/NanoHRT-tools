#!/bin/bash

workdir=`pwd`

echo `hostname`
echo "workdir: $workdir"
echo "args: $@"
ls -l

jobid=$1

source /cvmfs/cms.cern.ch/cmsset_default.sh

### --------------------------------###
# Insert MiniAOD->NanoAOD production from https://github.com/colizz/Customized_NanoAOD

if [ -d /afs/cern.ch/user/${USER:0:1}/$USER ]; then
  export HOME=/afs/cern.ch/user/${USER:0:1}/$USER
fi
export SCRAM_ARCH=slc7_amd64_gcc700
scram p CMSSW CMSSW_10_6_30
cd CMSSW_10_6_30/src
eval `scram runtime -sh`

git clone https://github.com/colizz/Customized_NanoAOD.git -b stable-202401 .
./PhysicsTools/NanoTuples/scripts/install_onnxruntime.sh
scram b clean && scram b -j4

mkdir -p $workdir/nano_output

# read the year condition
year=$(cat $workdir/heavyFlavSFTree_cfg.json | jq -r ".year")

# read the processed miniaod files
file_paths=$(cat $workdir/metadata.json | jq -r ".jobs[$jobid].inputfiles[]")
IFS=$'\n' read -r -d '' -a file_array <<< "$file_paths"

# run mini->nano step
for i in "${!file_array[@]}"; do

    filein=${file_array[i]}
    echo "Index: $i, File: $filein"

    # check if the file is MC or data
    if [[ $filein == "/store/mc"* ]]; then
        ismc=1
    elif [[ $filein == "/store/data"* ]]; then
        ismc=0
    else
        echo "Error: filein is neither in the form of /store/mc nor /store/data"
        exit 1
    fi

    # do cmsRun depending on the year condition and MC/data
    echo "Start MiniAOD->NanoAOD production"
    echo ">>> year=$year, ismc=$ismc"
    if [[ $year == "2018" && $ismc == 1 ]]; then
        cmsDriver.py test_nanoTuples --mc -n -1 --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeMC --filein $filein --fileout file:nano_$i.root || exit $? ;

    elif [[ $year == "2017" && $ismc == 1 ]]; then
        cmsDriver.py test_nanoTuples --mc -n -1 --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 106X_mc2017_realistic_v10 --step NANO --era Run2_2017,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeMC --filein $filein --fileout file:nano_$i.root || exit $? ;

    elif [[ $year == "2016" && $ismc == 1 ]]; then
        cmsDriver.py test_nanoTuples --mc -n -1 --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 106X_mcRun2_asymptotic_v17 --step NANO --era Run2_2016,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeMC --filein $filein --fileout file:nano_$i.root || exit $? ;

    elif [[ $year == "2015" && $ismc == 1 ]]; then
        cmsDriver.py test_nanoTuples --mc -n -1 --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step NANO --era Run2_2016_HIPM,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeMC --filein $filein --fileout file:nano_$i.root || exit $? ;

    elif [[ $year == "2018" && $ismc == 0 ]]; then
        cmsDriver.py test_nanoTuples --data -n -1 --eventcontent NANOAOD --datatier NANOAOD --conditions 106X_dataRun2_v37 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeData --filein $filein --fileout file:nano_$i.root || exit $? ;

    elif [[ $year == "2017" && $ismc == 0 ]]; then
        cmsDriver.py test_nanoTuples --data -n -1 --eventcontent NANOAOD --datatier NANOAOD --conditions 106X_dataRun2_v37 --step NANO --era Run2_2017,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeData --filein $filein --fileout file:nano_$i.root || exit $? ;

    elif [[ $year == "2016" && $ismc == 0 ]]; then
        cmsDriver.py test_nanoTuples --data -n -1 --eventcontent NANOAOD --datatier NANOAOD --conditions 106X_dataRun2_v37 --step NANO --era Run2_2016,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeData --filein $filein --fileout file:nano_$i.root || exit $? ;

    elif [[ $year == "2015" && $ismc == 0 ]]; then
        cmsDriver.py test_nanoTuples --data -n -1 --eventcontent NANOAOD --datatier NANOAOD --conditions 106X_dataRun2_v37 --step NANO --era Run2_2016_HIPM,run2_nanoAOD_106Xv2 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeData --filein $filein --fileout file:nano_$i.root || exit $? ;

    else
        echo "Error: year condition is not 2016APV, 2016, 2017, or 2018"
        exit 1
    fi

    mv nano_$i.root $workdir/nano_output
done

cd $workdir
rm -r CMSSW_10_6_30
### --------------------------------###

tar -xf CMSSW*.tar.gz --warning=no-timestamp

### --------------------------------###
#Keep track of release sandbox version
basedir=$PWD
rel=$(echo CMSSW_*)
arch=$(ls $rel/.SCRAM/|grep slc) || echo "Failed to determine SL release!"
old_release_top=$(awk -F= '/RELEASETOP/ {print $2}' $rel/.SCRAM/slc*/Environment) || echo "Failed to determine old releasetop!"
 
# Creating new release
# This is done so e.g CMSSW_BASE and other variables are not hardcoded to the sandbox setting paths
# which will not exist here
 
echo ">>> creating new release $rel"
mkdir tmp
cd tmp
export SCRAM_ARCH="$arch"
scramv1 project -f CMSSW $rel
new_release_top=$(awk -F= '/RELEASETOP/ {print $2}' $rel/.SCRAM/slc*/Environment)
cd $rel
echo ">>> preparing sandbox release $rel"
 
for i in biglib bin cfipython config external include lib python src; do
    rm -rf "$i"
    mv "$basedir/$rel/$i" .
done
 
 
echo ">>> fixing python paths"
for f in $(find -iname __init__.py); do
    sed -i -e "s@$old_release_top@$new_release_top@" "$f"
done
 
eval $(scramv1 runtime -sh) || echo "The command 'cmsenv' failed!"
cd "$basedir"
echo "[$(date '+%F %T')] wrapper ready"
### --------------------------------###

ls -l

export MLAS_DYNAMIC_CPU_ARCH=99
export TMPDIR=`pwd`
python processor.py $jobid
status=$?

ls -l

exit $status
