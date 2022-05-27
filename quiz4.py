import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


file = open("result.csv", "w", encoding="utf-8_sig", newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(["დასახელება", "გარბენი", "გადაცემათა კოლოფი", "ძრავი", "საჭე", "ფასი ლარებში", "ფასი დოლარებში"])

for ind in range(1,7):
    url = f'https://ss.ge/ka/auto/list/iyideba?Page={ind}&AutoManufacturerId=&VehicleModelIds=&VehicleDealTypes=2&YearFrom=&YearTo=&CurrencyId=1&PriceFrom=&PriceTo=&CityIds=&Query=&MillageFrom=&MillageTo=&EngineFrom=&EngineTo=&IsCustomsCleared=&TechnicalInspection=&AutoDealershipId=&El_Windows=false&Hatch=false&CruiseControl=false&StartStopSystem=false&AUX=false&Bluetooth=false&AntiFogHeadlights=false&SeatHeater=false&SmartSeats=false&MultiWheel=false&Signalisation=false&BoardComputer=false&Conditioner=false&ClimateControl=false&RearViewCamera=false&Monitor=false&PanoramicCeiling=false&ParkingControl=false&ABS=false&CentralLocker=false&AutoParking=false&LedHeadlights=false&AdaptedForDisabled=false'
    r =  requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    main_body = soup.find('div', id='main-body')
    container = main_body.find('div', class_='col-md-12 c-listing-container')
    listing_container = container.find('div', class_='listing-container')
    car_list = listing_container.find('div', id='list')
    auto_result = car_list.find('div', class_='auto-result')

    cars_item = auto_result.find_all('div' , class_='cars-item')


    for car in cars_item:
        item_decription = car.find('div', class_='item-decription')
        price_item = car.find('div', class_='r-item')
        price = price_item.find('div', class_='price priceGel')
        price1 = price_item.find('div', class_='price priceUsd')

        name = item_decription.a.text
        features  = item_decription.div.text
        pricegel_usd = price_item.div.text
        feat = features.split('\n')
        pricesplt = pricegel_usd.split('\n')





        file_obj.writerow([name,feat[1], feat[2], feat[3], feat[4],pricesplt[1]+'₾', pricesplt[2]+'$'])

        
        # print(name)
        # print(features)

    sleep(randint(15, 20))






