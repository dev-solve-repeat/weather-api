from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station.zfill(6)) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    # return render_template("about.html")
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

if __name__ == "__main__":
    app.run(debug=True)

"""When this script is executed then value of __name__ is __main__. Otherwise if this script 
is executed after importing this in another script. Then value of __name __ will be just value of the 
python file i.e main. 
"""
