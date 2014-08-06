__author__ = 'mdejori'

import math
import gzip

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


with open("data/submission.csv", "wb") as outfile:
    outfile.write("Id,Predicted\n")
    for line in open("data/preds.txt"):
        row = line.strip().split(" ")
        outfile.write("%s,%f\n" % (row[1], sigmoid(float(row[0]))))

# and create a gzip version for faster upload
with open("data/submission.csv", "rb") as infile:
    f_out = gzip.open('data/submission.csv.gz', 'wb')
    f_out.writelines(infile)
    f_out.close()