import re
import sys 
import os 


"""
当前文件检擦verilog 文件中的 port 和 parameter 如果检测到，将数据存到list里面
"""

v_module_pt 	= r'^\s*(?:\bmodule\b)\s*(\w+)(?:\s*[#()]*\s*)*'
v_port_pt 		= r'(?:(\binput|output|inout\b))\s*'
v_logic_pt 		= r'(?:\bwire|reg\b)*\s*'
v_sign_pt 		= r'(?:\bsigned|unsigned\b)*\s*'
v_range_pt 		= r'(?:[^[]*\[([^]]*)\])*\s*'
v_ano_pt 		= r'(?:[/]{2}([\d\D]*))*\s*'
v_dft_val 		= r'(?:[=]\s*\S*)*\s*'
v_RL_range_pt 	= r'\s*([^:]*)\s*\:\s*([^\s]*)\s*'
v_port_attr_pt 	= r'^\s*' + v_port_pt + v_logic_pt + v_sign_pt + v_range_pt + r'(\w+)\s*' + v_dft_val + r'[,;]*\s*' + v_ano_pt
v_param_pt 		= r'^\s*(?:\bparameter\b)\s*'+ v_range_pt + r'(\w+)\s*[=]\s*(\S*)\s*(?:[;,])*\s*'+ v_ano_pt
#v_param_pt = r'^\s*(?:\bparameter\b)\s*'+ v_range_pt + r'\s*(\w+)\s*[=]\s*(.*?(?=[;,]))\s*'+ v_ano_pt + r'*\s*'


# 查找Port 以及相应属性，将其添加到 port_list


