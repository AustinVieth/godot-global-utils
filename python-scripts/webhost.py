#!/usr/bin/env python

# This is for running a local server to test godot 4 games that are built for the web!

try:
# Python 3
  from http.server import HTTPServer, SimpleHTTPRequestHandler, test as test_orig 
  import sys

  def test (*args):
    test_orig(*args, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)

except ImportError: # Python 2
  from BaseHTTPServer import HTTPServer, test
  from SimpleHTTPServer import SimpleHTTPRequestHandler

class CORSRequestHandler (SimpleHTTPRequestHandler):
  def end_headers (self):
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
    self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
    SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
  test(CORSRequestHandler, HTTPServer)