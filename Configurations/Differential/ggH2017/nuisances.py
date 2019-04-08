# nuisances
#FIXME: TO BE UPDATED FOR 2017!

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
mc.append('bbH_hww')
mc.append('WZgS_L')
signals.append('bbH_hww')

from LatinoAnalysis.Tools.HiggsXSection import *
HiggsXS = HiggsXSection()

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.023') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES

## FIXME: check the 30% lnN
nuisances['fake_syst_em'] = {
    'name': 'CMS_fake_syst_em_2017',
    'type': 'lnN',
    'samples': {},
    'samplespost': (lambda self, samples: {'Fake_em': '1.3'}),
    'perRecoBin': True
}

nuisances['fake_syst_me'] = {
    'name': 'CMS_fake_syst_me_2017',
    'type': 'lnN',
    'samples': {},
    'samplespost': (lambda self, samples: {'Fake_me': '1.3'}),
    'perRecoBin': True
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    },
    'samplespost': (lambda self, samples: {'Fake_em': self['samples']['Fake']}),
    #'AsLnN': '1'
    'perRecoBin': True
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    },
    'samplespost': (lambda self, samples: {'Fake_em': self['samples']['Fake']}),
    #'AsLnN': '1'
    'perRecoBin': True
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    },
    'samplespost': (lambda self, samples: {'Fake_me': self['samples']['Fake']}),
    #'AsLnN': '1'
    'perRecoBin': True
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    },
    'samplespost': (lambda self, samples: {'Fake_me': self['samples']['Fake']}),
    #'AsLnN': '1'
    'perRecoBin': True
}

##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    nuisances['btag_shape_%s' % shift] = {
        'name': 'CMS_btag_%s_2017' % shift,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
        'cutspost': (lambda self, cuts: [cut for cut in cuts if '_top_' not in cut])
    }

    nuisances['btag_shape_%s_top' % shift] = {
        'name': 'CMS_btag_%s_topCR_2017' % shift,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
        'cuts': [cut for cut in cuts if '_CR_' in cut],
        'cutspost': (lambda self, cuts: [cut for cut in cuts if '_top_' in cut]),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup'),
    'folderDown': makeMCDirectory('ElepTdo'),
    'AsLnN': '1'
}

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup'),
    'folderDown': makeMCDirectory('MupTdo'),
    'AsLnN': '1'
}

##### Jet energy scale

nuisances['jes'] = {
    'name': 'CMS_scale_j_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('JESup'),
    'folderDown': makeMCDirectory('JESdo'),
    'AsLnN': '1'
}

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup'),
    'folderDown': makeMCDirectory('METdo'),
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_DY_' not in cut]),
    'AsLnN': '1'
}

nuisances['met_DY'] = {
    'name': 'CMS_scale_met_DYCR_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup'),
    'folderDown': makeMCDirectory('METdo'),
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_DY_' in cut]),
    'AsLnN': '1'
}

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
        'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
        'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
}


##### PS and UE

# Scales are used to normalize the PS variation to the same integral as the nominal after the wwSel skim
nuisances['PS']  = {
    'name': 'PS',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WW': ['PSWeight[0]', 'PSWeight[3]'],
        #'ggH_hww': ['PSWeight[0]', 'PSWeight[3]'],
        #'qqH_hww': ['PSWeight[0]', 'PSWeight[3]']
    },
    'AsLnN': '1',
    #'symmetrize': True
}

# Scales are used to normalize the UE up/down variations to the same integral as the nominal after the wwSel skim
#'WW'      : ['1.12720771849', '1.13963144574'],
#'ggH_hww' : ['1.00211385568', '0.994966378288'], 
#'qqH_hww' : ['1.00367895901', '0.994831373195']

nuisances['UE'] = {
    'name': 'UE', 
    'skipCMS': 1,
    'kind': 'tree',
    'type': 'shape',
    'samples': {
        'WW'      : ['1', '1'],
        'ggH_hww' : ['1', '1'],
        'qqH_hww' : ['1', '1']
    },
    'AsLnN': '1',
    'folderUp': makeMCDirectory('UEup'),
    'folderDown': makeMCDirectory('UEdo')
}

####### Generic "cross section uncertainties"

apply_on = {
    'top': [
        '(( (topGenPt>0 && antitopGenPt<0) || (topGenPt<0 && antitopGenPt>0)  ) * 1.0816 + ( topGenPt>0 && antitopGenPt>0 ))',
        '(( (topGenPt>0 && antitopGenPt<0) || (topGenPt<0 && antitopGenPt>0)  ) * 0.9184 + ( topGenPt>0 && antitopGenPt>0 ))'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.","((1./Top_pTrw - 1)*(topGenPt>0 && antitopGenPt>0) + 1)"]},
    'symmetrize': True
}

###### pdf uncertainties

valuesggh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH','125.09','pdf','sm')
valuesggzh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.09','pdf','sm')
valuesbbh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','bbH','125.09','pdf','sm')

nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        'ggH_hww': valuesggh,
        'ggH_htt': valuesggh,
        'ggZH_hww': valuesggzh,
        'bbH_hww': valuesbbh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ttH','125.09','pdf','sm')

nuisances['pdf_Higgs_ttH'] = {
    'name': 'pdf_Higgs_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

valuesqqh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.09','pdf','sm')
valueswh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.09','pdf','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.09','pdf','sm')

nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        'qqH_hww': valuesqqh,
        'qqH_htt': valuesqqh,
        'WH_hww': valueswh,
        'WH_htt': valueswh,
        'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
}

#FIXME: check this 4%
nuisances['pdf_qqbar'] = {
    'name': 'pdf_qqbar',
    'type': 'lnN',
    'samples': {
        'Vg': '1.04',
        'VZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'WZgS_L': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
        'WZgS_H': '1.04' # PDF: 0.0064 / 0.1427 = 0.0448493
    },
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        'ggH_hww': '1.005',
        'ggH_htt': '1.005',
        'ggZH_hww': '1.005',
        'bbH_hww': '1.005'
    },
    'type': 'lnN',
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_gg_ACCEPT'] = {
    'name': 'pdf_gg_ACCEPT',
    'samples': {
        'ggWW': '1.005',
    },
    'type': 'lnN',
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_Higgs_qqbar_ACCEPT'] = {
    'name': 'pdf_Higgs_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_hww': '1.011',
        'qqH_htt': '1.011',
        'WH_hww': '1.007',
        'WH_htt': '1.007',
        'ZH_hww': '1.012',
        'ZH_htt': '1.012',
    },
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_qqbar_ACCEPT'] = {
    'name': 'pdf_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'VZ': '1.005',
    },
}

