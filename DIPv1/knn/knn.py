import pandas as pd
import matplotlib.pyplot as plt
import os
from data import parse_data_knn

K = 3

def make_model():

    if os.path.exists("CalSee\DIPv1\knn\density_procs.csv"):
        df = pd.read_csv("CalSee\DIPv1\knn\density_procs.csv")
    else:
        df = parse_data_knn()

    #plot data points based on type and density in knn
    plt.scatter(df["type"],df["volume(mm^3)"])
    plt.xlabel("Type")
    plt.ylabel("volume(mm^3)")
    plt.show()

make_model()