# -*- coding: utf-8 -*-

import os
import pandas as pd


def find_files(folder_location, keys, keep=False):
    
    #Setting up folder location for cythonising package
    file_loc = folder_location
    os.chdir(file_loc)
    
    #For keeping track for files not to binary compile
    df_file = pd.DataFrame()

    #Finding all the .py files present in directory
    for root, dirs, files in os.walk(file_loc):
        for file in files:
            if file.endswith('.py'):
                file_py = os.path.join(root, file)
                new_name = file.split('\\')[-1].split('.')[0]+'.c'
                file_c = os.path.join(root, new_name)
                df_file = pd.concat([ df_file, pd.DataFrame( [[file, file_py,file_c]] ) ], axis = 0)
            
    #setting names of columns of dataframe
    df_file.columns = ['file', 'filepy','filec']
    
    #Dropping __init__ and main.py files for not cythonising
    for i in keys:
       df_file = df_file[ df_file.file != i] 
    

    return df_file
#%%
def make_setup(dataframe):
    
    df_file = dataframe.copy()
    
    filename = 'setup.py'
    files = list ( df_file['filepy'] )
    
    line1 = 'from distutils.core import setup'
    line2 = 'from Cython.Build import cythonize'
    line3 = 'setup(ext_modules = cythonize('+str(files)+',exclude_failures=True))'
    
    L = [line1, line2, line3]
    
    with open(filename,'w') as file:
        for line in L:
            file.write(line+'\n')
    
    file.close()

    print('setup.py file generated')
    
    return 1

if __name__ == '__main__':
    import argparse
    from distutils.util import strtobool as stb
    
    parser = argparse.ArgumentParser(description='Welcome to CyMOD - A Python Module to generate Compiled Binaries using cython')
    
    parser.add_argument('path', metavar='PATH', help='Package Path' )
    
    parser.add_argument('--keep','-K', default='False' ,help = 'True if .py files are desirable in package')
    parser.add_argument('--addn','-A', default='__init__.py,main.py', help='Python file name as exception separated by comma without spaces, default: __init__.py,main.py')
    
    args = parser.parse_args()
    
    folder_loc = args.path 
    keep = bool(stb(args.keep))
    addn = args.addn
    addn = addn.split(',')
    
    df = find_files(folder_loc, addn, keep)
    make_setup(df)
    
    #Calling python file from commandline
    err = os.system('python setup.py build_ext --inplace')

    if(err == 0):
        print('='*20,'Binary compilation successfull','='*20)
        print('~'*20,'Please remove Build folder manually','~'*20)
        os.remove('setup.py')
        if(keep != True):
            for filepy, filec in zip( list(df.filepy), list(df.filec) ):
                os.remove( filepy)
                os.remove( filec )
            
    else:
        print('Some error occured')
