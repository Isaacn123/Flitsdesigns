from flask import Flask,redirect,render_template

app = Flask(__name__)

@app.route("/")
def get_root():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about_us.html")

@app.route("/services")
def service_page():
    return render_template("services.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)