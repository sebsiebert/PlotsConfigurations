# Configuration file to produce initial root files -- has both merged and binned ggH samples

treeName = 'Events'

tag = '2HDMaSemlep_2017'

# used by mkShape to define output directory for root files
outputDir = 'rootFile2HDMa_NoData'

# file with TTree aliases
aliasesFile = 'aliasesNoData.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples2HDMa_NoData_2017.py' 

# file with list of samples
plotFile = 'plot2HDMa_NoData.py' 

# luminosity to normalize to (in 1/fb)
lumi = 41.53

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plots2HDMa_NoData'

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'

# structure file for datacard
structureFile = 'structureNoData.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'

