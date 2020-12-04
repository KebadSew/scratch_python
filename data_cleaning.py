# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:07:57 2020

@author: legen
"""

from clear_console import cls
import pandas as pd

cls()

data = pd.DataFrame({'language':['English', 'French', 'Spanish', 
                                 'Amharic','Oromifa','Tigrigna',
                                 'Amharic','english']})

dict_country = {'English':'USA', 'French':'France', 
                'Spanish':'Spain', 'Amharic':'Ethiopia', 
                'Oromifa':'Ethiopia', 'Tigrigna':'Ethiopia'}

data['language'] = data['language'].str.title()

data = data.drop_duplicates(['language'], keep='last')

data['Country'] = data['language'].map(dict_country)

print(data)
