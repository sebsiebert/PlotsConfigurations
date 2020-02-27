# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()
#
#
# cutdict = {
#     'vbf': [
#         'BoostedSB_vbf', 'BoostedSR_vbf', 'BoostedTopCR_vbf',
#         'ResolvedSB_vbf', 'ResolvedSR_vbf', 'ResolvedTopCR_vbf'
#     ]
#     'top': [
#         'BoostedTopCR', 'ResolvedTopCR'
#     ]
# }
#
#
#
################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi'] = {
   'name': 'lumi_13TeV_2016',
   'type': 'lnN',
   # FIXME: also WWewk and ggWW excluded?
   'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

##############################################################################################

# ##### B-tagger
# for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
#     btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]
#
#     name = 'btag_%s' % shift
#     if 'stats' in shift:
#         name += '_2016'
#
#     nuisances['btag_shape_%s' % shift] = {
#         'name': name,
#         'kind': 'weight',
#         'type': 'shape',
#         'samples': dict((skey, btag_syst) for skey in mc),
#     }




##### Trigger Efficiency
# TODO can this be taken 1 to 1 from two leptonic?
# trig_syst = ['((TriggerEffWeight_1l_u)/(TriggerEffWeight_1l))*(TriggerEffWeight_1l>0.02) + (TriggerEffWeight_1l<=0.02)', '(TriggerEffWeight_1l_d)/(TriggerEffWeight_1l)']
#
# nuisances['trigg'] = {
#     'name': 'eff_hwwtrigger_2016',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': dict((skey, trig_syst) for skey in mc)
# }

##### Electron Efficiency and energy scale

# nuisances['eff_e'] = {
#     'name': 'eff_e_2016',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
# }

# TODO
# nuisances['electronpt'] = {
#     'name': 'scale_e_2016',
#     'type': 'shape',
#     'kind': 'suffix',
#     'mapUp':   'ElepTup',
#     'mapDown': 'ElepTdo',
#     'folderUp':   makeMCDirectory('ElepTup_suffix'),
#     'folderDown': makeMCDirectory('ElepTdo_suffix'),
#     'samples': dict((skey, ['1', '1']) for skey in mc),
#     # 'AsLnN': '1' #FIXME: obsolete?
# }

##### Muon Efficiency and energy scale

# nuisances['eff_m'] = {
#     'name': 'eff_m_2016',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
# }

# TODO
# nuisances['muonpt'] = {
#     'name': 'scale_m_2016',
#     'type': 'shape',
#     'kind': 'suffix',
#     'mapUp':   'MupTup',
#     'mapDown': 'MupTdo',
#     'folderUp':   makeMCDirectory('MupTup_suffix'),
#     'folderDown': makeMCDirectory('MupTdo_suffix'),
#     'samples': dict((skey, ['1', '1']) for skey in mc),
#     # 'AsLnN': '1'
# }


##### Jet energy scale
# TODO
# nuisances['jes'] = {
#     'name': 'scale_j_2016',
#     'type': 'shape',
#     'kind': 'suffix',
#     'mapUp':   'JESup',
#     'mapDown': 'JESdo',
#     'folderUp':   makeMCDirectory('JESup_suffix'),
#     'folderDown': makeMCDirectory('JESdo_suffix'),
#     'samples': dict((skey, ['1', '1']) for skey in mc),
#     # 'AsLnN': '1'
# }


##### MET energy scale
# TODO
# nuisances['met'] = {
#     'name': 'scale_met_2016',
#     'type': 'shape',
#     'kind': 'suffix',
#     'mapUp':   'METup',
#     'mapDown': 'METdo',
#     'folderUp':   makeMCDirectory('METup_suffix'),
#     'folderDown': makeMCDirectory('METdo_suffix'),
#     'samples': dict((skey, ['1', '1']) for skey in mc),
#     'AsLnN': '1'
# }



##### Pileup

