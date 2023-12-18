import datetime

class SystemInfo:
    def __init__(self):
        pass

    #comandos iniciais

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos!. você precisa de mais alguma coisa?'.format(now.hour, now.minute)
        return answer
    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}'.format(now.day, now.month, now.year)
        return answer

    #@staticmethod
    #def get_weather():
        #now = weather.weather.now()
        #answer = 'Hoje a temperatura e previão do tempo é'.format(now.temperature, now.clime)
        #return answer

class a:
    def __init__(self):
        pass
    @staticmethod
    def ok():
        answer = ' '
        return answer