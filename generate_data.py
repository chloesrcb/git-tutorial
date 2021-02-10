import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


mu, sigma1, sigma2 = 100, 15, 5
x_gaussian = mu + sigma1 * np.random.randn(10000)

x_nongaussian = mu + sigma2 * (np.random.randn(10,10000) ** 2).sum(0)


np.savetxt('file_data.csv', x_gaussian, delimiter=',')
np.savetxt('file_data_nongaussian.csv', x_nongaussian, delimiter=',')
