import xml.etree.ElementTree as ET
from xml.etree.ElementTree import  ElementTree,Element
from config.xmlLib.xmlLib import xmlLib
from config.xmlLib.xmlQtLib import xmlQWidget,xmlQPushButton, xmlQCheckBox
from GUI.pdfEditerToolGUI_UserAccessPermissions import pdfEditerToolGUI_UserAccessPermissions as ToolUI

from Lib.FileSysProcess import FileSysProcess

class toolNameLib(xmlLib):
    #ツール名称
    widTool:xmlQWidget
    """ toolName Setting"""
    def __init__(self)-> None:
 
        super(toolNameLib, self).__init__()

        #ツール名称
        self.toolName = "widTool" 
        self.toolTitle = "PDF Authorization Setting"
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
       
    def updateConfigSetting(self, toolUi:ToolUI) -> None:
        toolNameText = toolUi.windowTitle()
        self.widTool.modifyLabelProperty('WindowTitle', toolNameText)
        return
    
    def updateGUISetting(self, toolUi:ToolUI) -> None:
        toolNameText = self.widTool.getLabelValue('WindowTitle')
        toolUi.setWindowTitle(toolNameText)
        return


class actionToolList(xmlLib):

    #cbPrint(印刷禁止)
    cbPrint:xmlQCheckBox
    
    #cbContentCopy(内容コピー禁止)
    cbContentCopy:xmlQCheckBox
    
    #cbDocModify(ドキュメントの変更とアセンブリ禁止)
    cbDocModify:xmlQCheckBox
    
    #cbCommentModify(コメント記入禁止)
    cbCommentModify:xmlQCheckBox
    
    #cbFillFromFields(ドキュメントのアセンブリとページ抽出禁止)
    cbFillFromFields:xmlQCheckBox
    
    #btExecution(確定)
    btExecution:xmlQPushButton
    
    def __init__(self)-> None:
        super(actionToolList, self).__init__()
        
        #cbPrint(印刷禁止)
        self.cbPrintName = "cbPrint"
        self.cbPrintText = "Printing Prohibition"
        self.cbPrintChecked = False
        self.cbPrintEnabled = True
        self.cbPrintHidden = False
        
        #cbContentCopy(内容コピー禁止)
        self.cbContentCopyName = "cbContentCopy"
        self.cbContentCopyText = "Content copying prohibited"
        self.cbContentCopyChecked = False
        self.cbContentCopyEnabled = True
        self.cbContentCopyHidden = False
        
        #cbDocModify(ドキュメントの変更とアセンブリ禁止)
        self.cbDocModifyName = "cbDocModify"
        self.cbDocModifyText = "Document modification and assembly prohibited"
        self.cbDocModifyChecked = False
        self.cbDocModifyEnabled = True
        self.cbDocModifyHidden = False
        
        #cbCommentModify(コメント記入禁止)
        self.cbCommentModifyName = "cbCommentModify"
        self.cbCommentModifyText = "Input Comments prohibited"
        self.cbCommentModifyChecked = False
        self.cbCommentModifyEnabled = True
        self.cbCommentModifyHidden = False
        
        #cbFillFromFields(ドキュメントのアセンブリとページ抽出禁止)
        self.cbFillFromFieldsName = "cbFillFromFields"
        self.cbFillFromFieldsText = "Document assembly and page extraction prohibited"
        self.cbFillFromFieldsChecked = False
        self.cbFillFromFieldsEnabled = True
        self.cbFillFromFieldsHidden = False
        
        #btExecution(確定)
        self.btExecutionName = "btObjFileName"
        self.btExecutionText = "OK"
        self.btExecutionEnabled = True
        self.btExecutionHidden = False

        self.clearConfigSetting()
        self.createConfigSetting()
        return
        
    def clearConfigSetting(self) -> None:
        return

    def createConfigSetting(self) -> None:
        
        #cbPrint(印刷禁止)
        self.cbPrint = xmlQCheckBox(self.cbPrintName, 
                                    self.cbPrintText,
                                    self.cbPrintChecked,
                                    self.cbPrintEnabled,
                                    self.cbPrintHidden)
       
        #cbContentCopy(内容コピー禁止)
        self.cbContentCopy = xmlQCheckBox(self.cbContentCopyName, 
                                    self.cbContentCopyText,
                                    self.cbContentCopyChecked,
                                    self.cbContentCopyEnabled,
                                    self.cbContentCopyHidden)
       
        #cbDocModify(ドキュメントの変更とアセンブリ禁止)
        self.cbDocModify = xmlQCheckBox(self.cbDocModifyName, 
                                    self.cbDocModifyText,
                                    self.cbDocModifyChecked,
                                    self.cbDocModifyEnabled,
                                    self.cbDocModifyHidden)
       
        #cbCommentModify(コメント記入禁止)
        self.cbCommentModify = xmlQCheckBox(self.cbCommentModifyName, 
                                    self.cbCommentModifyText,
                                    self.cbCommentModifyChecked,
                                    self.cbCommentModifyEnabled,
                                    self.cbCommentModifyHidden)
       
        #cbFillFromFields(ドキュメントのアセンブリとページ抽出禁止)
        self.cbFillFromFields = xmlQCheckBox(self.cbFillFromFieldsName, 
                                    self.cbFillFromFieldsText,
                                    self.cbFillFromFieldsChecked,
                                    self.cbFillFromFieldsEnabled,
                                    self.cbFillFromFieldsHidden)
       
        #btExecution(確定)
        self.btExecution = xmlQPushButton(self.btExecutionName, 
                                          self.btExecutionText, 
                                          self.btExecutionEnabled, 
                                          self.btExecutionHidden)

        return
        
        
    def getConfigSetting(self, eleActionTool:Element|None)-> None:
        if eleActionTool is None :
            return
        
        #cbPrint(印刷禁止)
        self.cbPrint.getConfigSetting(eleActionTool,self.cbPrintName)
        
        #cbContentCopy(内容コピー禁止)
        self.cbContentCopy.getConfigSetting(eleActionTool,self.cbContentCopyName)
        
        #cbDocModify(ドキュメントの変更とアセンブリ禁止)
        self.cbDocModify.getConfigSetting(eleActionTool,self.cbDocModifyName)
        
        #cbCommentModify(コメント記入禁止)
        self.cbCommentModify.getConfigSetting(eleActionTool,self.cbCommentModifyName)
        
        #cbFillFromFields(ドキュメントのアセンブリとページ抽出禁止)
        self.cbFillFromFields.getConfigSetting(eleActionTool,self.cbFillFromFieldsName)
        
        #btExecution(確定)
        self.btExecution.getConfigSetting(eleActionTool,self.btExecutionName)

        return
        
    def outputConfigSetting(self, eleActionTool:Element) -> None:
        
        #cbPrint(印刷禁止)
        self.cbPrint.outputConfigSetting(eleActionTool)
        
        #cbContentCopy(内容コピー禁止)
        self.cbContentCopy.outputConfigSetting(eleActionTool)
        
        #cbDocModify(ドキュメントの変更とアセンブリ禁止)
        self.cbDocModify.outputConfigSetting(eleActionTool)
        
        #cbCommentModify(コメント記入禁止)
        self.cbCommentModify.outputConfigSetting(eleActionTool)
        
        #cbFillFromFields(ドキュメントのアセンブリとページ抽出禁止)
        self.cbFillFromFields.outputConfigSetting(eleActionTool)
        
        #確定
        comment = ET.Comment('【'+ self.btExecution.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #btExecution(確定)
        self.btExecution.outputConfigSetting(eleActionTool)
        
        return
    
    def updateConfigSetting(self, toolUi:ToolUI) -> None:

        #cbPrint(印刷禁止)
        self.cbPrint.updateConfigSetting(toolUi.cbPrint)
        
        #cbContentCopy(内容コピー禁止)
        self.cbContentCopy.updateConfigSetting(toolUi.cbContentCopy)
        
        #cbDocModify(ドキュメントの変更とアセンブリ禁止)
        self.cbDocModify.updateConfigSetting(toolUi.cbDocModify)
        
        #cbCommentModify(コメント記入禁止)
        self.cbCommentModify.updateConfigSetting(toolUi.cbCommentModify)
        
        #cbFillFromFields(ドキュメントのアセンブリとページ抽出禁止)
        self.cbFillFromFields.updateConfigSetting(toolUi.cbFillFromFields)
        
        #btExecution(確定)
        self.btExecution.updateConfigSetting(toolUi.btExecution)
        
        return
    
    def updateGUISetting(self, toolUi:ToolUI) -> None:
    
        #cbPrint(印刷禁止)
        self.cbPrint.updateGUISetting(toolUi.cbPrint)
        
        #cbContentCopy(内容コピー禁止)
        self.cbContentCopy.updateGUISetting(toolUi.cbContentCopy)
        
        #cbDocModify(ドキュメントの変更とアセンブリ禁止)
        self.cbDocModify.updateGUISetting(toolUi.cbDocModify)
        
        #cbCommentModify(コメント記入禁止)
        self.cbCommentModify.updateGUISetting(toolUi.cbCommentModify)
        
        #cbFillFromFields(ドキュメントのアセンブリとページ抽出禁止)
        self.cbFillFromFields.updateGUISetting(toolUi.cbFillFromFields)
        
        #btExecution(確定)
        self.btExecution.updateGUISetting(toolUi.btExecution)

        return
        
    def print(self) :
        return


class UserAccessPermissionsConfig():
    
    def __init__(self, configFileAddress:str, toolUi:ToolUI)-> None:
        super(UserAccessPermissionsConfig, self).__init__()
        self.FSP = FileSysProcess()
        self.CreateFileAddress = configFileAddress + "\\UserAccessPermissionsSetting_Jp.xml"
        if self.FSP.judgeFileExsit(self.CreateFileAddress) :
            self.configFileAddress = self.CreateFileAddress
        else :
            self.configFileAddress = configFileAddress + "\\Jp\\UserAccessPermissionsSetting_Jp.xml"

        self.ui = toolUi
        self.toolName = toolNameLib()
        self.actionToolList = actionToolList()
        return
        
    def getConfigSetting(self) -> bool:
        bResult = True
        try:
            tree = ET.parse(self.configFileAddress)
            elePdfEditerGUI =  tree.getroot()
            eleTool = elePdfEditerGUI.find("ToolName")
            self.toolName.getConfigSetting(eleTool)
            eleActionToolList = elePdfEditerGUI.find("actionToolList")
            self.actionToolList.getConfigSetting(eleActionToolList)
        except Exception as e:
            bResult = False  
        return bResult
    
    def outputConfigSetting(self) -> None:
        #ツール名称
        eleToolGUI = Element("UserAccessPermissionsSetting")

        #ツール名称GUI作成
        eleTool = Element("ToolName")
        self.toolName.outputConfigSetting(eleTool)
        eleToolGUI.append(eleTool)

        #【各pdfツール設定】GUI作成
        comment = ET.Comment('【pdf権限設定】GUI')
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
        
