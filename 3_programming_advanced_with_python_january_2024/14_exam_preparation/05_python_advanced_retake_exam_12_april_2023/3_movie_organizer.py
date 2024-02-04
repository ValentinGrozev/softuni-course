def movie_organizer(*movies):
    movies_information = {}

    for movie, genre in movies:
        if genre not in movies_information:
            movies_information[genre] = []
        movies_information[genre].append(movie)

    sorted_movie_information = sorted(movies_information.items(), key=lambda x: (-len(x[1]), x[0]))

    collection = ''
    for genre, movies in sorted_movie_information:
        collection += f'{genre} - {len(movies)}\n'
        for movie in sorted(movies):
            collection += f"* {movie}\n"

    return collection


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
