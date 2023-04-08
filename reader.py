import json

# v sentez vous libre de modifier cette variable au gré de vos besoins
FILES = ("StreamingHistory0.json", "StreamingHistory1.json")

def ms_to_readable(time_string: str) -> str:
    time = int(time_string)
    hours, mins = divmod(time, int(3.6e6))
    mins, secs = divmod(mins, int(6e4))
    secs //= int(1e3)
    return f"{hours}h {mins}m {secs}s"


def compile_data_from_files(files: tuple[str]) -> dict[str, int]:
    total = {}
    for file in files:
        with open(file) as contents:
            history = json.load(contents)
            for song in history:
                if total.get(song["artistName"]):
                    total[song["artistName"]] += int(song["msPlayed"])
                else:
                    total[song['artistName']] = int(song["msPlayed"])
    return total


def main(t_number) -> None:
    s = compile_data_from_files(FILES)
    keyz = list(s)
    keyz.sort(key=lambda x: s.get(x), reverse=True)
    top = keyz[:t_number]
    for rank, artist in enumerate(top, start=1):
        print(f"at number {rank}, we have {artist} with a total of {ms_to_readable(s.get(artist))}")


if __name__ == '__main__':
    top_number = int(input("How many artists would you like to see? "))
    main(top_number)
