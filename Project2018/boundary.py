import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt
from glob import glob
from radius import *
from priorshape import *


def get_boundary(image):
	redblob = image[:, :, 0]==255
	image[np.nonzero(redblob)] = [0, 255, 0]

	greenblob = image[:, :, 1] == 255
	greenblob = greenblob.astype(np.int)
	erodedgblob = ndimage.binary_erosion(greenblob, structure = np.ones((3,3)))
	erodedgblob = erodedgblob.astype(np.int)

	boundary = greenblob - erodedgblob

	peripts = np.nonzero(boundary)
	n = len(peripts[1])

	xc = np.sum(peripts[1])/n
	yc = np.sum(peripts[0])/n

	boundary[yc,xc]=1


	return (boundary, xc, yc)
