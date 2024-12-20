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

"""

def main(request):
    return render(request, "main/index.html", context={})


def transform_data_map_to_dataframe(data_map: dict):

    data = pd.DataFrame([data_map])  # Crée un dataframe avec une seule ligne
    return data


def transform_features(data: pd.DataFrame):

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

"""
"""
def predict(request):
    if request.method == "POST":
        try:
            # Récupération des données depuis le formulaire HTML
            ms_subclass = int(request.POST.get('ms_subclass', 0))
            ms_zoning = request.POST.get('ms_zoning', "")
            lot_area = float(request.POST.get('lot_area', 0))
            lot_frontage = float(request.POST.get('LotFrontage', 0))
            alley = request.POST.get('Alley', "")
            street = request.POST.get('street', "")
            land_contour = request.POST.get('LandContour', "")
            lot_shape = request.POST.get('lot_shape', "")
            land_slope = request.POST.get('LandSlope', "")
            neighborhood = request.POST.get('Neighborhood', "")
            condition1 = request.POST.get('Condition1', "")
            condition2 = request.POST.get('Condition2', "")
            bldg_type = request.POST.get('BldgType', "")
            house_style = request.POST.get('HouseStyle', "")
            utilities = request.POST.get('Utilities', "")
            lot_config = request.POST.get('LotConfig', "")
            roof_style = request.POST.get('roof_style', "")
            roof_matl = request.POST.get('roof_matl', "")
            year_built = int(request.POST.get('year_built', 0))
            year_remod_add = int(request.POST.get('year_remod_add', 0))
            exterior1st = request.POST.get('Exterior1st', "")
            exterior2nd = request.POST.get('exterior2nd', "")
            mas_vnr_type = request.POST.get('Mas_vnr_type', "")
            mas_vnr_area = float(request.POST.get('Mas_vnr_area', 0))
            exter_qual = request.POST.get('exter_qual', "")
            exter_cond = request.POST.get('exter_cond', "")
            foundation = request.POST.get('foundation', "")
            bsmt_qual = request.POST.get('BsmtQual', "")
            bsmt_cond = request.POST.get('BsmtCond', "")
            bsmt_exposure = request.POST.get('BsmtExposure', "")
            bsmt_fin_type1 = request.POST.get('BsmtFinType1', "")
            bsmt_fin_sf1 = float(request.POST.get('BsmtFinSF1', 0))
            bsmt_fin_type2 = request.POST.get('BsmtFinType2', "")
            bsmt_fin_sf2 = float(request.POST.get('BsmtFinSF2', 0))
            bsmt_unf_sf = float(request.POST.get('BsmtUnfSF', 0))
            total_bsmt_sf = float(request.POST.get('TotalBsmtSF', 0))
            heating = request.POST.get('Heating', "")
            heating_qc = request.POST.get('HeatingQC', "")
            central_air = request.POST.get('CentralAir', "")
            electrical = request.POST.get('Electrical', "")
            first_flr_sf = float(request.POST.get('1stFlrSF', 0))
            second_flr_sf = float(request.POST.get('2ndFlrSF', 0))
            low_qual_fin_sf = float(request.POST.get('LowQualFinSF', 0))
            gr_liv_area = float(request.POST.get('GrLivArea', 0))
            bsmt_full_bath = int(request.POST.get('BsmtFullBath', 0))
            bsmt_half_bath = int(request.POST.get('BsmtHalfBath', 0))
            full_bath = int(request.POST.get('FullBath', 0))
            half_bath = int(request.POST.get('HalfBath', 0))
            bedroom = int(request.POST.get('bedroom', 0))
            kitchen = int(request.POST.get('Kitchen', 0))
            kitchen_qual = request.POST.get('kitchen_qual', "")
            tot_rms_abv_grd = int(request.POST.get('TotRmsAbvGrd', 0))
            functional = request.POST.get('Functional', "")
            fireplaces = int(request.POST.get('Fireplaces', 0))
            garage_yr_blt = int(request.POST.get('GarageYrBlt', 0))
            garage_finish = request.POST.get('GarageFinish', "")
            garage_cars = int(request.POST.get('GarageCars', 0))
            garage_area = float(request.POST.get('GarageArea', 0))
            paved_drive = request.POST.get('PavedDrive', "")
            wood_deck_sf = float(request.POST.get('WoodDeckSF', 0))
            open_porch_sf = float(request.POST.get('OpenPorchSF', 0))
            enclosed_porch = float(request.POST.get('EnclosedPorch', 0))
            three_ssn_porch = float(request.POST.get('3SsnPorch', 0))
            screen_porch = float(request.POST.get('ScreenPorch', 0))
            pool_area = float(request.POST.get('PoolArea', 0))
            fence = request.POST.get('Fence', "")

            # Création du DataFrame à partir des données
            data_map = {
                'ms_subclass': ms_subclass,
                'ms_zoning': ms_zoning,
                'lot_area': lot_area,
                'lot_frontage': lot_frontage,
                'alley': alley,
                'street': street,
                'land_contour': land_contour,
                'lot_shape': lot_shape,
                'land_slope': land_slope,
                'neighborhood': neighborhood,
                'condition1': condition1,
                'condition2': condition2,
                'bldg_type': bldg_type,
                'house_style': house_style,
                'utilities': utilities,
                'lot_config': lot_config,
                'roof_style': roof_style,
                'roof_matl': roof_matl,
                'year_built': year_built,
                'year_remod_add': year_remod_add,
                'exterior1st': exterior1st,
                'exterior2nd': exterior2nd,
                'mas_vnr_type': mas_vnr_type,
                'mas_vnr_area': mas_vnr_area,
                'exter_qual': exter_qual,
                'exter_cond': exter_cond,
                'foundation': foundation,
                'bsmt_qual': bsmt_qual,
                'bsmt_cond': bsmt_cond,
                'bsmt_exposure': bsmt_exposure,
                'bsmt_fin_type1': bsmt_fin_type1,
                'bsmt_fin_sf1': bsmt_fin_sf1,
                'bsmt_fin_type2': bsmt_fin_type2,
                'bsmt_fin_sf2': bsmt_fin_sf2,
                'bsmt_unf_sf': bsmt_unf_sf,
                'total_bsmt_sf': total_bsmt_sf,
                'heating': heating,
                'heating_qc': heating_qc,
                'central_air': central_air,
                'electrical': electrical,
                'first_flr_sf': first_flr_sf,
                'second_flr_sf': second_flr_sf,
                'low_qual_fin_sf': low_qual_fin_sf,
                'gr_liv_area': gr_liv_area,
                'bsmt_full_bath': bsmt_full_bath,
                'bsmt_half_bath': bsmt_half_bath,
                'full_bath': full_bath,
                'half_bath': half_bath,
                'bedroom': bedroom,
                'kitchen': kitchen,
                'kitchen_qual': kitchen_qual,
                'tot_rms_abv_grd': tot_rms_abv_grd,
                'functional': functional,
                'fireplaces': fireplaces,
                'garage_yr_blt': garage_yr_blt,
                'garage_finish': garage_finish,
                'garage_cars': garage_cars,
                'garage_area': garage_area,
                'paved_drive': paved_drive,
                'wood_deck_sf': wood_deck_sf,
                'open_porch_sf': open_porch_sf,
                'enclosed_porch': enclosed_porch,
                'three_ssn_porch': three_ssn_porch,
                'screen_porch': screen_porch,
                'pool_area': pool_area,
                'fence': fence,
            }

            # Vérification des données reçues
            print("Données reçues :", data_map)

            # Transformation des données
            data_df = transform_data_map_to_dataframe(data_map)
            data_df_transformed = transform_features(data_df)

            # Chargement du modèle et prédiction
            model = jb.load("./assets/linear_model.pkl")
            prediction = model.predict(data_df_transformed)
            return render(request, "main/index.html", {"prediction": prediction[0]})
           

        except Exception as e:
            # Gestion des erreurs
            return render(request, "main/index.html", {"error": str(e)})

    return render(request, "main/index.html")
"""

