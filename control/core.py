import requests


def send_get_h(data):

	js = 0

	while js < 3 :
		try:
			response = requests.get(data, timeout=5)
			print("申请get方式发送完成！")
			js = 4
		except:
			js += 1
			print("传输超时！正在重连(%r/3)" %(str(js)))


def test():
#“update å years å year_name å describe å photo_path”
	api1 = "update"
	api2 = "year"
	api3 = "这是个名称"
	api4 = "这是个描述"
	api5 = "/static/img/det_min/a.jpg"
	data = "http://127.0.0.1:5000/api/?config="+api1+"å"+api2\
	+"å"+api3+"å"+api4+"å"+api5

	send_get_h(data)

def test2():
#“update å activity å activity_name å describe å photo_path å year_id”
	api1 = "update"
	api2 = "activity"
	api3 = "这是个名称2"
	api4 = "这是个描述2"
	api5 = "/static/img/det_min/c.jpg"
	api6 = "这是个名称"
	data = "http://127.0.0.1:5000/api/?config="+api1+"å"+api2\
	+"å"+api3+"å"+api4+"å"+api5+"å"+api6

	send_get_h(data)


def test3():
#““update å det å det_name å describe å photo_path å body å act_id”
	api1 = "update"
	api2 = "det"
	api3 = "这是个名称3"
	api4 = "这是个描述4"
	api5 = "/static/img/det_min/b.jpg"
	api6 = "h1ƒahhahahahah"
	api7 = "这是个名称2"
	data = "http://127.0.0.1:5000/api/?config="+api1+"å"+api2\
	+"å"+api3+"å"+api4+"å"+api5+"å"+api6+"å"+api7

	send_get_h(data)
test3()


