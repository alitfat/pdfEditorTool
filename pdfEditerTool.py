import sys
import os

from PyQt5.QtWidgets import QDialog,QApplication, QWidget
from PyQt5.QtGui import QCloseEvent

from GUI.pdfEditerToolGUI import Ui_pdfEditerToolGUI
from GUI.pdfEditerToolGUI_Version import pdfEditorTool_VerGUI

from Lib.FileSysProcess import FileSysProcess
from Lib.QtLib import qtBoxLib, qtTextEdit
from Lib.pdfFileLib import pdfFileLib
from Lib.PdfInfoSetting import PdfInfoSetting
from Lib.PdfUserAccessPermissions import PdfUserAccessPermissions
from Lib.EncryptListSetting import EncryptListSetting
from Lib.officeFile2pdfFileLib import office2PDFLib, eOfficeFileType
from config.xmlLib.pdfEditerToolConfig import pdfEditerToolConfig

class Ui_pdfEditorTool(Ui_pdfEditerToolGUI):

    pdfEditerToolType: int = 0
 
    #【メニューバー】GUI作成
    Form_SetWindowTitleList: list[str] = []
    
    def __init__(self):
        super(Ui_pdfEditorTool, self).__init__()
        self.FileSysProcess = FileSysProcess()
        self.qtTextEdit = qtTextEdit()
        self.pdfETConfig = pdfEditerToolConfig(os.getcwd() + "\\config",self)
        return
    
    def addUiSetting(self, pdfEditerTool:QWidget) -> None:
        """
        -----------------------------------------------------------------
        pdfEditorTool ui設定追加処理\n
        -----------------------------------------------------------------
        """
        self.Form = pdfEditerTool

        self.pdfETConfig.getConfigSetting()
        
        #【メニューバー】GUI作成
        self.Form_SetWindowTitleList = self.pdfETConfig.menubarList.actionToolNameList
        
        #【officeFile⇒pdfFile変換】
        self.pdfEditerToolType = 0
        self.pdfETConfig.updateGUISetting(self.pdfEditerToolType)
        self.actionGUI_Update()
        self.overrideSetting()
        return
    

    def actionGUI_Update(self) -> None:
        """
        -----------------------------------------------------------------
        pdfEditorTool GUI更新処理\n
        -----------------------------------------------------------------
        """
        #【メニューバー】GUI作成
        self.Form.setWindowTitle(self.Form_SetWindowTitleList[self.pdfEditerToolType])
        self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        
        return


    def overrideSetting(self) -> None:
        """
        -----------------------------------------------------------------
        pdfEditorTool overrideSetting処理\n
        -----------------------------------------------------------------
        """
        #ドラッグ処理で【pdfファイルアドレス】内容取得
        self.txObjFileName.dragEnterEvent = lambda e: self.qtTextEdit.DragEnterEvent(e)
        self.txObjFileName.dropEvent = lambda e:self.qtTextEdit.DragEvent_FileAddr(self.txObjFileName, e)
        
        #ドラッグ処理で【pdfファイルパス】内容取得
        self.txPdfFilePath.dragEnterEvent = lambda e: self.qtTextEdit.DragEnterEvent(e)
        self.txPdfFilePath.dropEvent = lambda e:self.qtTextEdit.DragEvent_FilePath(self.txPdfFilePath, e)
        
        #ドラッグ処理で【pdfファイル名称】内容取得
        self.txPdfFileName.dragEnterEvent = lambda e: self.qtTextEdit.DragEnterEvent(e)
        self.txPdfFileName.dropEvent = lambda e:self.qtTextEdit.DragEvent_FileName(self.txPdfFileName, e)

        self.txObjFileName.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.txPdfFilePath.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.txPdfFileName.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.txEncryptText.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.txEncrypt2Text.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)

        self.cbPdfFilePath.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.cbPdfFileName.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.cbPdfFileOverWrite.focusOutEvent = lambda e:self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.Form.closeEvent = lambda e:self.closeEvent(e)
        return
    
    def closeEvent(self, event: QCloseEvent|None ):
        """
        -----------------------------------------------------------------
        pdfEditorToolツールクロスイベント\n
        -----------------------------------------------------------------
        """
        self.pdfETConfig.updateConfigSetting(self.pdfEditerToolType)
        self.pdfETConfig.outputConfigSetting()
        return
    
