from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QPushButton,QCheckBox, QGridLayout

class pdfEditorTool_EncryptListSetting(QWidget):
    
    def __init__(self, parent=None):
        """
        -----------------------------------------------------------------
        PDF情報設定GUI\n
        -----------------------------------------------------------------
        """
        super(pdfEditorTool_EncryptListSetting, self).__init__(parent)
        self.setWindowTitle("EncryptListSetting")
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
        
        #タイトル設定
        self.lbRbIndex = QLabel("Index")
        self.lbRbComment = QLabel("ShowComment")
        self.lbRbUserPassword = QLabel("UserPassword")
        self.lbRbOwnerPassword = QLabel("OwnerPassword")
        self.lbRbProHidden = QLabel("HiddenSetting")
        
        #Rb0設定
        self.lbRb0Index = QLabel("Rb0")
        self.txRb0Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb0Comment)
        self.txRb0UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb0UserPassword)
        self.txRb0OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb0OwnerPassword)
        self.cbRb0ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb0ProHidden)
        
        #Rb1設定
        self.lbRb1Index = QLabel("Rb1")
        self.txRb1Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb1Comment)
        self.txRb1UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb1UserPassword)
        self.txRb1OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb1OwnerPassword)
        self.cbRb1ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb1ProHidden)
        
        #Rb2設定
        self.lbRb2Index = QLabel("Rb2")
        self.txRb2Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb2Comment)
        self.txRb2UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb2UserPassword)
        self.txRb2OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb2OwnerPassword)
        self.cbRb2ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb2ProHidden)
        
        #Rb3設定
        self.lbRb3Index = QLabel("Rb3")
        self.txRb3Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb3Comment)
        self.txRb3UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb3UserPassword)
        self.txRb3OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb3OwnerPassword)
        self.cbRb3ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb3ProHidden)
        
        #Rb4設定
        self.lbRb4Index = QLabel("Rb4")
        self.txRb4Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb4Comment)
        self.txRb4UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb4UserPassword)
        self.txRb4OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb4OwnerPassword)
        self.cbRb4ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb4ProHidden)
        
        #Rb5設定
        self.lbRb5Index = QLabel("Rb5")
        self.txRb5Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb5Comment)
        self.txRb5UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb5UserPassword)
        self.txRb5OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb5OwnerPassword)
        self.cbRb5ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb5ProHidden)
        
        #Rb6設定
        self.lbRb6Index = QLabel("Rb6")
        self.txRb6Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb6Comment)
        self.txRb6UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb6UserPassword)
        self.txRb6OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb6OwnerPassword)
        self.cbRb6ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb6ProHidden)
        
        #Rb7設定
        self.lbRb7Index = QLabel("Rb7")
        self.txRb7Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb7Comment)
        self.txRb7UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb7UserPassword)
        self.txRb7OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb7OwnerPassword)
        self.cbRb7ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb7ProHidden)
        
        #Rb8設定
        self.lbRb8Index = QLabel("Rb8")
        self.txRb8Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb8Comment)
        self.txRb8UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb8UserPassword)
        self.txRb8OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb8OwnerPassword)
        self.cbRb8ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb8ProHidden)
        
        #Rb9設定
        self.lbRb9Index = QLabel("Rb9")
        self.txRb9Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb9Comment)
        self.txRb9UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb9UserPassword)
        self.txRb9OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb9OwnerPassword)
        self.cbRb9ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb9ProHidden)
        
        #Rb10設定
        self.lbRb10Index = QLabel("Rb10")
        self.txRb10Comment = QTextEdit("")
        self.__QTextEdit0Setting(self.txRb10Comment)
        self.txRb10UserPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb10UserPassword)
        self.txRb10OwnerPassword = QTextEdit("")
        self.__QTextEditSetting(self.txRb10OwnerPassword)
        self.cbRb10ProHidden = QCheckBox("Hidden")
        self.__QCheckBoxSetting(self.cbRb10ProHidden)
        
        
        
        self.btExecution = QPushButton("OK", self)
        self.btExecution.setStyleSheet("font-weight:bold;font-size:25px;")
        return

    def __QTextEdit0Setting(self, txobj:QTextEdit) -> None:
        txobj.setAutoFillBackground(False)
        txobj.setGeometry(QtCore.QRect(0, 0, 200, 25))
        txobj.setMinimumSize(QtCore.QSize(200, 25))
        txobj.setMaximumSize(QtCore.QSize(200, 25))
        return

    def __QTextEditSetting(self, txobj:QTextEdit) -> None:
        txobj.setAutoFillBackground(False)
        txobj.setGeometry(QtCore.QRect(0, 0, 150, 25))
        txobj.setMinimumSize(QtCore.QSize(150, 25))
        txobj.setMaximumSize(QtCore.QSize(150, 25))
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
        self.__addTitleSetting(form_layout,rowIndex)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb0Index, self.txRb0Comment, self.txRb0UserPassword, self.txRb0OwnerPassword, self.cbRb0ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb1Index, self.txRb1Comment, self.txRb1UserPassword, self.txRb1OwnerPassword, self.cbRb1ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb2Index, self.txRb2Comment, self.txRb2UserPassword, self.txRb2OwnerPassword, self.cbRb2ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb3Index, self.txRb3Comment, self.txRb3UserPassword, self.txRb3OwnerPassword, self.cbRb3ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb4Index, self.txRb4Comment, self.txRb4UserPassword, self.txRb4OwnerPassword, self.cbRb4ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb5Index, self.txRb5Comment, self.txRb5UserPassword, self.txRb5OwnerPassword, self.cbRb5ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb6Index, self.txRb6Comment, self.txRb6UserPassword, self.txRb6OwnerPassword, self.cbRb6ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb7Index, self.txRb7Comment, self.txRb7UserPassword, self.txRb7OwnerPassword, self.cbRb7ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb8Index, self.txRb8Comment, self.txRb8UserPassword, self.txRb8OwnerPassword, self.cbRb8ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb9Index, self.txRb9Comment, self.txRb9UserPassword, self.txRb9OwnerPassword, self.cbRb9ProHidden)
        rowIndex += 1
        self.__addWidgetSetting(form_layout, rowIndex, self.lbRb10Index, self.txRb10Comment, self.txRb10UserPassword, self.txRb10OwnerPassword, self.cbRb10ProHidden)
        
        rowIndex = rowIndex + 4
        form_layout.addWidget(self.btExecution, rowIndex, 6, 2, 3)
        self.setLayout(form_layout)
        self.setGeometry(QtCore.QRect(100, 100, 650, 450))
        self.setMinimumSize(QtCore.QSize(650, 450))
        self.setMaximumSize(QtCore.QSize(650, 450))
        return

    def __addTitleSetting(self, form_layout:QGridLayout,rowIndex:int) -> None:
        colIndex = 0
        withLength = 1
        form_layout.addWidget(self.lbRbIndex, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        withLength = 5
        form_layout.addWidget(self.lbRbComment, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        withLength = 3
        form_layout.addWidget(self.lbRbUserPassword, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        form_layout.addWidget(self.lbRbOwnerPassword, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        withLength = 1
        form_layout.addWidget(self.lbRbProHidden, rowIndex,colIndex,1,withLength)
        return 

    def __addWidgetSetting(self,form_layout:QGridLayout, rowIndex:int,
                           lbIndex:QLabel, txComment:QTextEdit,
                           txUserPassword:QTextEdit, txOwnerPassword:QTextEdit,
                           cbProHidden:QCheckBox) -> None:
        colIndex = 0
        withLength = 1
        form_layout.addWidget(lbIndex, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        withLength = 5
        form_layout.addWidget(txComment, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        withLength = 3
        form_layout.addWidget(txUserPassword, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        form_layout.addWidget(txOwnerPassword, rowIndex,colIndex,1,withLength)
        colIndex += withLength
        withLength = 1
        form_layout.addWidget(cbProHidden, rowIndex,colIndex,1,withLength)
        return 
