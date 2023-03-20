from flask import Flask, render_template
import requests
app = Flask(__name__)

# route = url = link


@app.route("/")
def main():
    fetchedData = requests.get("https://www.omdbapi.com/?apikey=20f5e004&s=batman")
    movies = fetchedData.json()
    
    return render_template("home.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