##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)
# [0] is muR=0.50000E+00 muF=0.50000E+00
# [8] is muR=0.20000E+01 muF=0.20000E+01
nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {'DY': ['LHEScaleWeight[8]', 'LHEScaleWeight[0]']},
    'AsLnN': '1'
}

#FIXME: check this 3%
nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'type': 'lnN',
    'samples': {
        'Vg': ['LHEScaleWeight[8]', 'LHEScaleWeight[0]'],
        'VZ': ['LHEScaleWeight[8]', 'LHEScaleWeight[0]'],
        'WZgS_L': ['LHEScaleWeight[8]', 'LHEScaleWeight[0]'],
        'WZgS_H': ['LHEScaleWeight[8]', 'LHEScaleWeight[0]']
    }
}

# ggww and interference
nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    },
}

# NLL resummation variations
nuisances['Resumscale_WW'] = {
    'name': 'CMS_hww_WWresum',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WW': ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
    },
    'perRecoBin': True
}

nuisances['QCDscale_WW'] = {
    'name': 'CMS_hww_WWqscale',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
      'WW': ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
    'perRecoBin': True
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_DY'] = {
    'name': 'CMS_hww_CRSR_accept_DY',
    'type': 'lnN',
    #'samples': {'DY': '1.02'},
    'samples': {'DY': '1.1'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_DY_' in cut and cut in self['cuts']]),
    'perRecoBin': True
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_top'] = {
    'name': 'CMS_hww_CRSR_accept_top',
    'type': 'lnN',
    'samples': {'top': '1.05'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_top_' in cut and cut in self['cuts']]),
    'perRecoBin': True
}

# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop
#
#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools

thus = [
    ('THU_ggH_Mu', 'ggH_mu'),
    ('THU_ggH_Res', 'ggH_res'),
    ('THU_ggH_Mig01', 'ggH_mig01'),
    ('THU_ggH_Mig12', 'ggH_mig12'),
    ('THU_ggH_VBF2j', 'ggH_VBF2j'),
    ('THU_ggH_VBF3j', 'ggH_VBF3j'),
    ('THU_ggH_PT60', 'ggH_pT60'),
    ('THU_ggH_PT120', 'ggH_pT120'),
    ('THU_ggH_qmtop', 'ggH_qmtop')
]

for name, vname in thus:
    updown = [vname, '2.-%s' % vname]
    
    nuisances[name] = {
        'name': name,
        'skipCMS': 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
          'ggH_hww': updown,
          #'ggH_htt': updown
        }
    }

#### QCD scale uncertainties for Higgs signals other than ggH

values = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.09','scale','sm')

nuisances['QCDscale_qqH'] = {
    'name': 'QCDscale_qqH', 
    'samples': {
        'qqH_hww': values,
        'qqH_htt': values
    },
    'type': 'lnN'
}

valueswh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.09','scale','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.09','scale','sm')

nuisances['QCDscale_VH'] = {
    'name': 'QCDscale_VH', 
    'samples': {
        'WH_hww': valueswh,
        'WH_htt': valueswh,
        'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.09','scale','sm')

nuisances['QCDscale_ggZH'] = {
    'name': 'QCDscale_ggZH', 
    'samples': {
        'ggZH_hww': values
    },
    'type': 'lnN',
}

#values = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','bbH','125.09','scale','sm')
#
#nuisances['QCDscale_bbH'] = {
#  'name': 'QCDscale_bbH',
#  'samples': {
#    'bbH_hww': values
#  },
#  'type': 'lnN',
#}

values = HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ttH','125.09','scale','sm')

nuisances['QCDscale_ttH'] = {
    'name': 'QCDscale_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

nuisances['QCDscale_WWewk'] = {
    'name': 'QCDscale_WWewk',
    'samples': {
        'WWewk': '1.11',
    },
    'type': 'lnN'
}


#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_qqbar_ACCEPT'] = {
    'name': 'QCDscale_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_hww': '1.007',
        'qqH_htt': '1.007',
        'WH_hww': '1.05',
        'WH_htt': '1.05',
        'ZH_hww': '1.04',
        'ZH_htt': '1.04',
        'VZ': '1.029',
    }
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_gg_ACCEPT'] = {
    'name': 'QCDscale_gg_ACCEPT',
    'samples': {
        'ggH_hww': '1.027',
        'ggH_htt': '1.027',
        'ggZH_hww': '1.027',
        'ggWW': '1.027',
    },
    'type': 'lnN',
}

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '1',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}

#mynuisances = {}
#mynuisances['electronpt'] = nuisances['electronpt']
#mynuisances['lumi'] = nuisances['lumi']
#nuisances = mynuisances

for n in nuisances.values():
    n['skipCMS'] = 1

#nuisances = {}
