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
      return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'



map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles= "Stamen Terrain")


#we add elements or obejcts into the map from here 
#1.. Adding Map Markers
fgv = folium.FeatureGroup(name="Volcanoes")
#fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color="purple")))

#****** USING FOR LOOPS to ADD MULTIPLE MARKERS
#this is a data frame
#for coordinates in [[38.2, -99.1], [39.2, -97.1]]:



#to iterate over a new list in tupules (lat, lon, elev)
for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+ " m", icon=folium.Icon(color=color_producer(el))))


#to add better styles 
   fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",
   fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")



#adding polygons map layers- open is a way to object jSON file objects
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig')
.read(), style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#using lambda function to style and populate to yellow
#lambda function are functions written in a line of code
#example l = lambda x: x**2
#        l(5) = 25




#adding Layer Control
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map1.html")


#map.save("Map_html_popup_advanced.html")