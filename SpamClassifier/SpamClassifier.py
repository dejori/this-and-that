from sklearn.datasets import load_iris
from sklearn import tree
from SpamData import SpamData
import export




class SpamClassifier:

    def train(self):
        data = SpamData().load()
        model = tree.DecisionTreeClassifier(min_samples_leaf=100)
        model = model.fit(data['data'], data['target'])

        with open("spam.dot", 'w') as f:
            f = export.export_graphviz(model, out_file=f,feature_names=data['feature_names'], target_names=data['target_names'])

        return model

    def test(self,clf):
        data = SpamData().load()
        print "Accuracy: %0.3f" % clf.score(data['data'],data['target'])



if __name__ == '__main__':
    model = SpamClassifier().train()
    SpamClassifier().test(model)
