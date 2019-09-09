import requests
import xlrd
'''
import os
import uuid
import piexif
from PIL import Image
import requests
'''

def help():
	print("help ------------ 帮助选项(查看文档详细信息)")
	print("up [cho] [body] - 创建提交数据库信息")
	print("de [cho] [name] - 删除数据库信息")
	print("sc [cho] [none] - 搜索数据库信息")
	print("img [file_name] - 上传图像文件")
	print("rd [file_name] -- 读取excil文档内容")


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
	if cmd[0] == "up":
		update(cmd)
	if cmd[0] == "de":
		help()
	if cmd[0] == "sc":
		help()
	if cmd[0] == "img":
		help()
	if cmd[0] == "rd":
		read_word(cmd[1])




def read_word(path):
	#用于读取word的函数
	#返回一个二维数组
	word = []
	#打开xlsx
	workbook = xlrd.open_workbook(path)
	#导出一个表
	sheet = workbook.sheet_by_index(0)#使用索引导出

	#将表中的值按列导出
	ch2 = sheet.col_values(0)

	en2 = sheet.col_values(1)
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

	print(final_list)



#这里是主函数
def change_img_name(name_head):

	a, b = get_img_name(jdlj, name_head)
	changejpgexif(a)


	#a是带有绝对路径的列表
	#b是只有更改后图片的名字的列表
	return a, b



def update(cmd):
	#上传函数
	if cmd[1] == "year":
		api = "update"
		cho = cmd[1]
		year_name = cmd[2]
		describe = cmd[3]
		photo_user_path = cmd[4]
		photo_path = "/static/img/year_min/" + photo_user_path
		data = "http://127.0.0.1:5000/api/?config="+api+"å"+cho+"å"\
		+year_name+"å"+describe+"å"+photo_path

		send_get_http(data)


	if cmd[1] == "det":
		api = "update"
		cho = cmd[1]
		detname = cmd[2]
		describe = cmd[3]
		photo_user_path = cmd[4]
		photo_path = "/static/img/det_min/" + photo_user_path
		body = cmd[5]
		act_id = cmd[6]
		data = "http://127.0.0.1:5000/api/?config="+api+"å"+cho+"å"\
		+detname+"å"+describe+"å"+photo_path+"å"+body+"å"+act_id

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



'''


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

	#一个装有图片名称的列表 只有名称没有路径
	name_list = []

	#图片的数量
	img_num = 0

	#uuid列表
	uuid_list = []

	#现在路径的列表
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
		now_list.append(Jdlj + '\\' + head_of_img_name + '!' + a)

	#生成外来列表
	for b in uuid_list:
		future_list.append(head_of_img_name + '!' + b + '.jpg')

	#生成二位列表
	#生成暂存列表
	x = []
	for y in range(0, len(now_list)):
		x.append(name_list[y])
		x.append(future_list[y])
		quadratic_list.append(x)
		x = []

	
	for o, n in quadratic_list:
		os.rename(o, n)
	

	#now_list是带有绝对路径的列表
	#name_list是只有更改后图片的名字的列表
	return now_list, name_list
	

'''




if __name__ == '__main__':
	main()



