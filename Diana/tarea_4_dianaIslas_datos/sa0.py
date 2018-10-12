#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:12:48 2018

@author: amagaldi
"""

from datetime import datetime
import metpy
from siphon.catalog import TDSCatalog

date = datetime.utcnow()
channel = 8
region = 'Mesoscale-2'

cat = TDSCatalog('http://thredds-test.unidata.ucar.edu/thredds/catalog/satellite/goes16/GOES16/'
                 '{}/Channel{:02d}/{:%Y%m%d}/catalog.xml'.format(region, channel, date))
cat.datasets[-5:]

ds = cat.datasets[-2]
ds = ds.remote_access(service='OPENDAP', use_xarray=True)
list(ds)
print(ds['Sectorized_CMI'])


dat = ds.metpy.parse_cf('Sectorized_CMI')
proj = dat.metpy.cartopy_crs


print(dat)
print(proj)


x = dat['x']
y = dat['y']


import matplotlib.pyplot as plt


# Create a new figure with size 10" by 10"
fig = plt.figure(figsize=(10, 10))

# Put a single axes on this figure; set the projection for the axes to be our
# Lambert conformal projection
ax = fig.add_subplot(1, 1, 1, projection=proj)

# Plot the data with mostly the defaults
# Note, we save the image returned by imshow for later...
im = ax.imshow(dat, extent=(x.min(), x.max(), y.min(), y.max()), origin='upper')

# Add high-resolution coastlines to the plot
ax.coastlines(resolution='50m', color='black')
# Redisplay modified figure












