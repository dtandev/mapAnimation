import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import plotly

files = os.listdir('GrunwaldCSV/')
#files.sort()
df = pd.DataFrame()

for file in files:
    dfrob = pd.read_csv('GrunwaldCSV/' + file, error_bad_lines=False)
    print(file, dfrob.columns)
    dfrob['Timestamp'] = int(file[-7:-4])
    df = df.append(dfrob)

df = df.sort_values(by=['Timestamp'])

unitDict = {'KJ':'Krzyżacy - Jazda', 'KP': 'Krzyżacy Piechota', 'KA':"Krzyżacy - Artyleria", 'KM': 'Mistrz Zakonu', 'PSP':'Polska - Straż Przednia', 'POW':'Polska - Oddziały Wojsk', 'PPS':'Pułki Smoleńskie', 'POL':'Polska - Oddziały Litewsko-Ruskie', 'PKP':'Król Polski', 'PKW':'Książe Witold'}
unitColors = {'Krzyżacy - Jazda':"#a62b26", 'Krzyżacy Piechota':"#d83927", "Krzyżacy - Artyleria":"#f46d43", 'Mistrz Zakonu':"#fdae61", 'Polska - Straż Przednia':"#323a95", 'Polska - Oddziały Wojsk':"#4574b4", 'Pułki Smoleńskie':"#73add1", 'Polska - Oddziały Litewsko-Ruskie':"#aad9e9", 'Król Polski':"#ffea00", 'Książe Witold':'#000000'}

df['Jednostka'] = df['unit'].map(unitDict)


#dftest = df[(df['Timestamp']<200) & (df['Timestamp']>100) & (df['Timestamp']!=119) & (df['Timestamp']!=118)& (df['Timestamp']!=117)& (df['Timestamp']!=120)]
dftest = df
print(dftest.columns)

fig1 = px.scatter_mapbox(dftest, 
                         lon='xcoord', 
                         lat='ycoord', 
                         color='Jednostka', 
                         #color_discrete_map={"KJ":"#a62b26", "KP":"#d83927", "KA":"#f46d43", 'KM':"#fdae61", 'PSP':"#323a95", 'POW':"#4574b4", 'PPS':"#73add1", 'POL':"#aad9e9", 'PKP':"#ffea00", 'PKW':"#000000"}, 
                         color_discrete_map = unitColors,
                         animation_frame='Timestamp', 
                         animation_group = 'army',
                         mapbox_style='carto-positron',
                         zoom = 11,
                         hover_name = 'id')


# Zapis mapy do html
plotly.io.write_html(fig1, "bitwaUnit.html")