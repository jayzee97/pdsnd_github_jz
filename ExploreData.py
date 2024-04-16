<<<<<<< HEAD
# Importing modules required to explore survey data
||||||| 8ce79ab
# Importing modules 
=======
#---------------------------#
# Environment Preparation
#---------------------------#
# Importing modules 
>>>>>>> refactoring
import pandas as pd
import functools 

<<<<<<< HEAD
# Reading in public-use source data, downloaded from Census Bureau and saved in '~/udacity-git-course/pdsnd_github_jz'
||||||| 8ce79ab
# Reading in public-use source data, downloaded from Census Bureau
=======
#---------------------------#
# Data Cleaning
#---------------------------#
# Reading in public-use source data, downloaded from Census Bureau
>>>>>>> refactoring
allUnits = pd.read_csv(r'/Users/Jenny/udacity-git-course/pdsnd_github_jz/allunits_puf_21.csv')
occUnits = pd.read_csv(r'/Users/Jenny/udacity-git-course/pdsnd_github_jz/occupied_puf_21.csv')

# Dropping unit weight fields for estimating variance to enhance readability of tables, as these fields will not be used
allUnits2 = allUnits.drop(allUnits.iloc[:, 25:105], axis=1)
occUnits2 = occUnits.drop(occUnits.iloc[:, 152:232], axis=1)

# Merging together the parents (allunits) table with the occupied units table to calculate statistics 
final = pd.merge(allUnits2, occUnits2, how='left', on='CONTROL')

#---------------------------#
# Creating Summary Tables
#---------------------------#
occupancy_stats = final.query("OCC == 1").groupby('BORO')['OCC'].count().reset_index(name='occupied_units')

# Determining counts, by NYC borough, of reported instances of various problems known to occur in housing (value of 1 indicates presence of problem)
floor_stats = final.query("FLOORHOLES == 1").groupby('BORO')["FLOORHOLES"].count().reset_index(name='has_floorholes') 
wall_stats = final.query("WALLHOLES == 1").groupby('BORO')["WALLHOLES"].count().reset_index(name='has_wallholes')
leak_stats = final.query("LEAKS == 1").groupby('BORO')["LEAKS"].count().reset_index(name='has_leaks')
mold_stats = final.query("MOLD == 1").groupby('BORO')["MOLD"].count().reset_index(name='has_mold')

# Merging all summary tables together to create combined, borough-level, table
frames = [occupancy_stats, floor_stats, wall_stats, leak_stats, mold_stats]
borough_issues = functools.reduce(lambda left, right: pd.merge(left, right, on='BORO'), frames)

# Creating new variables containing percentage of units with each problem
for x in ['floorholes', 'wallholes', 'leaks', 'mold']:
    newvar = 'pct_' + x
    sourcevar = 'has_' + x
    borough_issues[newvar] = borough_issues[sourcevar] / borough_issues['occupied_units']

# Viewing results
borough_issues.head(5)


