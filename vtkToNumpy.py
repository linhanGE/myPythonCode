# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:55:20 2018

@author: c3216945
"""
import numpy as np
#from vtk.util import numpy_support as VN
import vtk
from vtk.util.numpy_support import vtk_to_numpy
#as_numpy = numpy_support.vtk_to_numpy(vtk_points.GetData())
reader = vtk.vtkPolyDataReader()
#reader = vtk.vtkGenericDataObjectReader()
reader.SetFileName('gp2007000.vtk')
reader.ReadAllVectorsOn()
reader.ReadAllScalarsOn()
reader.Update()
vtk_out = reader.GetOutput()

scalar_names = [reader.GetScalarsNameInFile(i) for i in range(0, reader.GetNumberOfScalarsInFile())]

#p = np.asarray(vtk_out.GetCellData().GetArray('pressure'))
points = vtk_out.GetPoints()
array = points.GetData()
numpy_nodes = vtk_to_numpy(array)
pointData = vtk_out.GetPointData()
scalarData = pointData.GetArray('pressure')
p = vtk_to_numpy(scalarData)
meanp=np.mean(p)
#p = pointData.GetArray('pressure')