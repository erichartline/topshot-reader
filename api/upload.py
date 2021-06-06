from http.server import BaseHTTPRequestHandler
import cgi
import csv

class handler(BaseHTTPRequestHandler):

def do_POST(self):
         # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')

        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                with open(field_item.filename) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    purchases = 0
                    sales = 0
                    for row in csv_reader:
                        if line_count == 0:
                            line_count += 1
                        else:
                            if row[0] == "NBA Top Shot purchase":
                                purchases += int(float(row[4]))
                            if row[0] == "NBA Top Shot sale":
                                sales += int(float(row[4]))
                            line_count += 1
                    self.wfile.write('\Processed %d lines.\n' % \
                        (line_count))
                    self.wfile.write('\Total purchases %d\n' % \
                        (purchases))
                    self.wfile.write('\Total sales %d\n' % \
                        (sales))
            else:
                # Regular form value
                self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return