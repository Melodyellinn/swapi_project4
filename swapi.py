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