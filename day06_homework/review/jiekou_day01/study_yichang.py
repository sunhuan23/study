"""
异常：
    try：
        可能出现异常的代码
    except：
        出现异常执行的代码
"""
try:
    open('test.txt','r',encoding='utf-8')
except:
    open('test.txt', 'w', encoding='utf-8')

"""
捕获指定异常：
    try：
        可能出现异常的代码
    except 异常类型：
        捕获到指定异常执行的代码
"""
try:
    print(n)
except NameError:
    n = 10
    print(n)

"""
捕获多个指定异常：
    try：
        可能出现异常的代码
    except （异常类型，异常类型,...）：
        捕获到指定异常执行的代码
"""
try:
    print(eval(10))
except (TypeError,NameError):
    print('eval（只能使用字符串）')

"""
捕获异常描述信息
    try：
        可能出现异常的代码
    except （异常类型，异常类型,...）as 变量名：
        捕获到指定异常执行的代码
"""
try:
    print(eval(10))
except (TypeError,NameError) as result:
    print(f'异常描述信息：{result}')

"""
捕获所有异常
    try:
        可能出现异常的代码
    except Exception：
        捕获到所有异常执行的代码
"""
try:
    # print(eval(10))
    print(x)
except Exception:
    print('发生异常')

"""
异常的else
    try:
        可能出现异常的代码
    except：
        捕获到指定异常执行的代码
    else:
        没有发生异常执行的代码
"""
try:
    print('11')
except:
    print('发生异常执行的代码')
else:
    print('没有发生异常执行的代码')

"""
异常的finally：
    try:
        可能出现异常的代码
    except：
        捕获到指定异常执行的代码
    else:
        没有发生异常执行的代码
    finally：
        有没有发生异常都会执行的代码，一般用在函数内部使用
"""
def func():
    try:
        n =10
        return n

    except:
        print('发生异常执行的代码')
    else:
        print('没有发生异常执行的代码1')
    finally:
        print(f"有没有异常都会执行的代码{n}")
func()
"""
需求：
1. 尝试只读⽅式打开test.txt⽂件，如果⽂件存在则读取⽂件内容，⽂件不存在则提示⽤户即可。
2. 读取内容要求：尝试循环读取内容，读取过程中如果检测到⽤户意外终⽌程序，则 except 捕获异常
并提示⽤户
"""
import time
try:
    f = open('test.txt','r',encoding="utf-8")
    try:

        while True:
            content = f.readlines()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        print('程序意外终止')
    finally:
        f.close()
except:
    print('文件不存在')

"""
⾃定义异常
    raise 异常类名（）
"""
try:
    try:
        print(x)
    except NameError as msg:
        raise msg
except NameError:
    print('外层异常')

