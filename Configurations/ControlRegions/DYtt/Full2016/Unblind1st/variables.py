# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 0
                        }
    
variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (10,40,80),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['mth']  = {   'name': 'mth',            #   variable name    
                        'range' : (12,0,60),    #   variable range
                        'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['ptll']  = {   'name': 'ptll',     
                        'range' : (10,30,90),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }

variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]',     
                        'range' : (15,25,100),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0                         
                        }

variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]',     
                        'range' : (14,10,80),   
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0                         
                        }

variables['met']  = {   'name': 'metPfType1',            #   variable name    
                        'range' : (6,20,100),    #   variable range
                        'xaxis' : 'E_{T}^{miss} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['eta1']  = {  'name': 'std_vector_lepton_eta[0]',     
                       'range' : (20,-2.5,2.5),   
                       'xaxis' : '#eta 1st lep',
                       'fold'  : 0                         
                       }

variables['eta2']  = {  'name': 'std_vector_lepton_eta[1]',     
                       'range' : (20,-2.5,2.5),   
                       'xaxis' : '#eta 2nd lep',
                       'fold'  : 0                         
                       }

#variables['mjj']  = {  'name': 'mjj',
#                       'range': (15,200,1000),  #for 500 < mjj < 1000
#                     # 'range': (15,1000,2000),  #for  mjj > 1000
#                       'xaxis': 'm_{jj} [GeV]',
#                       'fold': 0
#                       }
#
#
#variables['detajj']  = {  'name': 'detajj',
#                       'range': (12,0.0,6.0),
#                       'xaxis': '#Delta#eta_{jj}',
#                       'fold': 3
#                       }
#
#
#variables['jetpt1']  = {   'name': 'std_vector_jet_pt[0]',     
#                        'range' : (25,30,200),   
#                        'xaxis' : 'p_{T} 1st jet',
#                        'fold'  : 0                         
#                        }
#
#variables['jetpt2']  = {   'name': 'std_vector_jet_pt[1]',     
#                        'range' : (25,30,100),   
#                        'xaxis' : 'p_{T} 2nd jet',
#                        'fold'  : 0                         
#                        }




#variables['mth']  = {   'name': 'mth',            #   variable name    
                        #'range' : (20,0,200),    #   variable range
                        #'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                         #'fold' : 0
                        #}

#variables['dphill']  = {   'name': 'abs(dphill)',     
                        #'range' : (10,0,3.14),   
                        #'xaxis' : '#Delta#phi_{ll}',
                        #'fold' : 3
                        #}

#variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]*(1 - (abs(std_vector_lepton_flavour[0])==11)*0.01*(dataset != 0))',     
                        #'range' : (8,20,80),   
                        #'xaxis' : 'p_{T} 1st lep',
                        #'fold'  : 3                         
                        #}

#variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]*(1 - (abs(std_vector_lepton_flavour[1])==11)*0.01*(dataset != 0))',     
                        #'range' : (8,10,50),   
                        #'xaxis' : 'p_{T} 2nd lep',
                        #'fold'  : 3                         
                        #}


#variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]',     
                        #'range' : (100,0,200),   
                        #'xaxis' : 'p_{T} 1st lep',
                        #'fold'  : 3                         
                        #}

#variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]',     
#                        'range' : (50,0,200),   
#                        'xaxis' : 'p_{T} 2nd lep',
#                        'fold'  : 3                         
#                        }


#variables['expectedMissingInnerHits_1']  = {  'name': 'std_vector_electron_expectedMissingInnerHits[0]',     
                       #'range' : (3,0,3),   
                       #'xaxis' : 'std_vector_electron_expectedMissingInnerHits 1st lep',
                       #'fold'  : 3                         
                       #}


#variables['expectedMissingInnerHits_2']  = {  'name': 'std_vector_electron_expectedMissingInnerHits[1]',     
                       #'range' : (3,0,3),   
                       #'xaxis' : 'expectedMissingInnerHits 2nd lep',
                       #'fold'  : 3                         
                       #}




# variables['eta1']  = {  'name': 'std_vector_lepton_eta[0]',     
#                        'range' : (100,-3.2,3.2),   
#                        'xaxis' : '#eta 1st lep',
#                        'fold'  : 3                         
#                        }

# variables['eta2']  = {  'name': 'std_vector_lepton_eta[1]',     
#                        'range' : (100,-3.2,3.2),   
#                        'xaxis' : '#eta 2nd lep',
#                        'fold'  : 3                         
#                        }

# #variables['r91']   = {  'name': 'std_vector_electron_full5x5R9[0]',     
#                        #'range' : (100,0.8,1.05),   
#                        #'xaxis' : 'R9 1st lep',
#                        #'fold'  : 2                         
#                        #}


# #variables['r92']   = {  'name': 'std_vector_electron_full5x5R9[1]',     
#                        #'range' : (100,0.8,1.05),   
#                        #'xaxis' : 'R9 2nd lep',
#                        #'fold'  : 2                         
#                        #}

# #variables['sietaieta1']   = {  'name': 'std_vector_electron_full5x5_sigmaIetaIeta[0]',     
#                        #'range' : (100,0.0,0.04),   
#                        #'xaxis' : '#sigma ietaieta 1st lep',
#                        #'fold'  : 0                         
#                        #}


# #variables['sietaieta2']   = {  'name': 'std_vector_electron_full5x5_sigmaIetaIeta[1]',     
#                        #'range' : (100,0.0,0.04),   
#                        #'xaxis' : '#sigma ietaieta 2nd lep',
#                        #'fold'  : 0                         
#                        #}


