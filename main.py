import requests
from pyfiglet import Figlet as fig
import folium



def get_info_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]' : response.get('query'),
            '[Int prov]' : response.get('ips'),
            '[Country]' : response.get('country'),
            '[City]' : response.get('city'),
            '[Zip]' : response.get('zip'),
            '[Lat]' : response.get('lat'),
            '[Lon]' : response.get('lon')
        }

        area = folium.Map(location=[response.get('lat'),response.get('lon')],
                          zoom_start=1000)
        area.save(f'{response.get("query")}_{response.get("city")}.html')


        for k,v in data.items():
            print(f'{k} : {v}')

    except requests.exceptions.ConnectionError:
        print('Please check your connection!')


def main():
    preview_text = fig(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Enter the ip of the target:')
    get_info_ip(ip=ip)

if __name__ == '__main__':
    main()