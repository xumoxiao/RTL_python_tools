import re
import os

ModelsimXilinxLib = r' work.glbl -L unisims_ver -L secureip'
ModelsimLogAll = r'log -r /*'
ModelsimCmdPrefix = r'vlog -work work -sv'

class TclCreator:

    def __init__(self):
        self.OutputPath = ''
        self.Tb = ''
        self.TbName = ''
        self.Dut = ''
        self.SourceList = []
        self.LogAll = False
        self.XiinxLib = False
        self.RelativePath = False
        self.OverWrite = False
        self.TclList = []
        ''' 整理后的路径'''
        self.SourcePathList = []
        self.CompileList = []
        self.ModelsimCmd = ''
        self.ModelsimLogAll = ''
        self.TclGenReturnVal = 0


    def SetTb(self, path):
        self.Tb = path
        self.TbName = os.path.basename(self.Tb)
        self.TbSn, self.TbEs = os.path.splitext(self.TbName)

    def SetDut(self, path):
        self.Dut = path

    def SetSourceList(self, List):
        self.SourceList = List

    def SetOutputPath(self, path):
        self.OutputPath = path

    def SetLogAll(self, bool):
        self.LogAll = bool
        if bool == True:
            self.ModelsimLogAll = ModelsimLogAll
        else:
            self.ModelsimLogAll = '#' + ModelsimLogAll

    def SetXilinxLib(self, bool):
        self.XiinxLib = bool

    def SetRelativePath(self, bool):
        self.RelativePath = bool

    def SetOverWrite(self, bool):
        self.OverWrite = bool

    def TclDemo(self):
        '''
# -------------------------------------------------------------------------------------------------
# Get path of the script
# -------------------------------------------------------------------------------------------------
variable scriptPath [file dirname [file normalize [info script]]]
if {![file exists {work}]} {
	 echo &&TbName: create library
	 vlib {work}
}
# -------------------------------------------------------------------------------------------------
# Source File
# -------------------------------------------------------------------------------------------------
&&SourceFile

# -------------------------------------------------------------------------------------------------
# Execution Cmd
# -------------------------------------------------------------------------------------------------
&&ModelsimCmd

&&ModelsimLogAll
#source $scriptPath/wave.do

#run -all
'''
        self.DemoStrList = self.TclDemo.__doc__.split('\n')
        for str in self.DemoStrList:
            
            if re.match(r'.*&&SourceFile', str, re.IGNORECASE) != None:
                for path in self.CompileList:
                    path = path + '\n'
                    self.TclList.append(path)
            else:
                str = str.replace(r'&&TbName', self.TbSn)
                if self.XiinxLib == True:
                    self.ModelsimCmd = r'vsim -novopt -c work.' + self.TbSn + ModelsimXilinxLib
                else:
                    self.ModelsimCmd = r'vsim -novopt -c work.' + self.TbSn
                str = str.replace(r'&&ModelsimCmd', self.ModelsimCmd)
                str = str.replace(r'&&ModelsimLogAll', self.ModelsimLogAll)
                str = str + '\n'
                self.TclList.append(str)

    def AnaLysisPath(self):
        ''' 判断是否使用相对路径'''
        if self.RelativePath == True:
            for idx in range(len(self.SourceList)):
                try:
                    self.SourceList[idx] = os.path.relpath(self.SourceList[idx], self.OutputPath)
                    self.SourceList[idx] = self.SourceList[idx].replace('\\', '/')
                except BaseException:
                    self.SourceList[idx] = '***ErrPath*** ' + self.SourceList[idx]

    def CompileConstruct(self):
        '''组成 编译指令'''
        for i in self.SourceList:
            temp = ModelsimCmdPrefix + ' "$scriptPath/' + i + '"'
            print(temp)
            self.CompileList.append(temp)

    def TclListGen(self):
        self.AnaLysisPath()
        self.CompileConstruct()
        self.TclDemo()

    def CreateTclFile(self):
        tclname = self.OutputPath + '/run_' + self.TbSn + '.tcl'
        print(tclname)
        if self.OverWrite == True or os.path.exists(tclname) == False:
            fp = open(tclname, 'w', errors='ignore', encoding="utf-8")
            fp.writelines(self.TclList)
            fp.close()
            self.TclGenReturnVal = 0
        else:
            self.TclGenReturnVal = 1

    def KillSelf(self):
        del self

if __name__ == "__main__":
    str = '..\dut.sv'
    str = str.replace('\\', '/')
    print(str)
    pass