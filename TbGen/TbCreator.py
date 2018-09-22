import re
import sys
import os
import time
from V_Inst import V_Inst


class TbCreator:

    def __init__(self, DutPath, TbPath):
        self.VendorName = "XmX"
        self.AuthorName = "Moxiao Xu"
        self.file_path = TbPath
        self.file_name = os.path.basename(self.file_path)
        self.shotname, self.extension = os.path.splitext(self.file_name)
        self.ModuleName = self.shotname
        self.CurrentTime = time.strftime('%Y.%m.%d', time.localtime())
        self.DemoStrList = []
        self.ClkDict = {'ClkName': None, 'ClkFreq': None, 'ClkFreqPram': None, 'ClkRespPram': None,
                        'ClkRespTimePram': None}
        self.RstDict = {'RstName': None, 'Active': None, 'Inactive': None, 'SynClk': None}
        self.ClkList = []
        self.RstList = []
        self.TbList = []
        self.Inst = V_Inst(DutPath)
        self.Overwrite = False
        self.TbGenReturnVal = 0

    def SetOverwrite(self, bool):
        self.Overwrite = bool

    def CreateTbFile_f(self):
        if self.Overwrite == True or os.path.exists(self.file_path) == False:
            self.fp = open(self.file_path, "w", errors='ignore', encoding="utf-8")
            self.fp.writelines(self.TbList)
            self.fp.close()
        else:
            self.TbGenReturnVal = 1

    def KillSelf(self):
        del self

    def HeaderDemo(self):
        '''
// *************************************************************************************************
// Vendor           : &&VendorName
// Author           : &&AuthorName
// Filename         : &&ModuleName
// Date Created     : &&Date
// Version          : V1.0
// -------------------------------------------------------------------------------------------------
// File description :
// -------------------------------------------------------------------------------------------------
// Revision History :
// *************************************************************************************************
'''
        self.DemoStrList = self.HeaderDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            str = str.replace('&&VendorName', self.VendorName)
            str = str.replace('&&AuthorName', self.AuthorName)
            str = str.replace('&&ModuleName', self.ModuleName)
            str = str.replace('&&Date', self.CurrentTime)
            str = str + '\n'
            self.TbList.append(str)

    def ModelSofDemo(self):
        '''
`timescale   1ns/1ps
//--------------------------------------------------------------------------------------------------
// module declaration
//--------------------------------------------------------------------------------------------------

module &&ModuleName
#(
    &&ParamDefine
)();'''
        self.DemoStrList = self.ModelSofDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            if re.match(r'.*&&ParamDefine', str, re.IGNORECASE) != None:
                ''' match 到参数填充区'''
                self.ParamDefConstruct()
            else:
                str = str.replace('&&ModuleName', self.ModuleName)
                str = str + '\n'
                self.TbList.append(str)

    def LocalparamDemo(self):
        '''
    //----------------------------------------------------------------------------------------------
    // Localparam define
    //----------------------------------------------------------------------------------------------
    &&Localparam'''
        self.DemoStrList = self.LocalparamDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            if re.match(r'.*&&Localparam', str, re.IGNORECASE) != None:
                self.LocalConstruct()
            else:
                str = str + '\n'
                self.TbList.append(str)

    def LogicDefDemo(self):
        '''
    //----------------------------------------------------------------------------------------------
    // Logic define
    //----------------------------------------------------------------------------------------------
    &&LogicDefine'''

        self.DemoStrList = self.LogicDefDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            if re.match(r'.*&&LogicDefine', str, re.IGNORECASE) != None:
                ''' match 到参数填充区'''
                self.LogicDefConstruct()
            else:
                str = str + '\n'
                self.TbList.append(str)

    def LogicInitDemo(self):
        '''
    //----------------------------------------------------------------------------------------------
    // Logic Init
    //----------------------------------------------------------------------------------------------
    initial begin
        &&LogicInit
    end'''

        self.DemoStrList = self.LogicInitDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            if re.match(r'.*&&LogicInit', str, re.IGNORECASE) != None:
                ''' match 到参数填充区'''
                self.LogicInitConstruct()
            else:
                str = str + '\n'
                self.TbList.append(str)

    def ClockDefHeaderDemo(self):
        '''
    //----------------------------------------------------------------------------------------------
    // Clock define
    //----------------------------------------------------------------------------------------------'''
        self.DemoStrList = self.ClockDefHeaderDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            str = str + '\n'
            self.TbList.append(str)

    def ClockDefDemo(self):
        '''
    initial begin
        &&ClkName = 0;
        forever #((1e3/&&ClkFreq)/2) &&ClkName = !&&ClkName;
    end'''
        self.DemoStrList = self.ClockDefDemo.__doc__.split('\n')
        if self.ClkList != []:
            for port in self.ClkList:
                for str in self.DemoStrList:
                    str = str.replace(r'&&ClkName', port['ClkName'])
                    str = str.replace(r'&&ClkFreq', port['ClkFreqPram'])
                    str = str + '\n'
                    self.TbList.append(str)

    def TestCaseDemo(self):
        '''
    //----------------------------------------------------------------------------------------------
    // TestCase
    //----------------------------------------------------------------------------------------------
    initial begin
        &&RstInit
        #1000;
        //----- TestCase Start -----


        //----- Testcase Finish -----
        #1000;
        $finish;
    end'''
        self.DemoStrList = self.TestCaseDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            if re.match(r'.*&&RstInit', str, re.IGNORECASE) != None:
                ''' match 到参数填充区'''
                self.RstInitConstruct()
            else:
                str = str + '\n'
                self.TbList.append(str)

    def TaskDefDemo(self):
        '''
    //----------------------------------------------------------------------------------------------
    // Task Define
    //----------------------------------------------------------------------------------------------
    task TaskName(
        //input args,output args
    );
    begin
        //task logic
    end
    endtask'''
        self.DemoStrList = self.TaskDefDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            str = str + '\n'
            self.TbList.append(str)

    def AddInst(self):
        for str in self.Inst.InstStr:
            self.TbList.append(str)

    def ModelEofDemo(self):
        '''
endmodule
//--------------------------------------------------------------------------------------------------
// Eof
//--------------------------------------------------------------------------------------------------
'''
        self.DemoStrList = self.ModelEofDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            str = str + '\n'
            self.TbList.append(str)

    def ParamDefConstruct(self):
        if self.Inst.param_list != []:
            for i, str in enumerate(self.Inst.param_list):
                ''' parameter AXI_WIDTH = 32, '''
                TempStr = '\tparameter '
                if i == len(self.Inst.param_list) - 1:
                    TempStr = TempStr + str['Pm_Name'] + ' = ' + str['Pm_Value'] + '\n'
                else:
                    TempStr = TempStr + str['Pm_Name'] + ' = ' + str['Pm_Value'] + ',\n'
                self.TbList.append(TempStr)
        else:
            pass

    def LogicDefConstruct(self):
        if self.Inst.port_list != []:
            for str in self.Inst.port_list:
                ''' logic [31:0] s_axi_rdata; '''
                TempStr = '\tlogic '
                if str['Pt_Range'] != None:
                    TempStr = TempStr + '[' + str['Pt_Range'] + ']'
                TempStr = TempStr + str['Pt_UserName'] + ';\n'
                self.TbList.append(TempStr)
        else:
            pass

    def LogicInitConstruct(self):
        for str in self.Inst.port_list:
            ''' m_axi_wdata = 0;'''
            if re.match('input', str['Pt_Dir'], re.IGNORECASE):
                if str['Pt_Type'] == 'Rst' or str['Pt_Type'] == 'Rst_n' or str['Pt_Type'] == 'Clk':
                    TempStr = None
                else:
                    TempStr = '\t\t' + str['Pt_UserName'] + ' = 0;\n'
                if TempStr != None:
                    self.TbList.append(TempStr)

    def RstInitConstruct(self):
        for str in self.RstList:
            TempStr = '\t\t' + str['RstName'] + ' = ' + str['Active'] + ';\n'
            self.TbList.append(TempStr)

        TempStr = '\t\t#1000;\n'
        self.TbList.append(TempStr)

        for str in self.RstList:
            TempStr = '\t\t@(posedge ' + str['SynClk'] + ');\n'
            self.TbList.append(TempStr)
            TempStr = '\t\t' + str['RstName'] + ' = ' + str['Inactive'] + ';\n'
            self.TbList.append(TempStr)

    def PortListConstruct(self):
        if self.Inst.port_list != []:
            for str in self.Inst.port_list:
                if str['Pt_Type'] == 'Clk':
                    self.ClkDict['ClkName'] = str['Pt_UserName']
                    if str['Pt_TypeAttr'] != None:
                        self.ClkDict['ClkFreq'] = str['Pt_TypeAttr']
                    else:
                        self.ClkDict['ClkFreq'] = '100'
                    self.ClkDict['ClkFreqPram'] = str['Pt_UserName'].upper() + '_FREQ_M'
                    self.ClkDict['ClkRespTimePram'] = str['Pt_UserName'].upper() + '_RESP_TIME_NS'
                    self.ClkList.append(self.ClkDict)
                elif str['Pt_Type'] == 'Rst':
                    self.RstDict['RstName'] = str['Pt_UserName']
                    self.RstDict['Active'] = '1'
                    self.RstDict['Inactive'] = '0'
                    if str['Pt_SynClk'] != None:
                        self.RstDict['SynClk'] = str['Pt_SynClk']
                    else:
                        self.RstDict['SynClk'] = '`SYNCLK'
                    self.RstList.append(self.RstDict)
                elif str['Pt_Type'] == 'Rst_n':
                    self.RstDict['RstName'] = str['Pt_UserName']
                    self.RstDict['Active'] = '0'
                    self.RstDict['Inactive'] = '1'
                    self.RstList.append(self.RstDict)

    def LocalConstruct(self):
        if self.ClkList != []:
            for clk in self.ClkList:
                '''localparam CLK_NAME_FREQ_M = xxx;'''
                TempStr = '\tlocalparam ' + clk['ClkFreqPram'] + ' = ' + clk['ClkFreq'] + ';\n'
                self.TbList.append(TempStr)
                '''localparam CLK_NAME_RESP_TIME_NS = ((1e3/xxx)/10)*8;'''
                TempStr = '\tlocalparam ' + clk['ClkRespTimePram'] + ' = ((1e3/' + clk['ClkFreqPram'] + ')/10)*8;\n'
                self.TbList.append(TempStr)

    def InstDUT(self):
        ''' 分析rtl'''
        self.Inst.AnalysisRTL()
        if self.Inst.InstDone == True:
            self.TbGenReturnVal = 0
        else:
            self.TbGenReturnVal = 2

    def TbGen(self):
        self.InstDUT()
        if self.TbGenReturnVal == 0:
            self.PortListConstruct()
            self.HeaderDemo()
            self.ModelSofDemo()
            self.LocalparamDemo()
            self.LogicDefDemo()
            self.LogicInitDemo()
            self.ClockDefHeaderDemo()
            self.ClockDefDemo()
            self.TestCaseDemo()
            self.TaskDefDemo()
            self.AddInst()
            self.ModelEofDemo()
            self.CreateTbFile_f()
        else:
            pass


if __name__ == "__main__":
    # for arg in sys.argv:
    # print (arg)
    # file_path = sys.argv[1]
    file_path = 'C:\\Users\\xumoxiao\\Desktop\\Qt_Test\\str_ppl_stage.sv'
    hdl = TbCreator(file_path, 'str_ppl_stage_tb.sv')
    hdl.TbGen()
# input()