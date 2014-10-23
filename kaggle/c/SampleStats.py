# -*- coding: UTF-8 -*-
import sys
import math
from csv import DictReader


class SampleStats:
    def __init__(self):
        pass

    @staticmethod
    def calculate_stats(loc_csv):
        number_of_features = 0
        # instantiate a feature for each column except Id and Label
        for row in DictReader(open(loc_csv)):
            for k, v in row.items():
                if k in ["Id", "Label"]: continue
                number_of_features +=1
            break

        # calculate fraction of missing value per sample
        for idx, row in enumerate(DictReader(open(loc_csv))):
            number_of_features_with_data = 0.0
            for k, v in row.items():
                if k in ["Id", "Label"]: continue

                if v:
                    number_of_features_with_data += 1
            score = number_of_features_with_data/float(number_of_features)

            if score <=0.4:
                print "%f0.2\t%s" % (score, row)