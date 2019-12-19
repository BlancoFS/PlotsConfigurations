import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017nano_STXS_1p1
configurations = os.path.dirname(configurations) # ZH4l
configurations = os.path.dirname(configurations) # Configurations

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['class0'] = {
     'name': 'hww_ZH_newBDT(Entry$,0)',
     'range' : ([-1,-0.75,-0.5,-0.25,0.,0.15,0.25,0.35,0.50,1.],),
     'xaxis' : 'MVA discriminant ZH',
     'fold' : 3,
     'linesToAdd' : ['.L %s/ZH4l/nano_config/Full2017/hww_ZH_newBDT.C+' % configurations]
}

variables['class1'] = {
     'name': 'hww_ZH_newBDT(Entry$,0)',
     'range' : ([-0.85,-0.75,-0.5,-0.25,0.,0.15,0.25,0.35,0.50,1.],),
     'xaxis' : 'MVA discriminant ZH',
     'fold' : 3,
     'linesToAdd' : ['.L %s/ZH4l/nano_config/Full2017/hww_ZH_newBDT.C+' % configurations]
}

variables['class2'] = {
     'name': 'hww_ZH_newBDT(Entry$,0)',
     'range' : (20,-0.85,0.5),
     'xaxis' : 'MVA discriminant ZH',
     'fold' : 3,
     'linesToAdd' : ['.L %s/ZH4l/nano_config/Full2017/hww_ZH_newBDT.C+' % configurations]
}

variables['class3'] = {
     'name': 'hww_ZH_newBDT(Entry$,0)',
     'range' : (20,-0.90,0.5),
     'xaxis' : 'MVA discriminant ZH',
     'fold' : 3,
     'linesToAdd' : ['.L %s/ZH4l/nano_config/Full2017/hww_ZH_newBDT.C+' % configurations]
}

variables['class4'] = {
     'name': 'hww_ZH_newBDT(Entry$,0)',
     'range' : (20,-0.80,0.5),
     'xaxis' : 'MVA discriminant ZH',
     'fold' : 3,
     'linesToAdd' : ['.L %s/ZH4l/nano_config/Full2017/hww_ZH_newBDT.C+' % configurations]
}

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 3
                        }
