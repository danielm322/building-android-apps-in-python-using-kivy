import requests
files = {'media': open('/home/daniel/CLionProjects/C++_game_dev/Chapter_5_Finalizing_the_game/Assets/graphics/Adelita_1_small.png', 'rb')}
try:
    requests.post('http://192.168.0.12:6666/', files=files)
except requests.exceptions.ConnectionError:
    print("Connection Error! Make Sure Server is Active.")