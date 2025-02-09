import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)  # Flask is to create the flask application isrender_Templates to render HTML,

# jsonify is going to take the dictionary and conmvert it into json so that we can easily return it to the frontend
from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)


@app.route(
    "/"
)  # Our home page, it's going to load an index.html file we share the path to
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with(name=name)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url,  # If you are using mock=True, it wouldn't be able to show you the profile pic because the
            # link will expire in 1 hour
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
