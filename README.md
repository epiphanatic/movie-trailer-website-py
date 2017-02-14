# movie-trailer-website-py
Python driven web site where user can see movie trailers by clicking on a movie poster image

# Dependencies

You must have python installed in order to start the site

See instructions [here](https://classroom.udacity.com/nanodegrees/nd004/parts/0041345401/modules/356120945175460/lessons/990110642/concepts/36256587390923#) for Mac

See instructions [here](https://classroom.udacity.com/nanodegrees/nd004/parts/0041345401/modules/356120945175460/lessons/990110642/concepts/36691786570923#) for Windows

# Starting the site

Clone this repository or download the zip file.

In a command line, go to the project directory on your computer (wherever your cloned it to, or extracted the zip file) and type:
```
python entertainment_center.py
```

# Adding your own movies

Open the entertainment_center.py file. Copy and paste an instance of the Movie class such as:

```toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")```

Change toy_story to reflect what movie you would like to see (e.g. jurassic_park)
Change the four parameters (in the following order) to have the title, storyline, poster image, and link to the trailer.
So for example, a new one might look like:

```jurassic_park = media.Movie("Jurassic Park",
                        "An Adventure 65 Million Years In The Making",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_.jpg",
                        "http://www.imdb.com/video/imdb/vi177055257?playlistId=tt0107290&ref_=tt_ov_vi")```

Stop the python program (ctrl+c) and restart - you should see your movie added

