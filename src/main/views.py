from django.shortcuts import render
import numpy as np
import pandas as pd
import joblib as jb

"""
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
    # Création d'un dataframe avec les données du formulaire
    data_map = {
       'ms_subclass': ms_subclass,
       'ms_zoning': ms_zoning,
        'lot_area': lot_area,
       'street': street,
        'lot_shape': lot_shape,
        'year_built': year_built,
        'overall_qual': overall_qual,
        'overall_cond': overall_cond,
        'gr_liv_area': gr_liv_area,
        'full_bath': full_bath,
        'bedroom': bedroom,
        'kitchen_qual': kitchen_qual,
    }
    data_df = transform_data_map_to_dataframe(data_map)
    data_df_transformed = transform_feateares(data_df)
    model = jb.load("./assets/linear_model.pkl")
    prediction = model.predict(data_df_transformed)
    return render(request, "main/index.html", {"prediction": prediction[0]})
    #return render(request, "main/index.html", context={"ms_subclass": ms_subclass, "ms_zoning": ms_zoning, "lot_area": lot_area, "street": street, "lot_shape": lot_shape, "year_built": year_built, "overall_qual": overall_qual, "overall_cond": overall_cond, "gr_liv_area": gr_liv_area, "full

    #return render(request, "main/index.html")
"""



def main(request):
    return render(request, "main/index.html", context={})


def transform_data_map_to_dataframe(data_map: dict):
    """
    POUR TRANSFORMER LES DONNÉES EN DATAFRAME (TRAITABLES PAR PANDAS)
    """
    data = pd.DataFrame([data_map])  # Crée un dataframe avec une seule ligne
    return data


def transform_features(data: pd.DataFrame):
    """
    POUR PRÉPARER LES DONNÉES À LA PRÉDICTION
    """
    if isinstance(data, pd.DataFrame):
        # Convertir les colonnes en type string si nécessaire
        data['ms_subclass'] = data['ms_subclass'].astype(str)
        
        # Séparation des données numériques et catégoriques
        df_nums = data.select_dtypes(exclude='object')
        df_objs = data.select_dtypes(include='object')
        
        # Encodage des colonnes catégoriques
        df_objs = pd.get_dummies(df_objs, drop_first=True)
        
        # Concaténation des données encodées et numériques
        final_df = pd.concat([df_nums, df_objs], axis=1)
        return final_df
    return None


def predict(request):
    if request.method == "POST":
        try:
            # Récupération des données du formulaire HTML
            ms_subclass = int(request.POST.get('ms_subclass', 0))
            ms_zoning = request.POST.get('ms_zoning', "")
            lot_area = float(request.POST.get('lot_area', 0))
            street = request.POST.get('street', "")
            lot_shape = request.POST.get('lot_shape', "")
            year_built = int(request.POST.get('year_built', 0))
            overall_qual = int(request.POST.get('overall_qual', 0))
            overall_cond = int(request.POST.get('overall_cond', 0))
            gr_liv_area = float(request.POST.get('gr_liv_area', 0))
            full_bath = int(request.POST.get('full_bath', 0))
            bedroom = int(request.POST.get('bedroom', 0))
            kitchen_qual = request.POST.get('kitchen_qual', "")
            #dump(ms_subclass)
            
            # Création d'un dataframe avec les données du formulaire
            data_map = {
                'ms_subclass': ms_subclass,
                'ms_zoning': ms_zoning,
                'lot_area': lot_area,
                'street': street,
                'lot_shape': lot_shape,
                'year_built': year_built,
                'overall_qual': overall_qual,
                'overall_cond': overall_cond,
                'gr_liv_area': gr_liv_area,
                'full_bath': full_bath,
                'bedroom_abvgr': bedroom,
                'kitchen_qual': kitchen_qual,
            }
            
            data_df = transform_data_map_to_dataframe(data_map)
            data_df_transformed = transform_features(data_df)
            
            # Chargement du modèle et prédiction
            model = jb.load("./assets/linear_model.pkl")
            prediction = model.predict(data_df_transformed)
            dump(prediction)
            
            return render(request, "main/index.html", {"prediction": prediction[0]})
        
        except Exception as e:
            # En cas d'erreur, retour avec un message
            return render(request, "main/index.html", {"error": str(e)})
    
    return render(request, "main/index.html")
