#!/usr/bin/python3

import http.client

port = 8001
conn = http.client.HTTPConnection(f"localhost:{port}")
conn.request("QUIT", "/")
print(conn.getresponse())
