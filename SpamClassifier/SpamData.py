from numpy import genfromtxt


class SpamData:

    data = {}
    def __init__(self):

        my_data = genfromtxt('./data/spambase.data', delimiter=',')
        cols = my_data.shape[1]

        self.data["target"] = my_data[:,cols-1] #ndarray [0 0 1 1]
        self.data["data"] = my_data[:,0:cols-2] # [ndarray, ndarray, ndarray]
        self.data["feature_names"] = self._getfeature_names()
        self.data["target_names"] = ['no spam','spam']
        self.data

    def getfeature_vector(self, feature_name):
        index = self.data["feature_names"].index(feature_name)
        return self.data["data"][:,index-1]

    def _getfeature_names(self):
        feature_names = []
        with open('./data/spambase.names.txt') as f:
            content = f.readlines()
            for line in content:
                line = line.strip()
                if line and not line.startswith('|') and 'classes' not in line:
                    feature_name = line[0:line.find(':')]
                    feature_names.append(feature_name)
        return feature_names


if __name__ == '__main__':
    data = SpamData().load()