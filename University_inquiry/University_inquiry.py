# -*- coding: utf-8 -*- 
# 使用模块moduld school

import school
gd_s = school.gd_school()
s_names = gd_s.list_names
s_data = gd_s.data


from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_list_items = s_names,
                           the_title='欢迎来到网上查找广东本专科大学院校资料！！')

@app.route('/University_inquiry', methods=['POST'])
def pick_a_color() -> 'html':
	user_school_name= request.form['user_school']
	user_school_info=[]
	for i in range(len(s_data)):
		gg=gd_s.data[i]
		if user_school_name in s_data[i]['院校名称']:
			user_school_info.append(gg)
	return render_template('results.html',
							the_title = '以下是您选取的院校信息：',
							the_school_info = user_school_info,
							the_school_name = user_school_name,
							)

if __name__ == '__main__':
    app.run(debug=True)
