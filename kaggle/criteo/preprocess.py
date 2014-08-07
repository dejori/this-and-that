from DataStats import DataStats

features = DataStats.plot_stats("./data/train.csv")

for k in features.keys():
    features[k].print_stats()