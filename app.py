from flask import Flask, render_template, request
from weather import Weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def display_weather_data():
    if request.method == "POST":
        input_data = request.form["search"] #data gotten from inputfield
        w = Weather()
        w_data = w.get_weather(input_data)
        formated_data = w.format_data(w_data)
        return render_template("index.html", content=formated_data, data=input_data)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
    