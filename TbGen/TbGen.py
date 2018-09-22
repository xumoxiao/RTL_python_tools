# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TbGen.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
                            QListWidget, QListWidgetItem, QSpacerItem, QCheckBox, QSizePolicy, QFileDialog,\
                            QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox
from TclCreator import TclCreator
from TbCreator import TbCreator

class Ui_TbGen(object):
    def setupUi(self, TbGen):
        TbGen.setObjectName("TbGen")
        TbGen.setWindowIcon(QtGui.QIcon("TG.png"))
        TbGen.resize(500, 300)
        self.verticalLayout = QVBoxLayout(TbGen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout0 = QHBoxLayout()
        self.horizontalLayout0.setObjectName("horizontalLayout0")
        self.DutLabel = QLabel(TbGen)
        self.DutLabel.setObjectName("DutLabel")
        self.horizontalLayout0.addWidget(self.DutLabel)
        self.DutLineEdit = QLineEdit(TbGen)
        self.DutLineEdit.setObjectName("DutLineEdit")
        self.horizontalLayout0.addWidget(self.DutLineEdit)
        self.DutBrowseBT = QPushButton(TbGen)
        self.DutBrowseBT.setObjectName("DutBrowseBT")
        self.horizontalLayout0.addWidget(self.DutBrowseBT)
        self.verticalLayout.addLayout(self.horizontalLayout0)
        self.horizontalLayout1 = QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.OupLabel = QLabel(TbGen)
        self.OupLabel.setObjectName("OupLabel")
        self.horizontalLayout1.addWidget(self.OupLabel)
        self.OupLineEdit = QLineEdit(TbGen)
        self.OupLineEdit.setObjectName("OupLineEdit")
        self.horizontalLayout1.addWidget(self.OupLineEdit)
        self.OupBrowseBT = QPushButton(TbGen)
        self.OupBrowseBT.setObjectName("OupBrowseBT")
        self.horizontalLayout1.addWidget(self.OupBrowseBT)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SrcLabel = QLabel(TbGen)
        self.SrcLabel.setObjectName("SrcLabel")
        self.horizontalLayout_2.addWidget(self.SrcLabel)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.SrcAddBT = QPushButton(TbGen)
        self.SrcAddBT.setObjectName("SrcAddBT")
        self.horizontalLayout_2.addWidget(self.SrcAddBT)
        self.SrcRemoveBT = QPushButton(TbGen)
        self.SrcRemoveBT.setObjectName("SrcRemoveBT")
        self.horizontalLayout_2.addWidget(self.SrcRemoveBT)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        ''' File Table Widget '''
        self.FileTW = QTableWidget(TbGen)
        self.FileTW.setShowGrid(True)
        self.FileTW.setObjectName("FileTW")
        self.FileTW.setColumnCount(2)
        self.FileTW.setRowCount(0)

        item = QTableWidgetItem()
        self.FileTW.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.FileTW.setHorizontalHeaderItem(1, item)
        self.FileTW.horizontalHeader().setVisible(True)
        self.FileTW.horizontalHeader().setCascadingSectionResizes(False)

        self.FileTW.setColumnWidth(0, 500)
        self.FileTW.setColumnWidth(1, 82)
        self.FileTW.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        self.FileTW.horizontalHeader().setMinimumSectionSize(80)
        self.FileTW.horizontalHeader().setSortIndicatorShown(False)
        # 拉伸 最后一列
        #self.FileTW.horizontalHeader().setStretchLastSection(True)
        self.FileTW.horizontalHeader().setStretchLastSection(False)
        ''' 禁止 编辑 '''
        self.FileTW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalLayout.addWidget(self.FileTW)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RelativePathCB = QCheckBox(TbGen)
        self.RelativePathCB.setObjectName("RelativePathCB")
        self.horizontalLayout_3.addWidget(self.RelativePathCB)
        self.OverwriteCB = QCheckBox(TbGen)
        self.OverwriteCB.setObjectName("OverwriteCB")

        self.horizontalLayout_3.addWidget(self.OverwriteCB)
        self.XilinxLibCB = QCheckBox(TbGen)
        self.XilinxLibCB.setObjectName("XilinxLibCB")
        self.horizontalLayout_3.addWidget(self.XilinxLibCB)
        self.LogAllCB = QCheckBox(TbGen)
        self.LogAllCB.setObjectName("LogAllCB")
        self.horizontalLayout_3.addWidget(self.LogAllCB)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.TbGenBT = QPushButton(TbGen)
        self.TbGenBT.setObjectName("TbGenBT")
        self.verticalLayout.addWidget(self.TbGenBT)

        self.retranslateUi(TbGen)

        self.DutBrowseBT_SS(TbGen)
        self.OupBrowseBT_SS(TbGen)
        self.SrcAddBT_SS(TbGen)
        self.FileTW_SS(TbGen)
        self.SrcRemoveBT_SS(TbGen)
        self.XilinxLibCB_SS(TbGen)
        self.TbGenBT_SS(TbGen)
        QtCore.QMetaObject.connectSlotsByName(TbGen)

        self.DutFileFlag = False
        self.TbFileFlag = False
        self.CurrentTWRowSet = 0
        self.CurrentTWType = ""
        self.OupDirPath = ""
        self.DutFilePath = ""
        self.TbPath = ''
        self.LogAll = False
        self.XiinxLib = False
        self.RelativePath = False
        self.OverWrite = False
        self.SourceList = []
        self.LastPath = ''
        self.SetCB("Default")
        self.TbCreateDone = False

    def retranslateUi(self, TbGen):
        _translate = QtCore.QCoreApplication.translate
        TbGen.setWindowTitle(_translate("TbGen", "TbGen"))
        self.DutLabel.setText(_translate("TbGen", "DUT File Path:"))
        self.DutBrowseBT.setText(_translate("TbGen", "Browse"))
        self.OupLabel.setText(_translate("TbGen", "Output Path:  "))
        self.OupBrowseBT.setText(_translate("TbGen", "Browse"))
        self.SrcLabel.setText(_translate("TbGen", "Compile List"))
        self.SrcAddBT.setText(_translate("TbGen", "Add"))
        self.SrcRemoveBT.setText(_translate("TbGen", "Remove"))
        item = self.FileTW.horizontalHeaderItem(0)
        item.setText(_translate("TbGen", "File path"))
        item = self.FileTW.horizontalHeaderItem(1)
        item.setText(_translate("TbGen", "File type"))
        self.RelativePathCB.setText(_translate("TbGen", "Relative Path"))
        self.OverwriteCB.setText(_translate("TbGen", "Overwrite"))
        self.XilinxLibCB.setText(_translate("TbGen", "Add Xilinx Lib"))
        self.LogAllCB.setText(_translate("TbGen", "Log All Signals"))
        self.TbGenBT.setText(_translate("TbGen", "Generate Testbench"))


    def DutBrowseBT_SS(self, TbGen):
        self.DutBrowseBT.clicked.connect(lambda:self.DutBrowseBT_Slot(TbGen))

    def DutBrowseBT_Slot(self, TbGen):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.DutFilePath, _ = QFileDialog.getOpenFileName(TbGen, "DutBrowseBT_Slot", "",
                                                  "HDL (*.v *.sv)", options=options)
        if self.DutFilePath:
            head, tail = os.path.split(self.DutFilePath)
            self.LastPath = head
            self.TbShortName, self.TbExtension = os.path.splitext(tail)
            self.TbShortName = self.TbShortName + "_tb" + self.TbExtension
            self.DutLineEdit.setText(self.DutFilePath)
            self.AddTWFile(self.DutFilePath, "DUT")
            if self.OupDirPath != "":
                self.TbPath = self.OupDirPath + "/" + self.TbShortName
                self.AddTWFile(self.TbPath, "TestBench")
                self.SetCB("Enable")

    def OupBrowseBT_SS(self, TbGen):
        self.OupBrowseBT.clicked.connect(lambda:self.OupBrowseBT_Slot(TbGen))

    def OupBrowseBT_Slot(self, TbGen):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.OupDirPath = QFileDialog.getExistingDirectory(TbGen, "OupBrowseBT_Slot", "", options=options)
        if self.OupDirPath:
            self.OupLineEdit.setText(self.OupDirPath)
            if self.DutFilePath != "":
                self.TbPath = self.OupDirPath + "/" + self.TbShortName
                self.AddTWFile(self.TbPath, "TestBench")
                self.SetCB("Enable")


    def SrcAddBT_SS(self, TbGen):
        self.SrcAddBT.clicked.connect(lambda:self.SrcAddBT_Slot(TbGen))

    def SrcAddBT_Slot(self, TbGen):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        TempFileName, _ = QFileDialog.getOpenFileNames(TbGen, "SrcAddBT_Slot", "",
                                                  "HDL (*.v *.sv)", options=options)
        '''多文件添加'''
        if TempFileName:
            for fn in TempFileName:
                self.AddTWFile(fn, "Source")
                #print(fn)

    def SrcRemoveBT_SS(self, TbGen):
        self.SrcRemoveBT.clicked.connect(lambda: self.SrcRemoveBT_Slot(TbGen))

    def SrcRemoveBT_Slot(self, TbGen):
        if self.CurrentTWRowSet == 1:
            if self.CurrentTWType == "DUT" or self.CurrentTWType == "TestBench":
                pass
            else:
                if self.CurrentTWType == "XilLib":
                    self.XilinxLibCB.setChecked(False)
                self.FileTW.removeRow(self.CurrentTWRow)
        self.CurrentTWRowSet = 0

    def AddTWFile(self, path, type):
        '''添加, 路径到 table widget'''

        if self.FileTW.findItems(path, QtCore.Qt.MatchFlag.MatchCaseSensitive) == []:
            if type == "DUT":
                ''' Dut 会和testbench 放到 0,1两行'''

                if self.DutFileFlag != True:
                    self.FileTW.insertRow(0)

                self.FileTW.setItem(0, 0, QTableWidgetItem(path))
                self.FileTW.setItem(0, 1, QTableWidgetItem(type))
                self.DutFileFlag = True

            elif type == "TestBench":
                if self.TbFileFlag != True:
                    if self.DutFileFlag == True:
                        self.FileTW.insertRow(1)
                        self.FileTW.setItem(1, 0, QTableWidgetItem(path))
                        self.FileTW.setItem(1, 1, QTableWidgetItem(type))
                    else:
                        self.FileTW.insertRow(0)
                        self.FileTW.setItem(0, 0, QTableWidgetItem(path))
                        self.FileTW.setItem(0, 1, QTableWidgetItem(type))
                else:
                    if self.DutFileFlag == True:
                        self.FileTW.setItem(1, 0, QTableWidgetItem(path))
                        self.FileTW.setItem(1, 1, QTableWidgetItem(type))
                    else:
                        self.FileTW.setItem(0, 0, QTableWidgetItem(path))
                        self.FileTW.setItem(0, 1, QTableWidgetItem(type))

                self.TbFileFlag = True
            else:
                '''查找是否存在相同，没有则添加'''
                self.FileTW.insertRow(self.FileTW.rowCount())
                self.FileTW.setItem(self.FileTW.rowCount() - 1, 0, QTableWidgetItem(path))
                self.FileTW.setItem(self.FileTW.rowCount() - 1, 1, QTableWidgetItem(type))

    def FindAndDeleTW(self, item):
        TempItem = self.FileTW.findItems(item, QtCore.Qt.MatchFlag.MatchCaseSensitive)
        for i in TempItem:
            self.FileTW.removeRow(self.FileTW.row(i))

    def FileTW_SS(self, TbGen):
        self.FileTW.itemClicked.connect(self.FileTW_Slot)

    def FileTW_Slot(self, item):
        ''' item 为 itemClicked 的返回值 '''
        print(item)
        self.CurrentTWRow = self.FileTW.row(item)
        TempTItem = self.FileTW.item(self.CurrentTWRow, 1)
        self.CurrentTWType = TempTItem.text()
        self.CurrentTWRowSet = 1
        print("Select Row " + str(self.CurrentTWRow) + ", Type " + TempTItem.text())


    def XilinxLibCB_SS(self, TbGen):
        self.XilinxLibCB.stateChanged.connect(self.XilinxLibCB_Slot)

    def XilinxLibCB_Slot(self, state):
        '''state 为 stateChanged 的输入参数'''
        '''0 Unchecked, 1 PartiallyChecked, 2 Checked'''
        print(state)
        ''' 将glbl 添加到 output Path '''
        if state == 2:
            self.GlblPath = self.OupDirPath + "/" + "glbl.v"
            self.AddTWFile(self.GlblPath, "XilLib")
        else:
            self.FindAndDeleTW("XilLib")

    def TbGenBT_SS(self, TbGen):
        self.TbGenBT.clicked.connect(lambda:self.TbGenBT_Slot(TbGen))

    def TbGenBT_Slot(self, TbGen):
        ''' 1 生成 run_tcl'''
        #print(self.OupDirPath)
        #print(self.DutFilePath)
        self.LogAll = True if self.LogAllCB.checkState() == 2 else False
        self.XiinxLib = True if self.XilinxLibCB.checkState() == 2 else False
        self.RelativePath = True if self.RelativePathCB.checkState() == 2 else False
        self.OverWrite = True if self.OverwriteCB.checkState() == 2 else False
        for row in range(self.FileTW.rowCount()):
            #print(self.FileTW.item(row, 0).text())
            self.SourceList.append(self.FileTW.item(row, 0).text())
        self.TclCreate()
        self.TbCreate()
        self.SourceList = []
        self.ReturnMessage()
        self.KillSubObject()

    def SetCB(self, Type):
        if Type == "Default":
            ''' Default  默认状态'''
            self.RelativePathCB.setChecked(True)
            self.XilinxLibCB.setChecked(False)
            self.OverwriteCB.setChecked(False)
            self.LogAllCB.setChecked(False)
            self.RelativePathCB.setEnabled(False)
            self.XilinxLibCB.setEnabled(False)
            self.OverwriteCB.setEnabled(False)
            self.LogAllCB.setEnabled(False)

            self.SrcAddBT.setEnabled(False)
            self.SrcRemoveBT.setEnabled(False)
            self.TbGenBT.setEnabled(False)

        elif Type == "Enable":
            self.RelativePathCB.setEnabled(True)
            self.XilinxLibCB.setEnabled(True)
            self.OverwriteCB.setEnabled(True)
            self.LogAllCB.setEnabled(True)
            self.SrcAddBT.setEnabled(True)
            self.SrcRemoveBT.setEnabled(True)
            self.TbGenBT.setEnabled(True)

    def TclCreate(self):
        self.Tcl = TclCreator()
        self.Tcl.SetTb(self.TbPath)
        self.Tcl.SetDut(self.DutFilePath)
        self.Tcl.SetSourceList(self.SourceList)
        self.Tcl.SetOutputPath(self.OupDirPath)
        self.Tcl.SetLogAll(self.LogAll)
        self.Tcl.SetXilinxLib(self.XiinxLib)
        self.Tcl.SetRelativePath(self.RelativePath)
        self.Tcl.SetOverWrite(self.OverWrite)
        self.Tcl.TclListGen()
        self.Tcl.CreateTclFile()

    def TbCreate(self):
        self.Tb = TbCreator(self.DutFilePath, self.TbPath)
        self.Tb.SetOverwrite(self.OverWrite)
        self.Tb.TbGen()

    def ReturnMessage(self):
        if self.Tcl.TclGenReturnVal == 0 and self.Tb.TbGenReturnVal == 0:
            tempStr = 'TbGen Done!'
        elif self.Tcl.TclGenReturnVal == 1:
            tempStr = 'TbGen Failed\nTcl File was exist!'
        elif self.Tb.TbGenReturnVal == 1:
            tempStr = 'TbGen Failed\nTestbench File was exist!'
        elif self.Tb.TbGenReturnVal == 2:
            tempStr = 'TbGen Failed\nRTL Inst Failed'
        else:
            tempStr = 'TbGen Failed'
        button = QMessageBox.information(TbGen, "information", tempStr,
                                         QMessageBox.Ok, QMessageBox.Ok)

    def KillSubObject(self):
        self.Tcl.KillSelf()
        self.Tb.KillSelf()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    TbGen = QWidget()
    ui = Ui_TbGen()
    ui.setupUi(TbGen)
    TbGen.show()
    sys.exit(app.exec_())