class V_Inst:
	def __init__(self,file_path):

		self.port_list = []
		self.param_list = []
		self.ModuleDict = {'Md_Name': None, 'Md_NameLen': None }
		self.PortDict = {'Pt_Name': None, 'Pt_NameLen': None, 'Pt_Dir': None, 'Pt_Range': None, 'Pt_L_Range': None, 'Pt_R_Range': None,'Pt_Ano': None} 
		self.ParamDict = {'Pm_Name': None, 'Pm_NameLen': None, 'Pm_Value': None, 'Pm_Range': None, 'Pm_Ano': None}
		self.line_match = None
		self.Range_match = None
		self.file_line_list = []
		self.file_line = ''
		self.file_path = file_path
		self.file_name = os.path.basename(self.file_path)
		(self.shotname,self.extension) = os.path.splitext(self.file_name)
		self.MaxLen = 0
		self.TempStr = ''

	def test(self):
		self.OpenFile()
		self.Extract_ModuleInfo()
		self.CloseFile()
		self.Create_InstFile()
		self.Write_V_Inst()
		self.CloseFile()

	def Check_FileType(self):
		if(self.extension == 'vhd' or self.extension == 'VHD'):
			self.FileType = 'vhd'
			print('File is VHDL type')
		elif(self.extension == 'v' or self.extension == 'V'):
 			self.FileType = 'v'
 			print('File is Verilog type')
		elif(self.extension == 'sv' or self.extension == 'SV'):
 			self.FileType = 'sv'
 			print('File is System Verilog type')
		else:
			self.FileType = None
			print('Error : This file is not a VHDL file !')
			input()

	def OpenFile(self):
		self.fp = open(self.file_path,'r',errors = 'ignore',encoding="utf-8") 
		self.file_line_list = self.fp.readlines()

	def CloseFile(self):
		self.fp.close()

	def Extract_ModuleInfo(self):
		for file_line in self.file_line_list:
			#print(file_line)
			self.Match_V_Module(file_line)
			self.Match_V_Port(file_line)
			self.Match_V_Param(file_line)
		#print(self.port_list)
		#print(self.param_list)

	def Match_V_Module(self, file_line):
		self.line_match =  re.match(v_module_pt,file_line,re.IGNORECASE)
		if(self.line_match != None):
			self.ModuleDict['Md_Name'] = self.line_match.group(1)
			self.ModuleDict['Md_NameLen'] = len(self.line_match.group(1))
			#print(self.ModuleDict['Md_Name'])

	def Match_V_Port(self, file_line):
		self.line_match =  re.match(v_port_attr_pt,file_line,re.IGNORECASE)
		if(self.line_match != None):
			self.PortDict['Pt_Name'] = self.line_match.group(3)
			self.PortDict['Pt_NameLen'] = len(self.line_match.group(3))
			self.PortDict['Pt_Dir'] = self.line_match.group(1)
			self.PortDict['Pt_Range'] = self.line_match.group(2)
			#匹配 port的左右范围
			if(self.PortDict['Pt_Range'] != None):
				self.Range_match =  re.match(v_RL_range_pt,self.PortDict['Pt_Range'],re.IGNORECASE)
				self.PortDict['Pt_L_Range'] = self.Range_match.group(1)
				self.PortDict['Pt_R_Range'] = self.Range_match.group(2)
			else:
				self.PortDict['Pt_L_Range'] = None
				self.PortDict['Pt_R_Range'] = None
			self.PortDict['Pt_Ano'] = self.line_match.group(4)
			self.port_list.append(self.PortDict.copy())

			#找到最长的port name长度，用于后面输出对齐
			if(self.PortDict['Pt_NameLen'] > self.MaxLen ):
				self.MaxLen = self.PortDict['Pt_NameLen']

			#print(self.PortDict)

	def Match_V_Param(self, file_line):
		self.line_match =  re.match(v_param_pt,file_line,re.IGNORECASE)
		if(self.line_match != None):
			self.ParamDict['Pm_Name'] = self.line_match.group(2)
			self.ParamDict['Pm_NameLen'] = len(self.line_match.group(2))
			self.ParamDict['Pm_Value'] = self.line_match.group(3)
			self.ParamDict['Pm_Range'] = self.line_match.group(1)
			self.ParamDict['Pm_Ano'] = self.line_match.group(4)
			self.param_list.append(self.ParamDict.copy())

			#找到最长的param name长度，用于后面输出对齐
			if(self.ParamDict['Pm_NameLen'] > self.MaxLen ):
				self.MaxLen = self.ParamDict['Pm_NameLen']

			#print(self.ParamDict)

	def Create_InstFile(self):
		self.InstFileName = self.shotname+'.inst'
		self.InstFilePath = os.path.split(self.file_path)[0] + '\\' + self.InstFileName
		self.fp = open(self.InstFilePath,'w',errors = 'ignore',encoding="utf-8")

		print(self.InstFilePath)
	def Write_V_Inst(self):
		'''	HDL_Inst V2.0																		Design by XmX

	//------------------------------------------------------------------------------------------------
	// Module Name : 
	// Description :                                                                                  
	//------------------------------------------------------------------------------------------------'''
		
		self.InstStr = self.Write_V_Inst.__doc__.split('\n')#将以上doc添加到InstStr List当中。

		if(self.ModuleDict['Md_Name'] != None):
			for i in range(100 - 17 - self.ModuleDict['Md_NameLen'] - 2):
				self.TempStr = self.TempStr + ' '
			self.TempStr = self.ModuleDict['Md_Name'] + self.TempStr
			self.InstStr[3] = self.InstStr[3] + self.TempStr
		else:
			print('ModuleName is None')


		for i in range(len(self.InstStr)):
			self.InstStr[i] = self.InstStr[i] + '\n'


		self.InstStr.append('\t' + self.ModuleDict['Md_Name'] + '\n')

		print(self.param_list)
		if(self.param_list != []):
			self.InstStr.append('\t#(\n')

			for i in range(len(self.param_list)):
				if(i == (len(self.param_list)-1)):
					self.Write_V_AlignLine('param',self.param_list[i],True)
				else:
					self.Write_V_AlignLine('param',self.param_list[i],False)
				self.InstStr.append(self.TempStr)

			self.InstStr.append('\t)\n')

		self.InstStr.append('\tu_' + self.ModuleDict['Md_Name'] + '\n')#例化名字
		self.InstStr.append('\t(\n')

		if(self.port_list != []):
			for i in range(len(self.port_list)):
				if(i == (len(self.port_list)-1)):
					self.Write_V_AlignLine('port',self.port_list[i],True)
				else:
					self.Write_V_AlignLine('port',self.port_list[i],False)
				self.InstStr.append(self.TempStr)
			self.InstStr.append('\t);\n')

		self.InstStr.append('\n')

		self.fp.writelines(self.InstStr)


	def Write_V_AlignLine(self,V_type,LineDict,LastFlag):
		''' .name 	( name 	),//anotation'''
		if(V_type == 'param'):
			Name = LineDict['Pm_Name']
			BlankLen = self.MaxLen - LineDict['Pm_NameLen']
			if(LineDict['Pm_Ano'] != None):
				Anotation = '//' + LineDict['Pm_Ano']
			else:
				Anotation = '\n'	
		elif(V_type == 'port'):
			Name = LineDict['Pt_Name']
			if(LineDict['Pt_Range']!=None):
				Range = LineDict['Pt_Range']
			else:
				Range = ''
			BlankLen = self.MaxLen - LineDict['Pt_NameLen'] 
			if(LineDict['Pt_Ano'] != None):
				Anotation = '//' + LineDict['Pt_Dir'] + ' ' + Range + ' ' + LineDict['Pt_Ano']
			else:
				Anotation = '//' + LineDict['Pt_Dir'] + ' ' + Range + '\n'

		self.TempStr = ''
		for x in range(BlankLen):
			self.TempStr = self.TempStr + ' '

		if(LastFlag == True):
			self.TempStr = '\t\t.' + Name + self.TempStr + '\t( ' + Name + self.TempStr + '\t) ' + Anotation 
		else:
			self.TempStr = '\t\t.' + Name + self.TempStr + '\t( ' + Name + self.TempStr + '\t),' + Anotation 


for arg in sys.argv:  
    print (arg) 
file_path = sys.argv[1]
#file_path = 'C:\\Users\\xumoxiao\\Desktop\\test.sv'
#file_path = 'C:\\Users\\jc-aoi\\Desktop\\python_new\\aurora_8b10b_clock_module.v'
#file_path = 'G:\\ZYNQ\\zybo_test\\src\\two_always.sv'


hdl = V_Inst(file_path)
hdl.test()