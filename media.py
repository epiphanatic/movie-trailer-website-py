import webbrowser


class Movie:
    """This is documentation, notice the triple quotes. Print __doc__ to see"""

    # this is a class variable - can be used for all instances.
    # when declaring static variables like this, make it all caps
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Remember, init creates space in memory for a new instance of Movie when the class is called
    # below is also known as the constructor
    # self is the object/instance being created via the function that instantiates a Movie object
    #    so, when toy_story = media.Movie() in entertainment_center.py then self is toy_story
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method/s
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)