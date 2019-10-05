import xlrd

class Read_excil:
	"""
	这是用于读取excel的类 
	用于读取excel并返回相应的列表
	此类提供两个输入值 
	path 为一个路径 用于描述excel的位置
	line 的传入是一个列表
	列表内包含需要读取的excel中的列的索引
	"""

	def __init__(self,path,line):
		self.path = path
		self.line = line
		#此列表用于存放横版二维列表
		self.h_list = []
		self.final_list = []


	def read_excil_l(self):


		for x in self.line:

			#用于读取exicil的函数
			#返回一个数组
			word = []
			#打开xlsx
			workbook = xlrd.open_workbook(self.path)
			#导出一个表
			sheet = workbook.sheet_by_index(0)#使用索引导出

			#将表中的值按列导出
			row = sheet.col_values(x)

			new_row = []

			#全部转为str以防出现错误
			for x in row:
				y = str(x)
				new_row.append(y)

			self.h_list.append(new_row)
		return self.h_list



	def make_list(self):
		#用于整合列表 将列表转换方向的函数

		list_amount = len(self.h_list)

		list_son_amount = len(self.h_list[0])

		for row in range(list_son_amount):
			list_zc = []
			for col in range(list_amount):

				list_zc.append(self.h_list[col][row])

			self.final_list.append(list_zc)

		return self.final_list















		

