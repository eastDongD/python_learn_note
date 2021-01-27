# Base64：用64个字符表示任意二进制数据（二进制数据文件如exe,jpg,pdf.....），让记事本打开后没有乱码
# 即将二进制数据转换为字符串（该字符串的字符类型共64种）
# 原理：原来3字节数据（3*8=24bit）视为4个字节的数据（4*6=24bit，每自己6bit） 2**6=64正好表示64个字符
# 如果要编码的二进制数据不是3的倍数，Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，
# 表示补了多少字节，解码的时候，会自动去掉。
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

#  encode以指定的格式编码字符串    decode以指定的格式解码字符串
import base64
base64.b64encode(b'binary\x00string') #b'YmluYXJ5AHN0cmluZw=='  让字符串用base64进行编码
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')#b'binary\x00string'    用base64对byte数据进行解码
# "url safe"的base64编码,去除标准base64编码中的+和/，改为-和_
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff') #b'abcd++//'
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')#b'abcd--__'
base64.urlsafe_b64decode('abcd--__')#b'i\xb7\x1d\xfb\xef\xff'
print(base64.urlsafe_b64encode(b'q\xa6\xdcu\xd6\xfe\xfb\xff')) #b'cabcddb--_8='  字符数量不够4的倍数时加=补足
print(base64.urlsafe_b64decode('cabcddb--__=')) #b'q\xa6\xdcu\xd6\xfe\xfb\xff'

# 由于=在URL，Cookie等地方可能有歧义，所以可以手动去掉Base64最后的=
# 去掉=后的解码思路：Base64编码的长度（字符数量）永远是4的倍数，不是4的倍数时，加=使其成为4的倍数


#由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
# 'abcd' -> 'YWJjZA=='
# 自动去掉=:
# 'abcd' -> 'YWJjZA'


