


from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>this is main page</p>"

@app.route("/about")
def about():
    return "<p>this is about page</p>"


@app.route("/careers")
def carrers():
    return "<p>careers page</p>"



app.run()