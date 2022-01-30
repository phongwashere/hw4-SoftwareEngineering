import flask

main = flask.Flask(__name__)

favShow = ["How I met your mother","Big Bang Theory","Jimmy Neutron","Fairly Odd Parents","Property Brothers"]
favImages = [
    "https://m.media-amazon.com/images/M/MV5BNjg1MDQ5MjQ2N15BMl5BanBnXkFtZTYwNjI5NjA3._V1_FMjpg_UX1000_.jpg",
    "https://flxt.tmsimg.com/assets/p185554_b_v10_az.jpg",
    "http://s3.shoutfactory.com/images/32553/div_96/documents/d96c17r32553/JiNeBoGeTCS_DVD__Cover_72dpi.png",
    "https://m.media-amazon.com/images/M/MV5BNzUyOGEyMDQtOWVkMS00NGFkLTgxNWQtOWJiZTE0OTY3NjE2XkEyXkFqcGdeQXVyODA4OTIyMzY@._V1_FMjpg_UX1000_.jpg",
    "https://media.hgtv.ca/uploadedimages/landing_pages/show_pages/property_brothers/propertybrothers.jpg"
]

@main.route("/")
def index():
    return flask.render_template("index.html", len = len(favShow), favShow = favShow, favImages = favImages)

main.run(debug = True)