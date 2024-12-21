from django.shortcuts import render
import numpy as np
import pandas as pd
import joblib as jb
from sklearn.linear_model import LinearRegression


def main(request):
    return render(request, "main/index.html", context={})

def transform_features(data: pd.DataFrame):
    
    # LOAD TRAIN DATASET
    total_ds = pd.read_csv('./assets/Ames_NO_Missing_Data.csv')
    
    # CONCAT TRAIN DATASET WITH INPUT DATA ---> FOR DUMMIES
    final_df = pd.concat([total_ds,data],axis=0)

    # TRANSFORM MS BUILD CLASS TO STR
    final_df['MS SubClass'] = final_df['MS SubClass'].apply(str) 
    
    # ********************* TARIN DS *************************

    total_ds['MS SubClass'] = total_ds['MS SubClass'].apply(str)


    # ***************** STR | NUMS ***************************

    df_objs = final_df.select_dtypes(include='object')
    df_nums = final_df.select_dtypes(exclude='object') 


    model_obj_cls = total_ds.select_dtypes(include='object')
    model_num_cls = total_ds.select_dtypes(exclude='object')
    
    # ****************** GET DUMMIES ****************************
    df_objs = pd.get_dummies(df_objs, drop_first=True)
    model_obj_cls = pd.get_dummies(model_obj_cls, drop_first=True)


    model_obj_colums = model_obj_cls.columns
    ds_dummies_cols = df_objs.columns
    cols = [col for col in list(ds_dummies_cols) if col in list(model_obj_colums)]
    
            
    df_objs = df_objs[cols]
            
    final_df_with_dummies = pd.concat([df_nums, df_objs],axis=1) 
   

    return final_df_with_dummies


def predict_price(data: pd.DataFrame):

    # LOAD MODEL 
    model = jb.load("./assets/linear_model.pkl")
    X = data.drop('SalePrice', axis=1)

    # MARKE PREDICTIONS
    prediction = model.predict(X.tail(2))
    
    return prediction


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
                'SalePrice': [0],
                #'alley': request.POST.get('Alley', ""),
                #'fence': request.POST.get('Fence', ""),      
            }

    
            data_df = pd.DataFrame(data_map)
          
            
            final_df_with_dummies = transform_features(data_df)
            print('TRANSFORMATION FAITE finale')
            print(f"LA LONGUEUR: {len(final_df_with_dummies)}x{len(final_df_with_dummies.columns)}")
            
         
            prediction = predict_price(final_df_with_dummies)
            print(f"LES PRÉDICTIONS : ${prediction}")

            return render(request, "main/index.html", {"prediction": prediction[-1]})

        except Exception as e:
            # Gestion des erreurs
            print("Erreur :", e)
            return render(request, "main/index.html", {"error": str(e)})

    return render(request, "main/index.html")
