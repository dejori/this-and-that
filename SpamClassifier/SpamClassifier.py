from sklearn.datasets import load_iris
from sklearn import tree
from SpamData import SpamData
import export




class SpamClassifier:

    def train(self):
        spamdata = SpamData()
        model = tree.DecisionTreeClassifier(min_samples_leaf=100)
        model = model.fit(spamdata.data['data'], spamdata.data['target'])

        with open("spam.dot", 'w') as f:
            f = export.export_graphviz(model, out_file=f,feature_names=spamdata.data['feature_names'], target_names=spamdata.data['target_names'])

        return model

    def test(self,clf):
        spamdata = SpamData()
        print "Accuracy: %0.3f" % clf.score(spamdata.data['data'],spamdata.data['target'])



if __name__ == '__main__':
    model = SpamClassifier().train()
    SpamClassifier().test(model)
