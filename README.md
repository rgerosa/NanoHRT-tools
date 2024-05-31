# NanoHRT-tools

### Set up CMSSW and offcial NanoAOD-tools

If you are not running from el8 or el9 machine please activate the CMSSW singularity containers via `cmssw-el8` or `cmss-el9`, respectively.

```bash
cmsrel CMSSW_13_0_18
cd CMSSW_13_0_18/src
cmsenv
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
```

### Get customized NanoAOD tools for HeavyResTagging (NanoHRT-tools) 

Clone the dev-Run3 branch which is also the default one in this forked repository

```bash
git clone https://github.com/colizz/NanoHRT-tools.git PhysicsTools/NanoHRTTools -b dev-Run3
```

### Compile

```bash
scram b -j 4
```

### Test

Instructions to run the nanoAOD postprocessor can be found at [nanoAOD-tools](https://github.com/cms-nanoAOD/nanoAOD-tools#nanoaod-tools). 

### Production

```bash
cd PhysicsTools/NanoHRTTools/run
```

##### Make trees to produce ntuples for heavy flavour tagging (bb/cc) measurement

```bash
python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2022preEE --sfbdt 0 -n 1
python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2022preEE --run-data --sfbdt 0 -n 1

python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2022postEE --sfbdt 0 -n 1
python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2022postEE --run-data --sfbdt 0 -n 1

python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2023preBPIX --sfbdt 0 -n 1
python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2023preBPIX --run-data --sfbdt 0 -n 1

python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2023postBPIX --sfbdt 0 -n 1
python runHeavyFlavTrees.py -o /eos/<some-eos-path-on-lxplus>/20230926_ULNanoV9 --jet-type ak8 --channel qcd --year 2023postBPIX --run-data --sfbdt 0 -n 1
```

where, `/eos/<some-eos-path-on-lxplus>/` is some path on EOS you have write access to.

Follow the instruction on screen to submit condor jobs. After all condor jobs finish, run the same command appended with ` --post`, to merge the trees.
