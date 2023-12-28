import datetime
import requests

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos!.'.format(now.hour, now.minute)
        return answer
    
    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}'.format(now.day, now.month, now.year)
        return answer

    def get_weather(city_name):
        API_KEY = 'b2cb5554c22544762b967af9e5a17d85'  # Substitua pelo seu próprio API key
        API_URL = f'http://api.weatherstack.com/current?access_key={API_KEY}&query={city_name}'

        response = requests.get(API_URL)

        if response.status_code == 200:
            data = response.json()
            # Aqui você pode extrair as informações específicas que deseja, como temperatura, clima, etc.
            temperature = data['current']['temperature']
            weather_description = data['current']['weather_descriptions'][0]
            
            return f"A temperatura atual em {city_name} é {temperature}°C e o clima está {weather_description}."
        else:
            return "Não foi possível obter informações do clima."

class a:
    def __init__(self):
        pass
    
    @staticmethod
    def ok():
        answer = ' '
        return answer