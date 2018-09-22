import os
import sys

class Prj_Create:

    def __init__(self,folder_path):
        self.folder_path  = folder_path
        self.temp_path = None

    def mk_prj_dir(self):
        if os.listdir(self.folder_path):
            print('Error: Folder not empty!')
            input()
        else:
            self.temp_path = self.folder_path + "\\prj"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\prj\\vivado_prj"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\prj\\vivado_hls_prj"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\sdk"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\sim"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\src"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\doc"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\bit"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\sim\\modelsim"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\sim\\tb"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\src\\rtl"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\src\\hls"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\src\\ip"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\src\\hls_ip"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\src\\coe"
            os.makedirs(self.temp_path)
            self.temp_path = self.folder_path + "\\src\\constrs"
            os.makedirs(self.temp_path)

#folder_path = "C:\\Users\\xumoxiao\\Desktop\\python_new\\test"
#print(folder_path)

for arg in sys.argv:  
    print (arg) 
folder_path = sys.argv[1]

folder_obj = Prj_Create(folder_path)
folder_obj.mk_prj_dir()