from os import path
import pandas as pd
import time
import geopandas as gpd

if __name__ == '__main__':
    filePath = r'D:\self\202412\china\shp'
    filename = path.join(filePath, 'states.shp')
    dep2020File = r'D:\self\202412\china\2020 depression cleaned.csv'  # 替换为你的CSV文件路径
    dep2021File = r'D:\self\202412\china\2021 depression cleaned.csv'  # 替换为你的CSV文件路径
    dep2022File = r'D:\self\202412\china\2022 depression cleaned.csv'  # 替换为你的CSV文件路径
    incomeFile = r'D:\self\202412\china\income.xlsx'  # 替换为你的CSV文件路径
    eduFile = r'D:\self\202412\china\State_Level_Education.xlsx'  # 替换为你的CSV文件路径
    shiyeFile = r'D:\self\202412\china\yearly_unemployment_english.xlsx'  # 替换为你的CSV文件路径
    povertyFile = r'D:\self\202412\china\poverty.csv'  # 替换为你的CSV文件路径

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

    merged_data = gdf.merge(dep2020_df[['LocationDesc', 'Data_Value']], left_on='STATE_NAME', right_on='LocationDesc',
                            how='left')
    merged_data.rename(columns={'Data_Value': 'dep2020'}, inplace=True)

    merged_data = merged_data.merge(dep2021_df[['LocationDesc', 'Data_Value']], left_on='STATE_NAME',
                                    right_on='LocationDesc',
                                    how='left')
    merged_data.rename(columns={'Data_Value': 'dep2021'}, inplace=True)
    print('jjjj333', merged_data.shape)

    merged_data = merged_data.merge(dep2022_df[['LocationDesc', 'Data_Value']], left_on='STATE_NAME',
                                    right_on='LocationDesc',
                                    how='left')
    merged_data.rename(columns={'Data_Value': 'dep2022'}, inplace=True)
    print('jjjj0', merged_data.shape)

    merged_data = merged_data.merge(income2020_df[['State', 'income']], left_on='STATE_NAME',
                                    right_on='State',
                                    how='left')
    merged_data.rename(columns={'income': 'income2020'}, inplace=True)
    print('jjjj999', merged_data.shape)

    merged_data = merged_data.merge(income2021_df[['State', 'income']], left_on='STATE_NAME',
                                    right_on='State',
                                    how='left')
    merged_data.rename(columns={'income': 'income2021'}, inplace=True)
    merged_data = merged_data.drop_duplicates(subset='STATE_NAME', keep='first')
    print('jjjj888', merged_data.shape)

    merged_data = merged_data.merge(income2022_df[['State', 'income']], left_on='STATE_NAME',
                                    right_on='State',
                                    how='left')
    merged_data.rename(columns={'income': 'income2022'}, inplace=True)
    print('jjjj1', merged_data.shape)

    merged_data = merged_data.merge(edu2020_df[['State', 'Average Growth in Awarded Degrees']], left_on='STATE_NAME',
                                    right_on='State',
                                    how='left')
    merged_data.rename(columns={'Average Growth in Awarded Degrees': 'edu2020'}, inplace=True)
    print('jjjj2', merged_data.shape)

    merged_data = merged_data.merge(edu2021_df[['State', 'Average Growth in Awarded Degrees']], left_on='STATE_NAME',
                                    right_on='State',
                                    how='left')
    merged_data.rename(columns={'Average Growth in Awarded Degrees': 'edu2021'}, inplace=True)
    print('jjjj3', merged_data.shape)

    merged_data = merged_data.merge(edu2022_df[['State', 'Average Growth in Awarded Degrees']], left_on='STATE_NAME',
                                    right_on='State',
                                    how='left')
    merged_data.rename(columns={'Average Growth in Awarded Degrees': 'edu2022'}, inplace=True)
    print('jjjj4', merged_data.shape)

    print(shiye_df)
    print(shiye_df.columns.values)
    merged_data = merged_data.merge(shiye_df[['state', 2020]], left_on='STATE_NAME',
                                    right_on='state',
                                    how='left')
    merged_data.rename(columns={2020: 'shiye2020'}, inplace=True)
    print('jjjj5', merged_data.shape)

    merged_data = merged_data.merge(shiye_df[['state', 2021]], left_on='STATE_NAME',
                                    right_on='state',
                                    how='left')
    merged_data.rename(columns={2021: 'shiye2021'}, inplace=True)

    merged_data = merged_data.merge(shiye_df[['state', 2022]], left_on='STATE_NAME',
                                    right_on='state',
                                    how='left')
    merged_data.rename(columns={2022: 'shiye2022'}, inplace=True)

    merged_data = merged_data.merge(poverty2020_df[['Name', 'Percent in Poverty']], left_on='STATE_NAME',
                                    right_on='Name',
                                    how='left')
    merged_data.rename(columns={'Percent in Poverty': 'pov2020'}, inplace=True)

    merged_data = merged_data.merge(poverty2021_df[['Name', 'Percent in Poverty']], left_on='STATE_NAME',
                                    right_on='Name',
                                    how='left')
    merged_data.rename(columns={'Percent in Poverty': 'pov2021'}, inplace=True)

    merged_data = merged_data.merge(poverty2022_df[['Name', 'Percent in Poverty']], left_on='STATE_NAME',
                                    right_on='Name',
                                    how='left')
    merged_data.rename(columns={'Percent in Poverty': 'pov2022'}, inplace=True)

    # print merged data
    print("Merged data:")
    print('jjjj', merged_data.shape)
    print(list(merged_data.columns.values))

    fields = ['STATE_NAME', 'STATE_FIPS', 'SUB_REGION', 'STATE_ABBR', 'dep2020', 'dep2021', 'dep2022', 'income2020',
              'income2021', 'income2022', 'edu2020', 'edu2021', 'edu2022', 'shiye2020', 'shiye2021', 'shiye2022',
              'pov2020', 'pov2021', 'pov2022']

    merged_data = merged_data[fields]
    merged_data = merged_data[fields].drop_duplicates()
    print(merged_data.shape)
    # convert DataFrame into GeoDataFrame
    merged_data = gpd.GeoDataFrame(merged_data, geometry=gdf.geometry)

    # save new GeodataFrame into Shapefile
    merged_data.to_file(r'D:\self\202412\china\final.shp')

    print("Processing cost {} seconds".format(time.time() - t_start))
