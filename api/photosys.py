#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import uuid
import piexif
from PIL import Image


class Alter():
	"""
	此类用于更改图片名称，将图片名称改为绝对唯一的名称
	此类需要传入绝对路径与类别标识名称
	调用顺序为
	insert_name_into_list
	insert_name_into_quadratic_list
	change_img_name
	changejpgexif
	"""

	def __init__(self, jdlj = '0', head_of_img_name = '0'):
	 	#self.listb = []
	 	self.jdlj = jdlj
	 	self.head_of_img_name = head_of_img_name
	 	self.now_list = []
	 	self.future_list = []
	 	self.quadratic_list = []


	#删除列表中的其他元素
	def changejpgexif(self):
		print("开始移除照片其他信息")
		for x in self.now_list:
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



	#添加图片名称到列表 存到两个列表 分别是现在和未来的图片路径和名称
	def insert_name_into_list(self):

		#一个装有图片名称的列表 只有名称没有路径
		name_list = []

		#uuid列表
		uuid_list = []

		#装有现在的图片名称加上绝对路径
		self.now_list = []

		#未来路径的列表 带有结对路径
		self.future_list = []

		#图片的名称
		img_num = 0


		for root, dirs, files in os.walk(self.jdlj):  
			

			for file in files:  
				

				if os.path.splitext(file)[1] == '.jpeg' or os.path.splitext(file)[1] == '.JPEG':  
					name_list.append(os.path.join(file))
					self.now_list.append(self.jdlj + '/' + os.path.join(file))
					img_num += 1

					tail = 'jpeg'

					#生成uuid
					uuid_list.append(str(uuid.uuid4()))
					self.future_list.append(self.jdlj + "/" + self.head_of_img_name + '*!*' + str(uuid.uuid4()) + '.' + tail)

				elif os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == '.JPG':
					name_list.append(os.path.join(file))
					self.now_list.append(self.jdlj + '/' + os.path.join(file))
					img_num += 1

					tail = 'jpg'

					#生成uuid
					uuid_list.append(str(uuid.uuid4()))
					self.future_list.append(self.jdlj + "/" + self.head_of_img_name + '*!*' + str(uuid.uuid4()) + '.' + tail)

				elif os.path.splitext(file)[1] == '.png' or os.path.splitext(file)[1] == '.PNG':
					name_list.append(os.path.join(file))
					self.now_list.append(self.jdlj + '/' + os.path.join(file))
					img_num += 1

					tail = 'png'

					#生成uuid
					uuid_list.append(str(uuid.uuid4()))
					self.future_list.append(self.jdlj + "/" + self.head_of_img_name + '*!*' + str(uuid.uuid4()) + '.' + tail)

		return self.future_list


		
	#创建二位列表 两个参数为现文件绝对路径和重命名后文件
	def insert_name_into_quadratic_list(self):

		#适用于更改图片名称的二位列表
		self.quadratic_list = []

		#生成二位列表
		#生成暂存列表
		x = []
		for y in range(0, len(self.now_list)):
			x.append(self.now_list[y])
			x.append(self.future_list[y])
			self.quadratic_list.append(x)
			x = []





	#更改图片名称 参数为二维列表
	def change_img_name(self):

		for o, n in self.quadratic_list:
			os.rename(str(o), str(n))






