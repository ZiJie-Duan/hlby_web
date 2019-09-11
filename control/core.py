import requests
import xlrd
import os
import piexif
from PIL import Image
import requests
import uuid


def help():
	print("help ------------------- 帮助选项(查看文档详细信息)")
	print("sc [cho] --------------- 搜索数据库信息")
	print("de [cho] [name] -------- 删除数据库信息")
	print("img [path][name][sys] -- 上传图像文件")
	print("rd [file_name] --------- 读取excil上传格式")


def main():
	print("黑利博瑞_Web_API_控制程序")
	print("输入“help” 查看帮助")
	while True:
		cmd = input(">>")
		if len(cmd)==0: continue  # 如果传入空字符会阻塞
		cmd = cmd.split(" ")
		core_cmd(cmd)



def core_cmd(cmd):

	if cmd[0] == "help":
		help()
	if cmd[0] == "de":
		help()
	if cmd[0] == "sc":
		help()
	if cmd[0] == "img":
		update_img(cmd)
		
	if cmd[0] == "rd":
		core_update(cmd)
		

def update_img(cmd):
	path,name = change_img_name(cmd[1],cmd[2])

	for x in path:
		url = "http://127.0.0.1:5000/api/upload/"
		newname = x.split('/')
		s = newname[len(newname)-1]

		files = {'file':(s,open(x,'rb'),'image/jpg')}
		
		print("照片%r信息处理完成！" %(x))
		js = 0

		while js < 3:
			try:
				#r = requests.post(url,files = files, verify=False, timeout=5)
				r = requests.post(url,files = files, timeout=5)
				result = r.text
				print("照片%r传输完成！" %(x))
				js = 4
			except:
				js += 1
				print("照片传输超时！正在重连(%r/3)" %(str(js)))



def read_excil(path):
	#用于读取exicil的函数
	#返回一个二维数组
	word = []
	#打开xlsx
	workbook = xlrd.open_workbook(path)
	#导出一个表
	sheet = workbook.sheet_by_index(0)#使用索引导出

	#将表中的值按列导出
	en2 = sheet.col_values(1)

	ch = []

	#全部转为str以防出现错误
	for x in en2:
		y = str(x)
		ch.append(y)

	return ch


def read_word_for_det_body(path):
	#用于读取excil的函数
	#返回一个二维数组
	word = []
	#打开xlsx
	workbook = xlrd.open_workbook(path)
	#导出一个表
	sheet = workbook.sheet_by_index(0)#使用索引导出

	#将表中的值按列导出
	ch2 = sheet.col_values(2)

	en2 = sheet.col_values(3)
	ch = []
	en = []
	#全部转为str以防出现错误
	for x in ch2:
		y = str(x)
		ch.append(y)

	for x in en2:
		y = str(x)
		en.append(y)


	#求出列表含有多少个单词
	number_word = len(en)
	for x in range(number_word):

		#组合为一个单词二维列表
		add_word = [ch[x],en[x]]
		word.append(add_word)

	print(word)
	#return word
	lbfh_list = []
	for x in word:
		y = 'ƒ'.join(x)
		lbfh_list.append(y)


	final_list = '∂'.join(lbfh_list)

	return final_list



def change_img_name(jdlj,name_head):

	a, b = get_img_name(jdlj, name_head)
	changejpgexif(a)

	#a是带有绝对路径的列表
	#b是只有更改后图片的名字的列表
	return a, b


