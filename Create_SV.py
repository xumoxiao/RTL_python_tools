import re
import sys 
import os 
import time

class SV_Create:

	def __init__(self,file_path):		
		self.VendorName = "XmX"		
		self.AuthorName = "Moxiao Xu"	
		self.file_path  = file_path
		self.file_name = os.path.basename(self.file_path)
		(self.shotname,self.extension) = os.path.splitext(self.file_name)
		self.ModuleName = self.shotname
		self.CurrentTime = time.strftime('%Y.%m.%d', time.localtime())
		self.DemoStrList = []

	def CheckFileEmpty_f(self):
		try:
			if(os.path.getsize(self.file_path) == 0):
				self.FileEmpty = True
			else:
				self.FileEmpty = False
				print('Error: Isn\'t empty file!')
				input()
		except:
			print('Error: could not find file')
			input()

	def MatchAndReplace_f(self):
		self.DemoStrList = self.SV_Demo_f.__doc__.split('\n')
		for i in range(len(self.DemoStrList)):

			self.DemoStrList[i] = self.DemoStrList[i].replace('&&VendorName',self.VendorName)
			self.DemoStrList[i] = self.DemoStrList[i].replace('&&AuthorName',self.AuthorName)
			self.DemoStrList[i] = self.DemoStrList[i].replace('&&ModuleName',self.ModuleName)
			self.DemoStrList[i] = self.DemoStrList[i].replace('&&Date',self.CurrentTime)

			self.DemoStrList[i] = self.DemoStrList[i] + '\n'

	def CreateSvFile_f(self):
		self.fp = open(self.file_path,"w",errors = 'ignore',encoding="utf-8")
		self.fp.writelines(self.DemoStrList)
		self.fp.close()

	def Test_f(self):
		self.CheckFileEmpty_f()
		if(self.FileEmpty == True):
			self.MatchAndReplace_f()
			self.CreateSvFile_f()
		else:
			pass


	def SV_Demo_f(self):
		'''
// *************************************************************************************************
// Vendor 			: &&VendorName
// Author 			: &&AuthorName
// Filename 		: &&ModuleName
// Date Created 	: &&Date
// Version 			: V1.0
// -------------------------------------------------------------------------------------------------
// File description	:
// -------------------------------------------------------------------------------------------------
// Revision History :
// *************************************************************************************************

`timescale   1ns/1ps
//--------------------------------------------------------------------------------------------------
// module declaration
//--------------------------------------------------------------------------------------------------

module &&ModuleName
#(
)
(
	//------------------------------------------------
	// Port define
	//------------------------------------------------
	input	i_clk,
	input	i_rst,

);

	//----------------------------------------------------------------------------------------------
	// Fsm define
	//----------------------------------------------------------------------------------------------
	typedef enum {

	} Fsm_e;


	//----------------------------------------------------------------------------------------------
	// struct define
	//----------------------------------------------------------------------------------------------
	typedef struct {

  	} &&ModuleName_s;

	//----------------------------------------------------------------------------------------------
	// Register define
	//----------------------------------------------------------------------------------------------
  	&&ModuleName_s r,rn;


	//----------------------------------------------------------------------------------------------
	// combinatorial always
	//----------------------------------------------------------------------------------------------
	always_comb begin	
		rn = r;

	end


	//----------------------------------------------------------------------------------------------
	// sequential always
	//----------------------------------------------------------------------------------------------	
	always_ff @(posedge i_clk) begin
		r <= rn;
		if(i_rst == 1) begin

		end
	end

endmodule

//--------------------------------------------------------------------------------------------------
// eof
//--------------------------------------------------------------------------------------------------
'''
		

for arg in sys.argv:  
	print (arg) 
file_path = sys.argv[1]

#file_path = 'C:\\Users\\jc-aoi\\Desktop\\python_new\\axi_gth_wp.sv'
hdl = SV_Create(file_path)
hdl.Test_f()
#input()