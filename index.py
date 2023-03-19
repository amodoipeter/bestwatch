from flask import Flask

app = Flask(__name__)

# route = url = link


@app.route("/")
def main():
    return "This is a flask movies web app"


if __name__ == "__main__":
    app.run(debug=True)
