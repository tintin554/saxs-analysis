# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:33:32 2021

@author: Adam Milsom
"""
'''
SAXS analysis objects
'''



import numpy as np
import h5py as h5


class DiamondProcessedNxsReader():
    
    def __init__(self,processed_filename,raw_filename=None):
        
        self.filename = processed_filename
        
        self.I = None
        self.q = None
        self.I_err = None
        
        self.It = None
        self.I0 = None
        
        self.title = None
        
        self.pipeline = None
        
        search_terms = ['data','q','errors']
        
        collected_attr = [self.I,self.q,self.I_err]
        
        with h5.File(processed_filename,'r') as f:
            self.I = np.copy(f.get('processed/result/data'))
            self.q = np.copy(f.get('processed/result/q'))
            self.I_err = np.copy(f.get('processed/result/error'))
            # for i, term in enumerate(search_terms):
            #     for key in f['processed']['result'].keys():
            #         if key == term:
            #             print(f['processed']['result'][key].value)
            #             collected_attr[i] = f['processed']['result'][key].value
        
        # optional transformed I dependent on if 2-, 3- or 4-D data
        # i.e. a grid, vertical/horizontal or single scan
        self.I_transformed = None
        
        

        











