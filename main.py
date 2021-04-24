import requests
import json
#za opis koda, pogledati objasnjenje.txt.
# d81d4c7d - moze se koristiti moj api kljuc

urls = []
data = []
print('Unesi svoj api kljuc')
api_kljuc = input()

base_url = 'http://www.omdbapi.com/?apikey=' + api_kljuc

print('///Base url napravljen///')

print('Unesi imena filmova razmaknuta zarezom(,)')

titles = input('>>>').replace(" ", "+").split(',')

for title in titles:
     final_url = base_url + '&t=' + title
     urls.append(final_url)

print(urls)

for url in urls:
    request = requests.get(url)
    x = request.json()
    data.append(x)
print(data)


with open('output.txt', 'w') as file:
    file.write(json.dumps(data))



