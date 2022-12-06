import urllib.request
import json
import time

def get_weather():
    weather_url = 'http://127.0.0.1:5000/weather_api/v1/'
    response = urllib.request.urlopen(weather_url)
    weather_topics = response.read()
    json_topics = json.loads(weather_topics)
    print(json_topics)

def get_choice(choice):
    choice_url = f'http://127.0.0.1:5000/weather_api/v1/{choice}'
    response = urllib.request.urlopen(choice_url)
    hum_temp = response.read()
    json_hum_temp = json.loads(hum_temp)
    print(choice, json_hum_temp)

if __name__ == "__main__":
    main_loop = True
    while main_loop == True:
        choice = input('Fetch:\n' \
                   '1. All data\n' \
                   '2. Temperature data\n' \
                   '3. Humidity data\n' \
                   'To exit type "exit"\n')
        loop = True
        while (loop==True):
            time.sleep(1)
            if choice == '1':
                main_loop = False
                get_weather()
                fetching_choice = input('1. Continue \n'
                                        '2. Back to main menu \n')
                if fetching_choice == '2':
                    main_loop = True
                    loop = False
                elif fetching_choice == '1':
                    continue
            if choice == '2':
                main_loop = False
                choice = 'temp'
                get_choice(choice)
                fetching_choice = input('1. Continue \n'
                                        '2. Back to main menu \n')
                if fetching_choice == '2':
                    main_loop = True
                    loop = False
                elif fetching_choice == '1':
                    continue
            if choice == '3':
                main_loop = False
                choice = 'humidity'
                get_choice(choice)
                fetching_choice = input('1. Continue \n'
                                        '2. Back to main menu \n')
                if fetching_choice == '2':
                    main_loop = True
                    loop = False
                elif fetching_choice == '1':
                    continue
            elif (choice == 'exit'):
                main_loop = False
                loop = False




