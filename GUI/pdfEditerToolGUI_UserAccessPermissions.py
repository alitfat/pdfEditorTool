from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton,QCheckBox, QGridLayout

class pdfEditerToolGUI_UserAccessPermissions(QWidget):
    
    def __init__(self, parent=None):
        """
        -----------------------------------------------------------------
        PDF権限設定GUI\n
        -----------------------------------------------------------------
        """
        super(pdfEditerToolGUI_UserAccessPermissions, self).__init__(parent)
        self.setWindowTitle("PDF UserAccessPermissions")
        self.ui()
        return
    
    def ui(self) -> None:
        """
        -----------------------------------------------------------------
        UI作成処理\n
        -----------------------------------------------------------------
        """
        self.main_design()
        self.layouts()
        return
    
    def main_design(self) -> None:
        """
        -----------------------------------------------------------------
        UI画面Widget作成\n
        -----------------------------------------------------------------
        """
        
        #印刷禁止
        self.cbPrint = QCheckBox("印刷禁止")
        self.__QCheckBoxSetting(self.cbPrint)
        
        #内容コピー禁止
        self.cbContentCopy = QCheckBox("内容コピー禁止")
        self.__QCheckBoxSetting(self.cbContentCopy)
        
        #ドキュメントの変更とアセンブリ禁止
        self.cbDocModify = QCheckBox("ドキュメントの変更とアセンブリ禁止")
        self.__QCheckBoxSetting(self.cbDocModify)
        
        #コメント記入禁止
        self.cbCommentModify = QCheckBox("コメント禁止")
        self.__QCheckBoxSetting(self.cbCommentModify)

        #ドキュメントのアセンブリとページ抽出禁止
        self.cbFillFromFields = QCheckBox("ドキュメントのアセンブリとページ抽出禁止")
        self.__QCheckBoxSetting(self.cbFillFromFields)

        self.btExecution = QPushButton("OK", self)
        self.btExecution.setStyleSheet("font-weight:bold;font-size:25px;")
        return

        
    def __QCheckBoxSetting(self, cbobj:QCheckBox) -> None:
        cbobj.setAutoFillBackground(False)
        return
    
    def layouts(self) -> None:
        """
        -----------------------------------------------------------------
        UI画面layout設定\n
        -----------------------------------------------------------------
        """
        form_layout = QGridLayout()

        rowIndex = 0
        self.__addWidgetSetting(rowIndex, form_layout, self.cbPrint)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.cbContentCopy)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.cbDocModify)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.cbCommentModify)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.cbFillFromFields)

        rowIndex = rowIndex + 2
        form_layout.addWidget(self.btExecution, rowIndex, 1, 1, 2)
        self.setLayout(form_layout)
        self.setGeometry(QtCore.QRect(100, 100, 400, 200))
        self.setMinimumSize(QtCore.QSize(400, 200))
        self.setMaximumSize(QtCore.QSize(400, 200))
        return

    def __addWidgetSetting(self,rowIndex:int,form_layout:QGridLayout, cbobj:QCheckBox) -> None:
        form_layout.addWidget(cbobj, rowIndex,0,1,4)
        return 
