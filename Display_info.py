import Data_analysis
import pandas as pd
import tkinter as tk
"""
本文件完成若干函数，即显示用户界面中的职位列表，
数据分析和行业分析的内容。
"""
root_path = "数据库/"


def display_each_grid(canvas, lst, x, i=0):
    """
    把一整列的数据显示在canvas上
    lst是传入的一整列
    即那一列全部数据，
    其中x是摆放的位置坐标
    i是起始的位置参数
    """
    y = 10
    ten_data = lst[i+1:i+11]
    for each in ten_data:
        lbl = tk.Label(canvas, text=each, font=("黑体", 12), bg='#ffffff')
        lbl.place(x=x, y=y)
        y += 15


def display_job_list(event, canvas, job, city='全国'):
    """
    canvas指代文件中的白色背景画布
    job是查询的职位
    city是查询的城市
    """
    # 注意！！！！最后要留一栏按钮给具体要求！
    try:
        title_lst = ['职位', '城市', '薪酬', '公司', '规模']
        file_path = root_path + job + '.csv'
        dataframe = pd.read_csv(file_path)
        index = 0
        count = 0
        for each in title_lst:
            lst = dataframe[each]
            display_each_grid(canvas, lst, x=index, i=count)
    except TypeError:
        error_window = tk.Tk()
        error_window.geometry('300x100+650+300')
        error_window.resizable(0, 0)
        error_label = tk.Label(error_window, text='请确保输入框中内容正确！',
                               font=("华文中宋", 15),
                               bg='#efefef', fg='red')
        error_label.place(x=35, y=0)

