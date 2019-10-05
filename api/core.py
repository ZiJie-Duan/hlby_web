from photosys import Alter
from http_api import Http_operation
from excil_c import Read_excil

def help():
	print("help ------------------- 帮助选项(查看文档详细信息)")
	print("sc [cho] --------------- 搜索数据库信息")
	print("de [cho] [name] -------- 删除数据库信息")
	print("img [path][name] ------- 批量上传图像文件")
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

	change_img_name = Alter(jdlj=cmd[1],\
		head_of_img_name=cmd[2])
	file_path = change_img_name.insert_name_into_list()
	change_img_name.insert_name_into_quadratic_list()
	change_img_name.change_img_name()
	change_img_name.changejpgexif()

	for x in file_path:
		http = Http_operation(url="http://127.0.0.1:5000/api/upload/",\
			file_path=x)
		http.post_file()



def core_update():

	excil = Read_excil(cmd[1],)









if __name__ == '__main__':

	main()

