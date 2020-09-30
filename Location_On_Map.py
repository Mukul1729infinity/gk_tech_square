 # This is a small Python 3 code to get the location on the map by giving the coordinates as input and your 
 # map will get saved in your machine with the name ' index.html ' for that we are going to install a library 
 # by using the command pip install folium
 # the code is as follow
import folium
m=folium.Map(location=[26.2145,81.2528])
m.save('index.html')
