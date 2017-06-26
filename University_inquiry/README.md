# University_inquiry


英文项目名称University_inquiry，中文名称就是就是大学查询，指的就是查询关於大学院校的基本情况。


# 简介 
用户选取大学院校，通过选取下拉选单的方式，得到院校的基本信息。输出方面则是输出大学院校的毕业生数、招生数、在校学生数和校本部教职工人数4项数据，可查广东省广州市80所本专科大学院校的信息，数据来源为从广州市政府统一开放平台取得的csv档。



## 输入：
用户选取：通过下拉选单选取广东省广州市本专科80所大学院校名称，对应该所学校的四项基本信息。
## 输出：
用户得到输出结果为：所选取的大学院校的毕业生数、招生数、在校学生数和校本部教职工人数的基本信息。 

## 从输入到输出，本组作品使用了：
### 模块
csv
### 数据
* 数据来源为从广州市政府统一开放平台取得的csv档[data/uni.csv](data/uni.csv)。本组并未使用API。

## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 后端服务器启动：执行 University_inquiry.py 启动后端服务器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 后端服务器web 响应：[University_inquiry.py](University_inquiry.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)产生的《欢迎来到网上查找广东本专科大学院校资料！！》的HTML页面

4. 前端浏览器收到web 响应：出现HTML页面有HTML下拉的大学院校名称的选单，详见HTML模版[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取院校名称后点击提交按钮「查询」 请求，按照form元素中定义的method='POST' action='/University_inquiry'，以POST为方法，动作为/University_inquiry的web 请求

6. 后端服务器收到用户web 请求，匹配到@app.route('/University_inquiry', methods=['POST'])的函数 pick_a_color() 

7. [University_inquiry.py](University_inquiry.py) 中 def pick_a_color() 函数，把用户提交的数据，以flask 模块request.form['user_school']	取到Web 请求中，HTML表单变数名称的值user_school_name，存放在user_school这Python变数下，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出），其中模版中the_school_name的值，用user_school_name变数值，其他4项值以此类推。
8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，看到大学院校的相关数据。

## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)
