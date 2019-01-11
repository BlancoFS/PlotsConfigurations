# cuts

supercut = '   mll>12 \
            && Lepton_pt[0]>20 \
            && Lepton_pt[1]>10 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && MET_pt > 20 \
            && LepCut2l==1 \
           '


## Signal regions

cuts['hww2l2v_13TeV_of0j']  = '   (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                               && mth>60 \
                               && mtw2>30 \
                               && Alt$(CleanJet_pt[0],0)<30 \
                               && '+bVeto+' \
                              '

cuts['hww2l2v_13TeV_of1j']  = '   (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                               && mth>60 \
                               && mtw2>30 \
                               && Alt$(CleanJet_pt[0],0)>30 \
                               && Alt$(CleanJet_pt[1],0)<30 \
                               && '+bVeto+' \
                              '

cuts['hww2l2v_13TeV_of2j']  = '   (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                               && mth>60 \
                               && mtw2>30 \
                               && Alt$(CleanJet_pt[0],0)>30 \
                               && Alt$(CleanJet_pt[1],0)>30 \
                               && '+bVeto+' \
                              '


## Top control regions
cuts['hww2l2v_13TeV_top_of0j']  = '    (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                                    && mll>50 \
                                    && mtw2>30 \
                                    && Alt$(CleanJet_pt[0],0)<30 \
                                    && (  ( Alt$(CleanJet_pt[0],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[0]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[1],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[1]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[2],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[2]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[3],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[3]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[4],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[4]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[5],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[5]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[6],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[6]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[7],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[7]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[8],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[8]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[9],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[9]],0)>'+bWP+' ) \
                                    ||    ( Alt$(CleanJet_pt[10],0)>20 && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[10]],0)>'+bWP+' ) \
                                       ) \
                                  '

cuts['hww2l2v_13TeV_top_of1j']  = '    (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                                    && mll>50 \
                                    && mtw2>30 \
                                    && Alt$(CleanJet_pt[0],0)>30 \
                                    && Alt$(CleanJet_pt[1],0)<30 \
                                    && Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[0]],0)>'+bWP+' \
                                  '

cuts['hww2l2v_13TeV_top_of2j']  = '    (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                                    && mll>50 \
                                    && mtw2>30 \
                                    && Alt$(CleanJet_pt[0],0)>30 \
                                    && Alt$(CleanJet_pt[1],0)>30 \
                                    && ( Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[0]],0)>'+bWP+' || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[1]],0)>'+bWP+' ) \
                                  '


## DYtt control regions
cuts['hww2l2v_13TeV_dytt_of0j']  = '   (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                                    && mth<60 \
                                    && mll>40 && mll<80 \
                                    && Alt$(CleanJet_pt[0],0)<30 \
                                    && '+bVeto+' \
                                   '

cuts['hww2l2v_13TeV_dytt_of1j']  = '   (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                                    && mth<60 \
                                    && mll>40 && mll<80 \
                                    && Alt$(CleanJet_pt[0],0)>30 \
                                    && Alt$(CleanJet_pt[1],0)<30 \
                                    && '+bVeto+' \
                                   '

cuts['hww2l2v_13TeV_dytt_of2j']  = '   (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                                    && mth<60 \
                                    && mll>40 && mll<80 \
                                    && Alt$(CleanJet_pt[0],0)>30 \
                                    && Alt$(CleanJet_pt[1],0)>30 \
                                    && '+bVeto+' \
                                   '
