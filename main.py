import webapp2
import random

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
    ('/', Index)
], debug=True)
