import requests
"""
定义一个网络请求的类


"""
class ConfigHttp:
    def __init__(self,kwargs):
        self.kwargs = kwargs

    def confighttp(self):
        if self.kwargs['method'].lower() == 'get':
            return self.__get()
        elif self.kwargs['method'].lower() == 'post':
            return self.__post()

    def __get(self):
        res = requests.get(url=self.kwargs["interfaceUrl"], params=eval(self.kwargs['value']))
        return res
    def __post(self):
        res = requests.post(url=self.kwargs["interfaceUrl"], data=eval(self.kwargs['value']))
        return res

