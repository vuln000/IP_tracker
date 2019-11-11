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
 左边对一个botnet的C&C服务器进行测试,右边对百度的一个普通服务器测试  
 ## 看到一些有趣又明显的差别  
 首先是对外部数据的请求，C&C服务器一无所有，
 其次是证书，从issuer可以看到，显然C&C服务器的证书是伪造的（见过奥巴马签署的）
 最后看指纹信息，明显可以看到C&C服务器干净地不像一个提供内容服务的正常服务器。
![前半部分](https://github.com/sunxueliang96/IP_tracker/blob/master/screen%20shot/Screenshot%20from%202019-11-11%2012-33-40.png)
![后半部分](https://github.com/sunxueliang96/IP_tracker/blob/master/screen%20shot/Screenshot%20from%202019-11-11%2012-33-59.png)
