## STEP 1
cmsDriver.py Cosmics-fragment.py --python_filename Cosmics_step1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:Cosmic_step1.root --conditions 112X_mcRun3_2021cosmics_realistic_deco_v13 --step GEN,SIM --geometry DB:Extended --era Run3 --mc -n 1000000

## STEP 2
cmsDriver.py  --python_filename Cosmics_step2_cfg.py --eventcontent FEVTDEBUG --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI-RAW --fileout file:Cosmic_step2.root --conditions 112X_mcRun3_2021cosmics_realistic_deco_v13 --step DIGI,L1,DIGI2RAW,HLT:GRun --magField 0T --scenario cosmics --geometry DB:Extended --filein file:Cosmic_step1.root --era Run3 --mc -n -1

## STEP 3
cmsDriver.py  --python_filename Cosmics_step3_cfg.py --eventcontent FEVTDEBUG --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO --fileout file:Cosmic_step3.root --conditions 112X_mcRun3_2021cosmics_realistic_deco_v13 --step RAW2DIGI,L1Reco,RECO --magField 0T --scenario cosmics --geometry DB:Extended --filein file:Cosmic_step2.root --era Run3 --runUnscheduled --mc -n -1
