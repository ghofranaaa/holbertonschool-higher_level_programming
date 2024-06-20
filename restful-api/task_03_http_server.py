#!/usr/bin/python3
"""
This module contain a class SimpleHTTPRequestHandler to set up a web server
"""

import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Simple HTTP request handler with GET endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests.

        Responds with a greeting message at the root endpoint.
        Serves JSON data at the /data endpoint.
        Provides an OK status at the /status endpoint.
        Returns a 404 Not Found for undefined endpoints without a message.
        """
        # Check the requested path and respond accordingly
        if self.path == "/":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")  # Response body
        elif self.path == "/data":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)  # HTTP status 404 Not Found
            self.send_header("Content-type", "text/plain")
            self.end_headers()

        # For undefined endpoints, send an empty response body
        if self.path not in ["/", "/data", "/status"]:
            self.wfile.write(b"")  # Empty response body for 404

        # Log the request
        print(f"{self.client_address[0]} - - [{self.log_date_time_string()}] \"{self.command} {self.path} {self.request_version}\" {self.send_response(200)} -")

def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Set up and start the HTTP server.

    param server_class: The HTTP server class to use.
    param handler_class: The request handler class to use.
    param port: The port number to bind the server to.
    """
    server_address = ("localhost", port)  # Server address tuple
    httpd = server_class(server_address, handler_class)  # Create server instance
    print(f"Starting httpd server on port {port}")  # Log the start of server
    httpd.serve_forever()  # Start the server
