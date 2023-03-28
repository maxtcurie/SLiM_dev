import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys as sys

#import SLiM_phys
from SLiM_phys.SLiM_obj import mode_finder

#**********************************************
#**********Start of User block*****************
profile_type= "pfile"          # "ITERDB" "pfile", "profile_e", "profile_both" 
geomfile_type="gfile"          # "gfile"  "GENE_tracor"
outputpath='./../Test_files/'
path='./../Test_files/'
profile_name=path+'p174819.03560'
geomfile_name=path+'g174819.03560'
x0_min=0.93         # beginning of the range in rho_tor
x0_max=0.99         # ending of the range in rho_tor
#************End of User Block*****************
#**********************************************

mode_finder_obj=mode_finder(profile_type,profile_name,\
            geomfile_type,geomfile_name,\
            outputpath,path,x0_min,x0_max)

q_scale=1.03
mode_finder_obj.modify_profile(\
    q_scale=q_scale,q_shift=0.,\
    shat_scale=1.,\
    ne_scale=1,te_scale=1.,\
    ne_shift=0.,te_shift=0.,\
    Doppler_scale=1.,\
    show_plot=False)

mode_finder_obj.Plot_ome_q_surface_demo_no_box(\
    n_min=1,n_max=5,\
    n_unstable=[3,5],\
    with_doppler=False)
