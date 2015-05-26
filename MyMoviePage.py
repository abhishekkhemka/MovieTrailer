import movie
import fresh_tomatoes

braveHeart = movie.Movie("BraveHeart",
                        "http://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=wj0I8xVTV18")

sr = movie.Movie("Shawshank Redemption",
                "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                "https://www.youtube.com/watch?v=6hB3S9bIaco")

bourneIdentity = movie.Movie("The Bourne Identity",
                            "http://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                            "https://www.youtube.com/watch?v=AfkNq0CDx6w")

movies = [braveHeart, sr,bourneIdentity]

fresh_tomatoes.open_movies_page(movies)
