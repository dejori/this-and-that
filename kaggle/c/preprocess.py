from FeatureStats import FeatureStats
from SampleStats import SampleStats
from pylab import *

data_file = "./data/train.csv"

def plotitout(feature_name):
    data = FeatureStats.get_column(data_file,feature_name)
    # basic plot
    boxplot(data)
    savefig(feature_name+'.png')
    show()

feature_names = FeatureStats.feature_names(data_file)
for feature_name in feature_names:
    if "I" in feature_name:
        plotitout(feature_name)

# SampleStats.calculate_stats("./data/test.csv")

# features = FeatureStats.calculate_stats("./data/train.csv")
#
# for k in features.keys():
#     features[k].print_stats()


# data = FeatureStats.get_column("./data/test.csv","I9")
#
# print len(data)