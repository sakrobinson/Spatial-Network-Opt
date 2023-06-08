# Import necessary libraries
import os
import sys
import traceback
import numpy as np
import arcpy
from scipy import optimize

try:
    # Set up path and file names for inputs/outputs
    working_dir = 'C:/path/to/working/directory/'  # replace with your desired directory name
    if not os.path.exists(working_dir):
        os.mkdir(working_dir)  
    
    # Input paths for shapefiles
    input_shapefile1 = working_dir + 'input_polygon.shp'
    input_shapefile2 = working_dir + 'lengths.dbf'
    output_polyline = working_dir + 'optimized_lines.shp'
    
    # Check existence of files
    if (not arcpy.ExistsFileGDB('in_memory_workspace')):
        arcpy.CreateFileGDB('in_memory_workspace', '/') 
        
    if not arcpy.ExistsRasterLayer('input*'):
       if not arcpy.ExistsTable('input*'):
           raise Exception("Error: Couldn't find input files - check paths")
    
    # Load in input files
    lines_feature = fgdb = arcpy.OpenFeatureDataSource(working_dir + 'input_polygons.gdb')
    lines_fcid = str(fgdb._nativeGetID())
    lines_fldcustids_name = 'FLD_CUSTOMER_ID'
    length_fieldname = 'Length'
    weight_fieldname = 'Weight'
    input_length_table = arcpy.Table.FromRowBand(lines_feature, lines_fcid, lines_fldcustids_name)

    Max_distance = float(arcpy.AddWarningMessage("Maximum distance"))

    # Convert lengths to meters
    input_length_table = input_length_table.getRows()
    input_length_meter = []
    for i in range(len(input_length_table)):
        input_length_meter.append(float(input_length_table[i][0]) * 3937.)  # convert miles to km

    # Define objective function
    def objectiveFunction(x):
        # Calculate new network length and sum of weights after adding N points
        x_sum = sum(x[:N_points] ) / len(input_length_metr)
        total_weight_sum = sum([row[0] * row[1] for row in input_weight_table.asSpatialReference(None).search(*new_lines))] / len(new_lines) # sum total weight values
            return new_total_network_length - old_total_network_length - max_dist * len(new_lines) - max_dist**2 * 0.5 + x_sum * len(new_points) - total_weight_sum * max_dist

try:
    x = optimize.minimize(objectiveFunction, [0]*N_points)
except:
    print('Optimization failed! Try decreasing N_points...')
    exit()

print('\nNew lines:\n{}'.format(',\n'.join([str((x[0]+old_starting_coordinates) for x in zip(*optimized)])))
                                        
