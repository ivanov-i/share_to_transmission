import requests
import json


class Transmission:

  session_id_header_name = 'X-Transmission-Session-Id'

  def __init__(self, host='diskstation.local', port = 9091, auth = ('admin', 'admin')):
    self.url = 'http://{host}:{port}/transmission/rpc'.format(host = host, port = port)
    self.auth = auth
    self.session_id = None

  def get_custom_headers(self):
    return {} if self.session_id is None else {self.session_id_header_name: self.session_id}

  def request(self, method, data):
    custom_headers = self.get_custom_headers()
    response = method(self.url, auth = self.auth, headers = custom_headers, data=data)
    if response.status_code == 409 and self.session_id is None:
      self.session_id = response.headers[self.session_id_header_name]
      return self.request(method, data)
    elif response.status_code != 200:
    	raise RuntimeError(response.status_code)
    return response

  def Add(self, magnet):
    r ={"method": "torrent-add", "arguments": {"filename": magnet}}
    return self.request(requests.post, json.dumps(r))

if __name__ == '__main__':
  r = '''{
          "arguments": {
            "fields": [ "id", "name", "totalSize" ],
            "ids": [ 7, 10 ]
          },
          "method": "torrent-get",
          "tag": 39693
        }
	'''
  t = Transmission()
  print(t.request(requests.post, r).content)

