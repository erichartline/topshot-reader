from http.server import BaseHTTPRequestHandler
import logging

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    logging.debug("got request")
    logging.debug(self)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    return