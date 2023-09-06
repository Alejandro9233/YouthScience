from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    areas = {1,2,3,4,5,6}
    return render_template("home.html", areas = areas)

@app.route("/nosotros")
def us():
    areas = {1,2,3,4,5,6}
    return render_template("nosotros.html", areas = areas)


if __name__ == '__main__':
    app.run(debug = True)