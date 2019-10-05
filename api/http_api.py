from urllib.parse import quote
import requests


class Http_operation:
	'''
	这是一个用于简单操作http api的类
	具有post发送信息的函数和post发送文件的函数
	具有的参数有：
	url 提交的url链接 包含域名以及api等路由
	data 用于提交的字符串
	file_path 被上传文件的路径(目前只支持图片)

	'''

	def __init__(self,url="",data="",file_path=""):
		self.url = url
		self.data = data
		self.file_path = file_path



	def post_text(self):

		url = self.url

		#重点重点 ！！！中文post提交方法
		textmod = quote(self.data, 'utf-8')
		#重点重点 ！！！中文post提交方法

		js = 0
		headers = {'application':'json'}
		while js < 3 :
			try:
				response = requests.post(url, headers=headers, data=textmod)
				print("http post 方式发送完成！")
				js = 4
			except:
				js += 1
				print("传输超时！正在重连(%r/3)" %(str(js)))


	def post_file(self):

		url = self.url

		name_list = self.file_path.split('/')
		name = name_list[len(name_list)-1]

		files = {'file':(name,open(self.file_path,'rb'),'image/jpg')}
		
		js = 0

		while js < 3:
			try:
				#r = requests.post(url,files = files, verify=False, timeout=5)
				r = requests.post(url,files = files, timeout=5)
				result = r.text
				print("照片%r传输完成！" %(name))
				js = 4
			except:
				js += 1
				print("照片传输超时！正在重连(%r/3)" %(str(js)))



