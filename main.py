from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

RSS_FEED = {'zhihu':"https://www.zhihu.com/rss", "netease":"http://news.163.com/special/00011K6L/rss_newsattitude.xml"}

@app.route('/')
def get_news():

	# 使用request从form表单中获取用户提交的数据
	query = request.args.get("publication")
	if not query or query.lower() not in RSS_FEED:
		publication = 'zhihu'
	else:
		publication = query.lower()

	# 通过feedparser获取RSS消息
	feed = feedparser.parse(RSS_FEED[publication])
	first_content = feed['entries'] 

	
	# 将first_content已键值对形式传递给模板
	return render_template('home.html', articles=first_content)	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
