# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:20:34 2021

@author: vargh
"""
# Imports
import valispace
import keyring

from thermochem.janaf import Janafdb
from scipy.optimize import root_scalar
        
username = 'varghes5' # username for valispace
url = 'polarisproject.valispace.com' # url for our Valispace
id_roy = 'ramir169_onboarding' # id of the project that we are pulling from

# standard valispace API import as detailed in the Polaris Github documentation
valispace_API = valispace.API(url=url, username = username, password = keyring.get_password("valispace", username), )

# Specific valis/matrices. IDs obtained from looking at Valispace
vali_dict = {
    "Pressure": valispace_API.get_matrix(id=9068),
    "mdot":valispace_API.get_vali(id=19912),
    "T0":valispace_API.get_matrix(id=9069)
    }

# A function that processes the valis into a dictionary of either values or dictionaries based on states
# if you look at values dict, m_dot will be a single value since it does not change, and Pressure/T_0 will be dictionaries with the states 'On' and 'Off' as keys for their corresponding values
def process_vali_dict(vali_dict):
    values_dict = {}
    keys = list(vali_dict.keys())
    
    for i in range(len(vali_dict)):
        cur_entry = vali_dict[keys[i]]
        
        if isinstance(cur_entry, list):
            cur_append = {cur_entry_element[0]['shortname']:cur_entry_element[0]['value'] for cur_entry_element in cur_entry}
        
        else:
            cur_append = cur_entry['value']
        
        values_dict[keys[i]] = cur_append
    return values_dict

values_dict = process_vali_dict(vali_dict) # run the processing function
state = 'On' # state being considered

db = Janafdb() # locally intitializes the NIST thermochemical database
p = db.getphasedata(formula='N2') # chemical in question

# objective function to pass to the root_scalar root finder
def eq_to_solve(T_f, values_dict, state):
    
    # locally define values for convenience
    pressure = values_dict['Pressure'][state]*6894.76 # conversion from psi to Pa, pressure
    mdot = values_dict['mdot'] # mass flow rate
    T_0 = values_dict['T0'][state] #  initial temperature
    
    T_avg = (T_f + T_0)/2 # average temperature
    
    cur_cp = p.cp(T_avg).tolist() # calculate c_p at the current average temperature
    
    return(pressure/(mdot*cur_cp) + T_0 - T_f) # the equation we are trying to solve, solved for zero on LHS

soln = root_scalar(eq_to_solve, bracket = [values_dict['T0'][state], 10000], args=(values_dict, state)) # emplor root finder
root = soln.root # numerical value of solution
