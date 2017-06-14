import requests
response = requests.get('http://api.petfinder.com/breed.list?key=12345&arg1=foo')
if resp.status_code != 200:
    #something is wrong
    raise ApiError('GET/breedlist'/{}.format/resp.status_code)
for breed in response.json():
    print('{} {}'.format(breed['Animal'],breed['type of animal']))