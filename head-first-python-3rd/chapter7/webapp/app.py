from flask import Flask, session, render_template, request
import os
import swimclub
import data_utils
import convert_utils

app = Flask(__name__)
app.secret_key = "VLp5thL?-suslprlH8Vu"


@app.get("/")
def index():
    return render_template("index.html",
                           title="Welcome to the Swimclub")


def populate_data():
    if "swimmers" not in session:
        swim_files = os.listdir(swimclub.FOLDER)
        swim_files.remove('.DS_Store')
        session["swimmers"] = {}
        for file in swim_files:
            name, *_ = swimclub.read_swim_data(file)
            if name not in session["swimmers"]:
                session["swimmers"][name] = []
            session["swimmers"][name].append(file)


@app.get("/swims")
def display_swim_sessions():
    data = data_utils.get_swim_sessions()
    dates = [session[0].split(" ")[0] for session in data]
    return render_template(
        "select.html",
        title="Select a swim session",
        url="/swimmers",
        select_id="chosen_date",
        data=dates
    )


@app.post("/swimmers")
def display_swimmers():
    session["chosen_date"] = request.form["chosen_date"]
    data = data_utils.get_session_swimmers(session["chosen_date"])
    swimmers = [f"{swimmer[0]}-{swimmer[1]}" for swimmer in data]
    return render_template("select.html",
                           title="Select a swimmer",
                           url="/showevents",
                           select_id="swimmer",
                           data=sorted(swimmers))


@app.get("/showfiles/<swimmer>")
def get_swimmers_files(swimmer):
    populate_data()
    return str(session["swimmers"][swimmer])


@app.post("/showevents")
def display_swimmer_files():
    session["swimmer"], session["age"] = request.form["swimmer"].split("-")
    data = data_utils.get_swimmers_events(
        session["swimmer"], session["age"], session["chosen_date"])
    events = [f"{event[0]} {event[1]}" for event in data]
    return render_template("select.html",
                           title="Select a swimmer",
                           url="/showbarchart",
                           select_id="event",
                           data=events)


@app.post("/showbarchart")
def show_bar_chart():
    distance, stroke = request.form["event"].split(" ")
    data = data_utils.get_swimmers_times(
        session["swimmer"],
        session["age"],
        distance,
        stroke,
        session["chosen_date"],
    )
    times = [time[0] for time in data]
    world_records = convert_utils.get_worlds(distance, stroke)
    average_str, times_reversed, scaled = convert_utils.perform_conversions(
        times)
    header = f"{session['swimmer']} (Under {session['age']}) {distance} {stroke} - {session['chosen_date']}"
    return render_template("chart.html",
                           title=header,
                           average=average_str,
                           worlds=world_records,
                           data=list(zip(times_reversed, scaled)))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
