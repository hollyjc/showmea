from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def enter_page():
    return "<h1> enter page </h1>"

@app.errorhandler(404)
def page_error(e):
    print(e, "\n\n")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)