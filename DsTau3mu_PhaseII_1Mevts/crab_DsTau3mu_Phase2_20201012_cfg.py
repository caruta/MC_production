from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'DsToTauTo3Mu_Phase2_112X_mcRun4_realistic_v2_500kPerJob'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'L1T-PhaseIITDRSpring19GS-step0_cfg.py'
config.Data.outputPrimaryDataset = 'Pythia8_DsTau3Mu_Phase2_500kPerJob_GEN-SIM'
config.Data.splitting = 'EventBased'
config.JobType.eventsPerLumi = 500
config.Data.unitsPerJob = 500000
NJOBS = 5500
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.JobType.numCores = 4
config.JobType.maxMemoryMB = 8000
config.Data.publication = True
config.Data.outputDatasetTag = 'DsToTauTo3Mu_Phase2_112X_mcRun4_realistic_v2_500kPerJob'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
config.Site.ignoreGlobalBlacklist  = True
