__author__ = 'mdejori'

import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


with open("data/submission.csv", "wb") as outfile:
    outfile.write("Id,Predicted\n")
    for line in open("data/preds.txt"):
        row = line.strip().split(" ")
        outfile.write("%s,%f\n" % (row[1], sigmoid(float(row[0]))))
