# First, we import the Flask class from the Flask library.
from flask import Flask 

# We create a Flask application named app and specify the __name__ parameter as the name of our application.
app = Flask(__name__)

# The @app.route('/') decorator is used to handle HTTP GET requests to the root directory. 
# So, when the web browser accesses the root directory, the head function is executed, 
# and the response 'Hello world Human!' is returned to the browser.
@app.route('/')
def head():
    return 'Hello world Human!'

# The @app.route('/second') decorator is used to handle HTTP GET requests to the '/second' path. 
# So, when the '/second' path is accessed, the second function is executed, 
# and the response 'This is the second page' is returned to the browser.
@app.route('/second')
def second():
    return 'This is second page'

# The @app.route('/third') decorator is used to handle HTTP GET requests to the '/third' path. 
# So, when the '/third' path is accessed, the third function is executed, 
# and the response 'This is the third page' is returned to the browser.
@app.route('/third')
def third():
    return 'This is third page'

# The @app.route('/forth/<string:id>') decorator is used to handle HTTP GET requests to the '/forth/...' 
# path. Here, the id parameter is a string specified in the URL. 
# For example, when '/forth/123' path is accessed, the forth function is executed, and the response 'Id of this page is 123' is returned to the browser.
@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'

# The if __name__ == '__main__': block checks if this file is being run directly. 
# So, this block will not execute when this file is imported by another file.
if __name__ == '__main__':

# Finally, the app.run(debug=True) statement starts the Flask application and runs the web server. 
# The debug=True parameter enables the debug mode, so detailed error messages are shown in the web browser.
    app.run(debug=True)