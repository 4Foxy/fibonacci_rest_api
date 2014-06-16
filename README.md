fibonacci_rest_api
==================

A REST API for generating fibonacci sequence


To install requirements
'pip install -r requirements.txt'

To run tests
'nosetests'

Run the application
'python resources.py'

In your browser
http://localhost:5000/fibonacci/10

Using curl command
'curl -i -X GET "http://localhost:5000/fibonacci/10"'

invalid path parameter - large number
'curl -i -X GET "http://localhost:5000/fibonacci/10000"'

invalid path parameter - negative number
'curl -i -X GET "http://localhost:5000/fibonacci/-10"'

invalid http method
'curl -i -X POST "http://localhost:5000/fibonacci/10000"'