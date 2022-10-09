import pandas as pd

df = pd.read_csv('final.csv')

name = df["Name"].to_list()
dist = df["Distance"].to_list()
mass = df["Mass"].to_list()
rad = df["Radius"].to_list()
grav = df["Gravity"].to_list()

final_list = []
temp_dict = {}
for i in range(0,len(name)):
    temp_dict['Name'] = name[i],
    temp_dict['Planet_Distance'] = dist[i],
    temp_dict['Planet_Mass'] = mass[i],
    temp_dict['PLanet_Radius'] = rad[i],
    temp_dict['Planet_Gravity'] = grav[i]
    final_list.append(temp_dict)
    temp_dict = {}
print(final_list)