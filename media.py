import webbrowser


class Movie:

    """
    This class allows code elsewhere to create instances of the class
    Movie.

    It has an init method that takes in four parameters:
       movie_title, movie_storyline, poster_image, trailer_youtube
    and assigns the value of those parameters to instance variables.

    The instances created are then later passed to fresh_tomatoes.py where
       they are used to provide information to the webpage to be displayed

    The class contains one class variable (VALID_RATINGS) that can be used
       to check whether or not a rating is valid if one chooses to include
       that information in their webpage.

    The class contains one instance method (show_trailer), that plays the
       movie trailer for whatever instance is passed to it (self).

    """

    # this is a class variable - can be used for all instances.
    # when declaring static variables like this, make it all caps

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Remember, init creates space in memory for a new instance of Movie when
    #    the class is called
    # Below is also known as the constructor
    # self is the object/instance being created via the function that
    #    instantiates a Movie object. So, when toy_story = media.Movie() in
    # entertainment_center.py then self is toy_story

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method/s
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
