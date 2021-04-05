from flask import Flask, render_template, request
from flask_mail import Mail
import os

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

@app.route("/contact")
def contact():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        Mail.send_message('New Message from Show Me A Racoon', sender=email, recipients='holly_cooper@live.com.au',
                          body=subject)
    return render_template('contact.html')

@app.route("/sad")
def sad():
    return render_template('sad.html')

@app.errorhandler(404)
def page_error(e):
    print(e, "\n\n")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= os.environ.get("PORT", 5000), debug=False)