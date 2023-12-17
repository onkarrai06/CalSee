import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
import os
from knn.prepare import parse_data_knn

K = 9

def predict_weight(food, side_area, top_area):

    if os.path.exists(".\DIPv1\knn\density_procs.csv"):
        df = pd.read_csv(".\DIPv1\knn\density_procs.csv")
    else:
        df = parse_data_knn()
    
    #filter knn model with food
    df = df[df['image_name'] == food]

    #make knn model with side_area and top_area as features
    df = df[['side_area', 'top_area', 'real_calorie']]
    df = df.dropna()
    
    #make knn model
    knn = KNeighborsRegressor(n_neighbors=K)
    knn.fit(df[['side_area', 'top_area']], df['real_calorie'])

    #predict real_mass
    predict = knn.predict([[side_area, top_area]])
    
    return predict[0] 
 