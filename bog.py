from flask import Flask, redirect, url_for, render_template, request
from find_friends import write_to_file
from third_main import on_map

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home page
    """
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    """
    To get data from user
    """
    domain = request.form.get("domain")
    tocker = request.form.get("tocker")
    return f'{domain} {tocker}'


@app.route("/register/yakarta", methods=["POST"])
def file_html():
    """
    To return user a map
    """
    try:
        tockers = register().split()
        bearer_token = tockers[1]
        usr_name = tockers[0]
        file_friends = write_to_file(bearer_token, usr_name)
        mapa = on_map('friends_here.json')
        return mapa.get_root().render()
    except IndexError:
        return render_template("failure.html")

if __name__ == "__main__":
    app.run(debug=True)