nuisances['PU'] = {
    'name': 'PU_2016',
    'type': 'shape',
    'kind': 'weight',
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
# TODO: update https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/Template/nuisances_2016.py
# psweights = ['PSWeight[0]', 'PSWeight[1]', 'PSWeight[2]', 'PSWeight[3]']
#
# nuisances['PS']  = {
#     'name': 'PS',
#     'type': 'shape',
#     'kind': 'weight_envelope',
#     'samples': {
#         'WW': psweights,
#     },
#     'AsLnN': '1'
# }
# for MX in massggh:
#     nuisances['PS']['samples']['ggHWWlnuqq_M'+str(MX)] = psweights
# for MX in massvbf:
#     nuisances['PS']['samples']['qqHWWlnuqq_M'+str(MX)] = psweights

#TODO
#FIXME normalization factors need to be recomputed for 2016
# FIXME: HIGH MASS
# nuisances['UE']  = {
#                 'name'  : 'UE_CP5',
#                 'skipCMS' : 1,
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp':   'UEup',
#                 'mapDown': 'UEdo',
#                 'folderUp':   makeMCDirectory('UEup_suffix'),
#                 'folderDown': makeMCDirectory('UEdo_suffix'),
#                 'samples'  : {
#                  'WW'      : ['1.12720771849', '1.13963144574'],
#                 },
#                 # 'AsLnN'      : '1',
#                 'synchronized': False # TODO understand
# }
# for MX in massggh:
#     # FIXME: is this right, same weights for all masses? given weights are taken from SM
#     nuisances['UE']['samples']['ggHWWlnuqq_M'+str(MX)] = ['1.00211385568', '0.994966378288']
# for MX in massvbf:
#     nuisances['UE']['samples']['qqHWWlnuqq_M'+str(MX)] = ['1.00367895901', '0.994831373195']


####### Generic "cross section uncertainties"

apply_on = {
    'top': [
        'isSingleTop * 1.0816 + isTTbar',
        'isSingleTop * 0.9184 + isTTbar'
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
    'name': 'topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True
}




###############################################################################################






nuisances['VgStar'] = {
    'name': 'hww_VgStarScale',
    'type': 'lnN',
    'samples': {
        'VgS_L': '1.25'
    }
}

# FIXME: is this right?
nuisances['VZ'] = {
    'name': 'hww_VZScale',
    'type': 'lnN',
    'samples': {
        'VZ': '1.16' # TODO: should this be VgS_H instead of VZ?
    }
}

###### pdf uncertainties

valuesggh  = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH', '125.09','pdf','sm')
valuesggzh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm')
valuesbbh  = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH', '125.09','pdf','sm')

nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        'ggH_hww' : valuesggh,
        # 'ggH_htt' : valuesggh,
        # 'ggZH_hww': valuesggzh,
        # 'bbH_hww' : valuesbbh # FIXME: included in QCDscale?
    },
    'type': 'lnN',
}
for m in massggh:
    # FIXME: sample names (everywhere actually)
    values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(m),'pdf','bsm')
    nuisances['pdf_Higgs_gg']['samples'].update({'GGH_'+m: values})
    nuisances['pdf_Higgs_gg']['samples'].update({'GGHSBI_'+m: values})
    nuisances['pdf_Higgs_gg']['samples'].update({'MSSMGGH_'+m: values})
    nuisances['pdf_Higgs_gg']['samples'].update({'MSSMGGHSBI_'+m: values})



valuesqqh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm')
valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','pdf','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','pdf','sm')

nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        'qqH_hww': valuesqqh,
        # 'qqH_htt': valuesqqh,
        'WH_hww': valueswh,
        # 'WH_htt': valueswh,
        'ZH_hww': valueszh,
        # 'ZH_htt': valueszh
    },
}
for m in massvbf:
    values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(m),'bsm')
    nuisances['pdf_Higgs_qqbar']['samples'].update({'QQH_'+m: values})
    nuisances['pdf_Higgs_qqbar']['samples'].update({'QQHSBI_'+m: values})
    nuisances['pdf_Higgs_qqbar']['samples'].update({'MSSMQQH_'+m: values})
    nuisances['pdf_Higgs_qqbar']['samples'].update({'MSSMQQHSBI_'+m: values})



values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')

nuisances['pdf_Higgs_ttH'] = {
    'name': 'pdf_Higgs_ttH',
    'samples': {
        # 'ttH_hww': values
    },
    'type': 'lnN',
}


#FIXME: check this 4%
nuisances['pdf_qqbar'] = {
    'name': 'pdf_qqbar',
    'type': 'lnN',
    'samples': {
        'Vg': '1.04',
        'VZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'VgS': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
    },
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        'ggH_hww': '1.005',
        # 'ggH_htt': '1.005',
        # 'ggZH_hww': '1.005',
        # 'bbH_hww': '1.005'
    },
    'type': 'lnN',
}
for m in massggh:
    if int(m)<1500:
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'GGH_'+m+model_name:'1.007'})
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'GGHSBI_'+m+model_name:'1.010'})
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'MSSMGGH_'+m:'1.007'})
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'MSSMGGHSBI_'+m:'1.010'})
    elif int(m)>1499:
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'GGH_'+m+model_name:'1.012'})
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'GGHSBI_'+m+model_name:'1.035'})
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'MSSMGGH_'+m:'1.012'})
        nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'MSSMGGHSBI_'+m:'1.035'})

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
        # 'qqH_htt': '1.011',
        'WH_hww': '1.007',
        # 'WH_htt': '1.007',
        # 'ZH_hww': '1.012',
        # 'ZH_htt': '1.012',
    },
}
for m in massvbf:
    if int(m)<1000:
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'QQH_'+m+model_name:'1.005'})
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'QQHSBI_'+m+model_name:'1.005'})
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'MSSMQQH_'+m:'1.005'})
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'MSSMQQHSBI_'+m:'1.005'})
    elif int(m)>999:
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'QQH_'+m+model_name:'1.015'})
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'QQHSBI_'+m+model_name:'1.015'})
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'MSSMQQH_'+m:'1.015'})
      nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'MSSMQQHSBI_'+m:'1.015'})




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
# [1] is muR=0.50000E+00 muF=0.10000E+01
# [2] is muR=0.50000E+00 muF=0.20000E+01
# [3] is muR=0.10000E+01 muF=0.50000E+00
# [4] is muR=0.10000E+01 muF=0.10000E+01
# [5] is muR=0.10000E+01 muF=0.20000E+01
# [6] is muR=0.20000E+01 muF=0.50000E+00
# [7] is muR=0.20000E+01 muF=0.10000E+01
# [8] is muR=0.20000E+01 muF=0.20000E+01

