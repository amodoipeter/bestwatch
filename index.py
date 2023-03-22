from flask import Flask, render_template, url_for, request, session, redirect, flash
import requests
app = Flask(__name__)
app.secret_key="bestwatch"
# route = url = link


@app.route("/")
def main():
    fetchedData = requests.get("https://www.omdbapi.com/?apikey=20f5e004&s=batman")
    movies = fetchedData.json()
    
    return render_template("home.html", movies=movies)

@app.route("/<title>")
def movie_by_title(title):
    fetchedData = requests.get("https://www.omdbapi.com/?apikey=20f5e004&s="+title)
    movies = fetchedData.json()
    
    return render_template("home.html", movies=movies)

@app.route("/single_move/<title>")
def single_movie(title):
    fetchedData = requests.get("https://www.omdbapi.com/?apikey=20f5e004&t="+title)
    movie = fetchedData.json()
    
    return render_template("movie.html", movie=movie)

@app.route("/search")
def search_form():
    return render_template("search.html")

@app.route("/search_by_title", methods=["post"])
def search_by_title():
    title = request.form["title"]
    year = request.form["year"]
    if year != "":
        fetchedData = requests.get("https://www.omdbapi.com/?apikey=20f5e004&t="+title+"&y="+year)
    else:
        fetchedData = requests.get("https://www.omdbapi.com/?apikey=20f5e004&t="+title)
    
    movie = fetchedData.json()
    
    return render_template("search.html", movie=movie)

@app.route("/favorite_list")
def favorite_list():
    favorite_list = session.get("favorite")
    if favorite_list == None:
        flash("The favorite list is empty")
        return redirect(url_for("main"))
    else:
        return render_template("favorite.html", favorite_list=favorite_list)
    
@app.route("/add_to_favorite/<title>")
def add_to_favorite(title):
    favorite_list = {}
    if "favorite" in session:
        favorite_list = session.get("favorite")
    else:
        session["favorite"] = {}
    favorite_list[title] = title
    session["favorite"] = favorite_list
    return redirect(url_for("main"))
    
@app.route("/remove_from_favorite/<title>")
def remove_from_favorite(title):
    favorite_list = session.get('favorite')
    favorite_list.pop(title, None)
    session['favorite'] = favorite_list
    return redirect(url_for('favorite_list'))


if __name__ == "__main__":
    app.run(debug=True)
