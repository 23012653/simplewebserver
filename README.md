# EX01 Developing a Simple Webserver

## Date:16.02.2024

## AIM:

To develop a simple webserver to serve html pages.

## DESIGN STEPS:

### Step 1:

HTML content creation.

### Step 2:

Design of webserver workflow.

### Step 3:

Implementation using Python code.

### Step 4:

Serving the HTML pages.

### Step 5:

Testing the webserver.

## PROGRAM:

```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
<title>Top Software Companies</title>
</head>
<body>
<table border=2>
<tr>
<th>Company</th> <th>Sales</th> <th>Nationality</th>
</tr>
<tr>
<td>Micro Soft</td> <th>57.9</td> <td>USA</td>
</tr>
<tr>
<td>oracle</td> <td>21.0</td> <td>USA</td>
</tr>
<tr>
<td>SAP</td> <td>16.1</td> <td>Germany</th>
</tr>
<tr>
<td>Adobe</td> <td>3.4</th> <td>USA</td>
</tr>
<tr>
<td>Activision</td> <td>2.6</th> <td>USA</td>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:

![alt text](<WEBSERVER EX-01.png>)
![alt text](<EX 03 web terminal.png>)

## RESULT:

The program for implementing simple webserver is executed successfully.
