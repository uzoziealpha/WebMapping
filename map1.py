import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles= "Stamen Terrain")
#we add elements or obejcts into the map from here 
#1.. Adding Map Markers
fg = folium.FeatureGroup(name="MyMap")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color="purple")))
map.add_child(fg)



map.save("Map1.html")