def core_update(cmd):

	up_date_list = read_excil(cmd[1])
	if up_date_list[0] == "year":
		api = "update"
		cho = up_date_list[0]
		year_name = up_date_list[1]
		describe = up_date_list[2]
		photo_user_path = up_date_list[3]
		photo_path = "/static/img/year_min/" + photo_user_path
		data = "http://127.0.0.1:5000/api/?config="+api+"å"+cho+"å"\
		+year_name+"å"+describe+"å"+photo_path

		print("\n")
		print("api:"+ api)
		print("cho:" + cho)
		print("name:" + year_name)
		print("describe:" + describe)
		print("photo_path:" + photo_path)
		print("send_data:" + data)
		input("按下回车进行发送...")

		send_get_http(data)



	if up_date_list[0] == "det":
		det_body = read_word_for_det_body(cmd[1])
		api = "update"
		cho = up_date_list[0]
		detname = up_date_list[1]
		describe = up_date_list[2]
		photo_user_path = up_date_list[3]
		photo_path = "/static/img/det_min/" + photo_user_path
		body = str(det_body)
		act_id = up_date_list[4]
		data = "http://127.0.0.1:5000/api/?config="+api+"å"+cho+"å"\
		+detname+"å"+describe+"å"+photo_path+"å"+body+"å"+act_id

		print("\n")
		print("api:"+ api)
		print("cho:" + cho)
		print("name:" + detname)
		print("describe:" + describe)
		print("photo_path:" + photo_path)
		print("body:" + body)
		print("act_id:" + act_id)
		print("send_data:" + data)
		input("按下回车进行发送...")

		send_get_http(data)



def send_get_http(data):

	js = 0

	while js < 3 :
		try:
			response = requests.get(data, timeout=5)
			print("申请get方式发送完成！")
			js = 4
		except:
			js += 1
			print("传输超时！正在重连(%r/3)" %(str(js)))


def changejpgexif(listb):
	print("开始移除照片其他信息")
	for x in listb:
		try:
			zc = 1

			exif_dict = piexif.load(x)

			if exif_dict is not None:
				print("已检测照片属性")
				if exif_dict["0th"][274] == 3:
					zc = 3
					print("照片旋转参数为3")

				if exif_dict["0th"][274] == 6:
					zc = 6
					print("照片旋转参数为6")

				if exif_dict["0th"][274] == 8:
					zc = 8
					print("照片旋转参数为8")

				im = Image.open(x)

				exif_dict["0th"][274] = 1

				bit = piexif.dump(exif_dict)

				if zc == 3:
					im = im.transpose(Image.ROTATE_180)

				if zc == 6:
					im = im.transpose(Image.ROTATE_270)

				if zc == 8:
					im = im.transpose(Image.ROTATE_90)

				im.save(x, exif=bit,quality=80)
		except:
			print("图片未检测到附加属性")

		else:
			print("图片未检测到附加属性")



#获取文件绝对路径
jdlj = os.path.dirname(os.path.abspath(__file__))




def get_img_name(Jdlj, head_of_img_name):

	#一个装有图片名称的列表 名称+路径
	name_list = []

	#图片的数量
	img_num = 0

	#uuid列表 名称+路径
	uuid_list = []

	#现在无路径
	now_list = []

	#未来路径的列表 带有结对路径
	future_list = []

	#适用于更改图片名称的二位列表
	quadratic_list = []

	#添加图片名称到列表
	for root, dirs, files in os.walk(Jdlj):  

		for file in files:  

			if os.path.splitext(file)[1] == '.jpeg' or os.path.splitext(file)[1] == '.JPEG':  
				name_list.append(os.path.join(file))
				img_num += 1

				#生成uuid
				uuid_list.append(str(uuid.uuid4()))

			elif os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == '.JPG':
				name_list.append(os.path.join(file))
				img_num += 1

				#生成uuid
				uuid_list.append(str(uuid.uuid4()))

			elif os.path.splitext(file)[1] == '.png' or os.path.splitext(file)[1] == '.PNG':
				name_list.append(os.path.join(file))
				img_num += 1

				#生成uuid
				uuid_list.append(str(uuid.uuid4()))

	#生成现在列表
	for a in name_list:
		now_list.append(Jdlj + '/' + a)

	#生成外来列表
	for b in uuid_list:
		future_list.append(Jdlj + '/' + head_of_img_name + '!' + b + '.jpg')

	#生成二位列表
	#生成暂存列表
	x = []
	for y in range(0, len(now_list)):
		x.append(now_list[y])
		x.append(future_list[y])
		quadratic_list.append(x)
		x = []


	for o, n in quadratic_list:
		os.rename(o, n)
	

	#now_list是带有绝对路径的列表
	#name_list是只有更改后图片的名字的列表
	return future_list, uuid_list
	



if __name__ == '__main__':
	main()



