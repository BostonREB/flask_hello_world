from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template2.html', my_string="This is my STRING!!", my_list=[0,1,2,3,4,5,6,7])

@app.route("/hello")
def say_hi():
  return render_template('template2.html', my_string="Hello World!!")

@app.route("/hello/<name>")
def hi_person(name):
  return render_template('template2.html', my_string="Hello {}!".format(name.title()))

@app.route("/jedi/<first_name>/<last_name>")
def get_jedi_name(first_name, last_name):
  jedi_name = last_name[0:3] + first_name[0:2]
  return render_template('template2.html', my_string='Your Jedi Name is: {}'.format(jedi_name.title()))

@app.route("/home")
def home():
    return render_template('template2.html',
                           my_string="I'm the home page",
                           my_list=[0,1,2,3,4,5])

@app.route("/about")
def about():
    return render_template('template2.html',
                            my_string="I'm the about page",
                            my_list=[0,1,2,3,4,5])

@app.route("/contact")
def contact():
    return render_template('template2.html',
                           my_string="I'm the contact page",
                           my_list=[0,1,2,3,4,5])

if __name__ == "__main__":
  app.run()