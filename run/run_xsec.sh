hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files

hash=$(dasgoclient --query "file dataset=/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM" | tail -3)
files=$(echo $hash | sed 's/ /,/g')
cmsRun makeGenXsecAnalyzer_cfg.py inputFiles=$files
