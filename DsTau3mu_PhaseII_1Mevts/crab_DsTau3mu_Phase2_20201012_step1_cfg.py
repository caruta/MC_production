from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'DsToTauTo3Mu_Phase2_112X_mcRun4_realistic_v2_500kPerJob-GEN-SIM-DIGI-RAW'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'L1T-PhaseIITDRSpring19DR-step1_cfg.py'
config.Data.inputDataset = '/Pythia8_DsTau3Mu_Phase2_500kPerJob_GEN-SIM/caruta-DsToTauTo3Mu_Phase2_112X_mcRun4_realistic_v2_500kPerJob-893d5de68a0cb04501c1862902c63525/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 16000
config.Data.publication = True
config.Data.outputDatasetTag = 'DsToTauTo3Mu_Phase2_112X_mcRun4_realistic_v2_500kPerJob-GEN-SIM-DIGI-RAW'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
config.Site.ignoreGlobalBlacklist  = True