"""
def predict(request):
    if request.method == "POST":
        try:
            # Récupération des données depuis le formulaire HTML
            data_map = {
                'ms_subclass': int(request.POST.get('ms_subclass', 0)),
                'ms_zoning': request.POST.get('ms_zoning', ""),
                'lot_area': float(request.POST.get('lot_area', 0)),
                'lot_frontage': float(request.POST.get('LotFrontage', 0)),
                'alley': request.POST.get('Alley', ""),
                'street': request.POST.get('street', ""),
                'land_contour': request.POST.get('LandContour', ""),
                'lot_shape': request.POST.get('lot_shape', ""),
                'land_slope': request.POST.get('LandSlope', ""),
                'neighborhood': request.POST.get('Neighborhood', ""),
                'condition1': request.POST.get('Condition1', ""),
                'condition2': request.POST.get('Condition2', ""),
                'bldg_type': request.POST.get('BldgType', ""),
                'house_style': request.POST.get('HouseStyle', ""),
                'utilities': request.POST.get('Utilities', ""),
                'lot_config': request.POST.get('LotConfig', ""),
                'roof_style': request.POST.get('roof_style', ""),
                'roof_matl': request.POST.get('roof_matl', ""),
                'year_built': int(request.POST.get('year_built', 0)),
                'year_remod_add': int(request.POST.get('year_remod_add', 0)),
                'exterior1st': request.POST.get('Exterior1st', ""),
                'exterior2nd': request.POST.get('exterior2nd', ""),
                'mas_vnr_type': request.POST.get('Mas_vnr_type', ""),
                'mas_vnr_area': float(request.POST.get('Mas_vnr_area', 0)),
                'exter_qual': request.POST.get('exter_qual', ""),
                'exter_cond': request.POST.get('exter_cond', ""),
                'foundation': request.POST.get('foundation', ""),
                'bsmt_qual': request.POST.get('BsmtQual', ""),
                'bsmt_cond': request.POST.get('BsmtCond', ""),
                'bsmt_exposure': request.POST.get('BsmtExposure', ""),
                'bsmt_fin_type1': request.POST.get('BsmtFinType1', ""),
                'bsmt_fin_sf1': float(request.POST.get('BsmtFinSF1', 0)),
                'bsmt_fin_type2': request.POST.get('BsmtFinType2', ""),
                'bsmt_fin_sf2': float(request.POST.get('BsmtFinSF2', 0)),
                'bsmt_unf_sf': float(request.POST.get('BsmtUnfSF', 0)),
                'total_bsmt_sf': float(request.POST.get('TotalBsmtSF', 0)),
                'heating': request.POST.get('Heating', ""),
                'heating_qc': request.POST.get('HeatingQC', ""),
                'central_air': request.POST.get('CentralAir', ""),
                'electrical': request.POST.get('Electrical', ""),
                'first_flr_sf': float(request.POST.get('1stFlrSF', 0)),
                'second_flr_sf': float(request.POST.get('2ndFlrSF', 0)),
                'low_qual_fin_sf': float(request.POST.get('LowQualFinSF', 0)),
                'gr_liv_area': float(request.POST.get('GrLivArea', 0)),
                'bsmt_full_bath': int(request.POST.get('BsmtFullBath', 0)),
                'bsmt_half_bath': int(request.POST.get('BsmtHalfBath', 0)),
                'full_bath': int(request.POST.get('FullBath', 0)),
                'half_bath': int(request.POST.get('HalfBath', 0)),
                'bedroom': int(request.POST.get('bedroom', 0)),
                'kitchen': int(request.POST.get('Kitchen', 0)),
                'kitchen_qual': request.POST.get('kitchen_qual', ""),
                'tot_rms_abv_grd': int(request.POST.get('TotRmsAbvGrd', 0)),
                'functional': request.POST.get('Functional', ""),
                'fireplaces': int(request.POST.get('Fireplaces', 0)),
                'garage_yr_blt': int(request.POST.get('GarageYrBlt', 0)),
                'garage_finish': request.POST.get('GarageFinish', ""),
                'garage_cars': int(request.POST.get('GarageCars', 0)),
                'garage_area': float(request.POST.get('GarageArea', 0)),
                'paved_drive': request.POST.get('PavedDrive', ""),
                'wood_deck_sf': float(request.POST.get('WoodDeckSF', 0)),
                'open_porch_sf': float(request.POST.get('OpenPorchSF', 0)),
                'enclosed_porch': float(request.POST.get('EnclosedPorch', 0)),
                'three_ssn_porch': float(request.POST.get('3SsnPorch', 0)),
                'screen_porch': float(request.POST.get('ScreenPorch', 0)),
                'pool_area': float(request.POST.get('PoolArea', 0)),
                'fence': request.POST.get('Fence', ""),
            }

            # Vérification des données reçues
            print("Données reçues :", data_map)

            # Transformation des données
            data_df = transform_data_map_to_dataframe(data_map)

            # Supprimer les noms de colonnes pour éviter les conflits
            data_values = data_df.to_numpy()

            # Chargement du modèle et prédiction
            model = jb.load("./assets/linear_model.pkl")
            prediction = model.predict(data_values)

            return render(request, "main/index.html", {"prediction": prediction[0]})

        except Exception as e:
            # Gestion des erreurs
            print("Erreur :", e)
            return render(request, "main/index.html", {"error": str(e)})

    return render(request, "main/index.html")
"""

