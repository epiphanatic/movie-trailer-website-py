import media
import fresh_tomatoes
# since media is the file that contains all the classes, it is also the 'library'
# following calls the init function in the Movie class in the media library that requires arguments listed
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_matrix = media.Movie("The Matrix",
                         "I took the red pill...",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

fight_club = media.Movie("Fight Club",
                         "You're not your fucking khakis",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "Get busy livin, or get busy dyin, that's goddamned right",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

three_hundred = media.Movie("300",
                            "Does anybody know wtf this is about? seriously",
                            "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
                            "https://www.youtube.com/watch?v=UrIbxk7idYA")

movies = [toy_story, avatar, the_matrix, fight_club, shawshank_redemption, three_hundred]

fresh_tomatoes.open_movies_page(movies)