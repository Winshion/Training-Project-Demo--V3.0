import Winscrawler as wc
import re

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 '
        'Safari/537.36 Edg/91.0.864.64 ',
    'Referer':
        'https://www.51job.com/',  # 使用防盗链进行反反爬
    'Host': 'jobs.51job.com'
}


def search_for_job(job, num, city='全国'):
    """
    该函数进行网页源代码的爬取，获取到网页的文本信息。
    其中num变量代表第num页的内容
    """
    f = open("D://学习/大一下/暑期实训/招聘网站项目/city_code.txt")
    dic = eval(f.read())
    dic = dict(dic)
    city_value = str(dic[city])
    url = 'https://search.51job.com/list/' + city_value + ',000000,0000,00,9,99,' + job + ',2,' + str(num) + '.html'
    text = wc.get_html_text(url, headers=headers)
    text.replace("\xa0", "")
    return text


def get_needed_data(txt):
    """
    该函数进行bs和re模块的综合使用，返回一个由字典组成的列表，包含需要的数据
    """
    lst = []
    long_dic = wc.bs_craw(txt, "script", {"type": "text/javascript"}, return_type="text")
    obj0 = re.compile('{"type":"engine.*?"is_sp.*?",(?P<info>.*?),"adid":""}', re.S)
    ingredient = obj0.findall(long_dic)
    for each_items in ingredient:
        new_temp = ('{' + each_items + '}')
        lst.append(eval(new_temp))
    return lst


def craw_concrete_demand(url):
    """
    该函数进行进一步爬取细致的招聘信息，具体到每一个职位的内容
    """
    url = url.replace('\\', '')  # 去掉Python自带的加反斜杠机制
    resp = wc.get_html(url, headers=headers)
    resp.encoding = 'gbk'
    text = resp.text
    target_demand = wc.bs_craw(text, "div", attr={"class": "bmsg job_msg inbox"}, return_type='text')
    obj_demand = re.compile("<p>(?P<para>.*?)</p>", re.S)
    iterator_demand = obj_demand.finditer(target_demand)
    demand = ''
    for each in iterator_demand:
        demand += each.group('para')
    strings_demand = string_processing(demand)
    return strings_demand


def list_fulfilling(job_info_list, job_name=[], company_name=[], company_type=[],
                    date=[], company_ind=[], company_size=[], concrete_data=[],
                    salary_level=[], work_city=[]):
    """
    添加元素，不删除原表单数据。
    """
    for each in job_info_list:
        job_name.append(each['job_name'].replace("\\", ""))
        company_name.append(each['company_name'])
        salary_level.append(each['providesalary_text'].replace("\\", ""))
        company_type.append(each['companytype_text'])
        date.append(each['updatedate'])
        company_ind.append(each['companyind_text'].replace("\\", ""))
        company_size.append(each['companysize_text'])
        concrete_data.append(craw_concrete_demand(each['job_href']))
        work_city.append(each["workarea_text"])
    return job_name, work_city, company_name, company_type, company_size, company_ind, date, concrete_data


def string_processing(strings):
    """
    处理异常字符串，使得可以较好地适配目前的解码方案；
    使用数据分析中常用的drop方法，即把无法解析的数据去除。
    """
    strings = strings.replace('<br>', '\n')
    strings = strings.replace('<br/>', '\n')
    strings = strings.replace('<span>', '')
    strings = strings.replace('</span>', '')
    strings = strings.replace('<b>', '')
    strings = strings.replace('</b>', '')
    strings = strings.replace('<i>', '')
    strings = strings.replace('</i>', '')
    strings = strings.replace('<u>', '')
    strings = strings.replace('</u>', '')
    strings = strings.replace('<strong>', '')
    strings = strings.replace('</strong>', '')
    strings = strings.replace('<p>', '')
    strings = strings.replace('</p>', '')
    strings = strings.replace('&amp', '')
    strings = strings.replace('\xa0', '')
    strings = strings.replace('\ufffd', '')
    strings = strings.replace('\xae', '')
    return strings
