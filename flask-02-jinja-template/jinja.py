# We import the Flask and render_template modules.
from flask import Flask, render_template

# We create a Flask application.
# The __name__ variable is a special variable in Python that contains the name of the Python file. 
# We use this parameter to ensure the Flask application runs correctly.
app = Flask(__name__)

# The @app.route('/') decorator indicates that we are defining a function for the "/" URL route. 
# We define the "head" function, which will be executed when a request is made to this route. 
# The function uses the render_template function to return the "index.html" template file. 
# Additionally, we assign values 112500 and 225200 to the number1 and number2 variables, respectively. 
# These values can be used in the template file.
@app.route('/')

def head():
    return render_template('index.html', number1=112500, number2=225200)

# We define a function for the second URL route ("/mult").
# The @app.route('/mult') decorator indicates that we are defining a function for the "/mult" URL route. 
# We define the "number" function, which will be executed when a request is made to this route. 
# The function uses the render_template function to return the "body.html" template file. 
# Additionally, we assign values 15 and 20 to the num1 and num2 variables, respectively. 
# We also define a variable named mult that contains the product of num1 and num2. 
# These values can be used in the template file.
@app.route('/mult')

def number():
    x=15
    y=20
    return render_template('body.html', num1=x, num2=y, mult=x*y)

# We run the application.
# The if __name__ == '__main__': statement checks if the Python file is being run directly. 
# If the file is being run directly, the app.run() function is called to start the application. 
# The port parameter specifies the port number on which the application will be accessible. 
# The debug=True parameter enables the debug mode, allowing for easier debugging and error tracking.
if __name__ == '__main__':
    app.run(port=3000, debug=True)

