import requests

url = 'https://www.cs.hmc.edu/~dodds/demo.html'

result= requests.get(url)


t = result.text