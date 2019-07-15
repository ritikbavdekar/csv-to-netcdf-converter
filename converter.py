import os
import scipy
import numpy
import netCDF4
import csv

from numpy import arange, dtype 

rootdir = os.getcwd()
filelist=list()
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filelist.append(subdir + os.sep + file)

obstime = []
tempr = []
rh =[]
ws = []
wd = []
ap = []
no=[]
ncout = netCDF4.Dataset('station_data.nc','w')
j=0
for i in range(len(filelist)):
	j=j+1
	f = open(filelist[i], 'r').readlines()

	for line in f[0:]:                          #Put 1 instead if column headings present
	    fields = line.split(',')
	    obstime.append(fields[0])
	    tempr.append(fields[1])
	    rh.append(fields[2])#country
	    ws.append(int(fields[3]))#code
	    wd.append(float(fields[4]))#lat
	    ap.append(float(fields[5]))
	    no.append(j)#lon
ncout.createDimension('serial number',no)
num=ncout.createVariable('serial number',dtype('int').char,('serial number'))
time = ncout.createVariable('obstime',dtype('object').char,('serial number',))
temperature = ncout.createVariable('tempr',dtype('float32').char,('serial number'))
relhumid = ncout.createVariable('rh',dtype('float32').char,('serial number'))
windspeed = ncout.createVariable('ws',dtype('float32').char,('serial number'))
winddirection=ncout.createVariable('wd',dtype('float32').char,('serial number'))
airpress = ncout.createVariable('ap',dtype('float32').char,('serial number'))

num[:]= no
time[:] =obstime
temperature[:]=tempr
relhumid[:]=rh
windspeed[:]=ws
winddirection[:]=wd
airpress[:]=ap

ncout.close()







        