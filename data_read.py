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
    
    def __init__(self,processed_filename,raw_filename=None,
                 hdf_file_locations = {'I':'processed/result/data',
                                   'q':'processed/result/q',
                                   'I_err':'processed/result/error',
                                   'pipeline':None,}):
        
        self.filename = processed_filename
        
        self.I = None
        self.q = None
        self.I_err = None
        
        self.It = None
        self.I0 = None
        
        self.title = None
        
        self.pipeline = None
        
        self.hdf_file_locations = hdf_file_locations
        
        # search_terms = ['data','q','errors']
        
        collected_attr = [self.I,self.q,self.I_err]
        
        with h5.File(processed_filename,'r') as f:
            self.I = np.copy(f.get(self.hdf_file_locations['I']))
            self.q = np.copy(f.get(self.hdf_file_locations['q']))
            self.I_err = np.copy(f.get(self.hdf_file_locations['I_err']))
            # for i, term in enumerate(search_terms):
            #     for key in f['processed']['result'].keys():
            #         if key == term:
            #             print(f['processed']['result'][key].value)
            #             collected_attr[i] = f['processed']['result'][key].value
        
        # optional transformed I dependent on if 2-, 3- or 4-D data
        # i.e. a grid, vertical/horizontal or single scan
        self.I = np.transpose(self.I[:,0,:])
        
        

# function to make an array of saxs patterns collected at one scan position

def make_saxs_scanpos_arrays(imported_2Ddata_list):
    '''
    This will return q_values* and a 2-D array of shape (len(q),len(imported_2Ddata_list))
    
    imported_2Ddata_list --> list of DiamondProcessedNxsReader objects or numpy arrays containing I vs Q data
                            (rows=q axis, columns=scan number axis, values=I)
    
                            
    Visualisation...
          for each scan:
  
                       frames ->                                               time/scan number ->
                ------------------------                                    ------------------
              |+ + + + + + + + + + + + +   for each frame:                 |+ + + + +
            q |+ + + + + + + + + + + + +    slice each frame               | + + + +
              |+ + + INTENSITIES + + + +  -------------------->          q | INTENSITIES
              |+ + + + + + + + + + + + +    make a dict. of                |+ + + + + 
                                        SAXS patt. vs t for frame(i)    (THIS IS FOR EVERY FRAME,
                                                                         STORED IN A DICT.)
                                        
    returns: q_values, frame_dict (keys correspond to frame numbers)
    
    * will return an empty list for q_vals if only numpy array supplied
    
    '''
    
    assert type(imported_2Ddata_list) == list, "imported_2Ddata_list needs to be a list, even if 1 member"
    
    output_dict = {}

    # for each saxs scan (nxs file if considering diamond data)
    for ind, saxs_array in enumerate(imported_2Ddata_list):
        
        # account for if saxs_array is a numpy array or a DiamondProcessedNxsReader
        # object
        
        try:
            data = saxs_array.I # if DiamondProcessedNxsReader
        except:
            data = saxs_array # if numpy array
        
        # for each frame
        for frameno in np.arange(len(data[0,:])):
            # get the saxs pattern 
            saxs_pattern = data[:,frameno]
            
            # add this saxs pattern to the output dictionary
            # create the key-value pair in the dict for the first set of saxs patterns
            if ind == 0:
                output_dict[f'{frameno}'] = saxs_pattern
        
            else: 
                output_dict[f'{frameno}'] = np.column_stack((output_dict[f'{frameno}'],saxs_pattern))
                
    # will return q vals if a DiamondProcessedNxsReader object was used
    try:            
        return saxs_array.q, output_dict
    
    except:
        return np.array([]), output_dict 
                    










