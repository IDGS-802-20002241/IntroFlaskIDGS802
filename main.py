from flask import Flask
app=Flask(__name__)

@app.route("/")

def hola():
    return "<p>Hola mundo<p>"

if __name__ == "__main__":
    app.run()