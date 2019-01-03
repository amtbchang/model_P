# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:41:42 2018

@author: ThinkPad
"""
from sklearn.metrics import r2_score

import numpy as np
import spotpy
from spotpy.dndc.dndc_setup import dndc_setup
#from spotpy.examples.spot_setup_hymod_python import spot_setup
import matplotlib.pyplot as plt


if __name__ == "__main__":
    parallel ='seq'
    # Initialize the Hymod example
    spot_setup = dndc_setup()
    rep=100
    
      
    #Start a sensitivity analysis
    sampler = spotpy.algorithms.fast(spot_setup, dbname='FAST_dndc', dbformat='csv')
    sampler.sample(rep)
    
    # Load the results gained with the fast sampler, stored in FAST_hymod.csv
    results = spotpy.analyser.load_csv_results('FAST_dndc')
    
    # Example plot to show the sensitivity index of each parameter
    spotpy.analyser.plot_fast_sensitivity(results, number_of_sensitiv_pars=3)
    
    # Example to get the sensitivity index of each parameter    
    SI = spotpy.analyser.get_sensitivity_of_fast(results)


#    for i in range(10):
#        x= spot_setup.parameters()['random']
#        sti=(spot_setup.simulation(x))
#        
#        print('%d 组数据为：'%i, x, '###R2：', r2_score(spot_setup.evals, sti))
