import StringIO
from sklearn import tree
from SpamData import SpamData
import export
import pydot


# dot -Tpdf spam.dot -o spam.pdf

class SpamClassifier:




    def train(self):
        model = tree.DecisionTreeClassifier(min_samples_leaf=100)
        data = SpamData()
        model.fit(data.data, data.target)

        self.__save(model, data)
        return model


    def __save(self, model, data):
        dot_data = StringIO.StringIO()
        export.export_graphviz(model, out_file=dot_data, feature_names=data.feature_names, target_names=data.target_names)
        graph = pydot.graph_from_dot_data(dot_data.getvalue())
        graph.write_png("spam.png")

    def test(self, clf):
        data = SpamData()
        print "Accuracy: %0.3f" % clf.score(data.data, data.target)



if __name__ == '__main__':

    model = SpamClassifier().train()

    SpamClassifier().test(model)
