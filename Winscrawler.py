import requests
from bs4 import BeautifulSoup


def get_html(url, headers, approches='get', attr=None):
    """
    返回response的对象
    attr指的是表单数据
    """
    if approches == 'get':
        response = requests.get(url, headers=headers, params=attr)
        return response
    elif approches == 'post':
        response = requests.post(url, data=attr, headers=headers)
        return response
    else:
        raise TypeError("只能使用post或者get方法！")


def get_html_text(url, headers, approches='get', attr=None):
    """
    以字符串形式返回页面源代码
    """
    if approches == 'get':
        response = requests.get(url, headers=headers, params=attr)
        return response.text
    elif approches == 'post':
        response = requests.post(url, data=attr, headers=headers)
        return response.text
    else:
        raise TypeError("只能使用post或者get方法！")


def re_craw(obj, text, namestr, lst=[]):
    """
    使用正则表达式爬取文本，返回的是一个包含文本的列表
    若原来就有列表，则添加新的元素
    obj指的是预先配置好的正则文本
    """
    # obj是已经配置好了的re对象
    result = obj.finditer(text)
    for each in result:
        lst.append(each.group(namestr))
        print(each.group(namestr), end='  ')
    return lst


def bs_craw(html_text, param, attr=None, return_type='obj', approach='1'):
    """
    使用BeautifulSoup进行爬取。其中param指的是形如div这种标签值，attr指的是html标签的属性，
    使用字典传入。return_type指的是返回类型，obj返回bs的对象，text返回html的文本，approach
    指的是使用的方法，0使用find方法，1使用find_all方法。
    """
    if return_type == 'obj':
        soup = BeautifulSoup(html_text, "html.parser")
        if approach == '0':
            return soup.find(param, attrs=attr)
        elif approach == '1':
            return soup.find_all(param, attrs=attr)
        else:
            raise TypeError("Approaches的值只能是0或1！")
    elif return_type == 'text':
        soup = BeautifulSoup(html_text, "html.parser")
        if approach == '0':
            return str(soup.find(param, attrs=attr))
        elif approach == '1':
            return str(soup.find_all(param, attrs=attr))
        else:
            raise TypeError("Approaches的值只能是0或1！")
