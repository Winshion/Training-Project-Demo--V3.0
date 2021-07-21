import tkinter as tk
from tkinter import ttk
import pandas as pd

import Data_analysis as da
from gui_classes import *

"""
本文件进行按钮的函数绑定
"""


def raise_error(text):
    error_window = tk.Tk()
    error_window.geometry('300x100+570+300')
    error_window.resizable(0, 0)
    error_window.title("错误提示")
    error_label = tk.Label(error_window, text=text,
                           font=("华文中宋", 15),
                           bg='#efefef', fg='red')
    error_label.pack(anchor="center")


# 1.城市匹配函数
def match_city(event, search_city_text, combo, lst_of_cities):
    if search_city_text in lst_of_cities:
        index = lst_of_cities.index(search_city_text)
        combo.current(index)
        combo.configure()
    else:
        raise_error("未找到该城市！")


# 2.更新数据库按钮
def update_database(event, canvas0, canvas1, canvas2, canvas3, job, city, root_path, total_page=5):
    #                                      画布                  职    城     路径       爬取页面数
    """
    该函数进行数据库的更新，更新之后将显示最新的词云图
    """
    canvas1.canvas.place_forget()
    canvas2.canvas.place_forget()
    canvas3.canvas.place_forget()
    canvas0.place()
    csv_path = root_path + job + '.csv'
    try:
        da.general_func(job, city, filename=job, num=total_page, path=root_path)
        cloud_path = root_path + job + '.jpg'
        canvas0.show_image(cloud_path)
    except ValueError:
        raise_error('搜索出错\n请仔细检查输入内容！')


# 3.词云图按键
def show_cloud_image(event, canvas0, canvas1, canvas2, canvas3, job, root_path):
    canvas1.canvas.place_forget()
    canvas2.canvas.place_forget()
    canvas3.canvas.place_forget()
    canvas0.place()
    csv_path = root_path + job + '.csv'
    try:
        cloud_path = root_path + job + '.jpg'
        canvas0.show_image(cloud_path)
    except FileNotFoundError:
        raise_error('数据库中无此职位\n请点击更新数据库')


# 4. 职位列表按键
def show_job_list(event, canvas0, canvas1, canvas2, canvas3, job, root_path):
    try:
        canvas1.canvas.place_forget()
        canvas2.canvas.place_forget()
        canvas3.canvas.place_forget()
        canvas0.place()  # 把需要展示的canvas放在首个位置
        csv_path = root_path + job + '.csv'
        csv = pd.read_csv(csv_path, encoding='gbk')
        columns = ("职位", "薪酬", "城市", "公司名称", "公司类型",
                   "公司规模（人）", "公司经营方向", "发布日期")
        # # 布置滚动条
        # vbar1 = ttk.Scrollbar(canvas0.canvas, orient="vertical")
        # vbar1.pack(fill='both', anchor='e')
        treeview = ttk.Treeview(canvas0.canvas, height=21, show='headings', columns=columns)
        # 展示表头
        treeview.column("职位", width=120, anchor="center")
        treeview.column("薪酬", width=70, anchor="center")
        treeview.column("城市", width=100, anchor="center")
        treeview.column("公司名称", width=180, anchor="center")
        treeview.column("公司类型", width=100, anchor="center")
        treeview.column("公司规模（人）", width=80, anchor="center")
        treeview.column("公司经营方向", width=100, anchor="center")
        treeview.column("发布日期", width=50, anchor="center")
        treeview.heading("职位", text="职位")
        treeview.heading("薪酬", text="薪酬")
        treeview.heading("城市", text="城市")
        treeview.heading("公司名称", text="公司名称")
        treeview.heading("公司类型", text="公司类型")
        treeview.heading("公司规模（人）", text="公司规模")
        treeview.heading("公司经营方向", text="公司经营方向")
        treeview.heading("发布日期", text="日期")
        treeview.place(x=50, y=20)
        # vbar1.config(command=treeview.yview)
        # 展示内容
        job_lst = csv['职位']
        salary_level = csv['薪酬']
        location = csv['城市']
        cmpn_name = csv["公司名称"]
        cmpn_type = csv["公司类型"]
        cmpn_scale = csv["公司规模（人）"]
        cmpn_ind = csv["公司经营方向"]
        date = csv['发布日期']
        for i in range(min(len(job_lst), len(salary_level), len(location),
                           len(cmpn_name), len(cmpn_type), len(cmpn_scale),
                           len(cmpn_ind), len(date))):  # 写入数据
            treeview.insert('', i, values=(job_lst[i], salary_level[i],
                                           location[i], cmpn_name[i],
                                           cmpn_type[i], cmpn_scale[i],
                                           cmpn_ind[i], date[i]))
        """
        现在仍然存在的问题：1.需要解决NaN的问题
                        2.滚动条的布置
                        3.没有实现城市的筛选功能
                        4.还需要分析文本，得到详细信息的链接，
                        并实现点击就能打开的效果
        """
    except FileNotFoundError:
        raise_error("数据库文件未找到\n请检查输入是否正确")


def salary_show(event, canvas0, canvas1, canvas2, canvas3, job, box_path):
    try:
        canvas1.canvas.place_forget()
        canvas2.canvas.place_forget()
        canvas3.canvas.place_forget()
        canvas0.place()  # 把需要展示的canvas放在首个位置
        cloud_path = box_path + job + 'slry.png'
        canvas0.show_image(cloud_path)
    except FileNotFoundError:
        raise_error('数据库中无此职位\n请点击更新数据库')


def box_intro(event):
    intro = tk.Toplevel()
    intro.geometry("900x600+100+100")
    intro.title("箱线图简介")
    canvas = wscanvas(intro, 547, 852, x=20, y=25)
    canvas.show_image("数据库/箱线图.jpg")
    canvas.place()
