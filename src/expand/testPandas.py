# 与numpy配合完成机器学习

# 看的b站视频，地址是： https://www.bilibili.com/video/BV1UJ411A7Fs?p=1
# fork了他的笔记： https://github.com/eastDongD/ant-learn-pandas

# 注意要点：
# 对于DataFrame类型数据df, df[["a","b"]] 获取a，b两列组成的dataframe
#  df.loc[1] 获取索引为1的那一行，##########df.loc[1:3] 获取索引为1，2，3的3行#######
# python的与或用and or  此处条件查询时，多条件用 & |
# loc[ 条件,:]  满足条件后，显示该行所有列元素
# 添加为判断直接写，为函数，若是匿名函数，要传数据df，若是自己定义的函数，函数要穿数据df，但是传函数时不用写df
# 若函数有多个参数，可以写在apply等函数括号的后面，第一个参数为df，不用写
# assign不修改本身，而是返回新的dataframe
# head方法查看前几行，看是否操作成功
# value_counts() 对某列进行统计，看某个元素都有多少个
# std为标准差
# axis=0代表对行进行操作，axis=1代表对列进行操作
# loc[x,y]  x代表行，可以用:代表所有行， y代表列，可以用：代表所有列
# df["ymd"].str.startswith("2018-03") python3的方法，看是否以2018-03开头，返回的是true和false的series，故可用于筛选
#【重要知识】在选择数据时：元组(key1,key2)代表筛选多层索引，其中key1是索引第一级，key2是第二级，比如key1=JD, key2=2019-10-02       都满足
#                       列表[key1,key2]代表同一层的多个KEY，其中key1和key2是并列的同级索引，比如key1=JD, key2=BIDU               都显示

# 讲述内容：
# 02. Pandas读取数据 ： pandas如何读取 csv txt excel mysql数据
# 03. Pandas数据结构 ： Series DataFrame的创建及基础查询，以及Dataframe->Series->python基础数据结构的降维
# 04. Pandas查询数据 ： 将一列设置为索引，以及loc的各种查询（索引，多列，切片，条件，函数）
# 05. Pandas新增数据列 ：四种赋值方法 直接复制，apply，assign，条件选择赋值。
# 06. Pandas数据统计函数：包括 计数，平均，最大，最小，标准差，中位数，协方差，相关系数，去重，按值计数
# 07. Pandas缺失值处理 : 将常用的统计性表格改为每项都有内容的表格。isnull和notnull  dropna：丢弃、删除缺失值 fillna：填充空值
# 08. Pandas的SettingWithCopyWarning报警 ：pandas不允许先筛选子dataframe，再进行修改写入，要么使用.loc实现一个步骤直接修改源dataframe，要么先复制一个子dataframe再一个步骤执行修改
# 09. Pandas数据排序 ： sort_values的参数及说明
# 10. Pandas字符串处理 ： 先获取Series的str属性，然后在属性上调用函数。且直接支持正则表达式，可能是大部分函数第一个参数都可以写正则如replace
# 11. Pandas的axis参数怎么理解 ： 一维时，=0代表行，=1代表列  二维时，=0代表跨行（去掉行的维度），=1代表跨列。以及一个传入函数时apply的axis参数使用
# 12. Pandas的索引的用途 ：  更方便的数据查询；使用index可以获得性能提升；自动的数据对齐功能；更多更强大的数据结构支持；
# 13. Pandas怎样实现DataFrame的Merge ： 相当于数据库的操作，各种合并，1对多，内连接等等
# 14. Pandas实现数据的合并concat ： 相当于数据直接拼接，concat和append 以及高效的一行一行插入
# 15. Pandas批量拆分与合并Excel

# 后面不写了，看其列表就行





