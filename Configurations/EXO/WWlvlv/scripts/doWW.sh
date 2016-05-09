
workdir=${CMSSW_BASE}/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv/combine
datacardDir=${CMSSW_BASE}/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv/datacards
modDatacardDir=${CMSSW_BASE}/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv/ModificationDatacards

variable=mll



## prune nuisances
cd $modDatacardDir
bash examples/doPruneNuisanceXWW.sh

cd $workdir

cd ~/Combine/CMSSW_7_4_7/src/
eval `scramv1 runtime -sh`
cd -

## prune again
cat ${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.txt.pruned.txt  | grep -v "_DY_ibin_1" | grep -v "_Vg_ibin_1" | grep -v "_VVV_ibin_1" &> ${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.test.txt.pruned.txt
mv ${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.test.txt.pruned.txt ${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.txt.pruned.txt

cat ${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.txt.pruned.txt  | grep -v "_DY_ibin_1" | grep -v "_Vg_ibin_1" | grep -v "_VVV_ibin_1" &> ${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.test.txt.pruned.txt
mv ${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.test.txt.pruned.txt ${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.txt.pruned.txt

cat ${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.txt.pruned.txt   | grep -v "_VVV_ibin_1"  &> ${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.test.txt.pruned.txt
mv ${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.test.txt.pruned.txt ${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.txt.pruned.txt

cat ${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.txt.pruned.txt   | grep -v "_VVV_ibin_1"  &> ${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.test.txt.pruned.txt
mv ${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.test.txt.pruned.txt ${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.txt.pruned.txt


# combine datacards
 
combineCards.py   em1j13=${datacardDir}/hwwhighmass_13TeV_em_1j/${variable}/datacard.txt.pruned.txt \
                  me1j13=${datacardDir}/hwwhighmass_13TeV_me_1j/${variable}/datacard.txt.pruned.txt \
                  em0j13=${datacardDir}/hwwhighmass_13TeV_em_0j/${variable}/datacard.txt.pruned.txt \
                  me0j13=${datacardDir}/hwwhighmass_13TeV_me_0j/${variable}/datacard.txt.pruned.txt \
                  of0j13Top=${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.txt.pruned.txt \
                  of1j13Top=${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.txt.pruned.txt \
                  of0j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.txt.pruned.txt \
                  of1j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.txt.pruned.txt \
                  >   Moriond2016.v1.txt.pruned.txt

combineCards.py   em1j13=${datacardDir}/hwwhighmass_13TeV_em_1j/${variable}/datacard.txt.pruned.txt \
                  me1j13=${datacardDir}/hwwhighmass_13TeV_me_1j/${variable}/datacard.txt.pruned.txt \
                  of1j13Top=${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.txt.pruned.txt \
                  of1j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.txt.pruned.txt \
                  >   Moriond2016.1jet.txt

combineCards.py   em0j13=${datacardDir}/hwwhighmass_13TeV_em_0j/${variable}/datacard.txt.pruned.txt \
                  me0j13=${datacardDir}/hwwhighmass_13TeV_me_0j/${variable}/datacard.txt.pruned.txt \
                  of0j13Top=${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.txt.pruned.txt \
                  of0j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.txt.pruned.txt \
                  >   Moriond2016.0jet.txt

combineCards.py   em0j13=${datacardDir}/hwwhighmass_13TeV_em_0j/${variable}/datacard.txt.pruned.txt \
                  of0j13Top=${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.txt.pruned.txt \
                  of0j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.txt.pruned.txt \
                  >   Moriond2016.0jet.em.txt

combineCards.py   me0j13=${datacardDir}/hwwhighmass_13TeV_me_0j/${variable}/datacard.txt.pruned.txt \
                  of0j13Top=${datacardDir}/hww2l2v_13TeV_top_of0j/events/datacard.txt.pruned.txt \
                  of0j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of0j/events/datacard.txt.pruned.txt \
                  >   Moriond2016.0jet.me.txt

                  
combineCards.py   em1j13=${datacardDir}/hwwhighmass_13TeV_em_1j/${variable}/datacard.txt.pruned.txt \
                  of1j13Top=${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.txt.pruned.txt \
                  of1j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.txt.pruned.txt \
                  >   Moriond2016.1jet.em.txt

combineCards.py   me1j13=${datacardDir}/hwwhighmass_13TeV_me_1j/${variable}/datacard.txt.pruned.txt \
                  of1j13Top=${datacardDir}/hww2l2v_13TeV_top_of1j/events/datacard.txt.pruned.txt \
                  of1j13DYtt=${datacardDir}/hww2l2v_13TeV_dytt_of1j/events/datacard.txt.pruned.txt \
                  >   Moriond2016.1jet.me.txt

# results
#combine -M MaxLikelihoodFit -t -1 --expectSignal 1        Moriond2016.1jet.txt             >   result.MaxLikelihoodFit.Moriond2016.1jet.txt
#combine -M MaxLikelihoodFit -t -1 --expectSignal 1        Moriond2016.0jet.txt             >   result.MaxLikelihoodFit.Moriond2016.0jet.txt
#combine -M MaxLikelihoodFit -t -1 --expectSignal 1        Moriond2016.0jet.em.txt          >   result.MaxLikelihoodFit.Moriond2016.0jet.em.txt
#combine -M MaxLikelihoodFit -t -1 --expectSignal 1        Moriond2016.0jet.me.txt          >   result.MaxLikelihoodFit.Moriond2016.0jet.me.txt
#combine -M MaxLikelihoodFit -t -1 --expectSignal 1        Moriond2016.1jet.em.txt          >   result.MaxLikelihoodFit.Moriond2016.1jet.em.txt
#combine -M MaxLikelihoodFit -t -1 --expectSignal 1        Moriond2016.1jet.me.txt          >   result.MaxLikelihoodFit.Moriond2016.1jet.me.txt


#combine -M ProfileLikelihood --significance -t -1 --expectSignal 1        Moriond2016.1jet.txt             >   result.Significance.Moriond2016.1jet.txt
#combine -M ProfileLikelihood --significance -t -1 --expectSignal 1        Moriond2016.0jet.txt             >   result.Significance.Moriond2016.0jet.txt
#combine -M ProfileLikelihood --significance -t -1 --expectSignal 1        Moriond2016.0jet.em.txt          >   result.Significance.Moriond2016.0jet.em.txt
#combine -M ProfileLikelihood --significance -t -1 --expectSignal 1        Moriond2016.0jet.me.txt          >   result.Significance.Moriond2016.0jet.me.txt
#combine -M ProfileLikelihood --significance -t -1 --expectSignal 1        Moriond2016.1jet.em.txt          >   result.Significance.Moriond2016.1jet.em.txt
#combine -M ProfileLikelihood --significance -t -1 --expectSignal 1        Moriond2016.1jet.me.txt          >   result.Significance.Moriond2016.1jet.me.txt




#combine -M MaxLikelihoodFit -t -1 --expectSignal 1        Moriond2016.v1.txt.pruned.txt             >   result.MaxLikelihoodFit.Moriond2016.v1.txt.pruned.txt
    
#combine -M ProfileLikelihood --significance Moriond2016.v1.txt.pruned.txt -t -1 --expectSignal=1       >   result.Significance.Moriond2016.v1.txt.pruned.txt

#combine -M MultiDimFit Moriond2016.v1.txt.pruned.txt -m 125 --algo=grid --points 50 --setPhysicsModelParameterRanges r=0.01,3 -n "LHScanH"   -t -1 --expectSignal=1        >   result.LikelihoodScan.Moriond2016.v1.txt.pruned.txt


     
