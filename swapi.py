import requests
import pandas as pd

def fetch_planets(n_planets):
    uri = 'https://swapi.dev/api/planets/'
    url = f'{uri}/{str(n_planets)}'
    r = requests.get(url)
    data = r.json()
    return data

def datasetplanet(planets_list, planet_df, n_planets):
    planet_df.loc[n_planets,'name'] = planets_list['name']
    planet_df.loc[n_planets,'rotation_period'] = planets_list['rotation_period']
    planet_df.loc[n_planets,'orbital_period'] = planets_list['orbital_period']
    planet_df.loc[n_planets,'diameter'] = planets_list['diameter']
    planet_df.loc[n_planets,'climate'] = planets_list['climate']
    planet_df.loc[n_planets,'gravity'] = planets_list['gravity']
    planet_df.loc[n_planets,'terrain'] = planets_list['terrain']
    planet_df.loc[n_planets,'surface_water'] = planets_list['surface_water']
    planet_df.loc[n_planets,'population'] = planets_list['population']
    return planet_df

def get_planet_data(n_planets=60):
    columns = ['name','rotation_period','orbital_period','diameter','climate','gravity','terrain','surface_water','population']
    planet_df = pd.DataFrame(columns=columns)

    n = n_planets

    for i in range (1,n+1):
        planets_list = fetch_planets(i)
        planet_df = datasetplanet(planets_list, planet_df,i)
    
    return planet_df



#Melo

import requests
import pandas as pd
import json


def datastarships(starships_list, starships_df, n_starships):
    starships_df.loc[n_starships,'name'] = starships_list['name']
    starships_df.loc[n_starships,'model'] = starships_list['model']
    starships_df.loc[n_starships,'manufacturer'] = starships_list['manufacturer']
    starships_df.loc[n_starships,'cost_in_credits'] = starships_list['cost_in_credits']
    starships_df.loc[n_starships,'length'] = starships_list['length']
    starships_df.loc[n_starships,'max_atmosphering_speed'] = starships_list['max_atmosphering_speed']
    starships_df.loc[n_starships,'crew'] = starships_list['crew']
    starships_df.loc[n_starships,'passengers'] = starships_list['passengers']
    starships_df.loc[n_starships,'cargo_capacity'] = starships_list['cargo_capacity']
    starships_df.loc[n_starships,'consumables'] = starships_list['consumables']
    starships_df.loc[n_starships,'hyperdrive_rating'] = starships_list['hyperdrive_rating']
    starships_df.loc[n_starships,'MGLT'] = starships_list['MGLT']
    starships_df.loc[n_starships,'starship_class'] = starships_list['starship_class']
    starships_df.loc[n_starships,'pilots'] = starships_list['pilots']
    return starships_df

columns = ['name','model', 'manufacturer', 'cost_in_credits', 'length', 'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity', 'consumables', 'hyperdrive_rating', 'MGLT', 'starship_class', 'pilots']
starships_df = pd.DataFrame(columns=columns)

n=10

for i in range (2,n+1):
    try:
        data = fetch_starships(i)
        starships_df = datastarships(data,starships_df,i)
    except:
        print(f"Cette entrée numéro {i} n'existe pas sur l'API")
#starships_df

#Youcef

#import json
uri = "https://swapi.dev/api/vehicles/"

def fetch_vehicles(n_vehicles):
    uri = 'https://swapi.dev/api/vehicles/'
    url = f'{uri}/{str(n_vehicles)}'
    r = requests.get(url)
    data = r.json()
    return data
#response = requests.get("https://swapi.dev/api/vehicles/")
#datap=response.json()
#datap

def datasetvehicles(vehicles_list, vehicles_df, n_vehicles):
    vehicles_df.loc[n_vehicles,'name'] = vehicles_list['name']
    vehicles_df.loc[n_vehicles,'model'] = vehicles_list['model']
    vehicles_df.loc[n_vehicles,'manufacturer'] = vehicles_list['manufacturer']
    vehicles_df.loc[n_vehicles,'cost_in_credits'] = vehicles_list['cost_in_credits']
    vehicles_df.loc[n_vehicles,'length'] = vehicles_list['length']
    vehicles_df.loc[n_vehicles,'max_atmosphering_speed'] = vehicles_list['max_atmosphering_speed']
    vehicles_df.loc[n_vehicles,'crew'] = vehicles_list['crew']
    vehicles_df.loc[n_vehicles,'passengers'] = vehicles_list['passengers']
    vehicles_df.loc[n_vehicles,'cargo_capacity'] = vehicles_list['cargo_capacity']
    vehicles_df.loc[n_vehicles,'consumables'] = vehicles_list['consumables']
    vehicles_df.loc[n_vehicles,'vehicle_class'] = vehicles_list['vehicle_class']
    return vehicles_df
#vehicles = pd.DataFrame(datap)
#vehicles

columns = ['name', 'model', 'manufacturer', 'cost_in_credits', 'length', 'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity', 'consumables', 'vehicles_class']
vehicles_df = pd.DataFrame(columns=columns)

n = 39

for i in range (1,n+1):
    vehicles_lists = fetch_vehicles(i)
    vehicles_df = datasetvehicles(vehicles_list, vehicles_df,i)
planet_df
#vehicles_2 = vehicles.drop(["next", "previous", "count"], axis=1)

vehicles_2


results
0	{'name': 'Sand Crawler', 'model': 'Digger Craw...
1	{'name': 'T-16 skyhopper', 'model': 'T-16 skyh...
2	{'name': 'X-34 landspeeder', 'model': 'X-34 la...
3	{'name': 'TIE/LN starfighter', 'model': 'Twin ...
4	{'name': 'Snowspeeder', 'model': 't-47 airspee...
5	{'name': 'TIE bomber', 'model': 'TIE/sa bomber...
6	{'name': 'AT-AT', 'model': 'All Terrain Armore...
7	{'name': 'AT-ST', 'model': 'All Terrain Scout ...
8	{'name': 'Storm IV Twin-Pod cloud car', 'model...
9	{'name': 'Sail barge', 'model': 'Modified Luxu...