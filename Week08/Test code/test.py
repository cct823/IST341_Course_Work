import requests
import string
import json

search_url = "https://itunes.apple.com/search"
parameters = {"term": 'Jack Johnson', "entity": "musicArtist", "media": "music", "limit": 200}
result = requests.get(search_url, params=parameters)
data = result.json()

# save to a local file so we can examine it
filename_to_save = "appledata.json"
f = open(filename_to_save, "w")  # opens the file for writing
string_data = json.dumps(data, indent=2)  # this writes it to a string
f.write(string_data)  # then, writes that string to a file...
f.close()  # and closes the file
print("\nfile", filename_to_save, "written.")

with open('appledata.json', 'r') as f:
    distros_dict = json.load(f)

artistid = []
for i in range(len(distros_dict['results'])):
    if 'Jack Johnson' == distros_dict['results'][i]['artistName']:
        artistid.append(distros_dict['results'][i]['artistId'])
print(artistid)