from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', ['0'])[0]
  	b = d.get('b', ['0'])[0]
	try:
		if a.isdigit() and b.isdigit():
			a, b = int(a), int(b)
		else: a, b = float(a),float(b)
		sum, mul = a+b, a*b
	except ValueError:
		sum, mul = "Error", "Error"
	response_body = html % {
		'sum': sum,
		'mul': mul,
	}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]
