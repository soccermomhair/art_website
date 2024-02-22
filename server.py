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


@app.route("/work/rooms/1")
def show_rooms_1():
    return render_template("rooms_1.html")


@app.route("/work/rooms/2")
def show_rooms_2():
    return render_template("rooms_2.html")


@app.route("/work/rooms/3")
def show_rooms_3():
    return render_template("rooms_3.html")


@app.route("/work/rooms/4")
def show_rooms_4():
    return render_template("rooms_4.html")


@app.route("/work/rooms/5")
def show_rooms_5():
    return render_template("rooms_5.html")


@app.route("/work/rooms/6")
def show_rooms_6():
    return render_template("rooms_6.html")


@app.route("/work/rooms/7")
def show_rooms_7():
    return render_template("rooms_7.html")


@app.route("/work/rooms/8")
def show_rooms_8():
    return render_template("rooms_8.html")


@app.route("/work/rooms/9")
def show_rooms_9():
    return render_template("rooms_9.html")


@app.route("/work/circling_bug")
def show_circling_bug():
    return render_template("circling_bug.html")


@app.route("/work/circling_bug/9099_weboptimized")
def show_circling_bug_shot():
    return render_template("9099_weboptimized.html")


@app.route("/work/woven_panels")
def show_woven_panels():
    return render_template("woven_panels.html")


@app.route("/work/woven_panels/leatherpouch")
def show_leather_pouch():
    return render_template("leatherpouch.html")


@app.route("/work/woven_panels/leatherpouch_detail")
def show_leather_pouch_detail():
    return render_template("leatherpouch_detail.html")


@app.route("/work/woven_panels/whitecoil")
def show_white_coil():
    return render_template("whitecoil.html")


@app.route("/work/woven_panels/whitecoil_detail")
def show_white_coil_detail():
    return render_template("whitecoil_detail.html")


@app.route("/work/woven_panels/orangering")
def show_orange_ring():
    return render_template("orangering.html")


@app.route("/work/woven_panels/orangering_detail")
def show_orange_ring_detail():
    return render_template("orangering_detail.html")


@app.route("/work/woven_panels/pinkmacrame")
def show_pink_macrame():
    return render_template("pinkmacrame.html")


@app.route("/work/woven_panels/pinkmacrame_detail")
def show_pink_macrame_detail():
    return render_template("pinkmacrame_detail.html")


@app.route("/work/woven_panels/greendiamond")
def show_green_diamond():
    return render_template("greendiamond.html")


@app.route("/work/woven_panels/greendiamond_detail")
def show_green_diamond_detail():
    return render_template("greendiamond_detail.html")


@app.route("/work/woven_panels/arch")
def show_arch():
    return render_template("arch.html")


@app.route("/work/woven_panels/arch_detail")
def show_arch_detail():
    return render_template("arch_detail.html")


@app.route("/work/objects_for_home/numbers")
def show_numbers():
    return render_template("numbers.html")


@app.route("/work/objects_for_home/carpet")
def show_carpet():
    return render_template("carpet.html")


@app.route("/work/objects_for_home/thesis_chair")
def show_thesis_chair():
    return render_template("thesis_chair.html")


@app.route("/work/objects_for_home/plexi_baskets")
def show_plexi_baskets():
    return render_template("plexi_baskets.html")


@app.route("/work/objects_for_home/plexi_baskets_detail")
def show_plexi_baskets_detail():
    return render_template("plexi_baskets_detail.html")


@app.route("/work/central_il/1")
def show_central_il_1():
    return render_template("central_il_1.html")


@app.route("/work/central_il/2")
def show_central_il_2():
    return render_template("central_il_2.html")


@app.route("/work/central_il/3")
def show_central_il_3():
    return render_template("central_il_3.html")


@app.route("/work/central_il/4")
def show_central_il_4():
    return render_template("central_il_4.html")


@app.route("/work/ice_cream_truck")
def show_ice_cream_truck():
    return render_template("ice_cream_truck.html")


@app.route("/work/woven_panels/whitetear")
def show_white_tear():
    return render_template("whitetear.html")


@app.route("/work/woven_panels/whitetear_detail")
def show_white_tear_detail():
    return render_template("whitetear_detail.html")


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
