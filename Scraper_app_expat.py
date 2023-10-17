import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.markdown("<h1 style='text-align: center; color: black;'>EXPAT DATA SCRAPER APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app performs simple webscraping of data from expat-dakar over multiples pages!
* **Python libraries:** base64, pandas, streamlit, requests, bs4
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")

st.sidebar.header('User Input Features')
Pages1 = st.sidebar.selectbox('Vehicles data pages', list([int(p) for p in np.arange(2, 500)]))
Pages2 = st.sidebar.selectbox('Motocycle data pages', list([int(p) for p in np.arange(2, 500)]))
Pages3 = st.sidebar.selectbox('Apartment data pages', list([int(p) for p in np.arange(2, 300)]))
Pages4 = st.sidebar.selectbox('Furnished Apartment data pages', list([int(p) for p in np.arange(2, 200)]))
Pages5= st.sidebar.selectbox('Land data pages', list([int(p) for p in np.arange(2, 200)]))
Pages6 = st.sidebar.selectbox('House data pages', list([int(p) for p in np.arange(2, 100)]))
Pages7 = st.sidebar.selectbox('Car rental data pages', list([int(p) for p in np.arange(2, 100)]))
Pages8 = st.sidebar.selectbox('Equipements-pieces data pages', list([int(p) for p in np.arange(2, 100)]))
Pages9 = st.sidebar.selectbox('Laptop data pages', list([int(p) for p in np.arange(2, 500)]))
Pages10 = st.sidebar.selectbox('Phone data pages', list([int(p) for p in np.arange(2, 500)]))
Pages11 = st.sidebar.selectbox('accessories-multimedia data pages', list([int(p) for p in np.arange(2, 200)]))
Pages12 = st.sidebar.selectbox('Tv data pages', list([int(p) for p in np.arange(2, 150)]))
Pages13 = st.sidebar.selectbox('Videos games consoles data pages', list([int(p) for p in np.arange(2, 100)]))
Pages14 = st.sidebar.selectbox('Tablet data pages', list([int(p) for p in np.arange(2, 100)]))
Pages15 = st.sidebar.selectbox('Audio-videos equipment data pages', list([int(p) for p in np.arange(2, 60)]))
Pages16 = st.sidebar.selectbox('Printer-scanners data pages', list([int(p) for p in np.arange(2, 60)]))
Pages17 = st.sidebar.selectbox('Camera data pages', list([int(p) for p in np.arange(2, 50)]))
Pages18 = st.sidebar.selectbox('electromenager data pages', list([int(p) for p in np.arange(2, 500)]))

# Background function
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('img_file2.jpg') 
# Web scraping of Vehicles data on expat-dakar
@st.cache_data

# Fonction for web scraping vehicle data
def load_vehicle_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/voitures/dakar?page={p}" 
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers : 
            try :
                Gen = container.find('div', class_ ='listing-card__header__tags').find_all('span')
                Label = Gen[0].text
                Brand= Gen[1].text 
                Year = Gen[2].text
                Gearbox = Gen[3].text
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                    'Label': Label,
                    'Brand': Brand, 
                    'Year': int(Year), # convertir en Integer
                    'Gearbox': Gearbox, 
                    'Adress': Adress,
                    'Price': int(Price),
                    'Imagelink': Imagelink 
                }
                data.append(obj)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_motocycle_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/motos-scooters?sdc_search_offer_id=krmhqaiyuc&page={p}" 
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers : 
            try :
                Gen = container.find('div', class_ ='listing-card__header__tags').find_all('span')
                Type_Motos = Gen[0].text
                Brand= Gen[1].text 
                Year = Gen[2].text
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Type_Motos': Type_Motos,
                        'Brand': Brand, 
                        'Year': int(Year), 
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df   

