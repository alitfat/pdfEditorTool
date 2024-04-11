import copy

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QListWidget, QPushButton, QAbstractItemView, QGridLayout

class pdfEditorTool_ExcelSheetSelectGUI(QWidget):
    
    def __init__(self, parent=None):
        super(pdfEditorTool_ExcelSheetSelectGUI, self).__init__(parent)
        self.setWindowTitle("Excelファイルシート選択パネル")
        self.ui()
    
    
    # UI作成
    def ui(self) -> None:
        self.main_design()
        self.layouts()
    
    # UI画面Widget作成
    def main_design(self) -> None:
        
        self.lbFileAddr = QLabel("Excelファイルアドレス：")
        self.lbFileAddr.setStyleSheet("font-weight:bold;")
        self.txFileAddr = QLabel("")
        
        self.cbOneSheet = QCheckBox("シート毎にpdf出力(未実装)")
        self.cbOneSheet.setEnabled(False)
        
        self.lbExcelSheet = QLabel("Excelファイルシートリスト")
        self.lbExcelSheet.setStyleSheet("font-weight:bold;")
        self.lstExcelSheet = QListWidget()
        
        self.btAddAllSheet = QPushButton(">>\n(AddAllSheets)", self)
        self.btAddOneSheet = QPushButton(">\n(AddSheets)", self)
        self.btdelOneSheet = QPushButton("<\n(DelSheets)", self)
        self.btdelAllSheet = QPushButton("<<\n(DelAllSheets)", self)
        
        self.lbSelectedSheet = QLabel("選択されたシートリスト")
        self.lbSelectedSheet.setStyleSheet("font-weight:bold;")
        self.lstSelectedSheet = QListWidget()
        
        self.btExecution = QPushButton("確定", self)
        self.btExecution.setStyleSheet("font-weight:bold;font-size:25px;")
        
        self.lstExcelSheet.setAcceptDrops(True)
        self.lstExcelSheet.setDragEnabled(True)
        self.lstExcelSheet.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.lstExcelSheet.setDefaultDropAction(Qt.DropAction.CopyAction)
        self.lstExcelSheet.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        
        self.lstSelectedSheet.setAcceptDrops(True)
        self.lstSelectedSheet.setDragEnabled(True)
        self.lstSelectedSheet.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.lstSelectedSheet.setDefaultDropAction(Qt.DropAction.CopyAction)
        self.lstSelectedSheet.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        
        
    
    # UI画面layout設定
    def layouts(self) -> None:
        form_layout = QGridLayout()
        rowIndex = 0
        form_layout.addWidget(self.lbFileAddr, rowIndex,0,1,1)
        form_layout.addWidget(self.txFileAddr, rowIndex,1,1,3)
        
        rowIndex = rowIndex + 4
        form_layout.addWidget(self.cbOneSheet, rowIndex,3,1,2)
        
        rowIndex = rowIndex + 1
        listCount = 32
        form_layout.addWidget(self.lbExcelSheet,   rowIndex + 0, 0,         1, 2)
        form_layout.addWidget(self.lstExcelSheet,  rowIndex + 1, 0, listCount, 2)
        
        form_layout.addWidget(self.lbSelectedSheet,  rowIndex + 0, 3,         1, 2)
        form_layout.addWidget(self.lstSelectedSheet, rowIndex + 1, 3, listCount, 2)
        
        form_layout.addWidget(self.btAddAllSheet,rowIndex + 2 , 2)
        form_layout.addWidget(self.btAddOneSheet,rowIndex + 3 , 2)
        form_layout.addWidget(self.btdelOneSheet,rowIndex + listCount - 4, 2)
        form_layout.addWidget(self.btdelAllSheet,rowIndex + listCount - 2, 2)
        
        rowIndex = rowIndex + listCount + 6
        
        form_layout.addWidget(self.btExecution, rowIndex, 2, 3, 1)
        
        self.setLayout(form_layout)
    
    
