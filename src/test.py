import base64
def safe_base64_decode(s):
    s=s.decode("ascii")
    count=len(s)%4
    while(count>0):
        s=s+"="
        count-=1
    s=s.encode("ascii")
    return base64.urlsafe_b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')