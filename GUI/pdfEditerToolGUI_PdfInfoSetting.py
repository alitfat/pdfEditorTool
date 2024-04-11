from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QPushButton,QCheckBox, QGridLayout

class pdfEditorTool_PdfInfoSetting(QWidget):
    
    def __init__(self, parent=None):
        """
        -----------------------------------------------------------------
        PDF情報設定GUI\n
        -----------------------------------------------------------------
        """
        super(pdfEditorTool_PdfInfoSetting, self).__init__(parent)
        self.setWindowTitle("PDF Information")
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
        self.lbTitle = QLabel("Title:")
        self.lbSubject = QLabel("Subject:")
        self.lbAuthor = QLabel("Author:")
        self.lbKeywords = QLabel("Keywords:")
        self.lbProducer = QLabel("Producer:")
        self.lbCreator = QLabel("Creator:")

        self.txTitle = QTextEdit("")
        self.__QTextEditSetting(self.txTitle)

        self.txSubject = QTextEdit("")
        self.__QTextEditSetting(self.txSubject)

        self.txAuthor = QTextEdit("")
        self.__QTextEditSetting(self.txAuthor)

        self.txKeywords = QTextEdit("")
        self.__QTextEditSetting(self.txKeywords)

        self.txProducer = QTextEdit("")
        self.__QTextEditSetting(self.txProducer)

        self.txCreator = QTextEdit("")
        self.__QTextEditSetting(self.txCreator)

        self.cbTitle = QCheckBox("select")
        self.__QCheckBoxSetting(self.cbTitle)
        
        self.cbSubject = QCheckBox("select")
        self.__QCheckBoxSetting(self.cbSubject)

        self.cbAuthor = QCheckBox("select")
        self.__QCheckBoxSetting(self.cbAuthor)

        self.cbKeywords = QCheckBox("select")
        self.__QCheckBoxSetting(self.cbKeywords)

        self.cbProducer = QCheckBox("select")
        self.__QCheckBoxSetting(self.cbProducer)
        
        self.cbCreator = QCheckBox("select")
        self.__QCheckBoxSetting(self.cbCreator)

        self.btExecution = QPushButton("OK", self)
        self.btExecution.setStyleSheet("font-weight:bold;font-size:25px;")
        return

    def __QTextEditSetting(self, txobj:QTextEdit) -> None:
        txobj.setAutoFillBackground(False)
        txobj.setGeometry(QtCore.QRect(0, 0, 400, 30))
        txobj.setMinimumSize(QtCore.QSize(400, 30))
        txobj.setMaximumSize(QtCore.QSize(400, 30))
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
        self.__addWidgetSetting(rowIndex, form_layout, self.lbTitle, self.txTitle, self.cbTitle)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.lbSubject, self.txSubject, self.cbSubject)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.lbAuthor, self.txAuthor, self.cbAuthor)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.lbKeywords, self.txKeywords, self.cbKeywords)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.lbProducer, self.txProducer, self.cbProducer)
        rowIndex += 1
        self.__addWidgetSetting(rowIndex, form_layout, self.lbCreator, self.txCreator, self.cbCreator)

        rowIndex = rowIndex + 2
        form_layout.addWidget(self.btExecution, rowIndex, 3, 2, 3)
        self.setLayout(form_layout)
        self.setGeometry(QtCore.QRect(100, 100, 600, 300))
        self.setMinimumSize(QtCore.QSize(600, 300))
        self.setMaximumSize(QtCore.QSize(600, 300))
        return

    def __addWidgetSetting(self,rowIndex:int,form_layout:QGridLayout, lbobj:QLabel, txobj:QTextEdit, cbobj:QCheckBox) -> None:
        form_layout.addWidget(lbobj, rowIndex,0,1,1)
        form_layout.addWidget(txobj, rowIndex,1,1,8)
        form_layout.addWidget(cbobj, rowIndex,9,1,2)
        return 
