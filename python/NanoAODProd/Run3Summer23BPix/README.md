# NanoAODv12 production

## Preparation of release with GloParT in 13X

```sh
cmsrel CMSSW_13_0_18;
cd CMSSW_13_0_18/src;
cmsenv;
git-cms-init;
git-cms-addpkg RecoBTag/FeatureTools
git-cms-addpkg RecoBTag/ONNXRuntime
git-cms-addpkg PhysicsTools/NanoAOD
```

Copy relevant files from this PR [https://github.com/cms-sw/cmssw/pull/46523/](https://github.com/cms-sw/cmssw/pull/46523/).

## Generation of configuration file

Start from miniAOD data tier produced earlier

* **NANOAOD STEP**: [nanoaod_step.py](./nanoaod_step.py) is used to produce NANOAODSIM from MINIAODSIM. Configurable parameters are:
  * `nThreads`: number of parallel threads
  * `inputFiles`: name of the input files containing RECO events
  * `outputName`: name of the output MINIAOD file to be produced

* **CRAB configuration**: [crabConfig.py](./crabConfig.py) is the crab configuration file needed for the production containing the following informations
  * Configuration descriptor indicating base parameters for the crab production for each dataset [samples.py](./samples.py)
  * Output storage element and path needed for the publication of miniAOD

* **CRAB production submission**: eventually the submission of the CRAB production is performed by using [createCrabJob.py](../../createCrabJob.py) as follows

  ```sh
  cd $CMSSW_BASE/src/hh4banalysis/mcgeneration/python
  cmsenv
  python3 createCrabJob.py -s Run3Summer22EE/NanoAODProd/samples.py -t All -c  Run3Summer22EE/NanoAODProd/crabConfig.py -j ../crab_jobs/Run3Summer22EENanoProd/ -m submit
  ```

