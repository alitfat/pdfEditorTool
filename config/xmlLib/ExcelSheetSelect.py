import copy,os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget,QListWidgetItem
from PyQt5.QtGui import QDropEvent, QCloseEvent

from GUI.pdfEditerToolGUI_ExcelSheetSelect import pdfEditorTool_ExcelSheetSelectGUI
from config.xmlLib.ExcelSheetSelectConfig import ExcelSheetSelectConfig

from Lib.QtLib import qtListWidget

class ExcelSheetSelect(pdfEditorTool_ExcelSheetSelectGUI):

    excelFileAddr : str =""
    excelFileSheetList:dict[str, bool] = {}
    excelFileSheetList_old:dict[str, bool] = {}
    excelSelectedSheetList: list[str] = [] 


    def __init__(self, parent=None):
        super(ExcelSheetSelect, self).__init__(parent)
        self.qtListWidget = qtListWidget()
        self.ExcelSheetSelectConfig = ExcelSheetSelectConfig(os.getcwd() + "\\config", self)
        self.ExcelSheetSelectConfig.getConfigSetting()
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
        #ドラッグ処理で【Excelファイルシートリスト】更新
        self.lstExcelSheet.dragEnterEvent = lambda event:self.qtListWidget.DragEnterEvent(event)
        self.lstExcelSheet.dropEvent = lambda event:self.QListWidget_DragEvent_GetExcelSheetItemList(event)
        
        #ドラッグ処理で【選択されたシートリスト】更新
        self.lstSelectedSheet.dragEnterEvent = lambda event:self.qtListWidget.DragEnterEvent(event)
        self.lstSelectedSheet.dropEvent = lambda event:self.QListWidget_DragEvent_GetSelectedItemList(self.lstSelectedSheet, event)
        return
    

    def QListWidget_DragEvent_GetExcelSheetItemList(self, event: QDropEvent | None) -> None:
        """
        -----------------------------------------------------------------
        ドラッグ処理：【Excelファイルシートリスト】更新処理\n
        -----------------------------------------------------------------
        """
        self.btdelOneSheet_Click()
        return
    
    
    def QListWidget_DragEvent_GetSelectedItemList(self, listobj: QListWidget, event: QDropEvent| None) -> None:
        """
        -----------------------------------------------------------------
        ドラッグ処理：【選択されたシートリスト】更新処理\n
        -----------------------------------------------------------------
        """
        if event is None:
            return
        index2Data = listobj.itemAt(event.pos())
        index2 = listobj.row(index2Data)
        
        if index2 == -1:
            #【Excelファイルシートリスト】から【選択されたシートリスト】へ更新
            self.btAddOneSheet_Click()
        else:
            #【選択されたシートリスト】リスト順置換処理
            self.QListWidget_DragEvent_ExchangeSelectedItemList(listobj, event)
        self.button_update()
        return
    
    
    def QListWidget_DragEvent_ExchangeSelectedItemList(self, listobj: QListWidget, e: QDropEvent) -> None:
        """
        -----------------------------------------------------------------
        ドラッグ処理：QListWidgetリスト順置換処理\n
        -----------------------------------------------------------------
        """
        #print(f'x= {str(e.pos().x())} y= {str(e.pos().y())}')
        indexData = listobj.itemAt(e.pos())
        insertIndex: int = listobj.row(indexData)
        
        selectedItemList:dict[str, int] = {}
        sortedItemList:list[tuple[str, int]] = []
        
        for selectedItem  in reversed(listobj.selectedItems()) :
            selectedItemList[selectedItem.text()] = listobj.row(selectedItem)
        sortedItemList = sorted(selectedItemList.items(), key=lambda x:x[0])
        
        for  sortedItem in sortedItemList:
            selectedText = sortedItem[0]
            curItem = listobj.findItems(selectedText, Qt.MatchFlag.MatchExactly)
            selectedIndex = listobj.row(curItem[0])
            listobj.removeItemWidget(listobj.takeItem(selectedIndex))
            if insertIndex == -1:
                listobj.addItem(selectedText)
            elif insertIndex > selectedIndex :
                listobj.insertItem(insertIndex, selectedText)
            else :
                listobj.insertItem(insertIndex, selectedText)
                insertIndex = insertIndex + 1
        return
    
    
    def guiSlotConnect(self) -> None:
        """
        -----------------------------------------------------------------
        ExcelSheetSelect スロットコネクト処理\n
        -----------------------------------------------------------------
        """
        self.lstExcelSheet.itemClicked.connect(self.lstExcelSheet_itemClicked)
        self.lstSelectedSheet.itemClicked.connect(self.lstSelectedSheet_itemClicked)
        
        self.btAddAllSheet.clicked.connect(self.btAddAllSheet_Click)
        self.btAddOneSheet.clicked.connect(self.btAddOneSheet_Click)
        self.btdelOneSheet.clicked.connect(self.btdelOneSheet_Click)
        self.btdelAllSheet.clicked.connect(self.btdelAllSheet_Click)
        self.btExecution.clicked.connect(self.btExecution_Click)
        return
    

    def closeEvent(self, event: QCloseEvent|None ):
        """
        -----------------------------------------------------------------
        ExcelSheetSelect closeEvent処理\n
        -----------------------------------------------------------------
        """
        self.excelFileSheetList = copy.deepcopy( self.excelFileSheetList_old )
        
        self.lstExcelSheet.clear()
        for sheetName, flg in self.excelFileSheetList.items():
            if (flg == False ):
                self.lstExcelSheet.addItem(sheetName)
        
        self.lstSelectedSheet.clear()
        for sheetName in self.excelSelectedSheetList:
            self.lstSelectedSheet.addItem(sheetName)
        return
    
    def lstExcelSheet_itemClicked(self) -> None:
        self.button_update()
        return
    
    def lstSelectedSheet_itemClicked(self) -> None:
        self.button_update()
        return
    
    def btAddAllSheet_Click(self) -> None:
        textList:dict[str, int] = {}
        self.getListWidgetItemText(self.lstExcelSheet, textList)
        
        for sheetName, item1 in textList.items():
            self.lstSelectedSheet.addItem(sheetName)
            self.excelFileSheetList[sheetName] = True
        
        self.lstExcelSheet.clear()
        self.button_update()
        return
    
    def btAddOneSheet_Click(self, e: QDropEvent|None = None) -> None:
        
        sheetNameList: list[str] = []
        item1IndexList: list[int] = []
        item1Data: QListWidgetItem|None
        
        item1List = self.lstExcelSheet.selectedItems()
        for item1obj in item1List:
            sheetName = item1obj.text()
            sheetNameList.append(sheetName)
            item1 = self.getInsertExcelFileSheetIndex(sheetName)
            item1IndexList.append(item1)  
        item1IndexList.sort()
        
        for item1 in item1IndexList:
            item1Data = self.lstExcelSheet.item(item1)
            if item1Data is None:
                continue
            sheetName = item1Data.text()
            self.excelFileSheetList_Update(sheetName, True)
            self.lstSelectedSheet.addItem(sheetName)
            sheetNameList.append(sheetName)
        
        count: int = self.lstExcelSheet.count()
        for item1 in reversed( range(count) ) :
            item1Data = self.lstExcelSheet.item(item1)
            if item1Data is None:
                continue
            item1_text = item1Data.text()
            for sheetName in sheetNameList :
                if (item1_text == sheetName ):
                    self.lstExcelSheet.removeItemWidget(self.lstExcelSheet.takeItem(item1))
                    break
            
        self.button_update()
        return
    
    def btdelOneSheet_Click(self) -> None:
        
        sheetNameList: list[str] = []
        item2List = self.lstSelectedSheet.selectedItems()
        
        for item2obj in item2List:
            sheetName = item2obj.text()
            self.excelFileSheetList_Update(sheetName, False)
            item1 = self.getInsertExcelFileSheetIndex(sheetName)
            self.lstExcelSheet.insertItem(item1, sheetName)
            sheetNameList.append(sheetName)
        
        textList:dict[str, int] = {}
        self.getListWidgetItemText(self.lstSelectedSheet, textList)
        
        for item2_text, item2 in reversed( textList.items() ) :
            for sheetName in sheetNameList :
                if (item2_text == sheetName ):
                    self.lstSelectedSheet.removeItemWidget(self.lstSelectedSheet.takeItem(item2))
                    break
            
        self.button_update()
        return
    
    def btdelAllSheet_Click(self) -> None:
        
        textList:dict[str, int] = {}
        self.getListWidgetItemText(self.lstSelectedSheet, textList)
        
        for sheetName, item2 in textList.items():
            item1 = self.getInsertExcelFileSheetIndex(sheetName)
            self.lstExcelSheet.insertItem(item1, sheetName)
            self.excelFileSheetList_Update(sheetName, False)
        self.lstSelectedSheet.clear()
        self.button_update()
        return


    def btExecution_Click(self) -> None:
        self.ExcelSheetSelectConfig.updateConfigSetting()
        self.ExcelSheetSelectConfig.outputConfigSetting()
        self.hide()
        return


    def button_update(self) -> None:
        
        if self.lstExcelSheet.count() == 0 :
            self.btAddAllSheet.setEnabled(False)
        else :
            self.btAddAllSheet.setEnabled(True)

        if len(self.lstExcelSheet.selectedItems()) == 0 :
            self.btAddOneSheet.setEnabled(False)
        else :
            self.btAddOneSheet.setEnabled(True)
            
        if len(self.lstSelectedSheet.selectedItems())  == 0  :
            self.btdelOneSheet.setEnabled(False)
        else :
            self.btdelOneSheet.setEnabled(True)
               
        if self.lstSelectedSheet.count() == 0 :
            self.btdelAllSheet.setEnabled(False)
        else :
            self.btdelAllSheet.setEnabled(True)
        return


    def showGUI(self, excelFileAddr :str ="", excelFileSheetList : list[str] =[]) -> None:
        self.ExcelSheetSelectConfig.updateGUISetting()
        self.showGUIInit(excelFileAddr, excelFileSheetList)

        self.excelFileSheetList_old = copy.deepcopy(self.excelFileSheetList)
        self.excelSelectedSheetList.clear()
        
        textList:dict[str, int] = {}
        self.getListWidgetItemText(self.lstSelectedSheet, textList)
        
        for sheetName, item2 in textList.items():
            self.excelSelectedSheetList.append(sheetName)

        flags = self.windowFlags()
        self.setWindowFlags( flags | Qt.WindowType.WindowStaysOnTopHint)
        self.show()
        return


    def showGUIInit(self, excelFileAddr :str ="", excelFileSheetList : list[str] =[]) -> None: 
        self.txFileAddr.setText(excelFileAddr)
        self.excelFileSheetList_init(excelFileSheetList )
        textList:dict[str, int] = {}
        self.getListWidgetItemText(self.lstSelectedSheet, textList)
        
        for sheetName, item2 in reversed(textList.items()):
            bResult = self.excelFileSheetList_Update(sheetName, True) 
            if (bResult == False ):
                self.lstSelectedSheet.removeItemWidget(self.lstSelectedSheet.takeItem(item2))
        
        self.lstExcelSheet_init( ) 
        self.button_update()
        return

    
    def getInsertExcelFileSheetIndex(self, curSheetName : str) -> int :
        sheetIndex : int = 0
        for sheetName, flg in self.excelFileSheetList.items():
            if (sheetName != curSheetName ):
                if (flg == False ):
                    sheetIndex += 1
            else :
                break
        return sheetIndex
    
    
    def excelFileSheetList_init(self, excelFileSheetList : list[str] ) -> None:
        self.excelFileSheetList.clear()
        for sheetName in excelFileSheetList :
            self.excelFileSheetList[sheetName] = False
        return


    def excelFileSheetList_Update(self, curSheetName : str, curFlg : bool) -> bool :
        bResult : bool = False
        for sheetName, flg in self.excelFileSheetList.items():
            if (curSheetName == sheetName ):
                self.excelFileSheetList[curSheetName] = curFlg
                bResult = True
        return bResult
    
    
    def lstExcelSheet_init(self) -> None:
        self.lstExcelSheet.clear()
        for sheetName, flg in self.excelFileSheetList.items():
            if (flg == False ):
                self.lstExcelSheet.addItem(sheetName)
        return


    def getSelectSheetList(self, excelFileAddr:str = "", excelFileSheetList : list[str] =[], selectedSheetList : list[str] =[]) -> None:
        self.showGUIInit(excelFileAddr, excelFileSheetList)
        selectedSheetList.clear()
        textList:dict[str, int] = {}
        self.getListWidgetItemText(self.lstSelectedSheet, textList)
        for sheetName, item2 in textList.items():
            selectedSheetList.append(sheetName)
        return


    def getListWidgetItemText(self,objListWidgetItem:QListWidget, textList:dict[str, int]) -> None:
        itemData: QListWidgetItem|None
        textList.clear()
        count: int = objListWidgetItem.count()
        for itemIndex in range(count) :
            itemData = objListWidgetItem.item(itemIndex)
            if itemData is None:
                continue
            textList[itemData.text()] = itemIndex
        return
        