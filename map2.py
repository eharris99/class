#elise Harris
#march 18, 2019
#problem 43

#Import the folium package for making maps
import folium

#Create a map, centered (0,0), and zoomed out a bit:
mapNYC = folium.Map(location=[40.75, -74.125],zoom_start=3)
csvname=input("Enter CSV file name: ")
outputname=input("Enter output file: ")
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapNYC)



#Save the map:
mapNYC.save(outfile=outputname)
