import pandas as pd
import Data_analysis as da
import wordcloud
import jieba
import time
import matplotlib.pyplot as plt
import matplotlib


def format_word_cloud(job, text, path, encoding='utf-8'):
    """
    该函数进行云图的生成。传入文本，系统将自动生成云图对象。
    使用结巴分词库先分词，后存入文本
    """
    proc = jieba.cut(text)  # proc是处理后的文本迭代对象
    cloud_txt = ''
    for each in proc:
        cloud_txt += (' ' + each)
    wc = wordcloud.WordCloud(width=800, height=450, max_words=366,
                             background_color='white', font_path='C://Windows/Fonts/STZHONGS.TTF')
    wc.generate(cloud_txt)
    path = path + job + '.jpg'
    picture = wc.to_image()
    wc.to_file(path)


def salary_lst_filter(job_csv):
    """
    筛选数据，要么是千/月，要么是万/月
    然后再进行数据的处理
    画出城市的箱线图
    """
    min_lst = []
    max_lst = []
    new_city_lst = []
    city_lst = job_csv['城市']
    lst = [str(each) for each in job_csv['薪酬']]
    for salary in range(len(lst)):
        if lst[salary] == 'nan':
            continue
        elif ("千/月" not in lst[salary]) and ('万/月' not in lst[salary]):
            continue
        else:
            lst[salary] = lst[salary].split("-")
            min_lst.append(lst[salary][0])
            max_lst.append(lst[salary][1])
            new_city_lst.append(city_lst[salary])
    return min_lst, max_lst, new_city_lst


def process_salary_lst(job_csv):
    min_slr, max_slr, city_lst = salary_lst_filter(job_csv)
    final_min = [float(each) for each in min_slr]
    # 接下来处理max_list的内容
    final_max = [float(each[:-3]) for each in max_slr]
    for value in range(len(final_max)):
        if max_slr[value][-3] == '万':
            final_min[value] *= 10
            final_max[value] *= 10
    return final_min, final_max, city_lst


def give_complete_data(job_csv):
    mil, mal, cty = process_salary_lst(job_csv)
    avrgl = []  # 平均薪资列表
    for each in range(len(mil)):
        avrgl.append(0.5 * (mil[each] + mal[each]))
        cty[each] = cty[each][:2]
    return avrgl, cty


def get_city_lst(job_csv):
    """
    按照城市分配数据
    """
    avrg, cty = give_complete_data(job_csv)
    #   北京 上海  广州  深圳  杭州 南京  武汉  长沙  重庆 成都  厦门
    BJ = []
    SH = []
    GZ = []
    SZ = []
    HZ = []
    NJ = []
    WH = []
    CS = []
    CQ = []
    CD = []
    XM = []
    for value in range(len(avrg)):
        if cty[value] == '北京':
            BJ.append(avrg[value])
        elif cty[value] == '上海':
            SH.append(avrg[value])
        elif cty[value] == '广州':
            GZ.append(avrg[value])
        elif cty[value] == '深圳':
            SZ.append(avrg[value])
        elif cty[value] == '杭州':
            HZ.append(avrg[value])
        elif cty[value] == '南京':
            NJ.append(avrg[value])
        elif cty[value] == '武汉':
            WH.append(avrg[value])
        elif cty[value] == '长沙':
            CS.append(avrg[value])
        elif cty[value] == '重庆':
            CQ.append(avrg[value])
        elif cty[value] == '成都':
            CD.append(avrg[value])
        elif cty[value] == '厦门':
            XM.append(avrg[value])
    return BJ, SH, GZ, SZ, HZ, NJ, WH, CS, CQ, CD, XM


def store_plot(job_csv, job):
    BJ, SH, GZ, SZ, HZ, NJ, WH, CS, CQ, CD, XM = \
        get_city_lst(job_csv)
    fonts = matplotlib.font_manager.FontProperties(fname='C://Windows/Fonts/STZHONGS.TTF', size=12)
    plt.figure(figsize=(8, 4))
    plt.boxplot([BJ, SH, GZ, SZ, HZ, NJ, WH, CS, CQ, CD, XM],
                labels=['北京', '上海', '广州', '深圳', '杭州',
                        '南京', '武汉', '长沙', '重庆', '成都',
                        '厦门'])
    plt.xticks(fontproperties=fonts, fontsize=8)
    plt.ylabel(job + "全国平均薪资水平：千元/月", fontproperties=fonts)
    plt.savefig("数据库/" + job + 'slry' + '.png', dpi=125)


