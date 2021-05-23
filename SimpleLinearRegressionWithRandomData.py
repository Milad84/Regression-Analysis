#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      milad
#
# Created:     25/11/2020
# Copyright:   (c) milad 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


Rn = np.random.seed(100)
N = 20
beta0 = -4
beta1 = 2
x = np.random.randn(N)
e = np.random.randn(N)

#If positive int_like arguments are provided, randn generates an array of shape (d0, d1, ..., dn),
#filled with random floats sampled from a univariate “normal” (Gaussian) distribution of mean 0 and variance 1.
# A single float randomly sampled from the distribution is returned if no argument is provided.

y = beta0 + beta1 * x + e

true_x = np.linspace(min(x), max(x), num=50)
true_y = beta0 + beta1*true_x

fig, ax = plt.subplots()
sns.scatterplot(x, y, s= 40, label = 'Data')
sns.lineplot(true_x, true_y, color = 'red', label = 'True Model')
ax.set_xlabel('x', fontsize = 14)
ax.set_title(fr"$y = {beta0} + ${beta1}$x + \epsilon$", fontsize = 16)
ax.set_ylabel('y', fontsize=14, rotation=0, labelpad=10)
ax.legend(loc = 4)
sns.despine() # will put the frame around the figure

plt.show()



