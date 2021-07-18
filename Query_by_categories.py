
import requests
from bs4 import BeautifulSoup
import json

def List_ways_from_changesets(Changesets):
    Take_html=requests.get(f'https://www.openstreetmap.org/api/0.6/changeset/{Changesets}/download').text
    Soup=BeautifulSoup(Take_html,features='html.parser')
    Ways=Soup.find_all('way')
    List_ways_id=[]
    for Ways_id in Ways:
        List_ways_id.append(Ways_id['id'])
    return List_ways_id

def Take_nodes_from_ways(Ways_id):
    List_nodes_id=[]
    
    Take_html=requests.get(f'https://www.openstreetmap.org/api/0.6/way/{Ways_id}').text
    Soup_Way=BeautifulSoup(Take_html,'html.parser')
    Nodes=Soup_Way.find_all('nd')
        
    for nodes in Nodes:
        List_nodes_id.append(nodes['ref'])
    
    return List_nodes_id

def Take_latlong_from_node(Nodes_id): 
    List_latlong=[]
    for i in Nodes_id:
        Take_html=requests.get(f'https://www.openstreetmap.org/api/0.6/node/{i}').text
        Soup_latlong=BeautifulSoup(Take_html,features='html.parser')
        Latlong=Soup_latlong.find_all('node')
        
        for coordinate in Latlong:
            List_latlong.append(
                {
                    'node_id':coordinate['id'],
                    'lat': float(coordinate['lat']),
                    'long': float(coordinate['lon'])
                }
            )
    return List_latlong

def OSMCha_name_query(Start,End,User,Token):
    link=f'https://osmcha.org/api/v1/changesets/?page_size=75&page=1&date__lte={End}&date__gte={Start}&users={User}'
    header={
        'Authorization':f'{Token}'
    }
    html= requests.get(link,headers=header).text
    a=json.loads(html)
    features=a['features']
    id_list=[]
    
    for id in features:
        id_list.append(id['id'])
    
    return id_list