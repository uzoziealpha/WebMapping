import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

#created two list from the volcanoes.txt using python
lat = list(data["LAT"])
lon = list(data["LON"])

#making the popup markers dynamic
elev = list(data["ELEV"])
#name = list(data["NAME"])

#html = """
#Volcano name:<br>
#<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
#Height: %s m
#"""



#Creating a color generation function
def color_producer(elevation):
    if elevation < 1000:
      return 'purple'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'green'



map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles= "Stamen Terrain")


#we add elements or obejcts into the map from here 
#1.. Adding Map Markers
fg = folium.FeatureGroup(name="MyMap")
#fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color="purple")))

#****** USING FOR LOOPS to ADD MULTIPLE MARKERS
#this is a data frame
#for coordinates in [[38.2, -99.1], [39.2, -97.1]]:



#to iterate over a new list in tupules (lat, lon, elev)
for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+ " m", icon=folium.Icon(color=color_producer(el))))


#to add better styles 
   fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",
   fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))


map.add_child(fg)

map.save("Map1.html")
#map.save("Map_html_popup_advanced.html")