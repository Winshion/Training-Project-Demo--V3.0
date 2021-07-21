import Recrawler as rc
import Data_cleaning as dc
import pandas as pd
import time
import tkinter as tk

"""
本库旨在将爬取的数据进行整合，存储至pandas的一个DataFrame里面，
然后进行数据可视化。
"""


def form_frame(return_list):
    """
    将Recrawler中的list_fulfilling函数返回的信息列表
    进行处理，返回一个pandas的DataFrame的对象
    """
    frame = pd.DataFrame(
        {
            "职位": return_list[0],
            "薪酬": return_list[1],
            "城市": return_list[2],
            "公司名称": return_list[3],
            "公司类型": return_list[4],
            "公司规模（人）": return_list[5],
            "公司经营方向": return_list[6],
            "发布日期": return_list[7],
            "详细介绍": return_list[8]
        }
    )
    return frame


def store_to_local(content, filename, path, filetype='csv', encoding=None):
    """
    该函数提供一种方便的文件存储方式，filename是不带后缀的文件名，path是存储路径（以'/'结尾），
    filetype是存储的文件类型，默认为csv,还可以选择txt
    """
    if filetype == 'txt':
        location = path + filename + '.' + 'txt'
        with open(location, mode='a+', encoding=encoding) as f:
            print("正在存储文件中...")
            f.write(content)
        f.close()
        print("文件写入完毕，请到路径" + location + "中查看！")
    elif filetype == 'csv':
        location = path + filename + '.' + 'csv'
        print("正在存储文件中...")
        content.to_csv(location, index=False, encoding=encoding)
        print("文件写入完毕，请到路径" + location + "中查看！")
    else:
        raise TypeError("filetype只能是txt或csv！")


def form_wordcloud_text(job, data_list, path, encoding='utf-8'):
    text = ''
    for each in data_list:
        text = text + each + ' '
    dc.format_word_cloud(job, text, path, encoding=encoding)


def general_func(job, city, filename, num, path='数据库/'):
    job_name = []
    company_name = []
    work_city = []
    company_type = []
    date = []
    company_ind = []
    company_size = []
    concrete_data = []
    salary_level = []
    for i in range(1, (int(num) + 1)):
        t1 = time.time()
        print("开始爬取第" + str(i) + "页！", end=' ')
        html_text = rc.search_for_job(job, i, city)
        job_info_list = rc.get_needed_data(html_text)
        job_name, work_city, company_name, company_type, company_size, company_ind, date, concrete_data = rc.list_fulfilling(
            job_info_list, job_name, company_name, company_type,
            date, company_ind, company_size, concrete_data,
            salary_level, work_city)
        t2 = time.time()
        if (t2 - t1) < 3:
            print("第" + str(i) + "页为空！")
        else:
            print("第" + str(i) + "页爬取完毕，用时" + "%.2f" % (t2 - t1) + "秒！")
    final_list = [job_name, salary_level,
                  work_city, company_name, company_type, company_size,
                  company_ind, date, concrete_data]
    form_wordcloud_text(job, final_list[0], path)
    frame = form_frame(final_list)
    store_to_local(frame, filename, path, encoding='gbk')
    csv = pd.read_csv(path + job + '.csv', encoding='gbk')
    dc.store_plot(csv, job)
    return final_list
