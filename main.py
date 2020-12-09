from flask import Flask
import feedparser

app = Flask(__name__)

ZHIHU_FEED = "https://www.zhihu.com/rss"

#将默认/页面路由映射到get_news函数
@app.route('/')  
def get_news():
	# 通过feedparser获取RSS消息
	feed = feedparser.parse(ZHIHU_FEED)
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
