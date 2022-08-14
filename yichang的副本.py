# try:
#     open('test.txt','r',encoding='utf-8')
#     print('try')
# except:
#     open('test1.txt','w',encoding='utf-8')
#     print('except')

# open('test.txt','r',encoding='utf-8')
# print('try')
# try:
#     open('test.txt','r',encoding='utf-8')
#     print('try')
# except (NameError,FileNotFoundError):
#     open('test1.txt','w',encoding='utf-8')
#     print('except')
# try:
#     open('test1.txt','r',encoding='utf-8')
#     print('try')
# except Exception as m:
#     open('test1.txt','w',encoding='utf-8')
#     print(f'报错{m}')
# def func1():
#     try:
#         print('n')
#         return
#     except Exception as msg:
#         print("报错信息",msg)
#     else:
#         print('没有报错执行的代码')
#     finally:
#         print('有没有报错都会执行的代码')
#
#     print('有没有报错都会执行的代码')
# func1()

# try:
#     print('执行一段代码----')
#     try:
#         # 1/0
#         print(n)
#     except ZeroDivisionError as msg:
#         print(msg)
#
# except Exception as msg:
#     print("报错信息", msg)

try:
    print('执行一段代码----')
    try:
        1/0
        # print(n)
    except ZeroDivisionError as msg:
        print(msg)
        raise msg

except Exception as msg:
    print("报错信息", msg)
