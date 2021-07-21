import Winscrawler as wc
import Recrawler as rc
import Data_analysis as da
import Data_cleaning as dc
import tkinter as tk
from tkinter import ttk
from gui_classes import *  # 所有的窗口类
from gui_functions import *
import pandas as pd

with open("city_tuple.txt") as f:
    lst_of_cities = tuple(eval(f.read()))
    f.close()

Folder_path = "数据库/"

# 初始化窗口
window = tk.Tk()
window.geometry('950x670+250+75')
window.resizable(0, 0)
path = "Shenka.ico"
window.title("招聘网站数据分析")
window.iconbitmap(path)

# 置标题栏于上
mainlbl = wslabel(window, "招聘查询系统-Demo-V3.0", font=('华文中宋', 20), x=315, y=17)
mainlbl.place()

# 置四画布于心，色白如玉，平直四方。看似无异，实不同
# 其一用于展图片，而异者展表格
pic_canvas = wscanvas(window, height=490, width=900, x=23, y=120)
pic_canvas.place()
# 其二用于展示表格
table_canvas = wscanvas(window, height=490, width=900, x=23, y=120)
table_canvas.place()
# 其四用于展示前景
ana_canvas = wscanvas(window, height=490, width=900, x=23, y=120)
ana_canvas.place()
intro_btn = wsbutton(ana_canvas.canvas, "不会看箱线图？点我", font=("黑体", 10),
                     bg='#ffffff', height=1, width=18, x=730, y=18)
intro_btn.trigger(box_intro)
intro_btn.place()
# 其三用于展示信息
info_canvas = wscanvas(window, height=490, width=900, x=23, y=120)
info_canvas.place()

# 有三标签于顶，其位有异，故依次命，以示别。

# 其一：地名查询
search_city_lbl = wslabel(window, "查询城市", font=("黑体", 12), x=10, y=74)
search_city_lbl.place()

search_city_entry = wsentry(window, x=90, y=75)
search_city_entry.place()

search_city_btn = wsbutton(window, "查询", font=("黑体", 10), height=1, width=4, x=240, y=74)
search_city_btn.place()
search_city_btn.trigger(lambda event: match_city(event, search_city_entry.get_text(),
                                                 combo, lst_of_cities))

# 其二：地名复选
choose_city_lbl = wslabel(window, "选择城市", font=("黑体", 12), x=286, y=74)
choose_city_lbl.place()

combo = ttk.Combobox(window)
combo['values'] = lst_of_cities
combo.current(0)
combo.place(x=364, y=75)

# 其三：职位检索
choose_city_lbl = wslabel(window, "搜索职位", font=("黑体", 12), x=535, y=74)
choose_city_lbl.place()

search_job_entry = wsentry(window, x=615, y=75)
search_job_entry.place()

search_job_btn = wsbutton(window, "搜索", font=("黑体", 10), height=1, width=4, x=765, y=74)
search_job_btn.place()
search_job_btn.trigger(lambda event: show_cloud_image(event, pic_canvas, table_canvas,
                                                      info_canvas, ana_canvas,
                                                      search_job_entry.get_text(),
                                                      root_path=Folder_path))

# 其四：更新数据库键
update_dtbs = wsbutton(window, text='更新数据库', font=("华文中宋", 12),
                       bg='#33ddaa', width=8, height=1,
                       x=825, y=68)
update_dtbs.place()
update_dtbs.trigger(lambda event: update_database(event, pic_canvas, table_canvas,
                                                  info_canvas, ana_canvas,
                                                  job=search_job_entry.get_text(),
                                                  city=combo.get(),
                                                  root_path=Folder_path))

# 底部有四钮，分置功能各有异。
wordcloud_btn = wsbutton(window, text='词云图', font=("华文中宋", 14),
                         width=19, height=1, x=0, y=633)
wordcloud_btn.place()
wordcloud_btn.trigger(lambda event: show_cloud_image(event, pic_canvas, table_canvas,
                                                     info_canvas, ana_canvas,
                                                     search_job_entry.get_text(),
                                                     root_path=Folder_path))
# ------------------------------------------------------------------
table_btn = wsbutton(window, text='职位列表', font=("华文中宋", 14),
                     width=19, height=1, x=238, y=633)
table_btn.place()
table_btn.trigger(lambda event: show_job_list(event,
                                              table_canvas, pic_canvas,
                                              info_canvas, ana_canvas,
                                              search_job_entry.get_text(),
                                              root_path=Folder_path))
# ------------------------------------------------------------------
job_intro = wsbutton(window, text='这个按钮暂时还没用', font=("华文中宋", 14),
                     width=19, height=1, x=476, y=633)
job_intro.place()
# ------------------------------------------------------------------
job_analysis = wsbutton(window, text='热门城市薪资', font=("华文中宋", 14),
                        width=19, height=1, x=714, y=633)
job_analysis.trigger(lambda event: salary_show(event, ana_canvas,
                                               table_canvas, pic_canvas,
                                               info_canvas, search_job_entry.get_text(),
                                               box_path=Folder_path))
job_analysis.place()

window.mainloop()
