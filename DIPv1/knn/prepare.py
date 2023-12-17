import pandas as pd

"""
CALROIES_PER_GRAM = {
    "apple": 0.52,
    "banana": 0.89,
    "bread": 2.62,
    "bun": 2.35,
    "doughnut": 3.76,
    "egg": 1.55,
    "fired_dough_twist": 4.32,
    "grape": 0.69,
    "lemon": 0.31,
    "litchi": 0.66,
    "mango": 0.65,
    "mooncake": 4.12,
    "orange": 0.47,
    "pear": 0.58,
    "peach": 0.58,
    "plum": 0.46,
    "qiwi": 0.61,
    "sachima": 4.80,
    "tomato": 0.18,
}"""

def parse_data_knn():
    # Specify the path to your Excel file
    csv_file_path = '.\DIPv1\knn\\food.csv'

    # Load spreadsheet
    df = pd.read_csv(csv_file_path)

    df['image_name'] = df['image_name'].str.replace('\d+', '', regex=True)

    with open(".\DIPv1\classes.txt", "r") as f:
        classes = f.read().splitlines()
    
    
    df['image_name'] = df["image_name"].apply(lambda x: classes.index(x))
    df['side_area'] = df['Side_foodHeigth'] * df['Side_foodWidth']
    df['top_area'] = df['Top_foodHeigth'] * df['Top_foodWidth']

    df.drop(['Side_foodHeigth', 'Side_foodWidth'], axis=1, inplace=True)
    df.drop(['Top_foodHeigth', 'Top_foodWidth'], axis=1, inplace=True)

    df.drop(['Side_coinHeigth', 'Side_coinWidth'], axis=1, inplace=True)
    df.drop(['Top_coinHeigth', 'Top_coinWidth'], axis=1, inplace=True)

    df.drop(['Side_coinForeground_pixel','Top_coinForeground_pixel','Side_foodForeground_pixel','Top_foodForeground_pixel'], axis=1, inplace=True)
    df.drop(['food_label'], axis=1, inplace=True)

    with open(".\DIPv1\knn\density_procs.csv", "w") as f:
        df.to_csv(f, index=False)

    return df

parse_data_knn()