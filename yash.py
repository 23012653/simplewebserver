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