# Networking

## To make an HTTP GET request and print the response:
```python
import requests

response = requests.get('http://www.example.com')

print(response.text)
```

## To make an HTTP POST request:
```python
import requests

data = {'key': 'value'}

response = requests.post('http://www.example.com', data=data)

print(response.text)
```

## To send a GET request to a URL and retrieve the JSON response:
```python
import requests

response = requests.get('http://www.example.com/api/endpoint')

json_response = response.json()

print(json_response)
```

## To create a simple HTTP server:
```python
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
```
