from django.shortcuts import render
import numpy as np
import pandas as pd
import joblib as jb

# Create your views here.
def main(request):
    return render(request, "main/index.html", context={})

def transform_data_map_to_dataframe(data_map:map):
    data = pd.DataFrame(data=data)  
    return data

def transform_feateares(data:pd.DataFrame):
    if(data is pd.DataFrame):
        df['MS SubClass'] = df['MS SubClass'].apply(str)
        df_nums = df.select_dtypes(exclude='object')
        df_objs = df.select_dtypes(include='object')
        df_objs = pd.get_dummies(df_objs,drop_first=True)
        final_df = pd.concat([df_nums,df_objs],axis=1)
        return final_df
    return None

def predict(data:pd.DataFrame):
    model = jb.load("../assets/linear_model.pkl")
    prediction = model.predict(data)
    return prediction

