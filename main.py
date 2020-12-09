from flask import Flask
import feedparser

app = Flask(__name__)

RSS_FEED = {'zhihu':"https://www.zhihu.com/rss", "netease":"http://news.163.com/special/00011K6L/rss_newsattitude.xml"}

#将/zhihu url路由映射到zhihu()，然后调用get_news(args)
@app.route('/')
@app.route('/zhihu')
def zhihu():
	return get_news('zhihu')

@app.route('/netease')
def netease():
	return get_news('netease')
  

def get_news(publication):
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
