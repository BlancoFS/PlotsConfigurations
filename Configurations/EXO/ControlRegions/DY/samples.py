# samples

#samples = {}

samples['DY']  = {    'name': [

	'latino_DYJetsToLL_M-50-LO-ext1_0000__part0.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0000__part1.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0000__part2.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0000__part3.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0000__part4.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0001__part0.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0001__part1.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0001__part2.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0001__part3.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0001__part4.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0002__part0.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0002__part1.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0002__part2.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0002__part3.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0002__part4.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0003__part0.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0003__part1.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0003__part2.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0003__part3.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0003__part4.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0004__part0.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0004__part1.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0004__part2.root',
	'latino_DYJetsToLL_M-50-LO-ext1_0004__part3.root',
                            ],    
                      'weight' : 'baseW*metFilter*puW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*((8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140))',  
                   }


# data driven
samples['Fake']  = {    'name': [
                      #
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/23JunFake/latino_DD_Run2016B_PromptReco_DoubleEG.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/23JunFake/latino_DD_Run2016B_PromptReco_MuonEG.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/23JunFake/latino_DD_Run2016B_PromptReco_SingleMuon.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/23JunFake/latino_DD_Run2016B_PromptReco_DoubleMuon.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/23JunFake/latino_DD_Run2016B_PromptReco_SingleElectron.root',
                       #             
                       '../../../../../../../eos/user/j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2016B_PromptReco_DoubleEG.root',
                       '../../../../../../../eos/user/j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2016B_PromptReco_MuonEG.root',
                       '../../../../../../../eos/user/j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2016B_PromptReco_SingleMuon.root',
                       '../../../../../../../eos/user/j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2016B_PromptReco_DoubleMuon.root',
                       '../../../../../../../eos/user/j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2016B_PromptReco_SingleElectron.root',
                       #
                       ],     
                      #'weight' : 'trigger*(fakeW2l0j*(njet==0)+fakeW2l1j*(njet==1)+fakeW2l2j*(njet>=2))',              #   weight/cut 
                      'weight' : '2.6/0.8*trigger*(fakeW2l0j*(njet==0)+fakeW2l1j*(njet==1)+fakeW2l2j*(njet>=2))',              #   weight/cut 
                      'isData': ['all'],                             
                  }

             
samples['top'] = {   'name': [
                           #'latino_TTJets.root',
                           'latino_TTTo2L2Nu_ext1__part0.root',
                           'latino_TTTo2L2Nu_ext1__part1.root',
                           'latino_TTTo2L2Nu_ext1__part2.root',
                           'latino_TTTo2L2Nu_ext1__part3.root',
                           'latino_TTTo2L2Nu_ext1__part4.root',
                           'latino_TTTo2L2Nu_ext1__part5.root',
                           'latino_TTTo2L2Nu_ext1__part6.root',
                           'latino_TTTo2L2Nu_ext1__part7.root',
                           'latino_TTTo2L2Nu_ext1__part8.root',
                           'latino_TTTo2L2Nu_ext1__part9.root',
                           #
                           'latino_ST_tW_antitop.root',
                           'latino_ST_tW_top.root'
                          ],          
                       'weight' : 'baseW*puW*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*GEN_weight_SM/abs(GEN_weight_SM)',    #   weight/cut 
                   }





             
samples['WW']  = {    'name': [
                                  'latino_WWTo2L2Nu.root'
                                ],      
                      'weight' : 'nllW*puW*baseW*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                      #'weights': ['abs(nllW)'] ,           
                  }


samples['ggWW']  = {    'name': ['latino_GluGluWWTo2L2Nu_MCFM.root'],      
                      'weight' : 'puW*baseW*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]',          
                      #'weights': ['abs(nllW)'] ,           
                      #'weights': ['1.000'] ,           
                      'isData': ['0'],                            
                  }



# during tree production: 1.4 k-factor has been applied to both samples
# ggWW sample: k = 1.4 +/- 15%
# ggWW interference: k = 1.87 +/- 25%



#samples['Vg']  = {    'name': ['latino_Wg_AMCNLOFXFX.root'],      
                      #'weight' : 'puW*baseW*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*GEN_weight_SM/abs(GEN_weight_SM)\
                                  #* !(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 )',
                                 ##*(!(Gen_ZGstar_MomStatus==44 && Gen_ZGstar_MomId==22))',
                      #'weights': ['1'] ,           
                      ##'isData': ['0'],                            
                  #}



samples['VgS']  = {    'name': [
                             'latino_WgStarLNuEE.root', 
                             'latino_WgStarLNuMuMu.root'
                             ],      
                      'weight' : 'puW*baseW*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*GEN_weight_SM/abs(GEN_weight_SM)',
                      'weights': ['1','1'] ,           
                  }

# 
# Wg* scale factor is
#
# 1.98 +/- 0.54    in mumumu
# 2.0  +/- 0.5     in emumu
#
#



samples['VZ']  = {    'name': [
                          'latino_WZ.root', 
                          #'latino_WZTo3LNu.root', 
                          #'latino_ZZ.root', # ---> replaced by inclusive samples
                          'latino_ZZTo2L2Nu.root',
                          #'latino_ZZTo2L2Q.root'
                          'latino_ZZTo2L2Q__part0.root',
                          'latino_ZZTo2L2Q__part1.root',
                          'latino_ZZTo2L2Q__part3.root',
                          
                          #'latino_ZZTo4L.root'
                         ], 
                      'weight' : 'puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]',          
                      #'weights': ['1'] ,           
                      #'isData': ['0'],                            
                  }



samples['VVV'] = {    'name': [
                          'latino_WZZ.root', 
                          'latino_ZZZ.root',
                          'latino_WWW.root',
                          'latino_WWZ.root',
                          ],      
                      'weight' : 'puW*baseW*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*GEN_weight_SM/abs(GEN_weight_SM)',          
                      #'isData': ['0'],                            
                  }

###########################################
###########################################
###########################################


samples['DATA']  = {   'name': [
                                #
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose16bis__hadd__l2tight/latino_Run2016B_PromptReco_DoubleEG.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose16bis__hadd__l2tight/latino_Run2016B_PromptReco_DoubleMuon.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose16bis__hadd__l2tight/latino_Run2016B_PromptReco_MuonEG.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose16bis__hadd__l2tight/latino_Run2016B_PromptReco_SingleElectron.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose16bis__hadd__l2tight/latino_Run2016B_PromptReco_SingleMuon.root',
                                #     
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2016B_PromptReco_DoubleEG.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2016B_PromptReco_DoubleMuon.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2016B_PromptReco_MuonEG.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2016B_PromptReco_SingleElectron.root',
                                #'../../../../../j/jlauwers/HWW2015/07Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2016B_PromptReco_SingleMuon.root',
                                #
                                '../../../../../j/jlauwers/HWW2015/21Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight/latino_Run2016B_PromptReco_DoubleEG.root',
                                '../../../../../j/jlauwers/HWW2015/21Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight/latino_Run2016B_PromptReco_DoubleMuon.root',
                                '../../../../../j/jlauwers/HWW2015/21Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight/latino_Run2016B_PromptReco_MuonEG.root',
                                '../../../../../j/jlauwers/HWW2015/21Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight/latino_Run2016B_PromptReco_SingleElectron.root',
                                '../../../../../j/jlauwers/HWW2015/21Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr__l2tight/latino_Run2016B_PromptReco_SingleMuon.root',
                                #
                                ] ,     
                       'weight' : 'trigger',
                       #'weight' : '1',
                       #'weight' : 'std_vector_trigger[1]',
                       'isData': ['all'],                            
                  }






