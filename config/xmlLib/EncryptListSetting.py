import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent

from GUI.pdfEditerToolGUI_EncryptListSetting import pdfEditorTool_EncryptListSetting
from GUI.pdfEditerToolGUI import Ui_pdfEditerToolGUI
from config.xmlLib.EncryptListConfig import EncryptListConfig

class EncryptListSetting(pdfEditorTool_EncryptListSetting):
    userPasswordList:list[str] = []
    ownerPasswordList:list[str] = []
    def __init__(self,pdfEditerToolGUI:Ui_pdfEditerToolGUI, parent=None):
        super(EncryptListSetting, self).__init__(parent)
        self.setui()
        self.EncryptListConfig = EncryptListConfig(os.getcwd() + "\\config", self)
        self.EncryptListConfig.getConfigSetting()
        self.pdfEditerToolUi = pdfEditerToolGUI
        return
    def setui(self) -> None:
        self.overrideSetting()
        self.guiSlotConnect()
        return

    def overrideSetting(self):
        """
        -----------------------------------------------------------------
        override処理\n
        -----------------------------------------------------------------
        """
        return
    
    
    def guiSlotConnect(self) -> None:
        """
        -----------------------------------------------------------------
        EncryptListSetting スロットコネクト処理\n
        -----------------------------------------------------------------
        """
        self.btExecution.clicked.connect(self.btExecution_Click)
        return
    
    
    def closeEvent(self, event: QCloseEvent|None ):
        """
        -----------------------------------------------------------------
        EncryptListSetting closeEvent処理\n
        -----------------------------------------------------------------
        """
        self.btExecution_Click()
        return

    def showGUI(self, EncryptNumberList: list[str], Encrypt2NumberList: list[str]) -> None:
        self.InitGUI(EncryptNumberList, Encrypt2NumberList)
        self.EncryptListConfig.updateGUISetting()
        flags = self.windowFlags()
        self.setWindowFlags( flags | Qt.WindowType.WindowStaysOnTopHint)
        self.show()
        return

    def btExecution_Click(self) -> None:

        self.EncryptListConfig.updateConfigSetting()
        self.EncryptListConfig.outputConfigSetting()
        self.updateEncryListSettingGUI()
        self.hide()
        return
    
    def InitGUI(self, EncryptNumberList: list[str], Encrypt2NumberList: list[str]) -> None:
        self.userPasswordList = EncryptNumberList
        self.ownerPasswordList = Encrypt2NumberList
        #Rb0
        self.txRb0Comment.setText(self.pdfEditerToolUi.rbEncrypt00.text())
        
        #Rb1
        self.txRb1Comment.setText(self.pdfEditerToolUi.rbEncrypt01.text())
        self.txRb1UserPassword.setText(self.userPasswordList[1])
        self.txRb1OwnerPassword.setText(self.ownerPasswordList[1])
        self.cbRb1ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt01.isHidden())
        
        #Rb2
        self.txRb2Comment.setText(self.pdfEditerToolUi.rbEncrypt02.text())
        self.txRb2UserPassword.setText(self.userPasswordList[2])
        self.txRb2OwnerPassword.setText(self.ownerPasswordList[2])
        self.cbRb2ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt02.isHidden())
        
        #Rb3
        self.txRb3Comment.setText(self.pdfEditerToolUi.rbEncrypt03.text())
        self.txRb3UserPassword.setText(self.userPasswordList[3])
        self.txRb3OwnerPassword.setText(self.ownerPasswordList[3])
        self.cbRb3ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt03.isHidden())
        
        #Rb4
        self.txRb4Comment.setText(self.pdfEditerToolUi.rbEncrypt04.text())
        self.txRb4UserPassword.setText(self.userPasswordList[4])
        self.txRb4OwnerPassword.setText(self.ownerPasswordList[4])
        self.cbRb4ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt04.isHidden())
        
        #Rb5
        self.txRb5Comment.setText(self.pdfEditerToolUi.rbEncrypt05.text())
        self.txRb5UserPassword.setText(self.userPasswordList[5])
        self.txRb5OwnerPassword.setText(self.ownerPasswordList[5])
        self.cbRb5ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt05.isHidden())
        
        #Rb6
        self.txRb6Comment.setText(self.pdfEditerToolUi.rbEncrypt06.text())
        self.txRb6UserPassword.setText(self.userPasswordList[6])
        self.txRb6OwnerPassword.setText(self.ownerPasswordList[6])
        self.cbRb6ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt06.isHidden())
        
        #Rb7
        self.txRb7Comment.setText(self.pdfEditerToolUi.rbEncrypt07.text())
        self.txRb7UserPassword.setText(self.userPasswordList[7])
        self.txRb7OwnerPassword.setText(self.ownerPasswordList[7])
        self.cbRb7ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt07.isHidden())

        #Rb8
        self.txRb8Comment.setText(self.pdfEditerToolUi.rbEncrypt08.text())
        self.txRb8UserPassword.setText(self.userPasswordList[8])
        self.txRb8OwnerPassword.setText(self.ownerPasswordList[8])
        self.cbRb8ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt08.isHidden())

        #Rb9
        self.txRb9Comment.setText(self.pdfEditerToolUi.rbEncrypt09.text())
        self.txRb9UserPassword.setText(self.userPasswordList[9])
        self.txRb9OwnerPassword.setText(self.ownerPasswordList[9])
        self.cbRb9ProHidden.setChecked(self.pdfEditerToolUi.rbEncrypt09.isHidden())
        
        #Rb10
        self.txRb10Comment.setText(self.pdfEditerToolUi.rbEncryptOther.text())
        return
    
    def updateEncryListSettingGUI(self) -> None:
        #Rb0
        self.pdfEditerToolUi.rbEncrypt00.setText(self.txRb0Comment.toPlainText())
        self.userPasswordList[0] = self.txRb0UserPassword.toPlainText()
        self.ownerPasswordList[0] = self.txRb0OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt01.setHidden(self.cbRb1ProHidden.isChecked())

        #Rb1
        self.pdfEditerToolUi.rbEncrypt01.setText(self.txRb1Comment.toPlainText())
        self.userPasswordList[1] = self.txRb1UserPassword.toPlainText()
        self.ownerPasswordList[1] = self.txRb1OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt01.setHidden(self.cbRb1ProHidden.isChecked())

        #Rb2
        self.pdfEditerToolUi.rbEncrypt02.setText(self.txRb2Comment.toPlainText())
        self.userPasswordList[2] = self.txRb2UserPassword.toPlainText()
        self.ownerPasswordList[2] = self.txRb2OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt02.setHidden(self.cbRb2ProHidden.isChecked())

        #Rb3
        self.pdfEditerToolUi.rbEncrypt03.setText(self.txRb3Comment.toPlainText())
        self.userPasswordList[3] = self.txRb3UserPassword.toPlainText()
        self.ownerPasswordList[3] = self.txRb3OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt03.setHidden(self.cbRb3ProHidden.isChecked())

        #Rb4
        self.pdfEditerToolUi.rbEncrypt04.setText(self.txRb4Comment.toPlainText())
        self.userPasswordList[4] = self.txRb4UserPassword.toPlainText()
        self.ownerPasswordList[4] = self.txRb4OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt04.setHidden(self.cbRb4ProHidden.isChecked())

        #Rb5
        self.pdfEditerToolUi.rbEncrypt05.setText(self.txRb5Comment.toPlainText())
        self.userPasswordList[5] = self.txRb5UserPassword.toPlainText()
        self.ownerPasswordList[5] = self.txRb5OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt05.setHidden(self.cbRb5ProHidden.isChecked())

        #Rb6
        self.pdfEditerToolUi.rbEncrypt06.setText(self.txRb6Comment.toPlainText())
        self.userPasswordList[6] = self.txRb6UserPassword.toPlainText()
        self.ownerPasswordList[6] = self.txRb6OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt06.setHidden(self.cbRb6ProHidden.isChecked())

        #Rb7
        self.pdfEditerToolUi.rbEncrypt07.setText(self.txRb7Comment.toPlainText())
        self.userPasswordList[7] = self.txRb7UserPassword.toPlainText()
        self.ownerPasswordList[7] = self.txRb7OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt07.setHidden(self.cbRb7ProHidden.isChecked())

        #Rb8
        self.pdfEditerToolUi.rbEncrypt08.setText(self.txRb8Comment.toPlainText())
        self.userPasswordList[8] = self.txRb8UserPassword.toPlainText()
        self.ownerPasswordList[8] = self.txRb8OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt08.setHidden(self.cbRb8ProHidden.isChecked())

        #Rb9
        self.pdfEditerToolUi.rbEncrypt09.setText(self.txRb9Comment.toPlainText())
        self.userPasswordList[9] = self.txRb9UserPassword.toPlainText()
        self.ownerPasswordList[9] = self.txRb9OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncrypt09.setHidden(self.cbRb9ProHidden.isChecked())

        #Rb10
        self.pdfEditerToolUi.rbEncryptOther.setText(self.txRb10Comment.toPlainText())
        self.userPasswordList[10] = self.txRb10UserPassword.toPlainText()
        self.ownerPasswordList[10] = self.txRb10OwnerPassword.toPlainText()
        self.pdfEditerToolUi.rbEncryptOther.setHidden(self.cbRb10ProHidden.isChecked())
        return
    