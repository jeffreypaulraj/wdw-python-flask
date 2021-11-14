from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home_func():
    title = "Jeff's WDW Site"
    return render_template("generic.html", title = title)

@app.route('/page2')
def pg2_func():
    return render_template("elements.html")

if __name__ == "__main__":
    app.run(debug=True)