from os import path
import pandas as pd
import time
import geopandas as gpd

if __name__ == '__main__':
    filePath = r'D:\self\202412\china\shp'
    filename = path.join(filePath, 'states.shp')
    dep2020File = r'D:\self\202412\china\2020 depression cleaned.csv' 
    dep2021File = r'D:\self\202412\china\2021 depression cleaned.csv'  
    dep2022File = r'D:\self\202412\china\2022 depression cleaned.csv' 
    incomeFile = r'D:\self\202412\china\income.xlsx'  
    eduFile = r'D:\self\202412\china\State_Level_Education.xlsx' 
    shiyeFile = r'D:\self\202412\china\yearly_unemployment_english.xlsx' 
    povertyFile = r'D:\self\202412\china\poverty.csv' 

    t_start = time.time()

    dep2020_df = pd.read_csv(dep2020File)
    dep2021_df = pd.read_csv(dep2021File)
    dep2022_df = pd.read_csv(dep2022File)
    income2020_df = pd.read_excel(incomeFile, sheet_name='2020')
    income2021_df = pd.read_excel(incomeFile, sheet_name='2021')
    income2022_df = pd.read_excel(incomeFile, sheet_name='2022')
    edu_df = pd.read_excel(eduFile)
    edu2020_df = edu_df[edu_df['Year'] == 2020]
    edu2021_df = edu_df[edu_df['Year'] == 2021]
    edu2022_df = edu_df[edu_df['Year'] == 2022]
    shiye_df = pd.read_excel(shiyeFile)
    poverty_df = pd.read_csv(povertyFile)
    poverty2020_df = poverty_df[poverty_df['Year'] == 2020]
    poverty2021_df = poverty_df[poverty_df['Year'] == 2021]
    poverty2022_df = poverty_df[poverty_df['Year'] == 2022]

    gdf = gpd.read_file(filename)
    allNames = set(list(gdf['STATE_NAME']))

    dep2020Names = set(list(dep2020_df['LocationDesc']))
    dep2021Names = set(list(dep2021_df['LocationDesc']))
    dep2022Names = set(list(dep2022_df['LocationDesc']))
    income2020Names = set(list(income2020_df['State']))
    income2021Names = set(list(income2021_df['State']))
    income2022Names = set(list(income2022_df['State']))
    eduNames = set(list(edu_df['State']))
    shiyeNames = set(list(shiye_df['state']))
    povertyNames = set(list(poverty_df['Name']))


    print(allNames - povertyNames)
    print(povertyNames - allNames)

    print("Processing cost {} seconds".format(time.time() - t_start))
