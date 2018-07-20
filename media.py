import webbrowser


class Movie():
    """
        The class Movie is used to store all the information related to movies.

        Args:
            movie_title (str): Movie title of different movies.
            movie_storyline (str): Description of movie in few lines.
            poster_image (str): image of the poster to be displayed.
            trailer_youtube (str): YouTube trailer shortened url.
    """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        # Store movie title in instance variable title.
        self.title = movie_title
        # Store story line in instance variable storyline.
        self.storyline = movie_storyline
        # Store poster image in instance variable poster_image_url.
        self.poster_image_url = poster_image
        # Store youtube url in instance variable trailer_youtube.
        self.trailer_youtube_url = trailer_youtube
