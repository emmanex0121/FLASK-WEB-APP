#!/usr/bin/env python3
from website import create_app

app = create_app() # creates the flask app

if __name__ == '__main__':
    app.run(port='5003',debug=True) # debug-True automatically reruns the web server anytime we make changes to the python code