# #variables['deta1']   = {  'name': 'std_vector_electron_dEtaIn[0]',     
#                        #'range' : (100,-0.01,0.01),   
#                        #'xaxis' : '#Delta #eta 1st lep',
#                        #'fold'  : 0                         
#                        #}


# #variables['deta2']   = {  'name': 'std_vector_electron_dEtaIn[1]',     
#                        #'range' : (100,-0.01,0.01),   
#                        #'xaxis' : '#Delta #eta 2nd lep',
#                        #'fold'  : 0                         
#                        #}


# #variables['deta1phip']   = {  'name': 'std_vector_electron_dEtaIn[0]*(std_vector_lepton_phi[0]>0)+5*(std_vector_lepton_phi[0]<0)',     
#                        #'range' : (100,-0.01,0.01),   
#                        #'xaxis' : '#Delta #eta 1st lep',
#                        #'fold'  : 0                         
#                        #}


# #variables['deta1phim']   = {  'name': 'std_vector_electron_dEtaIn[0]*(std_vector_lepton_phi[0]<0)+5*(std_vector_lepton_phi[0]>0)',     
#                        #'range' : (100,-0.01,0.01),   
#                        #'xaxis' : '#Delta #eta 1st lep',
#                        #'fold'  : 0                         
#                        #}



# #variables['deta2phip']   = {  'name': 'std_vector_electron_dEtaIn[1]*(std_vector_lepton_phi[1]>0)+5*(std_vector_lepton_phi[1]<0)',     
#                        #'range' : (100,-0.01,0.01),   
#                        #'xaxis' : '#Delta #eta 2nd lep',
#                        #'fold'  : 0                         
#                        #}


# #variables['deta2phim']   = {  'name': 'std_vector_electron_dEtaIn[1]*(std_vector_lepton_phi[1]<0)+5*(std_vector_lepton_phi[1]>0)',     
#                        #'range' : (100,-0.01,0.01),   
#                        #'xaxis' : '#Delta #eta 2nd lep',
#                        #'fold'  : 0                         
#                        #}



# ##variables['phi1']  = {  'name': 'std_vector_lepton_phi[0]',
#                         ##'range' : (100,-3.2,3.2),
#                         ##'xaxis' : '#phi 1st lep',
#                         ##'fold'  : 3
#                         ##}

# ##variables['phi2']  = {  'name': 'std_vector_lepton_phi[1]',
#                         ##'range' : (100,-3.2,3.2),
#                         ##'xaxis' : '#phi 2nd lep',
#                         ##'fold'  : 3
#                         ##}

# ##variables['dphill']  = {   'name': 'abs(dphill)',     
#                         ##'range' : (20,0,3.14),   
#                         ##'xaxis' : '#Delta#phi_{ll}',
#                          ##'fold' : 3
#                         ##}


# #variables['trkMet']  = {   'name': 'trkMet',            #   variable name    
#                         #'range' : (20,0,200),    #   variable range
#                         #'xaxis' : 'trk met [GeV]',  #   x axis name
#                          #'fold' : 0
#                         #}

# ##variables['pupMet']  = {   'name': 'pupMet',            #   variable name    
#                         ##'range' : (20,0,200),    #   variable range
#                         ##'xaxis' : 'puppi met [GeV]',  #   x axis name
#                          ##'fold' : 0
#                         ##}

# ###variables['mpmet']  = {   'name': 'mpmet',            #   variable name    
#                         ###'range' : (20,0,200),    #   variable range
#                         ###'xaxis' : 'min proj met [GeV]',  #   x axis name
#                          ###'fold' : 0
#                         ###}

  
# variables['njet']  = {  'name': 'njet',      
#                         'range' : (5,0,5),  
#                         'xaxis' : 'njet', 
#                         'fold' : 3
#                         }


# #variables['jetpt1']  = {
#                         #'name': 'std_vector_jet_pt[0]',     
#                         #'range' : (20,0,200),   
#                         #'xaxis' : 'p_{T} 1st jet',
#                         #'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         #}

# ##variables['jetpt2']  = {
#                         ##'name': 'std_vector_jet_pt[1]',     
#                         ##'range' : (20,0,200),   
#                         ##'xaxis' : 'p_{T} 2nd jet',
#                         ##'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         ##}

# ##variables['jeteta1']  = {
#                         ##'name': 'std_vector_jet_eta[0]',
#                         ##'range' : (100,-5.2,5.2),
#                         ##'xaxis' : '#eta 1st jet',
#                         ##'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         ##}

# ##variables['jeteta2']  = {
#                         ##'name': 'std_vector_jet_eta[1]',
#                         ##'range' : (100,-5.2,5.2),
#                         ##'xaxis' : '#eta 2nd jet',
#                         ##'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         ##}

# ##variables['jetphi1']  = {
#                         ##'name': 'std_vector_jet_phi[0]',
#                         ##'range' : (100,-3.2,3.2),
#                         ##'xaxis' : '#phi 1st jet',
#                         ##'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         ##}


# ##variables['jetphi2']  = {
#                         ##'name': 'std_vector_jet_phi[1]',
#                         ##'range' : (100,-3.2,3.2),
#                         ##'xaxis' : '#phi 2nd jet',
#                         ##'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         ##}

# #variables['cmvav2_1']  = { 
#                         #'name': 'std_vector_jet_cmvav2[0]',     
#                         #'range' : (100,-1,1),   
#                         #'xaxis' : 'csvv2ivf 1st jet',
#                         #'fold'  : 3                         
#                         #}

# #variables['cmvav2_2']  = {
#                         #'name': 'std_vector_jet_cmvav2[1]',
#                         #'range' : (100,-1,1),
#                         #'xaxis' : 'csvv2ivf 2nd jet',
#                         #'fold'  : 3
#                         #}
