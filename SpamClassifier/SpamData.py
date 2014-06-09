from numpy import genfromtxt


class SpamData:

    data = []
    target = []
    feature_names = []
    target_names = []
    def __init__(self):

        my_data = genfromtxt('./data/spambase.data', delimiter=',')
        cols = my_data.shape[1]

        self.target = my_data[:, cols-1]
        self.data = my_data[:, 0:cols-1]
        self.feature_names = self._getfeature_names()
        self.target_names = ['no spam', 'spam']

        self.data

    def getfeature_vector(self, feature_name):
        index = self.feature_names.index(feature_name)
        return self.data[:, index]

    def _getfeature_names(self):
        names = []
        with open('./data/spambase.names') as f:
            content = f.readlines()
            for line in content:
                line = line.strip()
                if line and not line.startswith('|') and 'classes' not in line:
                    feature_name = line[0:line.find(':')]
                    names.append(feature_name)
        return names

    def summary(self):
        print "%d features, %d samples" % (self.number_of_features(), self.number_of_samples())

    def number_of_samples(self):
        return self.data.shape[0]

    def number_of_features(self):
        return self.data.shape[1]

if __name__ == '__main__':
    data = SpamData()
    data.summary()
    # data.getfeature_vector('word_freq_make')