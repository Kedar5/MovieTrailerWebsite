import media

import fresh_tomatoes

#Creating instances of class Movie for different movies.
iron_man = media.Movie("Iron Man",
                        "American superhero film on Genius, billionaire, playboy and philanthropist Tony Stark.",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=8hYlB38asDY")

titanic = media.Movie("Titanic",
                     "A fictionalized epic romance-disaster film of the sinking of the RMS Titanic.",
                     "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                     "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

#Creating a list of movies and store it in variable movies. 
movies = [iron_man, titanic, avatar]

#Pass the list of movies to the class open_movies_page of fresh_tomatoes html page.
fresh_tomatoes.open_movies_page(movies)
