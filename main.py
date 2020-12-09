from flask import Flask
import feedparser

app = Flask(__name__)

RSS_FEED = {'zhihu':"https://www.zhihu.com/rss", "netease":"http://news.163.com/special/00011K6L/rss_newsattitude.xml"}

#将URL中部分标记为变量，作为关键字参数传递给函数
@app.route('/')
@app.route('/<publication>')
def get_news(publication='zhihu'): # 注意这里一定要有默认参数
	# 通过feedparser获取RSS消息
	feed = feedparser.parse(RSS_FEED[publication])
	first_content = feed['entries'][0]  
	
	# 返回模板字符串
	html_format = """
	<html> <body>
	<h1> Zhihu Headlines </h1>
        <b> {0} </b> <br/>
        <i> {1} </i> <br/>
        <p> {2} </p> <br/>
    	<body> </html>"""
	
	return html_format.format(first_content.get('title'),
				first_content.get('published'),
				first_content.get('summary'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