class pdfEditerTool(QDialog):
    encryptNumber: str  =""
    encrypt2Number: str  =""
    encryptType: str  =""
    pdfrbEncryptIndex: int  = 1

    def __init__(self,parent=None):
        super(pdfEditerTool, self).__init__(parent)
        
        # 本ツールGUI画面設定
        self.ui = Ui_pdfEditorTool()
        self.ui.setupUi(self)
        self.ui.addUiSetting(self)
        
        self.pdfFileLib =  pdfFileLib()
        self.FileSysProcess = FileSysProcess()
        self.qtBoxLib = qtBoxLib()
        
        # pdf変換用ライブラリー
        self.office2PDFLib = office2PDFLib()
        
        # 本ツールソフトバジョンGUI画面設定
        self.verInfo = pdfEditorTool_VerGUI()
        self.pdfInfo = PdfInfoSetting()
        self.pdfAccessPermiss = PdfUserAccessPermissions()
        self.EncryptList = EncryptListSetting(self.ui)
        #【officeFile⇒pdfFile変換】
        self.ui.pdfEditerToolType = 0
        self.ui.pdfETConfig.updateGUISetting(self.ui.pdfEditerToolType)
        self.ui.actionGUI_Update()
        self.cbpdfFileName_Click()
        self.pdfrbEncryptIndex = self.ui.pdfETConfig.actionToolList.gbEncryptRbIndex[self.ui.pdfEditerToolType]
        
        # スロットコネクト処理
        self.guiSlotConnect()
        return


    #スロットコネクト処理
    def guiSlotConnect(self) -> None:
        """
        -----------------------------------------------------------------
        スロットコネクト処理\n
        -----------------------------------------------------------------
        """
        #【officeFile⇒pdfFile変換】ツール変更処理
        self.ui.actionToolName0.triggered.connect(self.actionTooloffice2pdf_Click)
        #【pdf暗号化ツール】ツール変更処理
        self.ui.actionToolName1.triggered.connect(self.actionToolpdflock_Click)
        #【pdf復唱化ツール】ツール変更処理
        self.ui.actionToolName2.triggered.connect(self.actionToolpdfunlock_Click)
        # pdfEditorToolについて
        self.ui.actionAboutPdfEditorTool.triggered.connect(self.actionAboutPdfEditorTool_Click)
        # 暗号化リスト設定
        self.ui.actionEncryptListSetting.triggered.connect(self.actionEncryptListSetting_Click)
        # その他(未使用)
        self.ui.actionOther.triggered.connect(self.actionOther_Click)

        # 対象ファイル選択処理
        self.ui.btObjFileName.clicked.connect(self.btobjFileName_Click)
        # 対象ファイルアドレス変更処理
        self.ui.txObjFileName.textChanged.connect(self.txPDFFilePath_Update)
        self.ui.txObjFileName.textChanged.connect(self.txPDFFileName_Update)
        self.ui.txObjFileName.textChanged.connect(self.txobjFileName_textChanged)
        # PDFファイルパス手入力判断処理
        self.ui.cbPdfFilePath.toggled.connect(self.cbpdfFilePath_Click)
        # PDFファイルパス選択処理
        self.ui.btPdfFilePath.clicked.connect(self.btpdfFilePath_Click)
        # PDFファイル名称手入力判断処理
        self.ui.cbPdfFileName.toggled.connect(self.cbpdfFileName_Click)
        #PDF情報設定追加判断処理
        self.ui.cbPdfDocAttribSet.toggled.connect(self.cbPdfDocAttribSet_Click)
        
        # RadioButton選択処理
        self.ui.rbEncrypt00.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt01.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt02.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt03.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt04.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt05.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt06.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt07.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt08.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncrypt09.clicked.connect(self.rbEncrypt_Click)
        self.ui.rbEncryptOther.clicked.connect(self.rbEncrypt_Click)

        # Excel Sheet選択処理
        self.ui.btExcelSheetSelect.clicked.connect(self.btExcelSheetSelect_Click)
        # 【officeFile⇒pdfFile変換へ生成処理】/【pdf暗号化処理】/【pdf復唱化処理】
        self.ui.btObjFile2pdfFile.clicked.connect(self.btobjFile2pdfFile_Click)

        # Pdf Information設定処理
        self.ui.btPdfDocAttribSet.clicked.connect(self.btPdfDocAttribSet_Click)

        #Pdf権限設定処理
        self.ui.btPdfAuthorSet.clicked.connect(self.btPdfAuthorSet_Click)
        return


    def btobjFileName_Click(self) -> None:
        """
        -----------------------------------------------------------------
        対象ファイル選択処理\n
        -----------------------------------------------------------------
        """
        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")
        self.ui.btObjFileName.setEnabled(False)
        if self.ui.pdfEditerToolType == 0 :
           objFullFileAddr = self.qtBoxLib.GetOfficeFileName(objFullFileAddr)
        else :
           objFullFileAddr = self.qtBoxLib.GetPdfFileName(objFullFileAddr)

        self.ui.btObjFileName.setEnabled(True)
        self.ui.txObjFileName.setText(objFullFileAddr)

        self.txPDFFilePath_Update()
        self.txPDFFileName_Update()
        return


    def cbpdfFilePath_Click(self) -> None:
        """
        -----------------------------------------------------------------
        PDFファイルパス手入力判断処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbPdfFilePath.isChecked()):
            self.ui.txPdfFilePath.setEnabled(True)
            self.ui.btPdfFilePath.setEnabled(True)
        else:
           self.ui.txPdfFilePath.setEnabled(False)
           self.ui.btPdfFilePath.setEnabled(False)
           self.txPDFFilePath_Update()
        return


    def btpdfFilePath_Click(self) -> None:
        """
        -----------------------------------------------------------------
        PDFファイルパス選択処理\n
        -----------------------------------------------------------------
        """
        pdfFilePath = self.ui.txPdfFilePath.toPlainText()
        pdfFilePath = pdfFilePath.strip(" ")
        self.ui.btPdfFilePath.setEnabled(False)
        pdfFilePath = self.qtBoxLib.getFilePathByPathDialog(pdfFilePath)
        self.ui.btPdfFilePath.setEnabled(True)
        self.ui.txPdfFilePath.setText(pdfFilePath)
        return


    def cbPdfDocAttribSet_Click(self) -> None:
        """
        -----------------------------------------------------------------
        PDF情報設定追加判断処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbPdfDocAttribSet.isChecked()):
            self.ui.btPdfDocAttribSet.setEnabled(True)
        else:
           self.ui.btPdfDocAttribSet.setEnabled(False)
        return

    def cbpdfFileName_Click(self) -> None:
        """
        -----------------------------------------------------------------
        PDFファイル名称手入力判断処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbPdfFileName.isChecked()):
            self.ui.txPdfFileName.setEnabled(True)
        else:
           self.ui.txPdfFileName.setEnabled(False)
           self.txPDFFileName_Update()
        return
    
    def txPDFFilePath_Update(self) -> None:
        """
        -----------------------------------------------------------------
        PDFファイルパス内容更新処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbPdfFilePath.isChecked()):
            return

        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")

        resultList = self.FileSysProcess.getDirByFileFullAddr(objFullFileAddr)

        if resultList[0] == False :
            return
        self.ui.txPdfFilePath.setText(resultList[1])
        return


    def txPDFFileName_Update(self) -> None:
        """
        -----------------------------------------------------------------
        PDFファイル名称内容更新処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbPdfFileName.isChecked()):
            return

        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")

        bResult = self.FileSysProcess.judgeFileExsit(objFullFileAddr)
        if ( bResult  == False ) :
            return

        objFileName: list[str]  = []
        bResult = self.FileSysProcess.getFileNameInfoByFileFullAddr(objFullFileAddr, objFileName)
        if ( bResult  == False ) :
            return

        match(self.ui.pdfEditerToolType):
            case 0: self.ui.txPdfFileName.setText( objFileName[1])
            case 1: self.ui.txPdfFileName.setText( objFileName[1] + "_Encrypt")
            case 2: self.ui.txPdfFileName.setText( objFileName[1] + "_Decrypt")
            case _: 
                self.ui.pdfEditerToolType = 0
                self.ui.txPdfFileName.setText( objFileName[1])
        return
    
    
    def txobjFileName_textChanged(self) -> None:
        """
        -----------------------------------------------------------------
        PDFファイル内容変更処理\n
        -----------------------------------------------------------------
        """
        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")
        
        bResult = self.FileSysProcess.judgeFileExsit(objFullFileAddr)
        if ( bResult  == False ) :
            self.ui.btExcelSheetSelect.setEnabled(False)
            return

        objFileName: list[str]  = []
        bResult = self.FileSysProcess.getFileNameInfoByFileFullAddr(objFullFileAddr, objFileName)
        if ( bResult  == False ) :
            self.ui.btExcelSheetSelect.setEnabled(False)
            return

        officeFiletype = self.office2PDFLib.GetOfficeFileTypeByFileAddr(objFullFileAddr)
        if ( officeFiletype  == eOfficeFileType.Excel ) :
            self.ui.btExcelSheetSelect.setEnabled(True)
        else :
            self.ui.btExcelSheetSelect.setEnabled(False)
        
        return


    def rbEncrypt_Click(self) -> None:
        """
        -----------------------------------------------------------------
        暗号化設定処理\n
        -----------------------------------------------------------------
        """
        self.pdfrbEncryptIndex = self.ui.pdfETConfig.actionToolList.gbEncryptRbIndex[self.ui.pdfEditerToolType]
        self.encryptNumber = self.ui.pdfETConfig.encryptButtonList.EncryptNumberList[self.pdfrbEncryptIndex]
        self.encrypt2Number = self.ui.pdfETConfig.encryptButtonList.Encrypt2NumberList[self.pdfrbEncryptIndex]
        if self.pdfrbEncryptIndex == 10:
            self.encryptNumber = self.ui.txEncryptText.toPlainText()
            self.encrypt2Number = self.ui.txEncrypt2Text.toPlainText()
            if self.ui.pdfEditerToolType == 2:
                self.encryptNumber = self.encrypt2Number
        self.ui.pdfETConfig.updateConfigSetting(self.ui.pdfEditerToolType)


    def btExcelSheetSelect_Click(self) -> None:
        """
        -----------------------------------------------------------------
        Excel Sheet選択処理\n
        -----------------------------------------------------------------
        """
        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")
        self.office2PDFLib.SelectExcelSheetFile(objFullFileAddr)
        return


    def btobjFile2pdfFile_Click(self) -> None:
        """
        -----------------------------------------------------------------
        ツール実施処理\n
            │  (下記処理を実施)\n
            ├ 【officeファイル⇒PDFファイルへ生成処理】\n
            ├ 【pdf暗号化処理】\n
            └ 【pdf復唱化処理】\n
        -----------------------------------------------------------------
        """
        self.ui.btObjFile2pdfFile.setEnabled(False)
        # GUI画面更新処理
        QApplication.processEvents()

        #GUI入力内容判定処理
        bResult:bool = self.btobjFile2pdfFile_CheckGUISetting()
        if ( bResult  == False ) :
            self.ui.btObjFile2pdfFile.setEnabled(True)
            return
        
        msgTitle = self.ui.Form_SetWindowTitleList[self.ui.pdfEditerToolType]
        objFileName= self.ui.txObjFileName.toPlainText() #【pdfファイルアドレス】内容取得
        pdfFilePath= self.ui.txPdfFilePath.toPlainText() #【pdfファイルパス】内容取得
        pdfFileName= self.ui.txPdfFileName.toPlainText() #【pdfファイル名称】内容取得
        
        #PDFファイルアドレス設定
        pdfFullFileName = pdfFilePath + '\\' + pdfFileName
        if pdfFilePath[len(pdfFilePath) - 1:]  == '\\' :
            pdfFullFileName = pdfFilePath + pdfFileName
        
        pdfFullFileName = pdfFullFileName + '.pdf'

        bResult = self.FileSysProcess.judgeFileExsit(pdfFullFileName)

        if ( bResult  == True ) :
            if ( not self.ui.cbPdfFileOverWrite.isChecked() ) :
                bResult = self.qtBoxLib.JudgeOverWriteFile(pdfFullFileName, msgTitle)
                if ( bResult  == False ) :
                    self.ui.btObjFile2pdfFile.setEnabled(True)
                    return

        if ( bResult  == True ) :
            bResult = self.qtBoxLib.delFile(pdfFullFileName,msgTitle)
            if ( bResult  == False ) :
                self.ui.btObjFile2pdfFile.setEnabled(True)
                return

        match(self.ui.pdfEditerToolType):
            case 0: self.officeFile2pdfFileProcess(objFileName, pdfFullFileName)
            case 1: self.pdfEncryptProcess(objFileName, pdfFullFileName)
            case 2: self.pdfDecryptProcess(objFileName, pdfFullFileName)
            case _: 
                self.ui.pdfEditerToolType = 0
                self.officeFile2pdfFileProcess(objFileName, pdfFullFileName)
        return

    
    def officeFile2pdfFileProcess(self, officeFileName:str, pdfFullFileName:str) -> None:
        """
        -----------------------------------------------------------------
        officeファイル⇒PDFファイルへ生成処理\n
        【引数 】\n
            officeFileName:officeファイルアドレス\n
            pdfFullFileName:生成されたpdfファイルアドレス\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        msgTitle:str = self.ui.Form_SetWindowTitleList[self.ui.pdfEditerToolType]

        #対象ファイルをPDFファイルへ変換
        bResult:bool = self.office2PDFLib.ConvertofficeFile2pdfFile(officeFileName, pdfFullFileName)

        # print ("bResult = ", bResult)
        if ( bResult  == False ) :
            msgStr = self.ui.pdfETConfig.logList.logPdfConvertErrText
            msgStr = msgStr.replace('__officeFileName__', officeFileName)
            self.qtBoxLib.showErrMsgBoxInfo(msgTitle, msgStr)
            self.ui.btObjFile2pdfFile.setEnabled(True)
            return
        
        self.rbEncrypt_Click()

        if len(self.encryptNumber) == 0 :
            #pdf情報設定追加処理
            if self.ui.cbPdfDocAttribSet.isChecked():
                pdfMetaData = self.pdfInfo.getPdfMetadata()
                self.pdfFileLib.update_metadata(pdfFullFileName,pdfFullFileName,pdfMetaData)
            msgStr = self.ui.pdfETConfig.logList.logPdfConvertWithoutEncryptText
            msgStr = msgStr.replace('__pdfFileName__', pdfFullFileName)
            self.qtBoxLib.showErrMsgBoxInfo(msgTitle, msgStr)
            self.ui.btObjFile2pdfFile.setEnabled(True)
            return
        
        # pdfファイルにパスワードを追加
        self.addPasssword2pdfFile(pdfFullFileName)
        return
        
    
    def pdfEncryptProcess(self, pdfSrcFileName:str, pdfDstFileAddr:str) -> None:
        """
        -----------------------------------------------------------------
        pdf暗号化処理を追加\n
        【引数 】\n
            pdfSrcFileName:暗号化対象pdfファイルアドレス\n
            pdfDstFileAddr:暗号化後pdfファイルアドレス\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        self.rbEncrypt_Click()
        
        msgTitle:str = self.ui.Form_SetWindowTitleList[self.ui.pdfEditerToolType]
        
        #PDFファイル暗号が存在しているかどうかを確認
        bResult:bool = self.pdfFileLib.JudgePdfFileIsEncrypted(pdfSrcFileName)
        if ( bResult  == True ) :
            msgStr = self.ui.pdfETConfig.logList.logPdfWithEncryptErrText
            msgStr = msgStr.replace('__pdfFileName__', pdfSrcFileName)
            self.qtBoxLib.showErrMsgBoxInfo( msgTitle, msgStr )
            self.ui.btObjFile2pdfFile.setEnabled(True)
            return
        
        self.FileSysProcess.copyfile(pdfSrcFileName, pdfDstFileAddr)

        # pdfファイルにパスワードを追加
        self.addPasssword2pdfFile(pdfDstFileAddr)

        return
        
    
    def addPasssword2pdfFile(self, pdfFullFileName:str) -> None:
        """
        -----------------------------------------------------------------
        pdfファイルにパスワードを追加\n
        【引数 】\n
            pdfFullFileName:暗号化対象pdfファイルアドレス\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        #PDF暗号化ラベル取得
        algText:str = self.ui.cmbPdfAlgorithm.currentText()
        self.encryptType = self.ui.pdfETConfig.algorithmLabelList.pdfAlgLabelList.get(algText, "AES-256")
        pdfAccessPer = self.pdfAccessPermiss.getPdfAccessPermission()
        #PDFファイルへパスワードを追加
        self.pdfFileLib.AddEncrypt2pdfFile(pdfFileName = pdfFullFileName,
                                           user_password = self.encryptNumber,
                                           owner_password= self.encrypt2Number,
                                           permissions_flag= pdfAccessPer,
                                           encryptType = self.encryptType)
        
        if self.ui.cbPdfDocAttribSet.isChecked():
            #pdf情報設定追加処理
            pdfMetaData = self.pdfInfo.getPdfMetadata()
            
            self.pdfFileLib.update_metadata(src_path= pdfFullFileName,
                                            dst_path= pdfFullFileName,
                                            metadata= pdfMetaData,
                                            user_password= self.encryptNumber,
                                            owner_password= self.encrypt2Number,
                                            encryptType= self.encryptType,
                                            permissions_flag= pdfAccessPer)

        msgTitle:str = self.ui.Form_SetWindowTitleList[self.ui.pdfEditerToolType]
        msgStr = self.ui.pdfETConfig.logList.logPdfConvertWithEncryptText
        msgStr = msgStr.replace('__pdfFileName__', pdfFullFileName)
        msgStr = msgStr.replace('__algorithmLabel__', algText)
        msgStr = msgStr.replace('__encryptNumber__', self.encryptNumber)
        msgStr = msgStr.replace('__encrypt2Number__', self.encrypt2Number)
        self.qtBoxLib.showStdMsgBoxInfo( msgTitle, msgStr )
        self.ui.btObjFile2pdfFile.setEnabled(True)
        return
    
    
    def pdfDecryptProcess(self, pdfFileName:str, pdfDecryptFileName:str) -> None:
        """
        -----------------------------------------------------------------
        pdf復唱化処理\n
        【引数 】\n
            pdfFileName:暗号化対象pdfファイルアドレス\n
            pdfDecryptFileName:復唱化後pdfファイルアドレス\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        self.rbEncrypt_Click()
        
        msgTitle:str = self.ui.Form_SetWindowTitleList[self.ui.pdfEditerToolType]

        #PDFファイル暗号が存在しているかどうかを確認
        bResult:bool = self.pdfFileLib.JudgePdfFileIsEncrypted(pdfFileName)
        if ( bResult  == False ) :
            msgStr = self.ui.pdfETConfig.logList.logPdfWithoutEncryptErrText
            msgStr = msgStr.replace('__pdfFileName__', pdfFileName)
            self.qtBoxLib.showErrMsgBoxInfo( msgTitle, msgStr )
            self.ui.btObjFile2pdfFile.setEnabled(True)
            return

        #PDFファイル復唱化
        bResult = self.pdfFileLib.DecryptpdfFile(pdfFileName, pdfDecryptFileName, self.encryptNumber)
        if ( bResult  == False ) :
            msgStr = self.ui.pdfETConfig.logList.logPdfDecryptErrText
            msgStr = msgStr.replace('__pdfFileName__', pdfFileName)
            self.qtBoxLib.showErrMsgBoxInfo( msgTitle, msgStr )
            self.ui.btObjFile2pdfFile.setEnabled(True)
            return
       
        if self.ui.cbPdfDocAttribSet.isChecked():
            #pdf情報設定追加処理
            pdfMetaData = self.pdfInfo.getPdfMetadata()
            self.pdfFileLib.update_metadata(pdfDecryptFileName,pdfDecryptFileName,pdfMetaData)

        msgStr = self.ui.pdfETConfig.logList.logPdfDecryptText
        msgStr = msgStr.replace('__pdfFileName__', pdfDecryptFileName)
        self.qtBoxLib.showStdMsgBoxInfo( msgTitle, msgStr )
        self.ui.btObjFile2pdfFile.setEnabled(True)
        return
        

    def btobjFile2pdfFile_CheckGUISetting(self) -> bool:
        """
        -----------------------------------------------------------------
        GUI入力内容判定処理\n
        -----------------------------------------------------------------
        """
        msgTitle:str = self.ui.Form_SetWindowTitleList[self.ui.pdfEditerToolType]
        msgObjFileName =  "【" + self.ui.lbObjFileName.text() + "】"
        msgPdfFilePath =  "【" + self.ui.lbPdfFilePath.text() + "】"
        msgPdfFileName =  "【" + self.ui.lbPdfFileName.text() + "】"

        msgStr:str = ""
        bResult:bool = False
        
        #【対象ファイルアドレス】内容取得
        objFileName = self.ui.txObjFileName.toPlainText()
        bResult = self.qtBoxLib.judgeFileExsit(objFileName, msgTitle, msgObjFileName)
        self.ui.txObjFileName.setText(objFileName)
        if ( bResult  == False ) :
            return bResult

        #ファイル拡張子判定
        if ( self.ui.pdfEditerToolType == 0 ) :
            bResult = self.office2PDFLib.JudgeOfficeFileByFileAddr(objFileName)
        else :
            bResult = self.pdfFileLib.JudgePdfFileByFileAddr(objFileName)

        if bResult  == False :
            msgStr = self.ui.pdfETConfig.logList.logPdfExtensionErrText
            msgStr = msgStr.replace('__ObjFileTitle__', msgObjFileName)
            msgStr = msgStr.replace('__pdfFileName__', objFileName)
            self.qtBoxLib.showErrMsgBoxInfo(msgTitle, msgStr)
            return bResult

        #【pdfファイルパス】内容取得
        pdfFilePath = self.ui.txPdfFilePath.toPlainText()
        bResult = self.qtBoxLib.judgeDirExsit(pdfFilePath, msgTitle, msgPdfFilePath)
        if ( bResult  == False ) :
            return bResult

        #【pdfファイル名称】内容取得
        pdfFileName = self.ui.txPdfFileName.toPlainText()
        bResult = self.qtBoxLib.judgeIllegalCharacter(pdfFileName, msgTitle, msgPdfFileName)
        if ( bResult  == False ) :
            return bResult
        
        return bResult


    def actionTooloffice2pdf_Click(self) -> None:
        """
        -----------------------------------------------------------------
        【officeFile⇒pdfFile変換】ツールへ\n
        -----------------------------------------------------------------
        """
        self.actionTool_Change(0)
        return
    

    def actionToolpdflock_Click(self) -> None:
        """
        -----------------------------------------------------------------
        【pdf暗号化ツール】ツールへ\n
        -----------------------------------------------------------------
        """
        self.actionTool_Change(1)
        return
    

    def actionToolpdfunlock_Click(self) -> None:
        """
        -----------------------------------------------------------------
        【pdf復唱化ツール】ツールへ\n
        -----------------------------------------------------------------
        """
        self.actionTool_Change(2)
        return
    
    def actionTool_Change(self, pdfEditerToolType:int) -> None:
        """
        -----------------------------------------------------------------
        ツール切替処理\n
        -----------------------------------------------------------------
        """
        self.ui.pdfETConfig.updateConfigSetting(self.ui.pdfEditerToolType)
        self.ui.pdfEditerToolType = pdfEditerToolType
        self.ui.pdfETConfig.updateGUISetting(self.ui.pdfEditerToolType)
        self.ui.actionGUI_Update()
        self.cbpdfFileName_Click()
        return
    
    def actionAboutPdfEditorTool_Click(self) -> None:
        """
        -----------------------------------------------------------------
        pdfEditorToolについて処理\n
        -----------------------------------------------------------------
        """
        self.verInfo.show()
    def actionEncryptListSetting_Click(self) -> None:
        """
        -----------------------------------------------------------------
        暗号化リスト設定処理\n
        -----------------------------------------------------------------
        """
        self.EncryptList.showGUI(self.ui.pdfETConfig.encryptButtonList.EncryptNumberList,
                                 self.ui.pdfETConfig.encryptButtonList.Encrypt2NumberList)
        return
    def actionOther_Click(self) -> None:
        #self.pdfAccessPermiss.show()
        return
    
    def btPdfDocAttribSet_Click(self) -> None:
        """
        -----------------------------------------------------------------
        Pdf Information設定処理\n
        -----------------------------------------------------------------
        """
        self.pdfInfo.showGUI()

        return
    def btPdfAuthorSet_Click(self) -> None:
        """
        -----------------------------------------------------------------
        Pdf権限設定処理\n
        -----------------------------------------------------------------
        """
        self.pdfAccessPermiss.showGUI()

        return
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = pdfEditerTool()
    window.show()
    sys.exit(app.exec_())
