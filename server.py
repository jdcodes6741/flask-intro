"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the <a href='/hello'>home page.</a></html>"


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    compliment_select = """<select name='name'>"""
    for compliment in AWESOMENESS:
      compliment_select += f"<option value='{compliment}'>{compliment}</option>"
    compliment_select += """</select>"""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <div>
          <form action="/greet" method="POST">
            What's your name? <input type="text" name="person">
            <input type="submit" value="Submit">

            {}
          </form>
        </div>
        <div>
           <form action="/diss" method="POST">
            What's your name? <input type="text" name="person">
            <input type="submit" value="Submit">

            <select name="choose-diss">
              <option value="ugly">Ugly</option>
              <option value="smelly">Smelly</option>
              <option value="bitter">Bitter</option>
            </select>
          </form>
        </div>
      </body>
    </html>
    """.format(compliment_select)


@app.route("/greet", methods=['POST'])
def greet_person():
    """Get user by name."""

    player = request.form.get("person")

    compliment = request.form.get("name")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss", methods=['POST'])
def diss_person():
    """Get user by name."""

    player = request.form.get("person")

    diss = request.form.get("choose-diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
