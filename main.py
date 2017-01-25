import webapp2
import random

page-header =

def get(self):
    edit_header = "<h3>Edit My Watchlist</h3>"

    add_form = '''
    <form action="/add" method="post">
        <label>
        I want to add
        <input type="text" name="new_movie">
        to my watchlist.
        <input type="submit"
    '''

class AddMovie(webapp2.RequestHandler):
    def post(self):
        new_movie = self.request.get("new_movie")

        new_movie_element = "<strong>{}</stong>".format(new_movie)
        sentence = new_movie_element + " has been added to your watchlist."

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)


<<<<<<< HEAD
        cross_form = """
        <form action="/cross" method="post">
            <label>
                I want to remove
                <select name="crossed-off-movie">
                    <option value="Star Wars">Star Wars</option>
                    <option value="Minions">Minions</option>
                    <option value="Freaky Friday">Freaky Friday</option>
                    <option value="Highlander">Highlander</option>
            </label>
            <input type="submit" value="Cross It Off"/>
        </form>
        """

        content = page_header + edit_header + add_form + cross_form + page_footer
        self.response.write(content)
=======
class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        movie_list = ["The Big Lebowski", "The Hitchhiker's Guide to the Galaxy", "MegaMind", "The Wizard of Oz", "Star Wars", "Harry Potter"]

        movie = movie_list[random.randrange(len(movie_list))]

        return movie
>>>>>>> 1814e567db4d13fdf372cfa06d67c5c82e7f5164

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        content += "<h1>Movie for Tommorrow</h1>"
        content += "<p>{movie_a}</p>".format(movie_a=self.getRandomMovie())


        self.response.write(content)


<<<<<<< HEAD
# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".
class CrossOffMovie(webapp2.RequestHandler):
    """Handles requests for '/cross'"""
    def post(self):

        crossed_off = self.request.get("crossed-off-movie")

        message = "<strike>" + crossed_off + "</strike>" + " has been removed from your watchlist."
        content = page_header + "<p>" + message + "</p>" + page_footer

        self.response.write(content)



# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
=======
>>>>>>> 1814e567db4d13fdf372cfa06d67c5c82e7f5164
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross', CrossOffMovie)
], debug=True)
