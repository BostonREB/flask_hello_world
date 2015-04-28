from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def say_hi():
  return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
  return "Hello {}!".format(name.title())

@app.route("/jedi/<first_name>/<last_name>")
def get_jedi_name(first_name, last_name):
  jedi_name = last_name[0:3] + first_name[0:2]
  html = """
    <h1>
      Hello!
    </h1>
    <p> Your Jedi name is: <b>{}</b></p>
  """
  return html.format(jedi_name.title())

if __name__ == "__main__":
  app.run()