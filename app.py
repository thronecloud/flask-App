from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/airdrop')
def airdrop():
    title = "Batch Airdrop Check for Uniswap, Tornado & 1Inch"
    return render_template("airdrop.html",title=title)
    