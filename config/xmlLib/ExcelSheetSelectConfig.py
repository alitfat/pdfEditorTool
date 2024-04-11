import xml.etree.ElementTree as ET
from xml.etree.ElementTree import  ElementTree,Element
from config.xmlLib.xmlLib import xmlLib
from config.xmlLib.xmlQtLib import xmlQWidget, xmlQTextEdit,xmlQLabel,xmlQPushButton, xmlQCheckBox, xmlQListWidget
from GUI.pdfEditerToolGUI_ExcelSheetSelect import pdfEditorTool_ExcelSheetSelectGUI as ExcelSheetSelecttUI

from Lib.FileSysProcess import FileSysProcess

class toolNameLib(xmlLib):
    #ツール名称
    widTool:xmlQWidget
    """ toolName Setting"""
    def __init__(self)-> None:
 
        super(toolNameLib, self).__init__()

        #ツール名称
        self.toolName = "widTool" 
        self.toolTitle = "ExcelSheetSelectSetting"
        self.createConfigSetting()
        return

    def createConfigSetting(self) -> None:
        #ツール名称
        self.widTool = xmlQWidget(self.toolName, self.toolTitle)
        return

    def getConfigSetting(self, eleTool:Element|None)-> None:

        if eleTool is None :
            return
        
        #ツール名称
        self.widTool.getConfigSetting(eleTool, self.toolName)
        return
    
    def outputConfigSetting(self, eleTool:Element)-> None:
        comment = ET.Comment('ツール名称設定')
        eleTool.append(comment)
        self.widTool.outputConfigSetting(eleTool)
        return
       
    def updateConfigSetting(self, Ui:ExcelSheetSelecttUI) -> None:
        toolNameText = Ui.windowTitle()
        self.widTool.modifyLabelProperty('WindowTitle', toolNameText)
        return
    
    def updateGUISetting(self, Ui:ExcelSheetSelecttUI) -> None:
        toolNameText = self.widTool.getLabelValue('WindowTitle')
        Ui.setWindowTitle(toolNameText)
        return

