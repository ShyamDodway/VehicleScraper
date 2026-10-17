import requests
from bs4 import BeautifulSoup
import pandas as pd

first = True
x = False
current_page = 1
while True:
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="155", "Chromium";v="155", "Not(A:Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36',
        # 'cookie': '_CO_type=connecto; _CO_anonymousId=aa92b0e4-42d2-6486-0e3e-a4259850b75f; cd_session_id=56359e16211f107793a82e9edd9800c2; cd_ab_vdp_similar_cars=control; user_intent=used; CityId=74; __leadForm={"choices":{},"formData":{"cityName":"Gurgaon","cityId":"74"}}; lastUTMParamter=google#organic#null; _gcl_au=1.1.679323401.1792057362; CONNECTOID=aa92b0e4-42d2-6486-0e3e-a4259850b75f; pwa_source={"isDesktop":true,"isMobile":false,"domain":"https://www.cardekho.com","cellId":1}; __obref=85a50b9a-43fa-4f6b-b446-bc66d0a7a4a5; _CO_type=connecto; _CO_anonymousId=aa92b0e4-42d2-6486-0e3e-a4259850b75f; _pubcid=b36f5d9d-1012-4991-9547-5b29a25845a1; pbjs_debug=0; _ga=GA1.1.963978794.1792057363; _fbp=fb.1.1792057363151.2492765253294443; _cc_id=e43f386a7ddcfc565741501149c6c95b; panoramaId=f0ff10a69a112336889242c40231a9fb927acd44e070f9f0192de8d106b00350; panoramaIdType=panoDevice; _CO_html5PermissionStatus=%7B%22status%22%3A%22default%22%2C%22time%22%3A%222026-10-15T09%3A42%3A49.171Z%22%7D; srp_vdp_views=%7B%22s%22%3A100%2C%22v%22%3A0%7D; identifyCookie=eyJjYXJkZWtobyI6eyJfQ09faWQiOiJhYTkyYjBlNC00MmQyLTY0ODYtMGUzZS1hNDI1OTg1MGI3NWYiLCJsb3RhbWVfcGlkIjoiZTQzZjM4NmE3ZGRjZmM1NjU3NDE1MDExNDljNmM5NWIiLCJicm93c2VyTGlzdCI6W3siYnJvd3Nlck5hbWUiOiJDaHJvbWUiLCJicm93c2VyVmVyc2lvbiI6IjE1NS4wLjAuMCIsIm9zTmFtZSI6IldpbmRvd3MiLCJvc1ZlcnNpb24iOiIxMCIsImRldmljZVR5cGUiOiJkZXNrdG9wIn1dfX0=; srpAppliedFilters=%5B%7B%22l%22%3A%22Below%20%E2%82%B92L%22%2C%22v%22%3A%220-lakh-to-2-lakh%22%2C%22t%22%3A%22price%22%7D%5D; _co_session_active=1; __qca=I0-1577745515-1792080734294; __gads=ID=d9e7c38b80793e15:T=1792057360:RT=1792081239:S=ALNI_MY_QmTrGMWFKGXc7MgfHjKwGUM65w; __gpi=UID=000015af6ca6c938:T=1792057360:RT=1792081239:S=ALNI_MbOvH4ONzd0Tu0D4mQ-mW4Ibdikqw; __eoi=ID=0b236b058b7dc4ea:T=1792057360:RT=1792081239:S=AA-AfjYi7jQh7Bx99yl2eZ5G4xFW; recentSearches=%5B%7B%22u%22%3A%22used-cars%2B0-lakh-to-2-lakh%2Bin%2Bgurgaon%22%2C%22t%22%3A1792081298947%7D%5D; cto_bundle=JUtfxl91aXJsSDFQQlZoNlljd0p0JTJCaU5FUmtiNHlpZk5lV0VhYjVseUFEdGpZNXh5WGFmRFYlMkJIUk1aTU5HdmJNQnRKTWgxb2RCNkVQQ0lJYmJxdmQ4SUpYTGQ4dXVJT3gwQWJxTmk3alhGUFlCT1lUUlYlMkZXTWp4SjA1WW0wciUyRnBLbEVZdUw1REFoc0dqbHBvdlVhc2luVmc1ZyUzRCUzRA; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%220aa2f8c4-3a83-4c63-ae7c-25e9c2037fea%5C%22%2C%5B1792057362%2C227000000%5D%5D%22%5D%5D%5D; _ga_ZSZQ04WHM3=GS2.1.s1792080670$o3$g1$t1792081300$j1$l0$h0; FCNEC=%5B%5B%22AKsRol-iiRriaO59Dm-9m6pLI6k2zjXygdjydXSSDd_DaY85PuB0oABL6HjhCCE8h0UhV8MVeYNMLku_8qB4qMIoSWYd9SbPdeNfygdeKurugtkh1jXfjj9M9Jri1TwOD_xC2Dn5S4j1jXPV0GhKFGgvAgs1siw3eg%3D%3D%22%5D%5D; panoramaId_expiry=1792167717667',
    }

    response = requests.get(
        f'https://www.cardekho.com/used-cars+0-lakh-to-2-lakh+in+gurgaon//page-{current_page}',
        verify=False,
        headers=headers,
    )

    soup = BeautifulSoup(response.text, 'html.parser')
    LimitedCars_div = soup.find('div', class_ = 'LimitedCars')
    tag = LimitedCars_div.find('div', class_ = 'gsc_row')
    if tag.find('div', class_ = 'noCarSec'):
        break
    divs = tag.find_all('div', recursive=False)
    for div in divs:
        # if div.get('class') == 'noCarSec':
        #     x = True
        #     break
        try:
            data_div = div.find('div', class_ = 'title_heart_section')

            title_box = data_div.find('div', class_ = 'titlebox hover')
            title_box_flex = title_box.find('div', class_= 'titleboxFlex')
            flex_box = title_box_flex.find('div', class_ = 'flexbox')
            title_a_tag = flex_box.find('a')
            if title_a_tag and title_a_tag.get('href'):
                url = f'https://www.cardekho.com{title_a_tag.get('href')}'
                year = title_a_tag.find('span').text.strip()
                title = title_a_tag.text.strip().replace(year, '')
            price = title_box_flex.find('div', class_ = 'Price hover').text.strip()

            flex_2 = title_box.find('div', class_ = 'bottom_container_flex')
            dotsDetails  = flex_2.find('div', class_ = 'dotsDetails')
            ddivs = dotsDetails.find_all('div', recursive=False)
            kms_travelled = ddivs[0].text.strip()
            type_of_vehicle = ddivs[1].text.strip()
            consumption_type = ddivs[2].text.strip()

            address_tag = data_div.find('div', class_ = 'distanceText')
            address = address_tag.find('span').text.strip()

            record = {
                'Car Title' : title,
                'Price' : price,
                'Year' : year,
                'Kilometers Travelled' : kms_travelled,
                'Type of Vehicle' : type_of_vehicle,
                'Consumption Type' : consumption_type,
                'Address' : address,
                'Car Details URL' : url
            }
            pd.DataFrame([record]).to_csv('Car_Dekho_data.csv', mode='a', index = False, header=first)
            first = False
            # x = False
        except:
            pass
    # if x == True:
    #     break
    print(f'Page - {current_page}')
    current_page += 1