import pandas as pd
import zipfile

def load_dataset(zip_path='data/cuisine_updated.csv.zip', csv_name='cuisine_updated.csv'):
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(csv_name) as f:
            df = pd.read_csv(f, encoding='ISO-8859-1')
            df.fillna('', inplace=True)
            df['image_filename'] = df['image_url'].apply(
                lambda x: x.split('/')[-1].strip().replace(' ', '_') if pd.notna(x) else ''
            )
            return df

def search_dish(df, dish_name=None, diet=None):
    match = df.copy()

    if dish_name:
        dish_name = dish_name.lower().strip()
        match = match[match['name'].str.lower().str.contains(dish_name)]

    if diet:
        match = match[match['diet'].str.lower().str.contains(diet.lower())]

    match = match[match['image_filename'] != '']
    return match.to_dict(orient='records')
