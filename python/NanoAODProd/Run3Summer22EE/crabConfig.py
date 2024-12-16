import os
from CRABClient.UserUtilities import config

### General options
config = config()
config.General.transferOutputs = True
config.General.transferLogs = False
### Job type setting
basepath = os.getenv('CMSSW_BASE')+'/src/PhysicsTools/NanoHRTTools/NanoAODProd/Run3Summer22EE/'
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = basepath+'/nanoaod_step.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 2500
config.JobType.numCores    = 2
## Data
config.Data.inputDBS      = 'phys03'
config.Data.outLFNDirBase = '/store/user/rgerosa/PrivateMC/Run3Summer22EENanoAODV12/'
config.Data.outputDatasetTag = 'NanoAODv12-130X'
config.Data.publication   = True
## Site
config.Site.storageSite   = 'T2_US_UCSD'

from PhysicsTools.NanoAODProd.Run3Summer22EE.NanoAODProd.samples import AddAllSamples
samples = {};
AddAllSamples(samples);
dset = os.getcwd().replace(os.path.dirname(os.getcwd())+'/','')
config.Data.inputDataset   = samples[dset][0]
config.Data.splitting      = samples[dset][2]
config.Data.unitsPerJob    = samples[dset][3]
params = samples[dset][1]
params.append('nThreads='+str(config.JobType.numCores)) ## this must match number of numCores option
config.JobType.pyCfgParams = params
print ("Submitting jobs with pyCfg parameters: "+" ".join(params));