variations = ['LHEScaleWeight[%d]' % i for i in [0, 1, 3, 5, 7, 8]]

nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'DY': variations},
    'AsLnN': '1'
}
# FIXME: not LHEScaleWeight missing apparently
nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'Vg': variations,
        # 'VZ': variations, # not all included VZ samples have LHEScaleWeight
        'VgS': variations
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

# TODO: what about these? Template only has split into num  of jets https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/Template/nuisances_2016.py
# nllW missing, what is this
# nuisances['WWresum']  = {
#   'name'  : 'hww_WWresum',
#   'skipCMS' : 1,
#   'kind'  : 'weight',
#   'type'  : 'shape',
#   'samples'  : {
#      'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
#    },
#   'cutspost'  : lambda self, cuts: [cut for cut in cuts]
# }
#
# nuisances['WWqscale']  = {
#    'name'  : 'hww_WWqscale',
#    'skipCMS' : 1,
#    'kind'  : 'weight',
#    'type'  : 'shape',
#    'samples'  : {
#       'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'], #FIME: nllW_Qup not existing
#     },
#    'cutspost'  : lambda self, cuts: [cut for cut in cuts]
# }



# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_SB'] = {
    'name': 'hww_CRSR_accept_SB',
    'type': 'lnN',
    'samples': {'Wjets': '1.02'}, # TODO what value does this have to be?
    #'samples': {'DY': '1.1'},
    'cuts': [cut for cut in cuts if 'SB' in cut],
    #'cutspost': (lambda self, cuts: [cut for cut in cuts if '_DY_' in cut and cut in self['cuts']]),
    'cutspost': (lambda self, cuts: [cut for cut in cuts if 'SB' in cut]),
    #'perRecoBin': True
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_top'] = {
    'name': 'hww_CRSR_accept_top',
    'type': 'lnN',
    'samples': {'top': '1.01'},
    #'samples': {'top': '1.05'},
    'cuts': [cut for cut in cuts if 'TopCR' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if 'TopCR' in cut]),
}

# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop
#
#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools
# TODO: everything and high mass
# thus = [
#     ('THU_ggH_Mu', 'ggH_mu'),
#     ('THU_ggH_Res', 'ggH_res'),
#     ('THU_ggH_Mig01', 'ggH_mig01'),
#     ('THU_ggH_Mig12', 'ggH_mig12'),
#     ('THU_ggH_VBF2j', 'ggH_VBF2j'),
#     ('THU_ggH_VBF3j', 'ggH_VBF3j'),
#     ('THU_ggH_PT60', 'ggH_pT60'),
#     ('THU_ggH_PT120', 'ggH_pT120'),
#     ('THU_ggH_qmtop', 'ggH_qmtop')
# ]
#
# for name, vname in thus:
#     updown = [vname, '2.-%s' % vname]
#
#     nuisances[name] = {
#         'name': name,
#         'skipCMS': 1,
#         'kind': 'weight',
#         'type': 'shape',
#         'samples': {
#           'ggH_hww': updown,
#           'ggH_htt': updown
#         }
#     }






#### QCD scale uncertainties for Higgs signals other than ggH
# TODO: high mass
values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm')

nuisances['QCDscale_qqH'] = {
    'name': 'QCDscale_qqH',
    'samples': {
        'qqH_hww': values,
        'qqH_htt': values
    },
    'type': 'lnN'
}

valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm')

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

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm')

nuisances['QCDscale_ggZH'] = {
    'name': 'QCDscale_ggZH',
    'samples': {
        'ggZH_hww': values
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm')

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
        'VZ': '1.029', # this shouldn't be here because we have full shape-based uncertainty for VZ
    }
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_gg_ACCEPT'] = {
    'name': 'QCDscale_gg_ACCEPT',
    'samples': {
        'ggH_hww': '1.027', # shouldn't be here
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
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}

# ##rate parameters
# nuisances['DYttnorm0j']  = {
#                'name'  : 'hww_DYttnorm0j',
#                'samples'  : {
#                    'DY' : '1.00',
#                    },
#                'type'  : 'rateParam',
#                'cuts'  : cuts0j
#               }
#


for n in nuisances.values():
    n['skipCMS'] = 1

print(' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat')))
