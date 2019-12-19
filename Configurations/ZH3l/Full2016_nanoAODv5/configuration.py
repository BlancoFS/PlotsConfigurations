# example of configuration file

tag = 'ZH3l_2016_CR_sys'

# used by mkShape to define output directory for root files
outputDir = 'rootFiles_'+tag

# file with list of variables
variablesFile = 'variables_test.py'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of cuts
cutsFile = 'cuts_CR.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 35.867

# used by mkPlot to define output directory for plots
outputDirPlots = 'plot_'+tag

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
