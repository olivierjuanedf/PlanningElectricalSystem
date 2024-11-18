# -*- coding: utf-8 -*-
"""
First very simple toy Unit Commitment model of... YOUR COUNTRY zone - alone -> with PyPSA and ERAA data
-> 
(i) copy/paste/rename this file according to your country name
(ii) copy/paste pieces of code from long_term_uc/my_toy_ex_italy.py to this created file
(iii) Also, set the parameters of your country electricity generators in file {your country}_parameters.py,
following/adapting model of long_term_uc/toy_model_params/italy_parameters.py
"""


import os, sys
sys.path += [os.path.dirname(os.path.dirname(__file__))]
