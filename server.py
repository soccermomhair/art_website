from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "EllenRoseLacher"


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/work")
def show_entry():
    return render_template("work.html")


@app.route("/work/macrame_hangings")
def show_macrame_hangings():
    return render_template("macrameHangings.html")


@app.route("/work/objects_for_home")
def show_objects_for_the_home():
    return render_template("objects_for_home.html")


@app.route("/work/central_illinois")
def show_central_illinois():
    return render_template("central_illinois.html")


@app.route("/work/rooms")
def show_rooms():
    return render_template("rooms.html")


@app.route("/work/circling_bug")
def show_circling_bug():
    return render_template("circling_bug.html")


@app.route("/work/woven_panels")
def show_woven_panels():
    return render_template("woven_panels.html")


@app.route("/work/ice_cream_truck")
def show_ice_cream_truck():
    return render_template("ice_cream_truck.html")


@app.route("/work/every_cat_ive_ever_slept_with")
def show_every_cat_ive_ever_slept_with():
    return render_template("every_cat_ive_ever_slept_with.html")


@app.route("/work/glass")
def show_glass():
    return render_template("glass.html")


@app.route("/work/mound")
def show_mound():
    return render_template("mound.html")


@app.route("/work/older_work")
def show_assemblage():
    return render_template("older_work.html")


@app.route("/work/furniture")
def show_furniture():
    return render_template("furniture.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/go_back")
def reset():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
