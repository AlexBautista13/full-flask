from flask import Flask, render_template, request, jsonify 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.htm")

if __name__== "__main__":
    app.run(debug=True)

@app.route('/')
def show():
    return render_template("show.htm")

if __name__== "__main__":
    app.run(debug=True)