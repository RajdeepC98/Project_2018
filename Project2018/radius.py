import numpy as np
from scipy import misc, ndimage


def getradius(boundary, xc, yc):

	centre = np.array((xc, yc))
	radius_list = [0]*8; end_pts =[None]*8;

	l=0; r=0; xr=xc+1; xl = xc-1; yl=yc-1; yr=yc+1;

	while(boundary[yr][xr]==0 or boundary[yl][xl]==0):
		if(boundary[yl][xl]==0):
			boundary[yl][xl]=1; xl-=1; yl-=1; # 1

		if(boundary[yr][xr]==0):
			boundary[yr][xr]=1; xr+=1; yr +=1; # 5

	end_pts[1]= (xl, yl); end_pts[5] = (xr, yr);
	


	xr=xc+1; xl = xc-1; yl=yc+1; yr=yc-1;

	while(boundary[yr, xr]==0 or boundary[yl, xl]==0):

		if(boundary[yr,xr]==0):
			boundary[yr, xr]=1; yr-=1; xr+=1; # 3

		if(boundary[yl, xl]==0):
			boundary[yl, xl]=1; yl+=1; xl-=1; # 7

	end_pts[3] = (xr, yr); end_pts[7] = (xl,yl);

	xr=xc+1; xl=xc-1; yl=yc; yr=yc;

	while(boundary[yr, xr]==0 or boundary[yl, xl]==0):

		if(boundary[yr,xr]==0):
			boundary[yr, xr]=1;  xr+=1; # 4

		if(boundary[yl, xl]==0):
			boundary[yl, xl]=1;  xl-=1; # 0


	end_pts[4] = (xr, yr); end_pts[0] = (xl,yl);

	xr=xc; xl=xc; yr=yc+1; yl=yc-1;

	while(boundary[yr, xr]==0 or boundary[yl, xl]==0):

		if(boundary[yr,xr]==0):
			boundary[yr, xr]=1; yr+=1; # 6

		if(boundary[yl, xl]==0):
			boundary[yl, xl]=1; yl-=1; # 2

	end_pts[6] = (xr, yr); end_pts[2] = (xl,yl);


	for i in range(len(end_pts)):

		radius_list[i] = np.linalg.norm(np.array(end_pts[i]) - centre)


		
	return (boundary, radius_list, end_pts)
