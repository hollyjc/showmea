from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def enter_page():
    return render_template('enter.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/sad")
def about():
    return render_template('sad.html')

@app.errorhandler(404)
def page_error(e):
    print(e, "\n\n")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)