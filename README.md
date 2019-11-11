# IP_tracker
只从一个IP地址出发，得到尽可能多的信息.
# 运行环境
linux ,python 2.7,mida	(Paul Murley. [n.d.]. MIDA: A Tool for Measuring the Web. https://mida.sprai.org/)

# 使用样例：
	python tracker.py example.com
	python tracker.py 123.123.123.123

# 程序功能：只从一个IP地址出发，得到尽可能多的信息

## 具体描述：动态跟踪一个域名或者IP的https解析过程，首先输出一个页面在加载的过程中请求了哪些外部IP,该域名或IP的HTTPS证书是什么，其HTTP指纹信息是什么，
# 输出
[+]resource	#该网页自动加载了来自哪个IP的图片，来自哪个IP的广告外链，等等外部object 
[IPlist.....]

[+]javascript	#该网页自动加载了哪个IP下存放的JS脚本 
[IPlist.....]

[+]certificate  #输出该IP或者该域名的证书信息 
[certificate info .....] 
 
 
[+]http request figerprinting#输出该IP或域名的HTTP 指纹信息（通过构建五个请求来形成指纹）  
HEAD / HEAD/1.1
[response......]  
DELETE / HTTP/1.1
[response......]  
 GET / HTTP/1.1
[response......]  
 GET / HTTP/3.0
[response......]  
 GET / JUNK/1.1
[response......]  
# 一些截图
 
