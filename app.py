from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")

@app.route("/Music")
def Music():
    return render_template("Music.html")

@app.route("/Projects")
def Projects():
    return render_template("Projects.html")

if __name__ == "__main__":
    app.run()