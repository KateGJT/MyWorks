
import pyecharts.options as opts
from pyecharts.charts import Liquid
a = 68
t = 100
chart = Liquid()
chart.add(series_name = '商品A', data = [a / t])
chart.set_global_opts(title_opts = opts.TitleOpts(title = '产品销售业绩达成率', pos_left = 'center'))
chart.render('水球图.html')

import pyecharts.options as opts
from pyecharts.charts import Liquid
a = 68
t = 100
chart = Liquid()
chart.add(series_name = '商品A', data = [a / t], shape = 'rect')
chart.set_global_opts(title_opts = opts.TitleOpts(title = '产品销售业绩达成率', pos_left = 'center'))
chart.render('水球图.html')

import pyecharts.options as opts
from pyecharts.charts import Liquid
a1 = 68
a2 = 120
a3 = 37
t = 100
chart = Liquid()
chart.set_global_opts(title_opts=opts.TitleOpts(title='产品销售业绩达成率', pos_left='center'))
chart.add(series_name='商品A', data=[a1 / t], center=['20%', '50%'])
chart.add(series_name='商品B', data=[a2 / t], center=['50%', '50%'])
chart.add(series_name='商品C', data=[a3 / t], center=['80%', '50%'])
chart.render('水球图.html')
