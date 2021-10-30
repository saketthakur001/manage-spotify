import json

# loc = r'D:\music\spotify data'
data = open(r"C:\Users\saket\Desktop\MyData\Stream_History.json", encoding="utf-8")
ordered_tracks_ = open(r'C:\Users\saket\Desktop\MyData\tracks_data.txt', 'w', encoding='utf-8')
data = json.load(data)
trackname = []

for i in data:
    trackname.append(i['artistName']+' - '+i['trackName'])

track_count = {}

for i in trackname:
    if i not in track_count:
        track_count[i] = trackname.count(i)
        # print(i, trackname.count(i))
        trackname.remove(i)

oredted_track = []
track_count_count = len(track_count)
while len(oredted_track) < track_count_count:
    count, track = 0, None
    for i in track_count:
        if track_count[i] > count:
            count, track = track_count[i], i
    # print(track)
    track_count.pop(track)
    oredted_track.append(track)
    ordered_tracks_.write(track+'\n')

    # print(count, track)

# print(len(oredted_track))
# ordered_tracks_.close()