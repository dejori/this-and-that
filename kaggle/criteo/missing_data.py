# -*- coding: UTF-8 -*-
from csv import DictReader


def missing_value_stats(loc_csv):
    missing_value_cnts={}
    for idx, row in enumerate(DictReader(open(loc_csv))):
        for k, v in row.items():
            if not v:
                missing_value_cnts[k] = missing_value_cnts.get(k, 0) + 1
        #Reporting progress
        if not idx % 1000000:
            print("%d analyzed" % idx)

    for key in missing_value_cnts.keys():
        print "%s\t%0.3f" % (key, missing_value_cnts.get(key)/float(idx))


missing_value_stats("./data/train.csv")