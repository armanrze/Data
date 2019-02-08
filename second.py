import matplotlib.pyplot as plt
import geopandas as gpd
import pysal as ps
from pysal.contrib.viz import mapping as maps
shapetest=gpd.read_file("C:\Arman\learning\TxDOT_AADT_crop.shp")
shapetest.head()
shapetest.plot()
print ("hello world")