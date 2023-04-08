import json


def ms_to_readable(time_string: str) -> str:
    time = int(time_string)
    hours, mins = divmod(time, int(3.6e6))
    mins, secs = divmod(mins, int(6e4))
    secs %= int(e3)
    return f"{hours}h {mins}m {secs}s"


f = open('StreamingHistory0.json')
history=json.loads(f.read())
total = {}


for song in history:
    if total.get(song["artistName"]):
        total[song["artistName"]] += int(song["msPlayed"])
    else:
        total[song['artistName']] = int(song["msPlayed"])

f.close()
