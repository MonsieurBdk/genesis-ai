from django.shortcuts import render
import numpy as np
import pandas as pd
import joblib as jb


# Create your views here.
def main(request):
    return render(request, "main/index.html", context={})


def transform_data_map_to_dataframe(data_map: map):
    # POUR TRANSFORMER LES DONNÉES EN DATAFRAME ( TRAITABLES EN PANDA )

    data = pd.DataFrame(data=data_map)
    return data


def transform_feateares(data: pd.DataFrame):
    # POUR PRÉPARER LES DONNÉES À LA PRÉDICTION

    if (data is pd.DataFrame):
        df['MS SubClass'] = df['MS SubClass'].apply(str)
        df_nums = df.select_dtypes(exclude='object')
        df_objs = df.select_dtypes(include='object')
        df_objs = pd.get_dummies(df_objs, drop_first=True)
        final_df = pd.concat([df_nums, df_objs], axis=1)
        return final_df
    return None


"""
def predict(request):
    if request.method == 'GET':
        data_entry_1 = request.GET.get('predict1')
        data_entry_2 = request.GET.get('predict2')

        data_entry_transformed = pd.DataFrame({
            'predict1': [data_entry_1],
            'predict2': [data_entry_2],
        })
        model = jb.load("./assets/linear_model.pkl")
        prediction = model.predict(data_entry_transformed)
        return render(request, 'index.html', {prediction: prediction[0]})
"""


def predict(request):
    if request.method == "POST":
        # Récupération des données du formulaire html
        ms_subclass = int(request.POST.get('ms_subclass'))
        ms_zoning = request.POST.get('ms_zoning')
        lot_area = float(request.POST.get('lot_area'))
        street = request.POST.get('street')
        lot_shape = request.POST.get('lot_shape')
        year_built = int(request.POST.get('year_built'))
        overall_qual = int(request.POST.get('overall_qual'))
        overall_cond = int(request.POST.get('overall_cond'))
        gr_liv_area = float(request.POST.get('gr_liv_area'))
        full_bath = int(request.POST.get('full_bath'))
        bedroom = int(request.POST.get('bedroom'))
        kitchen_qual = request.POST.get('kitchen_qual')

    return render(request, "main/index.html")
