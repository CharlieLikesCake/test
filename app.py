import flask

from nyt import article_search

app= flask.Flask(__name__)

@app.route("/", method=["GET", "POST"])
def index():
    if flask.request.method =="POST":
        query = flask.request.form.get("query")
    else:
        query = "Apple"
    headlines, snippets = article_search()
    return flask.render_template(
        "index.html",
        num_articles=len(headlines),
        headlines=headlines,
        snippets=snippets,
    )


app.run()