# Python通过datetime模块处理时间问题
# datetime模块包括datetime,timedelta,timezone等类
# 如果通过import datetime导入模块，则访问datetime类需要datetime.datetime才能访问其所拥有的函数
# datetime是时间的一种存储方式（看起来更习惯），有时区的概念
# timestamp是计算机存储时间的方式，其值为某一时刻后的秒数。该时刻为1970年1月1日 00:00:00 UTC+00:00时区的时刻。故timestamp的值与时区无关
# 因此确定timestamp的值后即可转换为任何时区的时间
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

from datetime import datetime
now=datetime.now() # 返回当前日期和时间，其类型是datetime。被认为是本地时间。时区tzinfo=None
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime.  被认为是本地时间。时区tzinfo=None
dt.timestamp()   # 把一个datetime类型转换为timestamp.Python的timestamp是一个浮点数，整数位表示秒
                 # 因为此时dt没有时区，所以会将其按照你电脑的时间（本地时间）的时区来算
datetime.fromtimestamp(1429417200.0)         #   2015-04-19 12:20:00       timestamp转换为datetime
datetime.utcfromtimestamp(1429417200.0)      #   2015-04-19 04:20:00       timestamp转换为UTC标准时区的时间


# str与datetime的转换   
# 转换后的datetime是没有时区信息的
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S') # 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式                                                 
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))   #  Tue, Jan 26 14:36     
print(now.strftime('%Y-%m-%d %H:%M:%S')) #  2021-01-26 14:39:25
                  
            
# 时间的增减，如加10小时，或减3天。
# 需要导入timedelta这个类
from datetime import datetime, timedelta
now = datetime.now()
now + timedelta(hours=10)
now - timedelta(days=1)
now + timedelta(days=2, hours=12)


# datetime时区的转换
# 思路为获取带有时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 本地时间：即系统时间   北京时间：即UTC+8:00时区的时间  UTC时间：即UTC+0:00时区的时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None 。通过给tzinfo设置时区，进而改到其他时区
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
print(now)                 # 2021-01-26 14:56:29.854683
print(now.timestamp())     # 1611644274.66692
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)                  #2021-01-26 14:56:29.854683+08:00   加上了时区
print(dt.timestamp())      # 1611644274.66692  因为本地也是北京时间，所以timestamp按照本地时间转换的timestamp时间一样

# 先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间。（或者本地时间有时区的属性也可以）
# 不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如下面bj_dt到tokyo_dt的转换。
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) ## 拿到UTC时间，并强制设置时区为UTC+0:00
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) ## astimezone()将转换时区为北京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9))) # astimezone()将转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9))) # astimezone()将bj_dt转换时区为东京时间