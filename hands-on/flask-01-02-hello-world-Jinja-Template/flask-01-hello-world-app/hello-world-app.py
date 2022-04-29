from flask import Flask
app = Flask(__name__)

@app.route("/")
def head():
    return '<h1>Hello World!</h1>'

@app.route("/second")
def second():
    return 'This is my second page'

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpage of my third page!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
