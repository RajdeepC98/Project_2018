import numpy as np
from glob import glob
from scipy import misc
import matplotlib.pyplot as plt
from boundary import *
from radius import *
from priorshape import *

filelist = glob('/home/rajdeep/ml/Project2018/Dataset/Marked/*')

M = len(filelist)
N = 8       			#state variable perturbations in time series n(R_i)

X = np.ndarray((M,N))

for i in range(len(filelist)):

	image = misc.imread(filelist[i]);

	boundary, xc, yc = get_boundary(image)

	boundary, X[i],_ = getradius(boundary, xc, yc)


dist_bins = gen_radius_hist(X)
c=0
for i in range(len(dist_bins)):

	tp_bin = [0]*7; 
	for j in range(len(dist_bins[i])):

		if(dist_bins[i][j][0] < N-1):
			tp_bin[dist_bins[i][j][0]] +=1

	dist_bins[i] = tp_bin

for i in range(len(dist_bins)):
	c+=np.sum(np.array(dist_bins[i]));

print "dist bins ", dist_bins
print c
 