def main(request):
    return render(request, "main/index.html", context={})

def transform_features(data: pd.DataFrame):
    """
    Transforme les colonnes catégoriques en colonnes numériques et aligne les colonnes avec celles attendues par le modèle.
    """
    # Encode les colonnes catégoriques
    df_objs = data.select_dtypes(include='object')
    df_objs = pd.get_dummies(df_objs, drop_first=True)
    print(df_objs)

    # Colonnes numériques
    df_nums = data.select_dtypes(exclude='object')

    # Concaténation des deux
    transformed_df = pd.concat([df_nums, df_objs], axis=1)

    # Reindexer les colonnes pour correspondre au modèle
    #transformed_df = transformed_df.reindex(columns=expected_columns, fill_value=0)

    return transformed_df

def predict(request):
    if request.method == "POST":
        try:
            # Récupération des données depuis le formulaire HTML
            data_map = {
                'MS SubClass': [int(request.POST.get('ms_subclass'))],
                'MS Zoning': [request.POST.get('ms_zoning')],
                'Lot Frontage': [float(request.POST.get('LotFrontage'))],
                'Lot Area': [float(request.POST.get('lot_area', ))],
                'Street': [request.POST.get('street')],
                'Lot Shape': [request.POST.get('lot_shape')],
                'Land Contour': [request.POST.get('LandContour')],
                'Utilities': [request.POST.get('Utilities')],
                'Lot Config': [request.POST.get('LotConfig')],
                'Land Slope': [request.POST.get('LandSlope')],
                'Neighborhood':[ request.POST.get('Neighborhood')],
                'Condition 1': [request.POST.get('Condition1')],
                'Condition 2': [request.POST.get('Condition2')],
                'Bldg Type': [request.POST.get('BldgType')],
                'House Style': [request.POST.get('HouseStyle')],
                'Overall Qual': [int(request.POST.get('overall_qual'))],
                'Overall Cond': [int(request.POST.get('overall_cond'))],
                'Year Built': [int(request.POST.get('year_built'))],
                'Year Remod/Add': [int(request.POST.get('year_remod_add'))],
                'Roof Style': [request.POST.get('roof_style')],
                'Roof Matl': [request.POST.get('roof_matl')],
                'Exterior 1st': [request.POST.get('Exterior1st')],
                'Exterior 2nd': [request.POST.get('exterior2nd')],
                'Mas Vnr Type': [request.POST.get('Mas_vnr_type')],
                'Mas Vnr Area': [float(request.POST.get('Mas_vnr_area'))],
                'Exter Qual': [request.POST.get('exter_qual')],
                'Exter Cond': [request.POST.get('exter_cond')],
                'Foundation': [request.POST.get('foundation')],
                'Bsmt Qual': [request.POST.get('BsmtQual')],
                'Bsmt Cond': [request.POST.get('BsmtCond')],
                'Bsmt Exposure': [request.POST.get('BsmtExposure')],
                'BsmtFin Type 1': [request.POST.get('BsmtFinType1')],
                'BsmtFin SF 1': [float(request.POST.get('BsmtFinSF1'))],
                'BsmtFin Type 2': [request.POST.get('BsmtFinType2')],
                'BsmtFin SF 2': [float(request.POST.get('BsmtFinSF2'))],
                'Bsmt Unf SF': [float(request.POST.get('BsmtUnfSF'))],
                'Total Bsmt SF': [float(request.POST.get('TotalBsmtSF'))],
                'Heating': [request.POST.get('Heating')],
                'Heating QC': [request.POST.get('HeatingQC')],
                'Central Air': [request.POST.get('CentralAir')],
                'Electrical': [request.POST.get('Electrical')],
                '1st Flr SF': [float(request.POST.get('1stFlrSF'))],
                '2nd Flr SF': [float(request.POST.get('2ndFlrSF'))],
                'Low Qual Fin SF': [float(request.POST.get('LowQualFinSF'))],
                'Gr Liv Area': [float(request.POST.get('GrLivArea'))],
                'Bsmt Full Bath': [int(request.POST.get('BsmtFullBath'))],
                'Bsmt Half Bath': [int(request.POST.get('BsmtHalfBath'))],
                'Full Bath': [int(request.POST.get('FullBath'))],
                'Half Bath': [int(request.POST.get('HalfBath'))],
                'Bedroom AbvGr': [int(request.POST.get('bedroom'))],
                'Kitchen AbvGr': [int(request.POST.get('Kitchen'))],
                'Kitchen Qual':[ request.POST.get('kitchen_qual')],
                'TotRms AbvGrd': [int(request.POST.get('TotRmsAbvGrd'))],
                'Functional': [request.POST.get('Functional')],
                'Fireplaces': [int(request.POST.get('Fireplaces'))],
                'Fireplace Qu': [request.POST.get('FireplaceQu')],
                'Garage Type': [request.POST.get('GarageType')],
                'Garage Yr Blt': [int(request.POST.get('GarageYrBlt'))],
                'Garage Finish': [request.POST.get('GarageFinish')],
                'Garage Cars': [int(request.POST.get('GarageCars'))],
                'Garage Area': [float(request.POST.get('GarageArea'))],
                'Garage Qual': [request.POST.get('GarageQual')],
                'Garage Cond': [request.POST.get('GarageCond')],
                'Paved Drive': [request.POST.get('PavedDrive')],
                'Wood Deck SF': [float(request.POST.get('WoodDeckSF'))],
                'Open Porch SF': [float(request.POST.get('OpenPorchSF'))],
                'Enclosed Porch': [float(request.POST.get('EnclosedPorch'))],
                '3Ssn Porch': [float(request.POST.get('3SsnPorch'))],
                'Screen Porch': [float(request.POST.get('ScreenPorch'))],
                'Pool Area': [float(request.POST.get('PoolArea'))],
                'Misc Val': [float(request.POST.get('MiscVal'))],
                'Mo Sold': [float(request.POST.get('MoSold'))],
                'Yr Sold': [float(request.POST.get('YrSold'))],
                'Sale Type': [request.POST.get('SaleType')],
                'Sale Condition': [request.POST.get('SaleCondition')],
                #'SalePrice': int(request.POST.get('SalePrice', 0)),
                #'alley': request.POST.get('Alley', ""),
                #'fence': request.POST.get('Fence', ""),      
            }

            #print(f" nos data {data_map}")
            # Transformation des données
            data_df = pd.DataFrame(data_map)
            #print(f" c'est pour la transformation {data_df}")
            # Encode les colonnes catégoriques
            df_objs = data_df.select_dtypes(include='object')

            #print("Colonnes catégoriques (df_objs):")
            #print(df_objs.dtypes)
            #print(df_objs.head())
            df_objs = df_objs.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
            df_objs = df_objs.fillna("Missing")

            for col in df_objs.columns:
                unique_values = df_objs[col].nunique()
                print(f"Colonne '{col}' - Nombre de valeurs uniques : {unique_values}")

            df_objs_dummies = pd.get_dummies(df_objs, drop_first=True)
            #print(f"c'est pour les data categorielle{df_objs}")
            print(f"Colonnes après encodage (dummies): {df_objs_dummies.columns.tolist()}")
            print(df_objs_dummies.head())
            print(f"c'est pour les data categorielle dummies {df_objs_dummies}")

           # Colonnes numériques
            df_nums = data_df.select_dtypes(exclude='object')
            #print(f" c'est pour les data numerique{df_nums}")

          # Concaténation des deux
            #transformed_df = pd.concat([df_nums, df_objs], axis=1)
            # Chargement du modèle
            model = jb.load("./assets/linear_model.pkl")

            # Aligner les colonnes avec celles attendues par le modèle
           # expected_columns = model.feature_names_in_
            #data_df_transformed = transform_features(data_df)
           # print(len(data_df_transformed))

            # Prédiction
            #prediction = model.predict(transformed_df)

            return render(request, "main/index.html", {"prediction": prediction[0]})

        except Exception as e:
            # Gestion des erreurs
            print("Erreur :", e)
            return render(request, "main/index.html", {"error": str(e)})

    return render(request, "main/index.html")
