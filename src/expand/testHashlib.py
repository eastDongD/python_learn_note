# hashlib模块提供了常见的哈希算法（摘要算法）如MD5，SHA1等等
# 哈希算法：通过一个函数，把任意长度的数据转换为一个长度固定的数据串。目的是为了发现原始数据是否被人篡改过。
# 摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同
# 但是不同的数据可能通过摘要算法得到相同的摘要，但是非常非常困难。
# 应用：如存密码，在数据库存的密码为摘要，登录验证时，将用户输入密码转化为摘要，一致则登录成功
# 改进： 因为123456等常用密码很容易被提前计算出摘要和数据库的摘要进行比对，所以可以对所有密码加前后缀如123456->123456qqq
# 只要别人不知道你加的是qqq，即使被人知道数据库存的摘要，别人也不知道你的密码是什么
# 为防止多个摘要一样，可以把qqq变为用户的id，那么即使所以人密码都是111111，其摘要也不同
# 摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
# 但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。




# MD5算法： 生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest()) #d26a53750bc40b38b65a520292f69306
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 也可以直接调用
hashlib.md5('how to use md5 in python hashlib?'.encode('utf-8')).hexdigest() #d26a53750bc40b38b65a520292f69306


# SHA1算法：SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())





