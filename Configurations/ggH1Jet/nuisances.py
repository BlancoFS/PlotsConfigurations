# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py    
#

nuisances['lumi']  = {
               'name'  : 'lumi', 
               'all'   : 1 ,     # apply to all samples
               'type'  : 'lnN',
               'value' : 1.05 
              }


# old style "free floating", but still working!
#nuisances['WWnorm']  = {
               #'name'  : 'WWnorm', 
               #'samples'  : {
                   #'WW' : 2.00,
                   #},
               #'type'  : 'lnU',
              #}

# new style "free floating" background
# e.g. " z_norm rateParam  htsearch zll 1 "




## nuisances handled by means of a weight in the tree

#nuisances['pileup']  = {
                #'name'  : 'pileup', 
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {
                   ##'ttbar' : ['puWup/puW', 'puWdown/puW'],
                   ##'DY'    : ['puWup/puW', 'puWdown/puW']
                   #'ttbar' : ['3./puW', '0.3/puW'],
                   #'DY'    : ['3./puW', '0.3/puW']
                #}
#}


# nuisances handled by means of a different set of trees

#nuisances['eleScale']  = {
                #'name'  : 'eleScale', 
                #'kind'  : 'tree',
                #'type'  : 'shape',
                #'samples'  : {
                   #'ttbar' : ['1', '1'],
                   #'Wjets' : ['1', '1']
                #},
                #'folderUp'   : '/tmp/amassiro/Tree_eleScaleUp/',
                #'folderDown' : '/tmp/amassiro/Tree_eleScaleDown/' 
#}

# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
