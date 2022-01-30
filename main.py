import flask

main = flask.Flask(__name__)

favMovies = ["How I met your mother","Big Bang Theory","Jimmy Neutron","Fairly Odd Parents","Property Brothers"]

@main.route("/")
def index():
    return flask.render_template("index.html", len = len(favMovies), favMovies = favMovies)

main.run(debug = True)