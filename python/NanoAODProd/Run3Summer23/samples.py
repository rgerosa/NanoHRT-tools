def AddGluGluHToBBSamples(samples):

    samples['ggHto2B_PT-200_M-125'] = [
        '/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]

def AddGluGluHHTo4BSamples(samples):

    samples['ggHHto4B_kl-1p00_kt-1p00_c2-0p00'] = [
        '/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v3/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]

def AddQCDHTSamples(samples):
    samples['QCD-4Jets_HT-200to400'] = [
        '/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['QCD-4Jets_HT-400to600'] = [
        '/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v3/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['QCD-4Jets_HT-600to800'] = [
        '/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['QCD-4Jets_HT-800to1000'] = [
        '/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['QCD-4Jets_HT-1000to1200'] = [
        '/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['QCD-4Jets_HT-1200to1500'] = [
        '/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['QCD-4Jets_HT-1500to2000'] = [
        '/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v3/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['QCD-4Jets_HT-2000'] = [
        '/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]

def AddTopSamples(samples):
    samples['TTto4Q'] = [
        '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]

def AddVJetsSamples(samples):
    samples['Zto2Q-4Jets_HT-200to400'] = [
        '/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v1/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['Zto2Q-4Jets_HT-400to600'] = [
        '/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v1/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['Zto2Q-4Jets_HT-600to800'] = [
        '/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v1/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]
    samples['Zto2Q-4Jets_HT-800'] = [
        '/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v1/MINIAODSIM',
        ['isMC=True'],
        'EventAwareLumiBased',
        150000,
        ''
    ]

def AddDataSamples(samples):

    samples['JetMET0-Run2023C-v1'] = [
        '/JetMET0/Run2023C-22Sep2023_v1-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv1-22Sep2023'
    ]

    samples['JetMET1-Run2023C-v1'] = [
        '/JetMET1/Run2023C-22Sep2023_v1-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv1-22Sep2023'
    ]

    samples['JetMET0-Run2023C-v2'] = [
        '/JetMET0/Run2023C-22Sep2023_v2-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv2-22Sep2023'
    ]

    samples['JetMET1-Run2023C-v2'] = [
        '/JetMET1/Run2023C-22Sep2023_v2-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv2-22Sep2023'
    ]

    samples['JetMET0-Run2023C-v3'] = [
        '/JetMET0/Run2023C-22Sep2023_v3-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv3-22Sep2023'
    ]

    samples['JetMET1-Run2023C-v3'] = [
        '/JetMET1/Run2023C-22Sep2023_v3-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv3-22Sep2023'
    ]

    samples['JetMET0-Run2023C-v4'] = [
        '/JetMET0/Run2023C-22Sep2023_v4-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv4-22Sep2023'
    ]

    samples['JetMET1-Run2023C-v4'] = [
        '/JetMET1/Run2023C-22Sep2023_v4-v1/MINIAOD',
        ['isMC=False'],
        'LumiBased',
        50,
        'Run2023Cv4-22Sep2023'
    ]

def AddAllSamples(samples):
    AddGluGluHToBBSamples(samples)
    AddGluGluHHTo4BSamples(samples)
    AddQCDHTSamples(samples)
    AddTopSamples(samples)
    AddVJetsSamples(samples)
    AddDataSamples(samples)