def load_apartment_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/appartements-a-louer?page={p}" 
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers: 
            try :
                Type = container.find('div', class_ = 'listing-card__header__title').text.strip().split(' ')[0]
                Num_Room_Area = container.find('div', class_ = 'listing-card__header__tags').text.split('chambre')
                Number_Room = Num_Room_Area[0]
                Area_square_meter = Num_Room_Area[1].replace(' m²', '')
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Type': Type,
                        'Number_Room': int(Number_Room), 
                        'Area_square_meter': int(Area_square_meter),
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_furnished_apartment_data(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/appartements-meubles?page={p}" 
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers: 
            try :
                Type = container.find('div', class_ = 'listing-card__header__title').text.strip().split(' ')[0]
                Num_Room_Area = container.find('div', class_ = 'listing-card__header__tags').text.split('chambre')
                Number_Room = Num_Room_Area[0]
                Area_square_meter = Num_Room_Area[1].replace(' m²', '')
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Type': Type,
                        'Number_Room': int(Number_Room), 
                        'Area_square_meter': int(Area_square_meter),
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_land_data(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/terrains-a-vendre?page={p}" 
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers: 
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Area_square_meter = container.find('div', class_ = 'listing-card__header__tags').text.replace(' m²', '')
                
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Details': Details,
                        'Area_square_meter': int(Area_square_meter),
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_house_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/maisons-a-vendre?page={p}" 
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers: 
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Area_square_meter = container.find('div', class_ = 'listing-card__header__tags').text.replace(' m²', '')
                
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Details': Details,
                        'Area_square_meter': int(Area_square_meter),
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_car_rental_data(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/location-de-voiture?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Details': Details,
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_equipment_pieces_data(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/equipements-pieces?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Tool_name = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Tool_name': Tool_name,
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_laptop_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/ordinateurs?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Type_of_laptop = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[0].text.strip()
                Brand = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[1].text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Type_of_laptop': Type_of_laptop,
                        'Brand': Brand,
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_phone_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/telephones?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Type_of_phone = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[0].text.strip()
                Brand = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[1].text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Type_of_phone': Type_of_phone,
                        'Brand': Brand,
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)    
    return df

def load_accessories_multimedia_data(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/accessoires-multimedia?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Type_of_tool = container.find('div', class_ = 'listing-card__header__tags').span.text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = {
                        'Details':Details,             
                        'Type_of_tool': Type_of_tool,
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df


def load_tv_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/tv-home-cinema?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Type_of_TV = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[0].text.strip()
                Brand = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[1].text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = { 'Details': Details,
                        'Type_of_TV': Type_of_TV,
                        'Brand': Brand,
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df


def load_vid_gam_consol_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/jeux-videos-consoles?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Type_of_GameCon = container.find('div', class_ = 'listing-card__header__tags').span.text.strip()          
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = { 'Details': Details,
                        'Type_of_GameCon': Type_of_GameCon,                    
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_tablet_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/tablettes?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Type_of_Tablet = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[0].text.strip()
                Brand = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[1].text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = { 'Details': Details,
                        'Type_of_Tablet': Type_of_Tablet,
                        'Brand': Brand,
                        'Adress': Adress,
                        'Price': int(Price),
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df


def load_aud_vid_equipment(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/equipement-video-et-audio?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                Type_of_tool = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[0].text.strip()
                Brand = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[1].text.strip()
                Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                obj = { 'Details': Details,
                        'Type_of_tool': Type_of_tool,
                        'Brand': Brand,
                        'Adress': Adress,
                        'Price': int(Price), 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_printer_scanners_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/imprimantes-scanners?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                    Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                    Type_of_tool = container.find('div', class_ = 'listing-card__header__tags').span.text.strip()
                    Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                    Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                    Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                    obj = { 'Details': Details,
                            'Type_of_tool': Type_of_tool,
                            'Adress': Adress,
                            'Price': int(Price), 
                            'Imagelink': Imagelink
                        }
                    data.append(obj)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df 

def load_camera_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/appareils-photos?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                    Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                    Type_of_tool = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[0].text.strip()
                    Brand = container.find('div', class_ = 'listing-card__header__tags').find_all('span')[1].text.strip()
                    Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                    Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                    Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                    obj = { 'Details': Details,
                            'Type_of_tool': Type_of_tool,
                            'Brand': Brand,
                            'Adress': Adress,
                            'Price': int(Price), 
                            'Imagelink': Imagelink
                        }
                    data.append(obj)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df 

def load_electromenager_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.expat-dakar.com/electromenager?page={p}"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('div', class_ ='listings-cards__list-item')
        data = []
        for container in containers:
            try :
                    Details = container.find('div', class_ = 'listing-card__header__title').text.strip()
                    Type_of_tool = container.find('div', class_ = 'listing-card__header__tags').span.text.strip()
                    Adress = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                    Price = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                    Imagelink = container.find('div', class_ = 'listing-card__image__inner').img['src']
                    obj = { 'Details': Details,
                            'Type_of_tool': Type_of_tool,
                            'Adress': Adress,
                            'Price': int(Price), 
                            'Imagelink': Imagelink
                        }
                    data.append(obj)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df 



Vehicles_data_mul_pag = load_vehicle_data(Pages1)
Motocycle_data_mul_pag = load_motocycle_data(Pages2)
Apartment_data_mul_pag = load_apartment_data(Pages3)
Furnished_apartment_data_mul_pag = load_furnished_apartment_data(Pages4)
Land_data_mul_pag = load_land_data(Pages5)
House_data_mul_pag = load_house_data(Pages6)
load_car_rental_mul_pag = load_car_rental_data(Pages7)
load_equipment_pieces_data_mul_pag = load_equipment_pieces_data(Pages8)
load_laptop_data_mul_pag = load_laptop_data(Pages9)
load_phone_data_mul_pag = load_phone_data(Pages10)
load_accessories_multimedia_data_mul_pag = load_accessories_multimedia_data(Pages11)
load_tv_data_mul_pag = load_tv_data(Pages12)
load_vid_gam_consol_data_mul_pag = load_vid_gam_consol_data(Pages13)
load_tablet_data_mul_pag = load_tablet_data(Pages14)
load_aud_vid_equipment_mul_pag = load_aud_vid_equipment(Pages15)
load_printer_scanners_data_mul_pag = load_printer_scanners_data(Pages16)
load_camera_data_mul_pag = load_camera_data(Pages17)
load_electromenager_data_mul_pag = load_electromenager_data(Pages18)

# Download Vehicles data
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def load(dataframe, title, key, key1) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key1):
        # st.header(title)

        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

        csv = convert_df(dataframe)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Data.csv',
            mime='text/csv',
            key = key)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')        





load(Vehicles_data_mul_pag, 'Vehicles data', '1', '101')
load(Motocycle_data_mul_pag, 'Motocycle data', '2', '102')
load(Apartment_data_mul_pag, 'Apartment data', '3', '103')
load(Furnished_apartment_data_mul_pag, 'Furnished apartment data', '4', '115')
load(Land_data_mul_pag, 'Land data','5', '109')
load(House_data_mul_pag, 'House data', '6', '110')
load(load_car_rental_mul_pag, 'Car rental data', '7', '111')
load(load_equipment_pieces_data_mul_pag, 'Equipements-pieces data', '8', '114')
load(load_laptop_data_mul_pag, 'Laptop data', '9', '104')
load(load_phone_data_mul_pag, 'Phone data', '10', '105')
load(load_accessories_multimedia_data_mul_pag, 'Accessories-multimedia data', '11', '117')
load(load_tv_data_mul_pag, 'TV data', '12', '106')
load(load_vid_gam_consol_data_mul_pag, 'Videos games consoles data', '13', '116')
load(load_tablet_data_mul_pag, 'Tablet data','14', '107')
load(load_aud_vid_equipment_mul_pag, 'Audio-videos equipment data', '15', '118')
load(load_printer_scanners_data_mul_pag, 'Printer-scanners data','16', '113')
load(load_camera_data_mul_pag, 'Camera data', '17', '108')
load(load_electromenager_data_mul_pag, 'Electromenager data', '18', '112')







 


