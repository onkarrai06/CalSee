import pandas as pd

def parse_data_knn():
    # Specify the path to your Excel file
    excel_file_path = 'CalSee\DIPv1\knn\density.xls'

    # Read all sheets from the Excel file into a dictionary of DataFrames
    excel_data = pd.read_excel(excel_file_path, sheet_name=None)

    flattened_df = pd.concat(excel_data.values(), ignore_index=True)
    flattened_df = flattened_df.drop("id",axis=1)
    
    with open("CalSee\DIPv1\classes.txt", "r") as f:
        classes = f.read().splitlines()
    
    flattened_df["type"] = flattened_df["type"].apply(lambda x: classes.index(x))
    
    with open("CalSee\DIPv1\knn\density_procs.csv", "w") as f:
        flattened_df.to_csv(f, index=False)

    return flattened_df

parse_data_knn()