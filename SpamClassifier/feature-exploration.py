from SpamData import SpamData
#import matplotlib.pyplot as plt

spamData = SpamData()\

spamData.load()


featureA = spamData.getfeature_vector('char_freq_!')
featureB = spamData.getfeature_vector('capital_run_length_total')

#plt.scatter(data['data'], data['data'])
#plt.show()