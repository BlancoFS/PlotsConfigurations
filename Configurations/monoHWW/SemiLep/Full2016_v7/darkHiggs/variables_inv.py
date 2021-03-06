variables['Events']  = {   'name': '1',     
                           'range' : (1,0,1),   
                           'xaxis' : '1',
                           'fold'  : 3
                        }

variables['Puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (25,0,300),
                        'xaxis' : 'p_{T} puppiMET [GeV]',
                        'fold'  : 3
                        }

variables['l1_pt']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (25,20,200),   
                        'xaxis' : 'p_{T}^{l_{1}}',
                        'fold'  : 3
                        }

variables['j1_pt']  = {   'name': 'MHlnjj_pt_j1',     
                        'range' : (25,0,350),   
                        'xaxis' : 'p_{T}^{j_{1}}',
                        'fold'  : 3
                        }
variables['j2_pt']  = {   'name': 'MHlnjj_pt_j2',     
                        'range' : (25,0,150),   
                        'xaxis' : 'p_{T}^{j_{2}}',
                        'fold'  : 3
                        }
variables['njet']  = {   'name': 'Sum$(CleanJet_pt > 30)',     
                        'range' : (10,0,10),   
                        'xaxis' : 'nCleanJet (p_{T} > 30)',
                        'fold'  : 3
                        }

variables['l1_eta']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (25,-3,3),   
                        'xaxis' : '#eta^{l_{1}}',
                        'fold'  : 3                         
                        }
variables['j1_eta']  = {  'name': 'MHlnjj_eta_j1',     
                        'range' : (25,-5,5),   
                        'xaxis' : '#eta^{j_{1}}',
                        'fold'  : 3                         
                        }
variables['j2_eta']  = {  'name': 'MHlnjj_eta_j2',     
                        'range' : (25,-5,5),   
                        'xaxis' : '#eta^{j_{2}}',
                        'fold'  : 3                         
                        }

variables['m_jj']  = {  'name': 'MHlnjj_m_jj',     
                        'range' : (25,0,250),   
                        'xaxis' : 'm^{j,j}',
                        'fold'  : 3                         
                        }

# copied

variables['mt_lmet']  = {
                       #'name': 'MHlnjj_mt_lmet',
                       'name': 'mtw1',
                       'range' : (25,0,200),
                       #'range' : ([50,75,100,125,181,300],),
                       'xaxis' : 'm_{T}^{lmet} [GeV]',
                       'fold'  : 3
                       }
variables['mt_jj']  = {
                        'name': 'MHlnjj_mt_jj',
                        'range' : (25,0,200),
                        'xaxis' : 'm_{T}^{jj} [GeV]',
                        'fold'  : 3
                        }
variables['pt_jj']  = {
                        'name': 'MHlnjj_pt_jj',
                        'range' : (25,0,300),
                        'xaxis' : 'p_{T}^{jj} [GeV]',
                        'fold'  : 3
                        }
variables['pt_ljj']  = {
                        'name': 'MHlnjj_pt_ljj',
                        'range' : (25,0,300),
                        'xaxis' : 'p_{T}^{ljj} [GeV]',
                        'fold'  : 3
                        }

variables['dphi_ljj_met']  = {
                        'name': 'MHlnjj_dphi_ljjVmet',
                        'range' : (25,0,3.14),
                        'xaxis' : '#Delta#phi(ljj,met)',
                        'fold'  : 3,
                        }
variables['dphi_l_jj']  = {
                        'name': 'MHlnjj_dphi_jjVl',
                        'range' : (25,0,3.14),
                        'xaxis' : '#Delta#phi(l,jj)',
                        'fold'  : 3
                        }

bdt_bins = [-1.,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,1.]

variables['darkHiggsBDT_Ada16Var']  = { 
                        'name': 'MHlnjj_darkHiggsBDT_Ada16Var',
                        #'range' : (10,-1.1,1.1),
                        'range' : (bdt_bins,),
                        'xaxis' : 'darkHiggs BDT_{Ada16Var}',
                        #'xaxis' : 'BDT',
                        'fold'  : 3 
                        }   
variables['darkHiggsBDT_Grad16Var']  = { 
                        'name': 'MHlnjj_darkHiggsBDT_Grad16Var',
                        #'range' : (10,-1.1,1.1),
                        'range' : (bdt_bins,),
                        'xaxis' : 'darkHiggs BDT_{Grad16Var}',
                        #'xaxis' : 'BDT',
                        'fold'  : 3 
                        }   

