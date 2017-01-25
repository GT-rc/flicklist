import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

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


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)


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
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross', CrossOffMovie)
], debug=True)
