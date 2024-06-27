import typing, os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from pypdf.constants import DocumentInformationAttributes as pdfDocInfoAttr

from GUI.pdfEditerToolGUI_PdfInfoSetting import pdfEditorTool_PdfInfoSetting
from config.xmlLib.pdfInfoConfig import pdfInfoConfig

class PdfInfoSetting(pdfEditorTool_PdfInfoSetting):

    def __init__(self, parent=None):
        super(PdfInfoSetting, self).__init__(parent)
        self.setui()
        self.pdfInfoConfig = pdfInfoConfig(os.getcwd() + "\\config", self)
        self.pdfInfoConfig.getConfigSetting()
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
        PdfInfoSetting スロットコネクト処理\n
        -----------------------------------------------------------------
        """
        #cbTitle
        self.cbTitle.toggled.connect(self.cbTitle_Click)
        #cbSubject
        self.cbSubject.toggled.connect(self.cbSubject_Click)
        #cbAuthor
        self.cbAuthor.toggled.connect(self.cbAuthor_Click)
        #cbKeywords
        self.cbKeywords.toggled.connect(self.cbKeywords_Click)
        #cbProducer
        self.cbProducer.toggled.connect(self.cbProducer_Click)
        #cbCreator
        self.cbCreator.toggled.connect(self.cbCreator_Click)
        
        self.btExecution.clicked.connect(self.btExecution_Click)
        
        return
    
    def cbTitle_Click(self) -> None:
        """
        -----------------------------------------------------------------
        cbTitle(タイトル) クリック処理\n
        -----------------------------------------------------------------
        """
        if self.cbTitle.isChecked():
            self.txTitle.setEnabled(True)
        else:
            self.txTitle.setEnabled(False)
        return
    
    def cbSubject_Click(self) -> None:
        """
        -----------------------------------------------------------------
        cbSubject(件名) クリック処理\n
        -----------------------------------------------------------------
        """
        if self.cbSubject.isChecked():
            self.txSubject.setEnabled(True)
        else:
            self.txSubject.setEnabled(False)
        return
    
    def cbAuthor_Click(self) -> None:
        """
        -----------------------------------------------------------------
        cbAuthor(作成者)  クリック処理\n
        -----------------------------------------------------------------
        """
        if self.cbAuthor.isChecked():
            self.txAuthor.setEnabled(True)
        else:
            self.txAuthor.setEnabled(False)
        return

    def cbKeywords_Click(self) -> None:
        """
        -----------------------------------------------------------------
        cbKeywords(タグ) クリック処理\n
        -----------------------------------------------------------------
        """
        if self.cbKeywords.isChecked():
            self.txKeywords.setEnabled(True)
        else:
            self.txKeywords.setEnabled(False)
        return
    
    def cbProducer_Click(self) -> None:
        """
        -----------------------------------------------------------------
        cbProducer(Producer) クリック処理\n
        -----------------------------------------------------------------
        """
        if self.cbProducer.isChecked():
            self.txProducer.setEnabled(True)
        else:
            self.txProducer.setEnabled(False)
        return
    
    def cbCreator_Click(self) -> None:
        """
        -----------------------------------------------------------------
        cbCreator(Creator) クリック処理\n
        -----------------------------------------------------------------
        """
        if self.cbCreator.isChecked():
            self.txCreator.setEnabled(True)
        else:
            self.txCreator.setEnabled(False)
        return
    
    def closeEvent(self, event: QCloseEvent|None ):
        """
        -----------------------------------------------------------------
        PdfInfoSetting closeEvent処理\n
        -----------------------------------------------------------------
        """
        self.btExecution_Click()
        return

    def showGUI(self) -> None:
        self.pdfInfoConfig.updateGUISetting()
        flags = self.windowFlags()
        self.setWindowFlags( flags | Qt.WindowType.WindowStaysOnTopHint)
        self.show()
        return

    def btExecution_Click(self) -> None:
        self.pdfInfoConfig.updateConfigSetting()
        self.pdfInfoConfig.outputConfigSetting()
        self.hide()
        return
    
    def getPdfMetadata(self) -> dict[typing.Any, typing.Any]:
        """
        -----------------------------------------------------------------
        PdfInfoSetting PdfInfomation取得処理\n
        -----------------------------------------------------------------
        """
        self.pdfInfoConfig.updateGUISetting()
        metadata:dict[typing.Any, typing.Any]= {}
        #タイトル
        if self.cbTitle.isChecked():
            metadata[pdfDocInfoAttr.TITLE] = self.txTitle.toPlainText()
        #件名
        if self.cbSubject.isChecked(): 
            metadata[pdfDocInfoAttr.SUBJECT] = self.txSubject.toPlainText()
        #作成者
        if self.cbAuthor.isChecked():  
            metadata[pdfDocInfoAttr.AUTHOR] = self.txAuthor.toPlainText()
        #タグ
        if self.cbKeywords.isChecked(): 
            metadata[pdfDocInfoAttr.KEYWORDS] = self.txKeywords.toPlainText()
        #Producer
        if self.cbProducer.isChecked(): 
            metadata[pdfDocInfoAttr.PRODUCER] = self.txProducer.toPlainText()
        #Creator
        if self.cbCreator.isChecked(): 
            metadata[pdfDocInfoAttr.CREATOR] = self.txCreator.toPlainText()

        return metadata
    
    