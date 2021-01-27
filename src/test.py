import base64
print(base64.urlsafe_b64encode(b'q\xa6\xdcu\xd6\xfe\xfb\xff')) #b'cabcddb--_8='
print(base64.urlsafe_b64decode('cabcddb--__=')) #b'q\xa6\xdcu\xd6\xfe\xfb\xff'