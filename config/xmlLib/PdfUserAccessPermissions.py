import typing, os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from pypdf.constants import UserAccessPermissions

from GUI.pdfEditerToolGUI_UserAccessPermissions import pdfEditerToolGUI_UserAccessPermissions
from config.xmlLib.UserAccessPermissionsConfig import UserAccessPermissionsConfig


class PdfUserAccessPermissions(pdfEditerToolGUI_UserAccessPermissions):

    def __init__(self, parent=None):
        super(PdfUserAccessPermissions, self).__init__(parent)
        self.setui()
        self.PdfAuthorSet = UserAccessPermissionsConfig(os.getcwd() + "\\config", self)
        self.PdfAuthorSet.getConfigSetting()
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
        PdfUserAccessPermissions スロットコネクト処理\n
        -----------------------------------------------------------------
        """
        
        self.btExecution.clicked.connect(self.btExecution_Click)
        
        return
    
    def closeEvent(self, event: QCloseEvent|None ):
        """
        -----------------------------------------------------------------
        PdfUserAccessPermissions closeEvent処理\n
        -----------------------------------------------------------------
        """
        self.btExecution_Click()
        return

    def showGUI(self) -> None:
        self.PdfAuthorSet.updateGUISetting()
        flags = self.windowFlags()
        self.setWindowFlags( flags | Qt.WindowType.WindowStaysOnTopHint)
        self.show()
        return

    def btExecution_Click(self) -> None:
        self.PdfAuthorSet.updateConfigSetting()
        self.PdfAuthorSet.outputConfigSetting()
        self.hide()
        return
    
    def getPdfAccessPermission(self) -> UserAccessPermissions:
        """
        -----------------------------------------------------------------
        PdfUserAccessPermissions Pdf権限設定取得処理\n
        -----------------------------------------------------------------
        """
        AccessPermission = (2**31 - 1) - 3
        self.PdfAuthorSet.updateGUISetting()
        #印刷禁止
        if self.cbPrint.isChecked():
            #印刷
            #ページの抽出
            #テンプレートページの作成(要確認)
            AccessPermission -= UserAccessPermissions.PRINT

            #ページの抽出
            #テンプレートページの作成(要確認)
            AccessPermission -= UserAccessPermissions.PRINT_TO_REPRESENTATION
   

        #内容コピー禁止
        if self.cbContentCopy.isChecked(): 
            #コンテンツのコピー
            #ページの抽出
            #テンプレートページの作成(要確認)
            AccessPermission -= UserAccessPermissions.EXTRACT

            #アクセシビリティのためのコンテンツのコピー
            #ページの抽出
            #テンプレートページの作成(要確認)
            AccessPermission -= UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS
        
        #ドキュメントの変更とアセンブリ禁止
        if self.cbDocModify.isChecked(): 
            #ドキュメントの変更
            #ドキュメントアセンブリ
            #ページの抽出
            #テンプレートページの作成(要確認)
            AccessPermission -= UserAccessPermissions.MODIFY
        
        #コメント記入禁止
        if self.cbCommentModify.isChecked(): 
            #コメント
            #ページの抽出
            #テンプレートページの作成(要確認)
            AccessPermission -= UserAccessPermissions.ADD_OR_MODIFY
        
        #ドキュメントのアセンブリとページ抽出禁止
        if self.cbFillFromFields.isChecked():
            #ドキュメントアセンブリ
            #ページの抽出
            AccessPermission -= UserAccessPermissions.FILL_FORM_FIELDS
        
        return UserAccessPermissions(AccessPermission)
    
    