import media

import fresh_tomatoes

# Creating instances of class Movie for different movies.
iron_man = media.Movie("Iron Man",
                       "American superhero film on Tony Stark",
                       "https://bit.ly/2rLG8b8",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

titanic = media.Movie("Titanic",
                      "A film on sinking of the RMS Titanic.",
                      "https://bit.ly/2uKv6RE",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://bit.ly/1JofiD1",
                     "https://youtu.be/5PSNL1qE6VY")

# Creating a list of movies and store it in variable movies.
movies = [
    iron_man,
    titanic,
    avatar
]

""" Pass the list of movies as arguement to the
class open_movies_page of fresh_tomatoes html page."""
fresh_tomatoes.open_movies_page(movies)
