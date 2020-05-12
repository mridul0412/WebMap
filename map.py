import folium
import pandas

data=pandas.read_csv("Mass.csv")
lat=list(data["LATITUDE"])
lon=list(data["LONGITUDE"])
case=list(data["CASE"])
fat=list(data["FATALITIES"])

def color_producer(fatal):
    if fatal<10:
        return 'darkblue'
    elif 10<fatal<20:
        return 'orange'
    else:
        return 'red'


map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles='OpenStreetMap')

fgm=folium.FeatureGroup(name="Mass Killings")
for lt,ln,nm,ft in zip(lat,lon,case,fat):
    fgm.add_child(folium.CircleMarker(location=[lt,ln],radius=10,popup=str(nm),fill_color=color_producer(ft),color='grey',fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']< 20000000 else 'red'}))


map.add_child(fgm)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
