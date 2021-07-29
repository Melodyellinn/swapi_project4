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