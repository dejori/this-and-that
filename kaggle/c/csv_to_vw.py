# -*- coding: UTF-8 -*-

#########################################################
# adapted from Triskelion <info@mlwave.com>             #
#########################################################

from csv import DictReader


def csv_to_vw(loc_csv, loc_vw, train=True):
    print("\nTurning %s into %s. Is_train_set? %s" % (loc_csv, loc_vw, train))

    with open(loc_vw, "wb") as outfile:
        for idx, row in enumerate(DictReader(open(loc_csv))):

            #Creating the features
            numerical_features = ""
            categorical_features = ""
            for k, v in row.items():
                if k not in ["Label", "Id"] and v:
                    if "I" in k:  # numerical feature, example: I5
                        numerical_features += " %s:%s" % (k, v)
                    if "C" in k:  # categorical feature, example: C2
                        categorical_features += " %s" % v

                            #Creating the labels
            if train:  #we care about labels
                if row['Label'] == "1":
                    label = 1
                else:
                    label = -1  #we set negative label to -1
                outfile.write("%s '%s |i%s |c%s\n" % (label, row['Id'], numerical_features, categorical_features))

            else:  #we dont care about labels
                outfile.write("1 '%s |i%s |c%s\n" % (row['Id'], numerical_features, categorical_features))

                #Reporting progress
            if idx and not idx % 1000000:
                print("%d converted" % idx)
    outfile.close()


#csv_to_vw("train.csv", "train.vw", train=True)
csv_to_vw("data/train.csv", "data/train.vw", train=False)

