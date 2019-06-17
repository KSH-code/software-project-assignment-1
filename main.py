from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape
import empty_room
import json
from authorizer import Authorizer

def application(environ, start_response):
  d = parse_qs(environ['QUERY_STRING'])
  api_type = escape(d.get('api_type', [''])[0])
  action_method = {
    'send_mail': send_mail,
    'authorize': authorize,
    'search': search
  }.get(api_type)

  status_code = '200 OK'
  response_body = None
  if action_method:
    try:
      response_body = action_method(d)
    except:
      status_code = '400 Bad Request'
  response_body = json.dumps(response_body or {'result': True})

  response_headers = [
    ('Content-Type', 'application/json'),
    ('Content-Length', str(len(response_body)))
  ]
  start_response(status_code, response_headers)
  return [bytes(response_body, 'utf-8')]

def send_mail(d):
  email = escape(d.get('email', [''])[0])
  Authorizer(email).send_mail()

def authorize(d):
  email = escape(d.get('email', [''])[0])
  code = escape(d.get('code', [''])[0])
  if not Authorizer(email).authorize(code):
    raise Exception()

def search(d):
  day = escape(d.get('d', [''])[0])
  start_time = escape(d.get('start_time', [''])[0])
  end_time = escape(d.get('end_time', [''])[0])
  empty_rooms = empty_room.search(day, start_time, end_time)
  return empty_rooms

httpd = make_server('', 8000, application)
httpd.serve_forever()
