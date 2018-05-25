import numpy as np
from scipy import misc,ndimage
import matplotlib.pyplot as plt
import math



def gen_radius_hist( X ):

	PI = math.pi; 
	N = 20 #number of bins

	rmin = np.min(X); rmax = np.max(X);

	delta_r = float(rmax-rmin)/N

	indmax = np.unravel_index(np.argmax(X, axis=None), X.shape)
	indmin = np.unravel_index(np.argmin(X, axis=None), X.shape)
	
	print (indmax, rmax), (indmin, rmin), delta_r
	
	

	bin_centres =[]; dist_bins =[];

	for i in range(N):
		dist_bins.append([])

	for i in range(N):

		rleft = rmin+i*delta_r
		r = rleft + delta_r/2
		bin_centres.append(r)

	print bin_centres

	
	N = X.shape;

	for i in range(N[0]):

		for r in range(len(bin_centres)):

			for j in range(N[1]):

				left = bin_centres[r]-delta_r/2;

				if(r == len(bin_centres)-1):
					right = rmax;
				else:
					right = bin_centres[r]+delta_r/2;

				p = (X[i, j] - left)*(X[i, j] - right)

				if(p <= 0):
					
					if(j + 1 < N[1]):

						dist_bins[r].append((j, X[i, j + 1]))

					else:

						dist_bins[0].append((N[1]-1, X[i, 0]))



	return dist_bins

