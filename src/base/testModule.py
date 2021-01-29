#一个.py文件就称之为一个模块（Module）
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
#引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany
#一个包也可以看为一个大的模块

import re as r  #即可以用r访问re模块的函数
#r.match("","")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '   #是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Michael Liao' #使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import sys#导入该sys模块，导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能

def test():
    args = sys.argv #sys模块有一个argv变量，用list存储了命令行的所有参数
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':   #当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
    test()              #此时可以通过python3 hello.py执行该文件， hello.py是该文件名字


#正常变量和函数是公开的 如 test  PI
#特殊变量也可以直接引用 如 __author__  __name__  __doc__模块注释
#非公开变量不应该被直接引用，但是可以引用 如  __private  _private


#按照第三方模块
#使用pip进行完成，如果是Windows确保安装python时勾选pip和Add python.exe to Path
#win+R  cmd  后如果输入pip有反应则pip已经安装
#linux可能用pip3安装
#安装命令  pip install Pillow  安装Pillow
#推荐直接按照Anaconda，里面直接内置装好了各种python库
#输入python会看到Anaconda是否安装成功，其会将pyth路径指向anaconda的安装路径
#import numpy 导入已安装的模块，其会搜索当前路径，及内置模块和第三方模块
#搜索路径在 import sys   的   sys.path 中  sys.path是一个list，通过sys.path.append("你的路径")添加搜索目录 但运行结束即失效
#设置环境变量PYTHONPATH可使修改的搜索路径永久生效

