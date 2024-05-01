import pandas as pd
import streamlit as st
import numpy as np

class class_data:
    def __init__(self):
        path = r'C:\Users\Mohamed Hamde\OneDrive - Culture and Science City\Desktop\Clean Code AI\streamLite\dataset\data.csv'
        self.data = pd.read_csv(path)

    def add_count(self):
        self.data['count'] = 1
        return self.data
    
    def convert_to_date(self):
        self.data['Start_Time'].astype('object')
        self.data['Start_Time'] = pd.to_datetime(self.data['Start_Time'], format='mixed')
        return self.data

    def split_date(self):
        self.data['years'] = self.data['Start_Time'].dt.year
        self.data['months'] = self.data['Start_Time'].dt.month
        self.data['days'] = self.data['Start_Time'].dt.day
        self.data['hours'] = self.data['Start_Time'].dt.hour
        return self.data
    
    def int_columns(self):
        intFloat_data = []
        intFloat_data.append('Severity')
        for i in self.data.columns:
            if (self.data[i].dtype == np.float64):
                intFloat_data.append(i)
        return intFloat_data

    def get_correlation(self):
        intFloat_data = self.int_columns() 
        data_cor = pd.DataFrame()
        for i in intFloat_data:
            new_data = self.data[i]
            data_cor = pd.concat([data_cor, new_data], axis=1)
        return data_cor