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
            LotFrontage = int(request.POST.get('LotFrontage', 0))
            Alley = request.POST.get('Alley', "")
            street = request.POST.get('street', "")
            LandContour = request.POST.get('LandContour', "")
            lot_shape = request.POST.get('lot_shape', "")
            LandSlope = request.POST.get('LandSlope', "")
            Neighborhood = request.POST.get('Neighborhood', "")
            Condition1 = request.POST.get('Condition1', "")
            Condition2 = request.POST.get('Condition2', "")
            BldgType = request.POST.get('BldgType', "")
            HouseStyle = request.POST.get('HouseStyle', "")
            Utilities = request.POST.get('Utilities', "")
            LotConfig = request.POST.get('LotConfig', "")
            roof_style = request.POST.get('roof_style', "")
            roof_matl = request.POST.get('roof_matl', "")
            year_built = int(request.POST.get('year_built', 0))
            Exterior1st = request.POST.get('Exterior1st', "")
            year_remod_add = int(request.POST.get('year_remod_add', 0))
            overall_qual = int(request.POST.get('overall_qual', 0))
            overall_cond = int(request.POST.get('overall_cond', 0))
            exter_qual = request.POST.get('exter_qual', "")
            foundation = request.POST.get('foundation', "")
            exterior2nd = request.POST.get('exterior2nd', "")
            Exterior1st = request.POST.get('Exterior1st', "")
            Mas_vnr_type = request.POST.get('Mas_vnr_type', "")
            BsmtQual = request.POST.get('BsmtQual', "")
            BsmtCond = request.POST.get('BsmtCond', "")
            BsmtExposure = request.POST.get('BsmtExposure', "")
            BsmtFinType1 = request.POST.get('BsmtFinType1', "")
            BsmtFinType2 = request.POST.get('BsmtFinType2', "")
            Mas_vnr_area = float(request.POST.get('Mas_vnr_area', 0))
            exter_cond = request.POST.get('exter_cond', "")
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
                'LotConfig': LotConfig,
                'LotFrontage': LotFrontage,
                'Alley': Alley,
                'LandContour':  LandContour,
                'Utilities':  Utilities,
                'LandSlope': LandSlope,
                'Neighborhood': Neighborhood,
                'Condition1': Condition1,
                'Condition2': Condition2,
                'BldgType': BldgType,
                'HouseStyle': HouseStyle,
                'roof_style': roof_style,
                'roof_matl': roof_matl,
                'year_remod_add': year_remod_add,
                'exter_qual': exter_qual,
                'year_built': year_built,
                'foundation': foundation,
                'Exterior1st' : Exterior1st,
                'Mas_vnr_type': Mas_vnr_type,
                'exter_cond': exterior_cond,
                'exterior2nd': exterior2nd,
                'Mas_vnr_area': Mas_vnr_area,
                'BsmtQual': BsmtQual,
                'BsmtCond': BsmtCond,
                'BsmtExposure': BsmtExposure,
                'BsmtFinType1': BsmtFinType1,
                'BsmtFinType2': BsmtFinType2,
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
