def add_songs(*songs_information):
    songs_and_lyrics = {}

    for song, lyrics in songs_information:
        if song not in songs_and_lyrics:
            songs_and_lyrics[song] = []
        for current_lyric in lyrics:
            if len(current_lyric) > 0:
                songs_and_lyrics[song].append(current_lyric)

    result = ''

    for current_song, current_lyrics in songs_and_lyrics.items():
        result += f"- {current_song}\n"
        for current_lyric in current_lyrics:
            result += f"{current_lyric}\n"

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
