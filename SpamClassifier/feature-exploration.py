from SpamData import SpamData
import matplotlib.pyplot as plt
import numpy as np

spamData = SpamData()




neg_indices = np.where(spamData.data["target"] ==0 )
pos_indices = np.where(spamData.data["target"] ==1 )

featureA = spamData.getfeature_vector('char_freq_!')
featureB = spamData.getfeature_vector('char_freq_$')



plt.axis((0,10,0,10))
plt.scatter(np.take(featureA, neg_indices), np.take(featureB, neg_indices),color='green')
plt.scatter(np.take(featureA, pos_indices), np.take(featureB, pos_indices),color='orange')

plt.xlabel('char_freq_!')
plt.ylabel('char_freq_$')

plt.savefig('foo.png')