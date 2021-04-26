import requests
import json
#za dodatan opis koda, pogledati objasnjenje.txt.


urls = []  #inicijalizujem listu gde cu cuvati url-ove
data = {}  #inicijalizujem recnik gde cu privremeno cuvati podatke o filmovima

print('Unesi svoj api kljuc')
# d81d4c7d - moze se koristiti moj api kljuc
api_kljuc = input()

base_url = 'http://www.omdbapi.com/?apikey=' + api_kljuc

print('///Base url napravljen///')

print('Unesi imena filmova razmaknuta zarezom(,)')

titles = input('>>>').replace(" ", "+").split(',') #prihvatam podatke od korisnika

for title in titles: #prolazim kroz listu filmova
     final_url = base_url + '&t=' + title #za svaki film formiram jeidnstveni url
     urls.append(final_url) #koji potom pothranjujem u listu urls

print(urls) #printam url-ove

for url in urls: #prolazim kroz listu url-ova
    request = requests.get(url) #saljem get request za svaki url pojedinacno i stavljam ga u promenljivu
    data[url] = request.json()  #potom tu promenljivu pretvaram u json i pothranjujem je u recnik data

print(data)

with open('output.txt', 'w') as file:
    file.write(json.dumps(data))



