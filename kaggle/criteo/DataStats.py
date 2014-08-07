# -*- coding: UTF-8 -*-
import sys
import math
from csv import DictReader


class DataStats:
    def __init__(self):
        pass

    @staticmethod
    def plot_stats(loc_csv):
        features = {}
        # instantiate a feature for each column except Id and Label
        for row in DictReader(open(loc_csv)):
            for k, v in row.items():
                if k in ["Id", "Label"]: continue
                features[k] = Feature(k)
            break

        # calculate min max mean
        for idx, row in enumerate(DictReader(open(loc_csv))):
            for k, v in row.items():
                if k in ["Id", "Label"]: continue
                feature = features[k]
                if not v:
                    feature.missing_value_cnts += 1
                else:
                    if "I" in k:
                        v = int(v)
                        feature.mean += v

                        if v >= feature.max:
                            feature.max = v

                        if v <= feature.min:
                            feature.min = v

            #Reporting progress
            if not idx % 1000000:
                print("%d analyzed" % idx)

        for k in features.keys():
            features[k].N = idx
            features[k].calculate_mean()


        # calculate std
        for idx, row in enumerate(DictReader(open(loc_csv))):
            for k, v in row.items():
                if k in ["Id", "Label"]: continue
                if v and "I" in k:
                    feature = features[k]
                    feature.std += math.pow(int(v) - feature.mean, 2)

            #Reporting progress
            if not idx % 1000000:
                print("%d analyzed" % idx)

        for k in features.keys():
            features[k].calculate_std()

        return features


class Feature:
    def __init__(self, id):
        self.id = id
        self.mean = 0
        self.std = 0
        self.max = - sys.maxint
        self.min = sys.maxint
        self.missing_value_cnts = 0
        self.N = 0

    def missing_value_frac(self):
        return self.missing_value_cnts/float(self.N)

    def calculate_mean(self):
        self.mean /= float(self.N - self.missing_value_cnts)

    def calculate_std(self):
        self.std = math.sqrt(self.std / float(self.N - self.missing_value_cnts))

    def print_stats(self):
        if "I" in self.id:
            print "%s \t mean:%0.3f \t std:%0.3f \t min:%d \t max:%d \t missing-values:%0.3f" % (self.id, self.mean, self.std, self.min, self.max, self.missing_value_frac())
        else:
            print "%s \t missing-values:%0.3f" % (self.id, self.missing_value_frac())