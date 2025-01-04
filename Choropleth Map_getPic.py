import geopandas as gpd
import matplotlib.pyplot as plt
from os import path
import matplotlib
import time

matplotlib.use('TkAgg')

if __name__ == '__main__':
    # read Shapefile
    shapefile_path = r'D:\self\202412\china\final.shp'  
    picPath = r'D:\self\202412\china\pic'
    gdf = gpd.read_file(shapefile_path)

    t_start = time.time()

    titles = ['Depression rate in each state in 2020', 'Depression rate in each state in 2021',
              'Depression rate in each state in 2022', 'Income in each state in 2020', 'Income in each state in 2021',
              'Income in each state in 2022', 'Completions Growth in each state in 2020',
              'Completions Growth in each state in 2021',
              'Completions Growth in each state in 2022', 'Percent in Unemployment in each state in 2021',
              'Percent in Unemployment in each state in 2020', 'Percent in Unemployment in each state in 2022',
              'Percent in poverty in each state in 2020', 'Percent in poverty in each state in 2021',
              'Percent in poverty in each state in 2022']
    units = ["%", "%", "%", "USD", "USD", "USD", "%", "%", "%", "%", "%", "%", "%", "%", "%"]

    num = 0
    for field in ['dep2020', 'dep2021', 'dep2022', 'income2020',
                  'income2021', 'income2022', 'edu2020', 'edu2021', 'edu2022', 'shiye2020', 'shiye2021', 'shiye2022',
                  'pov2020', 'pov2021', 'pov2022']:
        print(field)
        # create map
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        gdf.boundary.plot(ax=ax, linewidth=1, color='black')
        gdf.plot(column=field, ax=ax, legend=True,
                 cmap='Reds', missing_kwds={"color": "lightgrey", "label": "No data"})

        colorbar = ax.get_figure().axes[-1]  
        colorbar.set_title(units[num], rotation=0, pad=15) 

        # add titles
        plt.title(titles[num], fontsize=15)
        plt.axis('off')  
        plt.savefig(path.join(picPath, "{}.jpg".format(field)), dpi=1000)

        num += 1

    print('Processing cost {} seconds.'.format(time.time() - t_start))
