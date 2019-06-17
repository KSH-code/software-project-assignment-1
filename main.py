from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape
import json
from authorizer import Authorizer

def application(environ, start_response):
  d = parse_qs(environ['QUERY_STRING'])
  api_type = escape(d.get('api_type', [''])[0])

  action_method = {
    'send_mail': send_mail,
    'authorize': authorize
  }.get(api_type)

  if action_method:
    response_body = action_method(d)
  response_body = json.dumps(response_body or {'result': True})

  response_headers = [
    ('Content-Type', 'application/json'),
    ('Content-Length', str(len(response_body)))
  ]
  start_response('200 OK', response_headers)
  return [bytes(response_body, 'utf-8')]

def send_mail(d):
  email = escape(d.get('email', [''])[0])
  Authorizer(email).send_mail()

def authorize(d):
  email = escape(d.get('email', [''])[0])
  code = escape(d.get('code', [''])[0])
  return {'result': Authorizer(email).authorize(code)}

httpd = make_server('', 8000, application)
httpd.serve_forever()