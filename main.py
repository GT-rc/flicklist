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


class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        movie_list = ["The Big Lebowski", "The Hitchhiker's Guide to the Galaxy", "MegaMind", "The Wizard of Oz", "Star Wars", "Harry Potter"]

        movie = movie_list[random.randrange(len(movie_list))]

        return movie

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        content += "<h1>Movie for Tommorrow</h1>"
        content += "<p>{movie_a}</p>".format(movie_a=self.getRandomMovie())


        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie)
], debug=True)
