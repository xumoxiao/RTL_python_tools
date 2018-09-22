import sys 
import os 
import re
import time


''' The user to change '''



Author = 'Moxiao Xu'



''' ------------------ '''






for arg in sys.argv:  
    print (arg) 
file_path = sys.argv[1]


#file_path = 'f:\\python_test\\Create_HDL\\test_file.vhd'



class Create_HDL :

    def __init__(self,file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        (self.shotname,self.extension) = os.path.splitext(self.file_name)
        self.file_flag = 0;
    def get_file_name(self):
        print( 'filename : ',self.file_name )
        print( 'extension : ',self.extension )

    def check_file_type(self):
        if( self.extension == '.vhd' or self.extension == '.VHD' ):
            print('File is VHDL type')
        else:
            print('Error : This file is not a VHDL file !')
            input()

    def cheak_file_empty(self):
        try:
            if(os.path.getsize(self.file_path)==0):
                self.file_flag = 1;
            else:
                self.file_flag = 0;
                input()
                
        except:
            print('Error: could not find file')
            input()

    def write_file(self,author_name):
        if(self.file_flag == 1):
            print(author_name)
            fp = open(file_path,"w")
            for x in range(100): fp.write('-')       
            fp.write('\n-- Project            : ' )
            fp.write('\n-- File name          : '+ self.file_name )
            fp.write('\n-- Create time        : '+ time.strftime('%Y.%m.%d', time.localtime()) )
            fp.write('\n-- File description   : ' )
            fp.write('\n-- Author             : '+ author_name + '\n' )
            for x in range(100): fp.write('-')
            fp.write('\n-- Copyright (c) ' + time.strftime('%Y', time.localtime())+' by XmX\n-- All rights reserved\n' )
            for x in range(100): fp.write('-') 
            fp.write('\n\n')
            for x in range(100): fp.write('-')
            fp.write('\n-- Libraries\n')
            for x in range(100): fp.write('-')
            fp.write('\nlibrary ieee;')
            fp.write('\n\tuse ieee.std_logic_1164.all;')
            fp.write('\n\tuse ieee.numeric_std.all;\n\n')
            for x in range(100): fp.write('-')
            fp.write('\n-- entity declaration\n')
            for x in range(100): fp.write('-')
            fp.write('\nentity '+self.shotname+' is')
            fp.write('\n\tgeneric (')
            fp.write('\n\t);')
            fp.write('\n\tport(\n\t\t')
            for x in range(50): fp.write('-')
            fp.write('\n\t\t-- Port define\n\t\t')
            for x in range(50): fp.write('-')
            fp.write('\n\t\tclk_in\t\t\t\t: in std_logic;')
            fp.write('\n\t\trst_in\t\t\t\t: in std_logic;\n')
            fp.write('\n\t);')
            fp.write('\nend '+self.shotname+';\n\n')
            for x in range(100): fp.write('-')
            fp.write('\n-- architecture implemention\n')
            for x in range(100): fp.write('-')
            fp.write('\narchitecture rtl of '+self.shotname+' is\n\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\t-- Fsm define\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\ttype Fsm_t    is( );\n\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\t-- struct define\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\ttype '+self.shotname+'_r is record\n\t\t')
            for x in range(50): fp.write('-')
            fp.write('\n\t\t-- Reg define\n\t\t')
            for x in range(50): fp.write('-')
            fp.write('\n\tend record '+self.shotname+'_r;\n\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\t-- signal define\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\tsignal r,r_next   : '+self.shotname+'_r;\n')
            fp.write('\nbegin\n\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\t-- combinatorial process\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\tp_comb : process ( r )')
            fp.write('\n\t\tvariable v : '+ self.shotname+'_r;')
            fp.write('\n\tbegin\n')
            fp.write('\n\t\t------ hold variables stable ------')
            fp.write('\n\t\tv := r;\n')
            fp.write('\n\t\t--------- processing part ---------\n\n\n\n')
            fp.write('\n\t\t---- write variables to signal ----')
            fp.write('\n\t\tr_next <= v;\n')
            fp.write('\n\tend process;\n\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\t-- internal assignment\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\n\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\t-- output assignments\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\n\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\t-- sequential process\n\t')
            for x in range(96): fp.write('-')
            fp.write('\n\n\tp_seq : process ( clk_in )')
            fp.write('\n\tbegin')
            fp.write('\n\t\tif rising_edge ( clk_in ) then ')
            fp.write('\n\t\t\tr <= r_next;')
            fp.write('\n\t\t\tif rst_in = \'1\' then\n\n')
            fp.write('\n\t\t\tend if;')
            fp.write('\n\t\tend if;')
            fp.write('\n\tend process;\n')
            fp.write('\nend rtl;\n\n')
            for x in range(100): fp.write('-')
            fp.write('\n-- eof\n')
            for x in range(100): fp.write('-')
            fp.close()
create = Create_HDL(file_path)
create.get_file_name()
create.cheak_file_empty()
create.check_file_type()
create.write_file(Author)


        