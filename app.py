from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-in-production"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/news-detail/")
def news_detail():
    return render_template("news_detail.html")


@app.route("/special-offer/")
def special_offer():
    return render_template("special_offer.html")


@app.route("/appointment", methods=["POST"])
def appointment():
    # Minimal handling: read form, redirect with flash
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    flash("Thank you for your request. We'll contact you soon.")
    return redirect(url_for("index", _anchor="appointment"))


if __name__ == "__main__":
    app.run(debug=True)
