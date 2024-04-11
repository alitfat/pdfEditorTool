# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdfEditerToolGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pdfEditerToolGUI(object):
    def setupUi(self, pdfEditerToolGUI):
        pdfEditerToolGUI.setObjectName("pdfEditerToolGUI")
        pdfEditerToolGUI.setWindowModality(QtCore.Qt.NonModal)
        pdfEditerToolGUI.setEnabled(True)
        pdfEditerToolGUI.resize(1020, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pdfEditerToolGUI.sizePolicy().hasHeightForWidth())
        pdfEditerToolGUI.setSizePolicy(sizePolicy)
        pdfEditerToolGUI.setMinimumSize(QtCore.QSize(1020, 400))
        pdfEditerToolGUI.setMaximumSize(QtCore.QSize(1020, 400))
        pdfEditerToolGUI.setAutoFillBackground(False)
        pdfEditerToolGUI.setStyleSheet("")
        self.menubar = QtWidgets.QMenuBar(pdfEditerToolGUI)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuChangTool = QtWidgets.QMenu(self.menuSetting)
        self.menuChangTool.setObjectName("menuChangTool")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.toolBar = QtWidgets.QToolBar(pdfEditerToolGUI)
        self.toolBar.setGeometry(QtCore.QRect(200, 360, 120, 40))
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setObjectName("toolBar")
        self.toolEncryptListBar = QtWidgets.QToolBar(pdfEditerToolGUI)
        self.toolEncryptListBar.setGeometry(QtCore.QRect(980, 20, 30, 40))
        self.toolEncryptListBar.setObjectName("toolEncryptListBar")
        self.lbObjFileName = QtWidgets.QLabel(pdfEditerToolGUI)
        self.lbObjFileName.setGeometry(QtCore.QRect(0, 30, 121, 20))
        self.lbObjFileName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbObjFileName.setObjectName("lbObjFileName")
        self.lbPdfFileName = QtWidgets.QLabel(pdfEditerToolGUI)
        self.lbPdfFileName.setGeometry(QtCore.QRect(19, 160, 101, 20))
        self.lbPdfFileName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbPdfFileName.setObjectName("lbPdfFileName")
        self.txObjFileName = QtWidgets.QTextEdit(pdfEditerToolGUI)
        self.txObjFileName.setGeometry(QtCore.QRect(130, 30, 480, 50))
        self.txObjFileName.setDocumentTitle("")
        self.txObjFileName.setObjectName("txObjFileName")
        self.txPdfFileName = QtWidgets.QTextEdit(pdfEditerToolGUI)
        self.txPdfFileName.setEnabled(False)
        self.txPdfFileName.setGeometry(QtCore.QRect(130, 160, 480, 30))
        self.txPdfFileName.setObjectName("txPdfFileName")
        self.btObjFileName = QtWidgets.QPushButton(pdfEditerToolGUI)
        self.btObjFileName.setGeometry(QtCore.QRect(620, 30, 50, 25))
        self.btObjFileName.setObjectName("btObjFileName")
        self.cbPdfFileName = QtWidgets.QCheckBox(pdfEditerToolGUI)
        self.cbPdfFileName.setGeometry(QtCore.QRect(620, 160, 101, 16))
        self.cbPdfFileName.setObjectName("cbPdfFileName")
        self.lbPdfFilePath = QtWidgets.QLabel(pdfEditerToolGUI)
        self.lbPdfFilePath.setGeometry(QtCore.QRect(20, 90, 101, 20))
        self.lbPdfFilePath.setTextFormat(QtCore.Qt.AutoText)
        self.lbPdfFilePath.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbPdfFilePath.setObjectName("lbPdfFilePath")
        self.txPdfFilePath = QtWidgets.QTextEdit(pdfEditerToolGUI)
        self.txPdfFilePath.setEnabled(False)
        self.txPdfFilePath.setGeometry(QtCore.QRect(130, 90, 480, 50))
        self.txPdfFilePath.setObjectName("txPdfFilePath")
        self.cbPdfFilePath = QtWidgets.QCheckBox(pdfEditerToolGUI)
        self.cbPdfFilePath.setEnabled(True)
        self.cbPdfFilePath.setGeometry(QtCore.QRect(620, 90, 91, 16))
        self.cbPdfFilePath.setChecked(False)
        self.cbPdfFilePath.setObjectName("cbPdfFilePath")
        self.btPdfFilePath = QtWidgets.QPushButton(pdfEditerToolGUI)
        self.btPdfFilePath.setEnabled(False)
        self.btPdfFilePath.setGeometry(QtCore.QRect(620, 110, 50, 25))
        self.btPdfFilePath.setObjectName("btPdfFilePath")
        self.lbPdfFileNote = QtWidgets.QLabel(pdfEditerToolGUI)
        self.lbPdfFileNote.setGeometry(QtCore.QRect(130, 200, 251, 20))
        self.lbPdfFileNote.setObjectName("lbPdfFileNote")
        self.gbEncrypt = QtWidgets.QGroupBox(pdfEditerToolGUI)
        self.gbEncrypt.setGeometry(QtCore.QRect(730, 20, 281, 321))
        self.gbEncrypt.setObjectName("gbEncrypt")
        self.rbEncrypt01 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt01.setGeometry(QtCore.QRect(20, 40, 191, 16))
        self.rbEncrypt01.setChecked(True)
        self.rbEncrypt01.setObjectName("rbEncrypt01")
        self.rbEncrypt02 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt02.setGeometry(QtCore.QRect(20, 60, 190, 15))
        self.rbEncrypt02.setObjectName("rbEncrypt02")
        self.rbEncrypt03 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt03.setGeometry(QtCore.QRect(20, 80, 200, 15))
        self.rbEncrypt03.setObjectName("rbEncrypt03")
        self.rbEncrypt04 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt04.setGeometry(QtCore.QRect(20, 100, 190, 15))
        self.rbEncrypt04.setObjectName("rbEncrypt04")
        self.rbEncrypt05 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt05.setGeometry(QtCore.QRect(20, 120, 170, 15))
        self.rbEncrypt05.setObjectName("rbEncrypt05")
        self.rbEncrypt06 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt06.setGeometry(QtCore.QRect(20, 140, 180, 15))
        self.rbEncrypt06.setObjectName("rbEncrypt06")
        self.rbEncryptOther = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncryptOther.setGeometry(QtCore.QRect(20, 220, 181, 16))
        self.rbEncryptOther.setObjectName("rbEncryptOther")
        self.txEncryptText = QtWidgets.QTextEdit(self.gbEncrypt)
        self.txEncryptText.setEnabled(False)
        self.txEncryptText.setGeometry(QtCore.QRect(120, 240, 150, 25))
        self.txEncryptText.setDocumentTitle("")
        self.txEncryptText.setObjectName("txEncryptText")
        self.rbEncrypt00 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt00.setGeometry(QtCore.QRect(20, 20, 150, 15))
        self.rbEncrypt00.setObjectName("rbEncrypt00")
        self.txEncrypt2Text = QtWidgets.QTextEdit(self.gbEncrypt)
        self.txEncrypt2Text.setEnabled(False)
        self.txEncrypt2Text.setGeometry(QtCore.QRect(120, 270, 150, 25))
        self.txEncrypt2Text.setDocumentTitle("")
        self.txEncrypt2Text.setObjectName("txEncrypt2Text")
        self.lbUserPassword = QtWidgets.QLabel(self.gbEncrypt)
        self.lbUserPassword.setGeometry(QtCore.QRect(20, 240, 91, 25))
        self.lbUserPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbUserPassword.setObjectName("lbUserPassword")
        self.lbOwnerPassword = QtWidgets.QLabel(self.gbEncrypt)
        self.lbOwnerPassword.setGeometry(QtCore.QRect(20, 270, 91, 25))
        self.lbOwnerPassword.setTextFormat(QtCore.Qt.AutoText)
        self.lbOwnerPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbOwnerPassword.setObjectName("lbOwnerPassword")
        self.rbEncrypt07 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt07.setGeometry(QtCore.QRect(20, 160, 180, 15))
        self.rbEncrypt07.setObjectName("rbEncrypt07")
        self.rbEncrypt08 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt08.setGeometry(QtCore.QRect(20, 180, 180, 15))
        self.rbEncrypt08.setObjectName("rbEncrypt08")
        self.rbEncrypt09 = QtWidgets.QRadioButton(self.gbEncrypt)
        self.rbEncrypt09.setGeometry(QtCore.QRect(20, 200, 180, 15))
        self.rbEncrypt09.setObjectName("rbEncrypt09")
        self.btObjFile2pdfFile = QtWidgets.QPushButton(pdfEditerToolGUI)
        self.btObjFile2pdfFile.setGeometry(QtCore.QRect(360, 250, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btObjFile2pdfFile.setFont(font)
        self.btObjFile2pdfFile.setObjectName("btObjFile2pdfFile")
        self.cbPdfFileOverWrite = QtWidgets.QCheckBox(pdfEditerToolGUI)
        self.cbPdfFileOverWrite.setGeometry(QtCore.QRect(500, 200, 121, 16))
        self.cbPdfFileOverWrite.setChecked(True)
        self.cbPdfFileOverWrite.setObjectName("cbPdfFileOverWrite")
        self.btExcelSheetSelect = QtWidgets.QPushButton(pdfEditerToolGUI)
        self.btExcelSheetSelect.setEnabled(False)
        self.btExcelSheetSelect.setGeometry(QtCore.QRect(130, 250, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btExcelSheetSelect.setFont(font)
        self.btExcelSheetSelect.setObjectName("btExcelSheetSelect")
        self.cmbPdfAlgorithm = QtWidgets.QComboBox(pdfEditerToolGUI)
        self.cmbPdfAlgorithm.setGeometry(QtCore.QRect(730, 360, 230, 22))
        self.cmbPdfAlgorithm.setObjectName("cmbPdfAlgorithm")
        self.lbPdfAlgorithmLabel = QtWidgets.QLabel(pdfEditerToolGUI)
        self.lbPdfAlgorithmLabel.setGeometry(QtCore.QRect(730, 340, 80, 15))
        self.lbPdfAlgorithmLabel.setObjectName("lbPdfAlgorithmLabel")
        self.btPdfDocAttribSet = QtWidgets.QPushButton(pdfEditerToolGUI)
        self.btPdfDocAttribSet.setGeometry(QtCore.QRect(30, 370, 121, 25))
        self.btPdfDocAttribSet.setObjectName("btPdfDocAttribSet")
        self.cbPdfDocAttribSet = QtWidgets.QCheckBox(pdfEditerToolGUI)
        self.cbPdfDocAttribSet.setGeometry(QtCore.QRect(370, 200, 121, 16))
        self.cbPdfDocAttribSet.setChecked(True)
        self.cbPdfDocAttribSet.setObjectName("cbPdfDocAttribSet")
        self.actionEncryptListSetting = QtWidgets.QAction(pdfEditerToolGUI)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icon/setting1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEncryptListSetting.setIcon(icon)
        self.actionEncryptListSetting.setObjectName("actionEncryptListSetting")
        self.actionAboutPdfEditorTool = QtWidgets.QAction(pdfEditerToolGUI)
        self.actionAboutPdfEditorTool.setObjectName("actionAboutPdfEditorTool")
        self.actionToolName0 = QtWidgets.QAction(pdfEditerToolGUI)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/icon/office2pdf2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionToolName0.setIcon(icon1)
        self.actionToolName0.setObjectName("actionToolName0")
        self.actionToolName1 = QtWidgets.QAction(pdfEditerToolGUI)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("GUI/icon/pdf_Encrypt2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionToolName1.setIcon(icon2)
        self.actionToolName1.setObjectName("actionToolName1")
        self.actionToolName2 = QtWidgets.QAction(pdfEditerToolGUI)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("GUI/icon/pdf_Decrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionToolName2.setIcon(icon3)
        self.actionToolName2.setObjectName("actionToolName2")
        self.actionOther = QtWidgets.QAction(pdfEditerToolGUI)
        self.actionOther.setObjectName("actionOther")
        self.gbEncrypt.raise_()
        self.toolEncryptListBar.raise_()
        self.toolBar.raise_()
        self.menubar.raise_()
        self.btObjFileName.raise_()
        self.lbObjFileName.raise_()
        self.lbPdfFileName.raise_()
        self.txObjFileName.raise_()
        self.txPdfFileName.raise_()
        self.cbPdfFileName.raise_()
        self.lbPdfFilePath.raise_()
        self.txPdfFilePath.raise_()
        self.cbPdfFilePath.raise_()
        self.btPdfFilePath.raise_()
        self.lbPdfFileNote.raise_()
        self.btObjFile2pdfFile.raise_()
        self.cbPdfFileOverWrite.raise_()
        self.btExcelSheetSelect.raise_()
        self.cmbPdfAlgorithm.raise_()
        self.lbPdfAlgorithmLabel.raise_()
        self.btPdfDocAttribSet.raise_()
        self.cbPdfDocAttribSet.raise_()
        self.menuChangTool.addAction(self.actionToolName0)
        self.menuChangTool.addAction(self.actionToolName1)
        self.menuChangTool.addAction(self.actionToolName2)
        self.menuSetting.addAction(self.menuChangTool.menuAction())
        self.menuSetting.addAction(self.actionEncryptListSetting)
        self.menuSetting.addAction(self.actionOther)
        self.menuHelp.addAction(self.actionAboutPdfEditorTool)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionToolName0)
        self.toolBar.addAction(self.actionToolName1)
        self.toolBar.addAction(self.actionToolName2)
        self.toolEncryptListBar.addAction(self.actionEncryptListSetting)

        self.retranslateUi(pdfEditerToolGUI)
        QtCore.QMetaObject.connectSlotsByName(pdfEditerToolGUI)

    def retranslateUi(self, pdfEditerToolGUI):
        _translate = QtCore.QCoreApplication.translate
        pdfEditerToolGUI.setWindowTitle(_translate("pdfEditerToolGUI", "pdfEditerToolGUI"))
        self.menuSetting.setTitle(_translate("pdfEditerToolGUI", "menuSetting"))
        self.menuChangTool.setTitle(_translate("pdfEditerToolGUI", "menuChangTool"))
        self.menuHelp.setTitle(_translate("pdfEditerToolGUI", "Help"))
        self.lbObjFileName.setText(_translate("pdfEditerToolGUI", "ObjectFileAddress"))
        self.lbPdfFileName.setText(_translate("pdfEditerToolGUI", "pdfFileName"))
        self.txObjFileName.setHtml(_translate("pdfEditerToolGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btObjFileName.setText(_translate("pdfEditerToolGUI", "select"))
        self.cbPdfFileName.setText(_translate("pdfEditerToolGUI", "Handwritting"))
        self.lbPdfFilePath.setText(_translate("pdfEditerToolGUI", "PdfFilePath"))
        self.cbPdfFilePath.setText(_translate("pdfEditerToolGUI", "Handwritting"))
        self.btPdfFilePath.setText(_translate("pdfEditerToolGUI", "select"))
        self.lbPdfFileNote.setText(_translate("pdfEditerToolGUI", "※ 👆 Don\'t input the extension name please."))
        self.gbEncrypt.setTitle(_translate("pdfEditerToolGUI", "gbEncrypt"))
        self.rbEncrypt01.setText(_translate("pdfEditerToolGUI", "rbEncrypt01"))
        self.rbEncrypt02.setText(_translate("pdfEditerToolGUI", "rbEncrypt02"))
        self.rbEncrypt03.setText(_translate("pdfEditerToolGUI", "rbEncrypt03"))
        self.rbEncrypt04.setText(_translate("pdfEditerToolGUI", "rbEncrypt04"))
        self.rbEncrypt05.setText(_translate("pdfEditerToolGUI", "rbEncrypt05"))
        self.rbEncrypt06.setText(_translate("pdfEditerToolGUI", "rbEncrypt06"))
        self.rbEncryptOther.setText(_translate("pdfEditerToolGUI", "other"))
        self.txEncryptText.setHtml(_translate("pdfEditerToolGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.rbEncrypt00.setText(_translate("pdfEditerToolGUI", "None-password"))
        self.txEncrypt2Text.setHtml(_translate("pdfEditerToolGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lbUserPassword.setText(_translate("pdfEditerToolGUI", "UserPassword"))
        self.lbOwnerPassword.setText(_translate("pdfEditerToolGUI", "OwnerPassword"))
        self.rbEncrypt07.setText(_translate("pdfEditerToolGUI", "rbEncrypt07"))
        self.rbEncrypt08.setText(_translate("pdfEditerToolGUI", "rbEncrypt08"))
        self.rbEncrypt09.setText(_translate("pdfEditerToolGUI", "rbEncrypt09"))
        self.btObjFile2pdfFile.setText(_translate("pdfEditerToolGUI", "ObjFile2pdfFileExecute"))
        self.cbPdfFileOverWrite.setText(_translate("pdfEditerToolGUI", "overwrite saving"))
        self.btExcelSheetSelect.setText(_translate("pdfEditerToolGUI", "ExcelSheetSelect"))
        self.lbPdfAlgorithmLabel.setText(_translate("pdfEditerToolGUI", "EncryptLabel:"))
        self.btPdfDocAttribSet.setText(_translate("pdfEditerToolGUI", "PdfInfoSetting"))
        self.cbPdfDocAttribSet.setText(_translate("pdfEditerToolGUI", "PdfInfoSetting"))
        self.actionEncryptListSetting.setText(_translate("pdfEditerToolGUI", "EncryptListSetting"))
        self.actionAboutPdfEditorTool.setText(_translate("pdfEditerToolGUI", "about pdfEditorTool"))
        self.actionToolName0.setText(_translate("pdfEditerToolGUI", "office2pdfTool"))
        self.actionToolName0.setShortcut(_translate("pdfEditerToolGUI", "Ctrl+1"))
        self.actionToolName1.setText(_translate("pdfEditerToolGUI", "pdfEncrypt"))
        self.actionToolName1.setShortcut(_translate("pdfEditerToolGUI", "Ctrl+2"))
        self.actionToolName2.setText(_translate("pdfEditerToolGUI", "pdfDecrypt"))
        self.actionToolName2.setShortcut(_translate("pdfEditerToolGUI", "Ctrl+3"))
        self.actionOther.setText(_translate("pdfEditerToolGUI", "actionOther(NoUse)"))
