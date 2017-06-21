# 二D

University_inquiry
英文项目名称University_inquiry，中文名称就是就是大学查询，指的就是关於大学院校的基恩情况的说明。


# 简介 
选取大学院校，输入方面用户可用 ，方便挑选，输入出方面则是输出大学院校的毕业生数、招生数、在校学生数和校本部教职工人数4项数据，可查总院校为广州市80所本专科大学院校，数据来源为从广州市政府统一开放平台取得的csv档。



## 输入：
用户选取：通过下拉选单选取广东省广州市本专科大学名称，对应该所学校的四项基本信息。
## 输出：
用户得到输出结果为：所选取的大学院校的毕业生数、招生数、在校学生数和校本部教职工人数的基本信息。 

## 从输入到输出，本组作品使用了：
### 模块
csv
### 数据
* 数据来源从广州市政府统一开放平台取得的csv档[data/uni.csv](data/uni.csv)。本组并未使用API。

## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 后端服务器启动：执行 University_inquiry.py 启动後端伺服器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 后端服务器web 响应：[University_inquiry.py](University_inquiry.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)及一个含指标代码及名称的字典（见代码 the_list_items = meta['cname']）产出的产生《欢迎来到网上查中国国家数据分省数据指标说明！》的HTML页面

4. 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'user_zb'，使用了HTML5的datalist 定义在 list="zbs" 及 datalist标签，详见HTML模版[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取指标後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_zb'，以POST为方法，动作为/pick_a_zb的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/pick_a_zb', methods=['POST'])的函数 pick_a_zb() 

7. [pick_a_zb_meta.py](pick_a_zb_meta.py) 中 def pick_a_zb() 函数，把用户提交的数据，以flask 模块request.form['user_zb']	取到Web 请求中，HTML表单变数名称user_zb的值，存放在user_zb这Python变数下，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出），其中模版中the_zb的值，用user_zb这变数之值，其他4项值如此类推。

8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。

## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)
