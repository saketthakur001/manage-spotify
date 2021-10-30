import json
loc = r'C:\Users\saket\Documents\GitHub\Pyhton\1Project_spotify\StreamingHistory.json'

f = open(loc, encoding="utf8")

data = json.load(f)

tracks = []
artists = []
for i in data:
    artists.append(i['artistName'])
    tracks.append(i['trackName'])
f = open('tracks.csv', 'w+', encoding='utf-8')


###### TRAck
f.write('trackName, Times\n')
lis = []
for i in tracks:
    if not {i:tracks.count(i)} in lis:
        lis.append({i:tracks.count(i)})
        f.write(i+', '+str(tracks.count(i))+'\n')


f = open('artists.csv', 'w+', encoding='utf-8')
##### ARTist
f.write('ArtistName,'+'Times\n')
lis = []
for i in artists:
    if not {i:tracks.count(i)} in lis:
        lis.append({i:tracks.count(i)})
        f.write(i+', '+str(artists.count(i))+'\n')