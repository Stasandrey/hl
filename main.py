import requests

url_data = "https://api.openweathermap.org/data/2.5/weather"
key = "dbc2bb795a4c0ddb04c9cc2772b4809f"
p = {'q': 'baranovichi,by', 'appid': key}
kelvin = 273.15

class Weather:
    def __init__(self):
        pass

    def run(self):
        r = requests.get( url_data, params = p )

        return r


if __name__ == '__main__':
    print('Начало работы')
    w = Weather()
    res = w.run()
    print(res)
    res = res.json()
    print(res)
    print('Температура', res['main']['temp'] - kelvin)
    print('Ощущается как:', res['main']['feels_like'] - kelvin)
    print('Ветер', res['wind']['speed'])
    print('Направление', res['wind']['deg'])