class actionToolList(xmlLib):

    #タイトル
    #lbFileAddr(Excelファイルアドレス)
    lbFileAddr:xmlQLabel
    #txFileAddr(Excelファイルアドレス)
    txFileAddr:xmlQTextEdit
    #cbOneSheet(シート毎にpdf出力)
    cbOneSheet:xmlQCheckBox

    
    #シート選択設定
    #lbExcelSheet(Excelファイルシートリスト)
    lbExcelSheet:xmlQLabel
    #lstExcelSheet(Excelファイルシートリスト)
    lstExcelSheet:xmlQListWidget
    lstExcelSheetList:dict[str, str] = {}
    
    #btAddAllSheet(全シート選択)
    btAddAllSheet:xmlQPushButton
    #btAddOneSheet(一つシート選択)
    btAddOneSheet:xmlQPushButton
    #btdelOneSheet(一つシート削除)
    btdelOneSheet:xmlQPushButton
    #btdelAllSheet(全シート削除)
    btdelAllSheet:xmlQPushButton
    
    #lbSelectedSheet(選択されたシートリスト)
    lbSelectedSheet:xmlQLabel
    #lstSelectedSheet(Excelファイルシートリスト)
    lstSelectedSheet:xmlQListWidget
    lstSelectedSheetList:dict[str, str] = {}
    
    #btExecution(確定)
    btExecution:xmlQPushButton
    
    def __init__(self)-> None:
        super(actionToolList, self).__init__()
        #タイトル設定
        self.__init_title()

        #シート選択設定
        self.__init_SelectList()

        #btExecution(確定)
        self.__init_Execution()

        self.clearConfigSetting()
        self.createConfigSetting()
        return
        
    def clearConfigSetting(self) -> None:
        return

    def createConfigSetting(self) -> None:
        #タイトル設定
        self.__createConfigSetting_title()

        #シート選択設定
        self.__createConfigSetting_SelectList()
        
        #btExecution(確定)
        self.__createConfigSetting_Execution()
        return
        
        
    def getConfigSetting(self, eleActionTool:Element|None)-> None:
        if eleActionTool is None :
            return
        #タイトル設定
        self.__getConfigSetting_title(eleActionTool)

        #シート選択設定
        self.__getConfigSetting_SelectList(eleActionTool)

        #btExecution(確定)
        self.__getConfigSetting_Execution(eleActionTool)
        return
        
    def outputConfigSetting(self, eleActionTool:Element) -> None:
        #タイトル設定
        self.__outputConfigSetting_title(eleActionTool)

        #シート選択設定
        self.__outputConfigSetting_SelectList(eleActionTool)

        #btExecution(確定)
        self.__outputConfigSetting_Execution(eleActionTool)
        return
    
    def updateConfigSetting(self, Ui:ExcelSheetSelecttUI) -> None:
        #タイトル設定
        self.__updateConfigSetting_title(Ui)

        #シート選択設定
        self.__updateConfigSetting_SelectList(Ui)

        #btExecution(確定)
        self.__updateConfigSetting_Execution(Ui)
        return
    
    def updateGUISetting(self, Ui:ExcelSheetSelecttUI) -> None:
        #タイトル設定
        self.__updateGUISetting_title(Ui)

        #シート選択設定
        self.__updateGUISetting_SelectList(Ui)

        #btExecution(確定)
        self.__updateGUISetting_Execution(Ui)
        return

    def __init_title(self) -> None:
        #lbFileAddr(Excelファイルアドレス)
        self.lbFileAddrName = "lbFileAddr" 
        self.lbFileAddrText = "Index"
        self.lbFileAddrHidden = False

        #txFileAddr(Excelファイルアドレス)
        self.txFileAddrName = "txFileAddr"
        self.txFileAddrText = ""
        self.txFileAddrEnabled = True
        self.txFileAddrHidden = False

        #cbOneSheet(シート毎にpdf出力)
        self.cbOneSheetName = "cbOneSheet"
        self.cbOneSheetText = "select"
        self.cbOneSheetChecked = False
        self.cbOneSheetEnabled = True
        self.cbOneSheetHidden = False
        
        return

    def __createConfigSetting_title(self) -> None:
        
        #lbFileAddr(Excelファイルアドレス)
        self.lbFileAddr = xmlQLabel(self.lbFileAddrName,
                                    self.lbFileAddrText,
                                    self.lbFileAddrHidden)
        
        #txFileAddr(Excelファイルアドレス)
        self.txFileAddr = xmlQTextEdit(self.txFileAddrName,
                                       self.txFileAddrText,
                                       self.txFileAddrEnabled,
                                       self.txFileAddrHidden)
        self.txFileAddr.delLabelProperty("Text")
        
        #cbOneSheet(シート毎にpdf出力)
        self.cbOneSheet = xmlQCheckBox(self.cbOneSheetName, 
                                       self.cbOneSheetText,
                                       self.cbOneSheetChecked,
                                       self.cbOneSheetEnabled,
                                       self.cbOneSheetHidden)

        return
    
    def __getConfigSetting_title(self, eleActionTool:Element)-> None:

        #lbFileAddr(Excelファイルアドレス)
        self.lbFileAddr.getConfigSetting(eleActionTool, self.lbFileAddrName)
        
        #txFileAddr(Excelファイルアドレス)
        self.txFileAddr.getConfigSetting(eleActionTool, self.txFileAddrName)
        
        #cbOneSheet(シート毎にpdf出力)
        self.cbOneSheet.getConfigSetting(eleActionTool, self.cbOneSheetName)

        return
    
    def __outputConfigSetting_title(self, eleActionTool:Element) -> None:

        #lbFileAddr(Excelファイルアドレス)
        self.lbFileAddr.outputConfigSetting(eleActionTool)
        
        #txFileAddr(Excelファイルアドレス)
        self.txFileAddr.outputConfigSetting(eleActionTool)
        
        #cbOneSheet(シート毎にpdf出力)
        self.cbOneSheet.outputConfigSetting(eleActionTool)

        return
    
    def __updateConfigSetting_title(self, Ui:ExcelSheetSelecttUI) -> None:
        
        #lbFileAddr(Excelファイルアドレス)
        self.lbFileAddr.updateConfigSetting(Ui.lbFileAddr)
        #txFileAddr(Excelファイルアドレス)
        self.txFileAddr.updateConfigSetting(Ui.txFileAddr)
        #cbOneSheet(シート毎にpdf出力)
        self.cbOneSheet.updateConfigSetting(Ui.cbOneSheet)

        return
    
    def __updateGUISetting_title(self, Ui:ExcelSheetSelecttUI) -> None:
    
        #lbFileAddr(Excelファイルアドレス)
        self.lbFileAddr.updateGUISetting(Ui.lbFileAddr)
        #txFileAddr(Excelファイルアドレス)
        self.txFileAddr.updateGUISetting(Ui.txFileAddr)
        #cbOneSheet(シート毎にpdf出力)
        self.cbOneSheet.updateGUISetting(Ui.cbOneSheet)
        return

    def __init_SelectList(self) -> None:
        
        #lbExcelSheet(Excelファイルシートリスト)
        self.lbExcelSheetName = "lbExcelSheet" 
        self.lbExcelSheetText = "ExcelFileSheetsList"
        self.lbExcelSheetHidden = False
        
        #lstExcelSheet(Excelファイルシートリスト)
        self.lstExcelSheetName = "lstExcelSheet"
        self.lstExcelSheetHidden = False
        self.lstExcelSheetList.clear()
        
        #btAddAllSheet(全シート選択)
        self.btAddAllSheetName = "btAddAllSheet"
        self.btAddAllSheetText = ">>\n"
        self.btAddAllSheetEnabled = True
        self.btAddAllSheetHidden = False
        
        #btAddOneSheet(一つシート選択)
        self.btAddOneSheetName = "btAddOneSheet"
        self.btAddOneSheetText = ">"
        self.btAddOneSheetEnabled = True
        self.btAddOneSheetHidden = False
        
        #btdelOneSheet(一つシート削除)
        self.btdelOneSheetName = "btdelOneSheet"
        self.btdelOneSheetText = "<"
        self.btdelOneSheetEnabled = True
        self.btdelOneSheetHidden = False
        
        #btdelAllSheet(全シート削除)
        self.btdelAllSheetName = "btdelAllSheet"
        self.btdelAllSheetText = "<<"
        self.btdelAllSheetEnabled = True
        self.btdelAllSheetHidden = False
        
        #lbSelectedSheet(選択されたシートリスト)
        self.lbSelectedSheetName = "lbSelectedSheet" 
        self.lbSelectedSheetText = "ExcelFileSlectedList"
        self.lbSelectedSheetHidden = False
        
        #lstSelectedSheet(Excelファイルシートリスト)
        self.lstSelectedSheetName = "lstSelectedSheet"
        self.lstSelectedSheetHidden = False
        self.lstSelectedSheetList.clear()
        
        return

    def __createConfigSetting_SelectList(self) -> None:
        
        #lbExcelSheet(Excelファイルシートリスト)
        self.lbExcelSheet = xmlQLabel(self.lbExcelSheetName,
                                      self.lbExcelSheetText,
                                      self.lbExcelSheetHidden)
        
        #lstExcelSheet(Excelファイルシートリスト)
        self.lstExcelSheet = xmlQListWidget(self.lstExcelSheetName,self.lstExcelSheetHidden, self.lstExcelSheetList)
        
        #btAddAllSheet(全シート選択)
        self.btAddAllSheet = xmlQPushButton(self.btAddAllSheetName,
                                            self.btAddAllSheetText,
                                            self.btAddAllSheetEnabled,
                                            self.btAddAllSheetHidden)
        #btAddOneSheet(一つシート選択)
        self.btAddOneSheet = xmlQPushButton(self.btAddOneSheetName,
                                            self.btAddOneSheetText,
                                            self.btAddOneSheetEnabled,
                                            self.btAddOneSheetHidden)
        #btdelOneSheet(一つシート削除)
        self.btdelOneSheet = xmlQPushButton(self.btdelOneSheetName,
                                            self.btdelOneSheetText,
                                            self.btdelOneSheetEnabled,
                                            self.btdelOneSheetHidden)
        #btdelAllSheet(全シート削除)
        self.btdelAllSheet = xmlQPushButton(self.btdelAllSheetName,
                                            self.btdelAllSheetText,
                                            self.btdelAllSheetEnabled,
                                            self.btdelAllSheetHidden)
        
        #lbSelectedSheet(選択されたシートリスト)
        self.lbSelectedSheet = xmlQLabel(self.lbSelectedSheetName,
                                         self.lbSelectedSheetText,
                                         self.lbSelectedSheetHidden)
        
        #lstSelectedSheet(Excelファイルシートリスト)
        self.lstSelectedSheet = xmlQListWidget(self.lstSelectedSheetName,self.lstSelectedSheetHidden, self.lstSelectedSheetList)
        
        return
    
    def __getConfigSetting_SelectList(self, eleActionTool:Element)-> None:

        #lbExcelSheet(Excelファイルシートリスト)
        self.lbExcelSheet.getConfigSetting(eleActionTool, self.lbExcelSheetName)
        #lstExcelSheet(Excelファイルシートリスト)
        self.lstExcelSheet.getConfigSetting(eleActionTool, self.lstExcelSheetName)
        
        #btAddAllSheet(全シート選択)
        self.btAddAllSheet.getConfigSetting(eleActionTool, self.btAddAllSheetName)
        #btAddOneSheet(一つシート選択)
        self.btAddOneSheet.getConfigSetting(eleActionTool, self.btAddOneSheetName)
        #btdelOneSheet(一つシート削除)
        self.btdelOneSheet.getConfigSetting(eleActionTool, self.btdelOneSheetName)
        #btdelAllSheet(全シート削除)
        self.btdelAllSheet.getConfigSetting(eleActionTool, self.btdelAllSheetName)
        
        #lbSelectedSheet(選択されたシートリスト)
        self.lbSelectedSheet.getConfigSetting(eleActionTool, self.lbSelectedSheetName)
        #lstSelectedSheet(Excelファイルシートリスト)
        self.lstSelectedSheet.getConfigSetting(eleActionTool, self.lstSelectedSheetName)
        
        return
    
    def __outputConfigSetting_SelectList(self, eleActionTool:Element) -> None:
        
        #lbExcelSheet(Excelファイルシートリスト)
        self.lbExcelSheet.outputConfigSetting(eleActionTool)
        #lstExcelSheet(Excelファイルシートリスト)
        self.lstExcelSheet.outputConfigSetting(eleActionTool)
        
        #btAddAllSheet(全シート選択)
        self.btAddAllSheet.outputConfigSetting(eleActionTool)
        #btAddOneSheet(一つシート選択)
        self.btAddOneSheet.outputConfigSetting(eleActionTool)
        #btdelOneSheet(一つシート削除)
        self.btdelOneSheet.outputConfigSetting(eleActionTool)
        #btdelAllSheet(全シート削除)
        self.btdelAllSheet.outputConfigSetting(eleActionTool)
        
        #lbSelectedSheet(選択されたシートリスト)
        self.lbSelectedSheet.outputConfigSetting(eleActionTool)
        #lstSelectedSheet(Excelファイルシートリスト)
        self.lstSelectedSheet.outputConfigSetting(eleActionTool)
        
        return
    
    def __updateConfigSetting_SelectList(self, Ui:ExcelSheetSelecttUI) -> None:
           
        #lbExcelSheet(Excelファイルシートリスト)
        self.lbExcelSheet.updateConfigSetting(Ui.lbExcelSheet)
        #lstExcelSheet(Excelファイルシートリスト)
        self.lstExcelSheet.updateConfigSetting(Ui.lstExcelSheet)
        
        #btAddAllSheet(全シート選択)
        self.btAddAllSheet.updateConfigSetting(Ui.btAddAllSheet)
        #btAddOneSheet(一つシート選択)
        self.btAddOneSheet.updateConfigSetting(Ui.btAddOneSheet)
        #btdelOneSheet(一つシート削除)
        self.btdelOneSheet.updateConfigSetting(Ui.btdelOneSheet)
        #btdelAllSheet(全シート削除)
        self.btdelAllSheet.updateConfigSetting(Ui.btdelAllSheet)
        
        #lbSelectedSheet(選択されたシートリスト)
        self.lbSelectedSheet.updateConfigSetting(Ui.lbSelectedSheet)
        #lstSelectedSheet(Excelファイルシートリスト)
        self.lstSelectedSheet.updateConfigSetting(Ui.lstSelectedSheet)
        
        return
    
    def __updateGUISetting_SelectList(self, Ui:ExcelSheetSelecttUI) -> None:
        
        #lbExcelSheet(Excelファイルシートリスト)
        self.lbExcelSheet.updateGUISetting(Ui.lbExcelSheet)
        #lstExcelSheet(Excelファイルシートリスト)
        self.lstExcelSheet.updateGUISetting(Ui.lstExcelSheet)
        
        #btAddAllSheet(全シート選択)
        self.btAddAllSheet.updateGUISetting(Ui.btAddAllSheet)
        #btAddOneSheet(一つシート選択)
        self.btAddOneSheet.updateGUISetting(Ui.btAddOneSheet)
        #btdelOneSheet(一つシート削除)
        self.btdelOneSheet.updateGUISetting(Ui.btdelOneSheet)
        #btdelAllSheet(全シート削除)
        self.btdelAllSheet.updateGUISetting(Ui.btdelAllSheet)
        
        #lbSelectedSheet(選択されたシートリスト)
        self.lbSelectedSheet.updateGUISetting(Ui.lbSelectedSheet)
        #lstSelectedSheet(Excelファイルシートリスト)
        self.lstSelectedSheet.updateGUISetting(Ui.lstSelectedSheet)
        
        return

    def __init_Execution(self) -> None:
        #btExecution(確定)
        self.btExecutionName = "btObjFileName"
        self.btExecutionText = "select"
        self.btExecutionEnabled = True
        self.btExecutionHidden = False
        return

    def __createConfigSetting_Execution(self) -> None:
        
        #btExecution(確定)
        self.btExecution = xmlQPushButton(self.btExecutionName, 
                                          self.btExecutionText, 
                                          self.btExecutionEnabled, 
                                          self.btExecutionHidden)
        return
    
    def __getConfigSetting_Execution(self, eleActionTool:Element)-> None:

        #btExecution(確定)
        self.btExecution.getConfigSetting(eleActionTool,self.btExecutionName)
        return
    
    def __outputConfigSetting_Execution(self, eleActionTool:Element) -> None:
        
        #確定
        comment = ET.Comment('【'+ self.btExecution.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #btExecution(確定)
        self.btExecution.outputConfigSetting(eleActionTool) 
        return
    
    def __updateConfigSetting_Execution(self, Ui:ExcelSheetSelecttUI) -> None:
        
        #btExecution(確定)
        self.btExecution.updateConfigSetting(Ui.btExecution)
        return
    
    def __updateGUISetting_Execution(self, Ui:ExcelSheetSelecttUI) -> None:
    
        #btExecution(確定)
        self.btExecution.updateGUISetting(Ui.btExecution)
        return

    def print(self) :
        return
        
class ExcelSheetSelectConfig():
    
    def __init__(self, configFileAddress:str, ui:ExcelSheetSelecttUI)-> None:
        super(ExcelSheetSelectConfig, self).__init__()
        self.FSP = FileSysProcess()
        self.CreateFileAddress = configFileAddress + "\\config3.xml"
        if self.FSP.judgeFileExsit(self.CreateFileAddress) :
            self.configFileAddress = self.CreateFileAddress
        else :
            self.configFileAddress = configFileAddress + "\\Jp\\ExcelSheetSelectSetting_Jp.xml"
        
        self.toolName = toolNameLib()
        self.ui = ui
        self.actionToolList = actionToolList()
        return
        
    def getConfigSetting(self) -> bool:
        bResult = True
        try:
            tree = ET.parse(self.configFileAddress)
            eleEncryptListGUI =  tree.getroot()
            eleTool = eleEncryptListGUI.find("ToolName")
            self.toolName.getConfigSetting(eleTool)
            eleActionToolList = eleEncryptListGUI.find("actionToolList")
            self.actionToolList.getConfigSetting(eleActionToolList)

        except Exception as e:
            bResult = False  
        return bResult
    
    def outputConfigSetting(self) -> None:
        #ツール名称
        eleToolGUI = Element("ExcelSheetSelectedList")

        #ツール名称GUI作成
        eleTool = Element("ToolName")
        self.toolName.outputConfigSetting(eleTool)
        eleToolGUI.append(eleTool)

        #【各pdfツール設定】GUI作成
        comment = ET.Comment('【' + self.toolName.widTool.getLabelValue('WindowTitle')+ '】GUI')
        eleToolGUI.append(comment)
        eleActionToolList = Element("actionToolList")
        self.actionToolList.outputConfigSetting(eleActionToolList)
        eleToolGUI.append(eleActionToolList)

        #ElementTreeを追加
        ET.indent(eleToolGUI)
        tree = ElementTree(eleToolGUI)
    
        #ファイル出力
        with open (self.CreateFileAddress, "wb") as xmlFileAddr :
            tree.write(xmlFileAddr, encoding='utf-8', xml_declaration=True)
        return
        
    def updateConfigSetting(self) -> None:
        self.toolName.updateConfigSetting(self.ui)
        self.actionToolList.updateConfigSetting(self.ui)
        return

    def updateGUISetting(self) -> None:
        self.toolName.updateGUISetting(self.ui)
        self.actionToolList.updateGUISetting(self.ui)
        return
        
    def print(self)-> None:
        #self.menubarList.print()
        return
        
