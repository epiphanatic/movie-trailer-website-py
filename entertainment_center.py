import media
import fresh_tomatoes

# Since media is the file that contains all the classes, it is also the
#   'library'

# The following calls the init function in the Movie class in the media
#   library that requires arguments listed in order to make instances
#   of the Movie class that will be fed to the website.
# So for example, toy_story is an instance of the Movie class in the media
#   library. As is avatar, the_matrix, etc. Each of the lines are a
#   parameter that becomes an instance variable in the Movie init def.
# The init def requires 4 parameters (movie_title, movie_storyline,
#   poster_image, trailer_youtube), hence the 4 lines in each instance
#   that make up these parameters.

toy_story = media.Movie(
    "Toy Story",
    "A Story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4"
)

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

the_matrix = media.Movie(
    "The Matrix",
    "I took the red pill...",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU"
)

fight_club = media.Movie(
    "Fight Club",
    "You're not your fucking khakis",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg"
)

shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "Get busy livin, or get busy dyin, that's goddamned right",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6hB3S9bIaco"
)

three_hundred = media.Movie(
    "300",
    "Does anybody know wtf this is about? seriously",
    "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
    "https://www.youtube.com/watch?v=UrIbxk7idYA"
)

# The following list provides the movies that we wish to render in
#   fresh_tomatoes.py
# While the instances are created above, the only ones that will actually
#   get rendered are what gets put in the list.
# So for example, if you remove three_hundred from the list and run the
#   script, then the movie 300 will not show up.

movies = [
    toy_story, avatar, the_matrix, fight_club, shawshank_redemption,
    three_hundred
]

# The following calls the open_movies_page def in fresh_tomatoes.py, and
#   passes it the list above so that it knows which movies to show.
# By doing this, a browser window is opened and the movies are listed.

fresh_tomatoes.open_movies_page(movies)

# The following line will print the documentation for the Media class,
#   which is located right beneath the class declaration in media.py
#   in triple quotes.

print (media.Movie.__doc__)
