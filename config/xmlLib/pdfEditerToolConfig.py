import xml.etree.ElementTree as ET
from xml.etree.ElementTree import  ElementTree,Element
from PyQt5.QtWidgets import QRadioButton
from config.xmlLib.xmlLib import xmlLib
from config.xmlLib.xmlQtLib import xmlQAction, xmlQMenu, xmlQMenuAction, xmlQRadioButton, xmlQTextEdit, xmlQGroupBox,xmlQLabel,xmlQComboBox,xmlQPushButton,xmlQCheckBox, xmlQLog
from GUI.pdfEditerToolGUI import Ui_pdfEditerToolGUI

from Lib.FileSysProcess import FileSysProcess


class menubarList(xmlLib):
    xmlMenuActions :list[xmlQMenuAction] = []
    """ pdfEditerTool Menu Bar Setting"""
    def __init__(self)-> None:
 
        super(menubarList, self).__init__()

        #【設定】
        self.menuSetting = "menuSetting"
        #【ツール切替】
        self.menuChangTool = "menuChangTool"
        #【officeFile⇒pdfFileへ変換】ツール/【pdf暗号化】ツール/【pdf復唱化】ツール
        self.actionToolNameList = ["【officeFile2pdfFile】Tool",
                                   "【pdfEncrypt】Tool",
                                   "【pdfDecrypt】Tool"]
        #【暗号化リスト設定】
        self.actionEncryptListSetting = "EncryptListSetting"
        #【その他】
        self.actionOther = "Other"
        #【ヘルプ】
        self.menuHelp = "help"
        #【pdfEditorToolについて】
        self.actionAboutPdfEditorTool = "About pdfEditorTool"
        self.clearConfigSetting()
        self.createConfigSetting()
        return

    def clearConfigSetting(self) -> None:
        self.xmlMenuActions.clear()
        return

    def createConfigSetting(self) -> None:
        #【menubar0】【設定】
        xmlMenuAction = xmlQMenuAction(self.menuSetting, self.menuSetting)
        #【menubar0|menu0】【ツール切替】
        xmlMenu = xmlQMenu("menu0", self.menuChangTool)
        #【menubar0|menu0|Action0】【officeFile⇒pdfFileへ変換】ツール
        #【menubar0|menu0|Action1】【pdf暗号化】ツール
        #【menubar0|menu0|Action2】【pdf復唱化】ツール
        xmlMenu.addQActions(self.actionToolNameList)
        xmlMenuAction.addQMenuAction(xmlMenu)
        #【menubar0|menu1】【暗号化リスト設定】
        xmlAction = xmlQAction("menu1", self.actionEncryptListSetting)
        xmlMenuAction.addQMenuAction(xmlAction)
        #【menubar0|menu2】【その他】
        xmlAction = xmlQAction("menu2", self.actionOther)
        xmlMenuAction.addQMenuAction(xmlAction)
        self.xmlMenuActions.append(xmlMenuAction)

        #【menubar1】 【ヘルプ】
        xmlMenuAction = xmlQMenuAction(self.menuHelp, self.menuHelp)
        #【menubar1|menu0】 【pdfEditorToolについて】
        xmlAction = xmlQAction("menu0", self.actionAboutPdfEditorTool)
        xmlMenuAction.addQMenuAction(xmlAction)
        self.xmlMenuActions.append(xmlMenuAction)
        return

    def getConfigSetting(self, eleMenubarList:Element|None)-> None:

        if eleMenubarList is None :
            return
        
        #【menubar0】【設定】
        eleMenu = self.xmlMenuActions[0].getConfigSetting(eleMenubarList, "menubar0")
        #【menubar1】【ヘルプ】
        eleMenu = self.xmlMenuActions[1].getConfigSetting(eleMenubarList, "menubar1")
        if isinstance(self.xmlMenuActions[0].qMenuActionList[0], xmlQMenu) :
            qActionList = self.xmlMenuActions[0].qMenuActionList[0].qActionList
            self.actionToolNameList[0] = qActionList[0].getLabelValue("Text", self.actionToolNameList[0])
            self.actionToolNameList[1] = qActionList[1].getLabelValue("Text", self.actionToolNameList[1])
            self.actionToolNameList[2] = qActionList[2].getLabelValue("Text", self.actionToolNameList[2])
        
        return
    
    def outputConfigSetting(self, eleMenubar:Element)-> Element:
        #【menubar0】 #【設定】
        eleSubMenubar = self.__outputLabelSetting(eleMenubar, 0)
        #【menubar1】 【ヘルプ】
        eleSubMenubar = self.__outputLabelSetting(eleMenubar, 1)
        return eleSubMenubar
       
    def __outputLabelSetting(self, eleMenubar:Element, qtIndex:int = 0) -> Element:
        eleSubMenubar = self.xmlMenuActions[qtIndex].outputLabelProperty(eleMenubar, qtIndex)
        return eleSubMenubar
       
    def updateConfigSetting(self, pdfEditerUi:Ui_pdfEditerToolGUI, index:int  = 0 ) -> None:
        #【メニューバー】GUI作成
        pdfEditerUi.actionToolName0.setEnabled(True)
        pdfEditerUi.actionToolName1.setEnabled(True)
        pdfEditerUi.actionToolName2.setEnabled(True)

        match(index):
            case 0: pdfEditerUi.actionToolName0.setEnabled(False)
            case 1: pdfEditerUi.actionToolName1.setEnabled(False)
            case 2: pdfEditerUi.actionToolName2.setEnabled(False)
            case _: 
                pdfEditerUi.actionToolName0.setEnabled(False)
        return
    
    def updateGUISetting(self, pdfEditerUi:Ui_pdfEditerToolGUI) -> None:
        #【設定】
        self.xmlMenuActions[0].updateGUISetting(pdfEditerUi.menuSetting)
        #【設定】【ツール切替】
        qMenuActionList = self.xmlMenuActions[0].qMenuActionList
        qMenuActionList[0].updateGUISetting(pdfEditerUi.menuChangTool)
        #【設定】【ツール切替】【officeFile⇒pdfFileへ変換】ツール/【pdf暗号化】ツール/【pdf復唱化】ツール
        if isinstance(qMenuActionList[0], xmlQMenu) :
            qActionList = qMenuActionList[0].qActionList
            qActionList[0].updateGUISetting(pdfEditerUi.actionToolName0)
            qActionList[1].updateGUISetting(pdfEditerUi.actionToolName1)
            qActionList[2].updateGUISetting(pdfEditerUi.actionToolName2)
        #【設定】【暗号化リスト設定】
        qMenuActionList[1].updateGUISetting(pdfEditerUi.actionEncryptListSetting)
        #【設定】【その他】
        qMenuActionList[2].updateGUISetting(pdfEditerUi.actionOther)

        #【ヘルプ】
        self.xmlMenuActions[1].updateGUISetting(pdfEditerUi.menuHelp)
        #【ヘルプ】【pdfEditorToolについて】
        qMenuActionList = self.xmlMenuActions[1].qMenuActionList
        qMenuActionList[0].updateGUISetting(pdfEditerUi.actionAboutPdfEditorTool)
        return
        
    def print(self) -> None:
        return

class xmlQEncryptButton(xmlQRadioButton):
    label:dict[str, str]= {}  
    def __init__(self, labelName = "", text="", bEnabled = True, bHidden = False, strEncrypt = "", strEncrypt2 = "", qtObj:QRadioButton|None = None)-> None:
        super(xmlQEncryptButton, self).__init__(labelName, text, False, bEnabled, bHidden,qtObj=qtObj)
        self.label["Encrypt"] = strEncrypt
        self.label["Encrypt2"] = strEncrypt2
        self.delLabelProperty('Checked')
        return

class encryptButtonList(xmlLib):
    """ pdfEditerTool EncryptButtonList Setting"""
    encryptButtonList:list[xmlQEncryptButton] = []
    lbUserPassword:xmlQLabel
    txEncrypt:xmlQTextEdit
    lbOwnerPassword:xmlQLabel
    txEncrypt2:xmlQTextEdit
    
    #cbPdfDocAttribSet
    cbPdfDocAttribSet:xmlQCheckBox
    #btPdfDocAttribSet
    btPdfDocAttribSet:xmlQPushButton
    #btPdfAuthorSet
    btPdfAuthorSet:xmlQPushButton
    
    def __init__(self, pdfEditerToolGUI:Ui_pdfEditerToolGUI)-> None:
        
        super(encryptButtonList, self).__init__()
        self.encryptButtonList.clear()
        #【暗号化表示名称リスト】
        self.EncryptTextList = [
                           "Non-Password",
                           "rbEncrypt01",
                           "rbEncrypt02",
                           "rbEncrypt03",
                           "rbEncrypt04",
                           "rbEncrypt05",
                           "rbEncrypt06",
                           "rbEncrypt07",
                           "rbEncrypt08",
                           "rbEncrypt09",
                           "rbEncryptOther" 
                           ]


        #【暗号化設定リスト(UserPassword)】
        self.EncryptNumberList = [
                           "",               # rbEncrypt00
                           "rbEncrypt01",
                           "rbEncrypt02",
                           "rbEncrypt03",
                           "rbEncrypt04",
                           "rbEncrypt05",
                           "rbEncrypt06",
                           "rbEncrypt07",
                           "rbEncrypt08",
                           "rbEncrypt09",
                           "rbEncryptOther" 
                           ]
        #【暗号化設定リスト(OwnerPassword)】
        self.Encrypt2NumberList = [
                           "",               # rbEncrypt00
                           "rbEncrypt01",
                           "rbEncrypt02",
                           "rbEncrypt03",
                           "rbEncrypt04",
                           "rbEncrypt05",
                           "rbEncrypt06",
                           "rbEncrypt07",
                           "rbEncrypt08",
                           "rbEncrypt09",
                           "rbEncryptOther" 
                           ]
        #【暗号化Enabled設定】
        self.EncryptEnabledList = [
                                    True,    # rbEncrypt00
                                    True,    # rbEncrypt01
                                    True,    # rbEncrypt02
                                    True,    # rbEncrypt03
                                    True,    # rbEncrypt04
                                    True,    # rbEncrypt05
                                    True,    # rbEncrypt06
                                    True,    # rbEncrypt07
                                    True,    # rbEncrypt08
                                    True,    # rbEncrypt09
                                    True     # rbEncryptOther
                                    ]

        #【暗号化Hidden設定】
        self.EncryptHiddenList = [
                                   False,    # rbEncrypt00
                                   False,    # rbEncrypt01
                                   False,    # rbEncrypt02
                                   False,    # rbEncrypt03
                                   False,    # rbEncrypt04
                                   False,    # rbEncrypt05
                                   False,    # rbEncrypt06
                                   False,    # rbEncrypt07
                                   False,    # rbEncrypt08
                                   False,    # rbEncrypt09
                                   False     # rbEncryptOther
                                   ]

        #lbUserPassword
        self.lbUserPasswordName = "lbUserPassword"
        self.lbUserPasswordText = "UserPassword:"

        #txEncryptText
        self.txEncryptName = "txEncryptText"
        self.txEncryptText = ""
        
        #lbOwnerPassword
        self.lbOwnerPasswordName = "lbOwnerPassword"
        self.lbOwnerPasswordText = "OwnerPassword:"

        #txEncrypt2Text
        self.txEncrypt2Name = "txEncrypt2Text"
        self.txEncrypt2Text = ""
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSetName = "cbPdfDocAttribSet"
        self.cbPdfDocAttribSetText = "PDFInfoSetting"
        self.cbPdfDocAttribSetChecked = False
        self.cbPdfDocAttribSetEnabled = True
        self.cbPdfDocAttribSetHidden = False
        
        #btPdfDocAttribSet
        self.btPdfDocAttribSetName = "btPdfDocAttribSet"
        self.btPdfDocAttribSetText = "PDFInfoSetting"
        self.btPdfDocAttribSetEnabled = True
        self.btPdfDocAttribSetHidden = False
        
        #btPdfAuthorSet
        self.btPdfAuthorSetName = "btPdfAuthorSet"
        self.btPdfAuthorSetText = "PDFInfoSetting"
        self.btPdfAuthorSetEnabled = True
        self.btPdfAuthorSetHidden = False
        
        self.clearConfigSetting()
        self.createConfigSetting(pdfEditerToolGUI)
        return

    def clearConfigSetting(self) -> None:
        self.encryptButtonList.clear()
        return
    
    def createConfigSetting(self, pdfEditerToolGUI:Ui_pdfEditerToolGUI) -> None:
        #encryptButton
        self.encryptButtonList.clear()
        for index, (EncryptText, 
                    EncryptNumber, 
                    Encrypt2Number,
                    EncryptEnabled,
                    EncryptHidden) in enumerate(zip(self.EncryptTextList,
                                                    self.EncryptNumberList,
                                                    self.Encrypt2NumberList,
                                                    self.EncryptEnabledList,
                                                    self.EncryptHiddenList)):
           self.encryptButtonList.append(xmlQEncryptButton(labelName = "rb" + str(index), 
                                                           text=EncryptText, 
                                                           bEnabled=EncryptEnabled, 
                                                           bHidden=EncryptHidden, 
                                                           strEncrypt=EncryptNumber,
                                                           strEncrypt2=Encrypt2Number))
        
        #lbUserPassword
        self.lbUserPassword= xmlQLabel(self.lbUserPasswordName,self.lbUserPasswordText)
        self.lbUserPassword.delLabelProperty("Hidden")
        #txEncryptText
        self.txEncrypt = xmlQTextEdit(labelName = self.txEncryptName,text = self.txEncryptText)
        self.txEncrypt.delLabelProperty("Hidden")
        #lbOwnerPassword
        self.lbOwnerPassword= xmlQLabel(self.lbOwnerPasswordName,self.lbOwnerPasswordText)
        #txEncrypt2Text
        self.txEncrypt2 = xmlQTextEdit(labelName = self.txEncrypt2Name,text = self.txEncrypt2Text)
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSet = xmlQCheckBox(self.cbPdfDocAttribSetName, 
                                              self.cbPdfDocAttribSetText,
                                              self.cbPdfDocAttribSetChecked,
                                              self.cbPdfDocAttribSetEnabled,
                                              self.cbPdfDocAttribSetHidden)
        self.cbPdfDocAttribSet.delLabelProperty("Checked")
        self.cbPdfDocAttribSet.delLabelProperty("Enabled")
        self.cbPdfDocAttribSet.delLabelProperty("Hidden")
        
        #btPdfDocAttribSet
        self.btPdfDocAttribSet = xmlQPushButton(self.btPdfDocAttribSetName,
                                                self.btPdfDocAttribSetText, 
                                                self.btPdfDocAttribSetEnabled,  
                                                self.btPdfDocAttribSetHidden)
        self.btPdfDocAttribSet.delLabelProperty("Enabled")
        self.btPdfDocAttribSet.delLabelProperty("Hidden")
        
        #btPdfAuthorSet
        self.btPdfAuthorSet = xmlQPushButton(self.btPdfAuthorSetName,
                                             self.btPdfAuthorSetText, 
                                             self.btPdfAuthorSetEnabled,  
                                             self.btPdfAuthorSetHidden)
        self.btPdfAuthorSet.delLabelProperty("Hidden")
        
        return
        
    def getConfigSetting(self, eleEncryptButtonList:Element|None)-> None:
        if eleEncryptButtonList is None :
            return
        
        #encryptButton
        for index in range(len(self.encryptButtonList)):
            self.encryptButtonList[index].getConfigSetting(eleEncryptButtonList, "rb" + str(index))
        
        #lbUserPassword
        self.lbUserPassword.getConfigSetting(eleEncryptButtonList, self.lbUserPasswordName)
        #txEncryptText
        self.txEncrypt.getConfigSetting(eleEncryptButtonList, self.txEncryptName)
        #lbOwnerPassword
        self.lbOwnerPassword.getConfigSetting(eleEncryptButtonList, self.lbOwnerPasswordName)
        #txEncrypt2Text
        self.txEncrypt2.getConfigSetting(eleEncryptButtonList, self.txEncrypt2Name)
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSet.getConfigSetting(eleEncryptButtonList, self.cbPdfDocAttribSetName)
        #btPdfDocAttribSet
        self.btPdfDocAttribSet.getConfigSetting(eleEncryptButtonList, self.btPdfDocAttribSetName)
        #btPdfAuthorSet
        self.btPdfAuthorSet.getConfigSetting(eleEncryptButtonList, self.btPdfAuthorSetName)
        
        return
          
    def outputConfigSetting(self, eleEncryptButton:Element) -> None:
        
        #encryptButton
        for index, encryptButton in enumerate(self.encryptButtonList):
            encryptButton.outputConfigSetting(eleEncryptButton, "rb" + str(index))

        #lbUserPassword
        self.lbUserPassword.outputConfigSetting(eleEncryptButton)
        #txEncryptText
        self.txEncrypt.outputConfigSetting(eleEncryptButton)
        #lbOwnerPassword
        self.lbOwnerPassword.outputConfigSetting(eleEncryptButton)
        #txEncrypt2Text
        self.txEncrypt2.outputConfigSetting(eleEncryptButton)
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSet.outputConfigSetting(eleEncryptButton)
        #btPdfDocAttribSet
        self.btPdfDocAttribSet.outputConfigSetting(eleEncryptButton)
        #btPdfAuthorSet
        self.btPdfAuthorSet.outputConfigSetting(eleEncryptButton)
        
        return
    
    def updateConfigSetting(self, pdfEditerUi:Ui_pdfEditerToolGUI, index:int  = 0 ) -> None:
        #encryptButton
        self.encryptButtonList[ 0].updateConfigSetting(pdfEditerUi.rbEncrypt00)
        self.encryptButtonList[ 1].updateConfigSetting(pdfEditerUi.rbEncrypt01)
        self.encryptButtonList[ 2].updateConfigSetting(pdfEditerUi.rbEncrypt02)
        self.encryptButtonList[ 3].updateConfigSetting(pdfEditerUi.rbEncrypt03)
        self.encryptButtonList[ 4].updateConfigSetting(pdfEditerUi.rbEncrypt04)
        self.encryptButtonList[ 5].updateConfigSetting(pdfEditerUi.rbEncrypt05)
        self.encryptButtonList[ 6].updateConfigSetting(pdfEditerUi.rbEncrypt06)
        self.encryptButtonList[ 7].updateConfigSetting(pdfEditerUi.rbEncrypt07)
        self.encryptButtonList[ 8].updateConfigSetting(pdfEditerUi.rbEncrypt08)
        self.encryptButtonList[ 9].updateConfigSetting(pdfEditerUi.rbEncrypt09)
        self.encryptButtonList[10].updateConfigSetting(pdfEditerUi.rbEncryptOther)
        
        for index in range(len(self.encryptButtonList)):
            self.encryptButtonList[index].modifyLabelProperty('Encrypt', self.EncryptNumberList[index])
            self.encryptButtonList[index].modifyLabelProperty('Encrypt2', self.Encrypt2NumberList[index])

        #lbUserPassword
        self.lbUserPassword.updateConfigSetting(pdfEditerUi.lbUserPassword)
        #txEncryptText
        self.txEncrypt.updateConfigSetting(pdfEditerUi.txEncryptText)
        #lbOwnerPassword
        self.lbOwnerPassword.updateConfigSetting(pdfEditerUi.lbOwnerPassword)
        #tx2EncryptText
        self.txEncrypt2.updateConfigSetting(pdfEditerUi.txEncrypt2Text)
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSet.updateConfigSetting(pdfEditerUi.cbPdfDocAttribSet)
        #btPdfDocAttribSet
        self.btPdfDocAttribSet.updateConfigSetting(pdfEditerUi.btPdfDocAttribSet)
        #btPdfAuthorSet
        self.btPdfAuthorSet.updateConfigSetting(pdfEditerUi.btPdfAuthorSet)
        
        
        return
    
    def updateGUISetting(self, pdfEditerUi:Ui_pdfEditerToolGUI) -> None:

        #encryptButton
        self.encryptButtonList[ 0].updateGUISetting(pdfEditerUi.rbEncrypt00)
        self.encryptButtonList[ 1].updateGUISetting(pdfEditerUi.rbEncrypt01)
        self.encryptButtonList[ 2].updateGUISetting(pdfEditerUi.rbEncrypt02)
        self.encryptButtonList[ 3].updateGUISetting(pdfEditerUi.rbEncrypt03)
        self.encryptButtonList[ 4].updateGUISetting(pdfEditerUi.rbEncrypt04)
        self.encryptButtonList[ 5].updateGUISetting(pdfEditerUi.rbEncrypt05)
        self.encryptButtonList[ 6].updateGUISetting(pdfEditerUi.rbEncrypt06)
        self.encryptButtonList[ 7].updateGUISetting(pdfEditerUi.rbEncrypt07)
        self.encryptButtonList[ 8].updateGUISetting(pdfEditerUi.rbEncrypt08)
        self.encryptButtonList[ 9].updateGUISetting(pdfEditerUi.rbEncrypt09)
        self.encryptButtonList[10].updateGUISetting(pdfEditerUi.rbEncryptOther)

        for index , EncryptNumber in enumerate(self.EncryptNumberList):
            self.EncryptNumberList[index] = self.encryptButtonList[index].getLabelValue("Encrypt", EncryptNumber)
            self.Encrypt2NumberList[index] = self.encryptButtonList[index].getLabelValue("Encrypt2", EncryptNumber)
            
        self.EncryptNumberList[10] = pdfEditerUi.txEncryptText.toPlainText()
        self.Encrypt2NumberList[10] = pdfEditerUi.txEncrypt2Text.toPlainText()

        #lbUserPassword
        self.lbUserPassword.updateGUISetting(pdfEditerUi.lbUserPassword)
        #txEncryptText
        self.txEncrypt.updateGUISetting(pdfEditerUi.txEncryptText)
        #lbOwnerPassword
        self.lbOwnerPassword.updateGUISetting(pdfEditerUi.lbOwnerPassword)
        #txEncrypt2Text設定
        self.txEncrypt2.updateGUISetting(pdfEditerUi.txEncrypt2Text)


        #cbPdfDocAttribSet
        self.cbPdfDocAttribSet.updateGUISetting(pdfEditerUi.cbPdfDocAttribSet)
        #btPdfDocAttribSet
        self.btPdfDocAttribSet.updateGUISetting(pdfEditerUi.btPdfDocAttribSet)
        #btPdfAuthorSet
        self.btPdfAuthorSet.updateGUISetting(pdfEditerUi.btPdfAuthorSet)

        pdfEditerUi.menubar.activateWindow()
        return
        
    def print(self)-> None:
        return
        
class algorithmLabelList(xmlLib):

    cmbPdfAlgorithmLabelList:dict[str, str] = {}
    pdfAlgLabelList:dict[str, str] = {}
    lbPdfAlgorithm:xmlQLabel
    cmbPdfAlgorithm:xmlQComboBox

    """ pdfEditerTool algorithmLabelList Setting"""
    def __init__(self)-> None:
        super(algorithmLabelList, self).__init__()

        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithmLabelName = "lbPdfAlgorithmLabel"
        self.lbPdfAlgorithmLabelText = "EncryptLabel:"

        #cmbPdfAlgorithm
        self.cmbPdfAlgorithmLabelName = "cmbPdfAlgorithm"
        self.cmbPdfAlgorithmLabelHiddenList = [False, True, True]
        self.cmbPdfAlgorithmLabelList.clear()
        self.cmbPdfAlgorithmLabelList[ "AES-256" ] ="Acrobat X/Acrobat 9.0"
        self.cmbPdfAlgorithmLabelList[ "AES-128" ] ="Acrobat 7.0"
        self.cmbPdfAlgorithmLabelList[ "RC4-128" ] ="Acrobat 6.0/Acrobat 5.0"
        self.cmbPdfAlgorithmLabelList[ "RC4-40"  ] ="Acrobat 3.0"
        
        self.clearConfigSetting()
        self.createConfigSetting()
        return

    def getConfigSetting(self, eleAlgorithmLabelList:Element|None)-> None:
        if eleAlgorithmLabelList is None :
            return
        
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithm.getConfigSetting(eleAlgorithmLabelList, self.lbPdfAlgorithmLabelName)
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithm.getConfigSetting(eleAlgorithmLabelList, self.cmbPdfAlgorithmLabelName)
        return
        
    def clearConfigSetting(self) -> None:
        return
        
    def createConfigSetting(self) -> None:
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithm = xmlQLabel(self.lbPdfAlgorithmLabelName, self.lbPdfAlgorithmLabelText)
        self.lbPdfAlgorithm.delLabelProperty("Hidden")
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithm = xmlQComboBox(self.cmbPdfAlgorithmLabelName, ItemList = self.cmbPdfAlgorithmLabelList)
        self.cmbPdfAlgorithm.delLabelProperty( "Hidden")
        return

    def outputConfigSetting(self, eleAlgorithmLabel:Element) -> None:
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithm.outputConfigSetting(eleAlgorithmLabel)
        #cmbPdfAlgorithm設定
        self.cmbPdfAlgorithm.outputConfigSetting(eleAlgorithmLabel)
        return
    
    def updateConfigSetting(self, pdfEditerUi:Ui_pdfEditerToolGUI, index:int  = 0 ) -> None:
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithm.updateConfigSetting(pdfEditerUi.lbPdfAlgorithmLabel)
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithm.updateConfigSetting(pdfEditerUi.cmbPdfAlgorithm)
        return
    
    def updateGUISetting(self, pdfEditerUi:Ui_pdfEditerToolGUI) -> None:
        #lbPdfAlgorithmLabel設定
        self.lbPdfAlgorithm.updateGUISetting(pdfEditerUi.lbPdfAlgorithmLabel)
        #cmbPdfAlgorithm設定
        self.cmbPdfAlgorithm.updateGUISetting(pdfEditerUi.cmbPdfAlgorithm)
        self.pdfAlgLabelList = self.cmbPdfAlgorithm.getItemValueDict()

        return
        
    def print(self) :
        return
        
class actionToolList(xmlLib):
    #lbObjFileName
    lbObjFileNameList:list[xmlQLabel] =[]
    #txObjFileName
    txObjFileNameList:list[xmlQTextEdit] = []
    #btObjFileName
    btObjFileNameList:list[xmlQPushButton] =[]
    
    #lbPdfFilePath
    lbPdfFilePathList:list[xmlQLabel] =[]
    #txPdfFilePath
    txPdfFilePathList:list[xmlQTextEdit] =[]
    #cbPdfFilePath
    cbPdfFilePathList:list[xmlQCheckBox] =[]
    #btPdfFilePath
    btPdfFilePathList:list[xmlQPushButton] =[]
    
    #lbPdfFileName
    lbPdfFileNameList:list[xmlQLabel] =[]
    #txPdfFileName
    txPdfFileNameList:list[xmlQTextEdit] =[]
    #cbPdfFileName
    cbPdfFileNameList:list[xmlQCheckBox] =[]
    #lbPdfFileNote
    lbPdfFileNoteList:list[xmlQLabel] =[]
    #cbPdfFileOverWrite
    cbPdfFileOverWriteList:list[xmlQCheckBox] =[]
    
    #btExcelSheetSelect
    btExcelSheetSelectList:list[xmlQPushButton] =[]
    #btObjFile2pdfFile
    btObjFile2pdfFileList:list[xmlQPushButton] =[]
    
    #lbUserPassword
    lbUserPasswordList:list[xmlQLabel] =[]
    #txEncryptText
    txEncryptList:list[xmlQTextEdit] =[]
    
    #lbPdfAlgorithmLabel
    lbPdfAlgorithmLabelList:list[xmlQLabel] =[]
    #cmbPdfAlgorithm
    cmbPdfAlgorithmList:list[xmlQComboBox] =[]
    
    #gbEncrypt
    gbEncryptList:list[xmlQGroupBox] =[]
    
    #cbPdfDocAttribSet
    cbPdfDocAttribSetList:list[xmlQCheckBox] =[]
    #btPdfDocAttribSet
    btPdfDocAttribSetList:list[xmlQPushButton]  =[]
    
    #btPdfAuthorSet
    btPdfAuthorSetList:list[xmlQPushButton]  =[]
    
    def __init__(self, parent:menubarList|None = None)-> None:
        super(actionToolList, self).__init__()
        self.menubarList = parent

        #lbObjFileName
        self.lbObjFileName = "lbObjFileName" 
        self.lbObjFileText = ["ObjectFileAddress", "ObjectFileAddress", "ObjectFileAddress"]
        self.lbObjFileHiddenList = [False, False, False]
        
        #txObjFileName
        self.txObjFileName = "txObjFileName"
        self.txObjFileText = ["", "", ""]
        self.txObjFileEnabled = [True, True, True]
        self.txObjFileHiddenList = [False, False, False]

        #btObjFileName
        self.btObjFileName = "btObjFileName"
        self.btObjFileText = ["select", "select", "select"]
        self.btObjFileEnabled = [True, True, True]
        self.btObjFileHiddenList = [False, False, False]
        
        #lbPdfFilePath
        self.lbPdfFilePathName = "lbPdfFilePath" 
        self.lbPdfFilePathText = ["PdfFilePath", "PdfFilePath", "PdfFilePath"]
        self.lbPdfFilePathHiddenList = [False, False, False]

        #txPdfFilePath
        self.txPdfFilePathName = "txPdfFilePath"
        self.txPdfFilePathText = ["", "", ""]
        self.txPdfFilePathEnabled = [True, True, True]
        self.txPdfFilePathHiddenList = [False, False, False]

        #cbPdfFilePath
        self.cbPdfFilePathName = "cbPdfFilePath"
        self.cbPdfFilePathText = ["Handwritting", "Handwritting", "Handwritting"]
        self.cbPdfFilePathChecked = [False, False, False]
        self.cbPdfFilePathEnabled = [True, True, True]
        self.cbPdfFilePathHiddenList = [False, False, False]

        #btPdfFilePath
        self.btPdfFilePathName = "btPdfFilePath"
        self.btPdfFilePathText = ["select", "select", "select"]
        self.btPdfFilePathEnabled = [True, True, True]
        self.btPdfFilePathHiddenList = [False, False, False]
        
        #lbPdfFileName
        self.lbPdfFileName = "lbPdfFileName"
        self.lbPdfFileText = ["PdfFileName", "PdfFileName", "PdfFileName"]
        self.lbPdfFileHiddenList = [False, False, False]

        #txPdfFileName
        self.txPdfFileName = "txPdfFileName"
        self.txPdfFileText = ["", "", ""]
        self.txPdfFileEnabled = [True, True, True]
        self.txPdfFileHiddenList = [False, False, False]
        
        #cbPdfFileName
        self.cbPdfFileName = "cbPdfFileName"
        self.cbPdfFileText = ["Handwritting", "Handwritting", "Handwritting"]
        self.cbPdfFileChecked = [False, False, False]
        self.cbPdfFileEnabled = [True, True, True]
        self.cbPdfFileHiddenList = [False, False, False]
        
        #lbPdfFileNote
        self.lbPdfFileNoteName = "lbPdfFileNote" 
        self.lbPdfFileNoteText = ["※ 👆 Do not input the extension please.", "※ 👆 Do not input the extension please.", "※ 👆 Do not input the extension please."]
        self.lbPdfFileNoteHiddenList = [True, True, True]
        
        #cbPdfFileOverWrite
        self.cbPdfFileOverWriteName = "cbPdfFileOverWrite"
        self.cbPdfFileOverWriteText = ["overwrite saving", "overwrite saving", "overwrite saving"]
        self.cbPdfFileOverWriteChecked = [False, False, False]
        self.cbPdfFileOverWriteEnabled = [True, True, True]
        self.cbPdfFileOverWriteHiddenList = [True, True, True]

        #btExcelSheetSelect
        self.btExcelSheetSelectName = "btExcelSheetSelect"
        self.btExcelSheetSelectText = ["ExcelSheetSelect", "ExcelSheetSelect", "ExcelSheetSelect"]
        self.btExcelSheetSelectEnabled = [False, False, False]
        self.btExcelSheetSelectHiddenList = [False, True, True]
        
        #btObjFile2pdfFile
        self.btObjFile2pdfFileName = "btObjFile2pdfFile"
        self.btObjFile2pdfFileText = ["ObjFile2pdfFileExecute", "PdfEncryptExecute", "PdfDecryptExecute"]
        self.btObjFile2pdfFileEnabled = [True, True, True]
        self.btObjFile2pdfFileHiddenList = [False, False, False]
        
        #lbUserPassword
        self.lbUserPasswordName = "lbUserPassword"
        self.lbUserPasswordHiddenList = [False, False, True]
        
        #txEncryptText
        self.txEncryptTextName = "txEncryptText"
        self.txEncryptTextHiddenList = [False, False, True]
        
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithmLabelName = "lbPdfAlgorithmLabel"
        self.lbPdfAlgorithmLabelHiddenList = [False, False, True]

        #cmbPdfAlgorithm
        self.cmbPdfAlgorithmLabelName = "cmbPdfAlgorithm"
        self.cmbPdfAlgorithmLabelHiddenList = [False, False, True]
       
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSetName = "cbPdfDocAttribSet"
        self.cbPdfDocAttribSetText = "PDFInfoSetting"
        self.cbPdfDocAttribSetChecked = [False, False, True]
        self.cbPdfDocAttribSetEnabled = [True, True, True]
        self.cbPdfDocAttribSetHiddenList = [False, False, True]
        
        #btPdfDocAttribSet
        self.btPdfDocAttribSetName = "btPdfDocAttribSet"
        self.btPdfDocAttribSetText = "PDFInfoSetting"
        self.btPdfDocAttribSetEnabled = [True, True, True]
        self.btPdfDocAttribSetHiddenList = [False, False, True]
        
        #btPdfAuthorSet
        self.btPdfAuthorSetName = "btPdfAuthorSet"
        self.btPdfAuthorSetText = "PdfAuthorizationSetting"
        self.btPdfAuthorSetEnabled = [True, True, True]
        self.btPdfAuthorSetHiddenList = [False, False, True]
        
        #gbEncrypt
        self.gbEncryptName = "gbEncrypt"
        self.gbEncryptNameList =  ["PasswordSetting", "PasswordSetting", "PasswordSetting"]
        self.gbEncryptRbIndex = [-1,-1,-1]
        
        
        self.clearConfigSetting()
        self.createConfigSetting()
        return
        
    def clearConfigSetting(self) -> None:
        #lbObjFileName
        self.lbObjFileNameList.clear()
        #txObjFileName
        self.txObjFileNameList.clear()
        #btObjFileName
        self.btObjFileNameList.clear()
        
        #lbPdfFilePath
        self.lbPdfFilePathList.clear()
        #txPdfFilePath
        self.txPdfFilePathList.clear()
        #cbPdfFilePath
        self.cbPdfFilePathList.clear()
        #btPdfFilePath
        self.btPdfFilePathList.clear()
        
        #lbPdfFileName
        self.lbPdfFileNameList.clear()
        #txPdfFileName
        self.txPdfFileNameList.clear()
        #cbPdfFileName
        self.cbPdfFileNameList.clear()
        #lbPdfFileNote
        self.lbPdfFileNoteList.clear()
        #cbPdfFileOverWrite
        self.cbPdfFileOverWriteList.clear()
        
        #btExcelSheetSelect
        self.btExcelSheetSelectList.clear()
        #btObjFile2pdfFile
        self.btObjFile2pdfFileList.clear()

        #lbUserPassword
        self.lbUserPasswordList.clear()
        #txEncryptText
        self.txEncryptList.clear()

        #lbPdfAlgorithmLabel
        self.lbPdfFileNoteList.clear()
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithmList.clear()
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSetList.clear()
        #btPdfDocAttribSet
        self.btPdfDocAttribSetList.clear()
        #btPdfAuthorSet
        self.btPdfAuthorSetList.clear()
        
        #gbEncrypt
        self.gbEncryptList.clear()
        return

    def createConfigSetting(self) -> None:

        if self.menubarList is None:
            return
        
        for index, actionToolName in enumerate(self.menubarList.actionToolNameList):
            self.__createConfigSetting(index)
        return
        
    def __createConfigSetting(self, index:int = 0) -> None:
        #lbObjFileName
        xmlLabel = xmlQLabel(self.lbObjFileName,
                             self.lbObjFileText[index],
                             self.lbObjFileHiddenList[index])
        self.lbObjFileNameList.append(xmlLabel)
        
        #txObjFileName
        xmlTextEdit = xmlQTextEdit(self.txObjFileName,
                                   self.txObjFileText[index],
                                   self.txObjFileEnabled[index],
                                   self.txObjFileHiddenList[index]
                                   )
        self.txObjFileNameList.append(xmlTextEdit)

        #btObjFileName
        xmlPushButton = xmlQPushButton(self.btObjFileName, 
                                       self.btObjFileText[index], 
                                       self.btObjFileEnabled[index],  
                                       self.btObjFileHiddenList[index])
        self.btObjFileNameList.append(xmlPushButton)

        #lbPdfFilePath
        xmlLabel = xmlQLabel(self.lbPdfFilePathName, 
                             self.lbPdfFilePathText[index], 
                             self.lbPdfFilePathHiddenList[index])
        self.lbPdfFilePathList.append(xmlLabel)

        #txPdfFilePath
        xmlTextEdit = xmlQTextEdit(self.txPdfFilePathName, 
                                   self.txPdfFilePathText[index],
                                   self.txPdfFilePathEnabled[index],
                                   self.txPdfFilePathHiddenList[index]
                                   )
        self.txPdfFilePathList.append(xmlTextEdit)
        
        #cbPdfFilePath
        xmlCheckBox = xmlQCheckBox(self.cbPdfFilePathName, 
                                   self.cbPdfFilePathText[index],
                                   self.cbPdfFilePathChecked[index],
                                   self.cbPdfFilePathEnabled[index],
                                   self.cbPdfFilePathHiddenList[index])
        self.cbPdfFilePathList.append(xmlCheckBox)
        
        #btPdfFilePath
        xmlPushButton = xmlQPushButton(self.btPdfFilePathName, 
                                       self.btPdfFilePathText[index], 
                                       self.btPdfFilePathEnabled[index],  
                                       self.btPdfFilePathHiddenList[index])
        self.btPdfFilePathList.append(xmlPushButton)
        
        #lbPdfFileName
        xmlLabel = xmlQLabel(self.lbPdfFileName, 
                             self.lbPdfFileText[index], 
                             self.lbPdfFileHiddenList[index])
        self.lbPdfFileNameList.append(xmlLabel)

        #txPdfFileName
        xmlTextEdit = xmlQTextEdit(self.txPdfFileName, 
                                   self.txPdfFileText[index],
                                   self.txPdfFileEnabled[index],
                                   self.txPdfFileHiddenList[index])
        self.txPdfFileNameList.append(xmlTextEdit)
        
        #cbPdfFileName
        xmlCheckBox = xmlQCheckBox(self.cbPdfFileName, 
                                   self.cbPdfFileText[index],
                                   self.cbPdfFileChecked[index],
                                   self.cbPdfFileEnabled[index],
                                   self.cbPdfFileHiddenList[index])
        self.cbPdfFileNameList.append(xmlCheckBox)
        
        
        #lbPdfFileNote
        xmlLabel = xmlQLabel(self.lbPdfFileNoteName, 
                             self.lbPdfFileNoteText[index], 
                             self.lbPdfFileNoteHiddenList[index])
        self.lbPdfFileNoteList.append(xmlLabel)
        
        
        #cbPdfFileOverWrite
        xmlCheckBox = xmlQCheckBox(self.cbPdfFileOverWriteName,
                                   self.cbPdfFileOverWriteText[index],
                                   self.cbPdfFileOverWriteChecked[index],
                                   self.cbPdfFileOverWriteEnabled[index],
                                   self.cbPdfFileOverWriteHiddenList[index])
        self.cbPdfFileOverWriteList.append(xmlCheckBox)
        
        
        #btExcelSheetSelect
        xmlPushButton = xmlQPushButton(self.btExcelSheetSelectName,
                                       self.btExcelSheetSelectText[index], 
                                       self.btExcelSheetSelectEnabled[index],  
                                       self.btExcelSheetSelectHiddenList[index])
        self.btExcelSheetSelectList.append(xmlPushButton)
        
        
        #btObjFile2pdfFile
        xmlPushButton = xmlQPushButton(self.btObjFile2pdfFileName,
                                       self.btObjFile2pdfFileText[index], 
                                       self.btObjFile2pdfFileEnabled[index],  
                                       self.btObjFile2pdfFileHiddenList[index])
        self.btObjFile2pdfFileList.append(xmlPushButton)

        #lbUserPassword
        xmlLabel = xmlQLabel(self.lbUserPasswordName, 
                             "", 
                             self.lbUserPasswordHiddenList[index])
        xmlLabel.delLabelProperty("Text")
        self.lbUserPasswordList.append(xmlLabel)
        
        #txEncryptText
        xmlTextEdit = xmlQTextEdit(self.txEncryptTextName, 
                                   "",
                                   "",
                                   self.txEncryptTextHiddenList[index])
        xmlTextEdit.delLabelProperty("Text")
        xmlTextEdit.delLabelProperty("Enabled")
        self.txEncryptList.append(xmlTextEdit)

        
        #lbPdfAlgorithmLabel
        xmlLabel = xmlQLabel(self.lbPdfAlgorithmLabelName, 
                             "", 
                             self.lbPdfAlgorithmLabelHiddenList[index])
        xmlLabel.delLabelProperty("Text")
        self.lbPdfAlgorithmLabelList.append(xmlLabel)

        #cmbPdfAlgorithm
        xmlComboBox = xmlQComboBox(self.cmbPdfAlgorithmLabelName, "", self.cmbPdfAlgorithmLabelHiddenList[index])
        xmlComboBox.delLabelProperty("Text")
        self.cmbPdfAlgorithmList.append(xmlComboBox)
        
        #cbPdfDocAttribSet
        xmlCheckBox = xmlQCheckBox(self.cbPdfDocAttribSetName, 
                                   self.cbPdfDocAttribSetText[index],
                                   self.cbPdfDocAttribSetChecked[index],
                                   self.cbPdfDocAttribSetEnabled[index],
                                   self.cbPdfDocAttribSetHiddenList[index])
        xmlCheckBox.delLabelProperty("Text")
        self.cbPdfDocAttribSetList.append(xmlCheckBox)
        
        #btPdfDocAttribSet
        xmlPushButton = xmlQPushButton(self.btPdfDocAttribSetName,
                                       self.btPdfDocAttribSetText[index], 
                                       self.btPdfDocAttribSetEnabled[index],  
                                       self.btPdfDocAttribSetHiddenList[index])
        xmlPushButton.delLabelProperty("Text")
        self.btPdfDocAttribSetList.append(xmlPushButton)
        
        #btPdfAuthorSet
        xmlPushButton = xmlQPushButton(self.btPdfAuthorSetName,
                                       self.btPdfAuthorSetText[index], 
                                       self.btPdfAuthorSetEnabled[index],  
                                       self.btPdfAuthorSetHiddenList[index])
        xmlPushButton.delLabelProperty("Text")
        xmlPushButton.delLabelProperty("Enabled")
        self.btPdfAuthorSetList.append(xmlPushButton)
        
        
        #gbEncrypt
        gbEncrypt =  xmlQGroupBox(self.gbEncryptName, self.gbEncryptNameList[index])
        gbEncrypt.delLabelProperty("Hidden")
        gbEncrypt.addLabelProperty("gbEncryptRbIndex", self.gbEncryptRbIndex[index])
        self.gbEncryptList.append(gbEncrypt)
        
        
        return
        
        
    def getConfigSetting(self, eleActionToolList:Element|None)-> None:
        if eleActionToolList is None or self.menubarList is None :
            return
        
        for index, actionToolName in enumerate(self.menubarList.actionToolNameList):
            self.__getConfigSetting(eleActionToolList, index)
        return
        
    def __getConfigSetting(self, eleActionToolList:Element,  index:int = 0) -> None:
        
        eleActionTool = self.findElement(eleActionToolList, "actionTool" + str(index))
        if eleActionTool is None:
            return
        
        #lbObjFileName
        self.lbObjFileNameList[index].getConfigSetting(eleActionTool,self.lbObjFileName)
        #txObjFileName
        self.txObjFileNameList[index].getConfigSetting(eleActionTool,self.txObjFileName)
        #btObjFileName
        self.btObjFileNameList[index].getConfigSetting(eleActionTool,self.btObjFileName)
        
        #lbPdfFilePath
        self.lbPdfFilePathList[index].getConfigSetting(eleActionTool,self.lbPdfFilePathName)
        #txPdfFilePath
        self.txPdfFilePathList[index].getConfigSetting(eleActionTool,self.txPdfFilePathName)
        #cbPdfFilePath
        self.cbPdfFilePathList[index].getConfigSetting(eleActionTool,self.cbPdfFilePathName)
        #btPdfFilePath
        self.btPdfFilePathList[index].getConfigSetting(eleActionTool,self.btPdfFilePathName)
        
        #lbPdfFileName
        self.lbPdfFileNameList[index].getConfigSetting(eleActionTool,self.lbPdfFileName)
        #txPdfFileName
        self.txPdfFileNameList[index].getConfigSetting(eleActionTool,self.txPdfFileName)
        #cbPdfFileName
        self.cbPdfFileNameList[index].getConfigSetting(eleActionTool,self.cbPdfFileName)
        #lbPdfFileNote
        self.lbPdfFileNoteList[index].getConfigSetting(eleActionTool,self.lbPdfFileNoteName)
        #cbPdfFileOverWrite
        self.cbPdfFileOverWriteList[index].getConfigSetting(eleActionTool,self.cbPdfFileOverWriteName)
        
        #btExcelSheetSelect
        self.btExcelSheetSelectList[index].getConfigSetting(eleActionTool,self.btExcelSheetSelectName)
        #btObjFile2pdfFile
        self.btObjFile2pdfFileList[index].getConfigSetting(eleActionTool,self.btObjFile2pdfFileName)

        #lbUserPassword
        self.lbUserPasswordList[index].getConfigSetting(eleActionTool,self.lbUserPasswordName)
        #txEncryptText
        self.txEncryptList[index].getConfigSetting(eleActionTool,self.txEncryptTextName)

        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithmLabelList[index].getConfigSetting(eleActionTool,self.lbPdfAlgorithmLabelName)
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithmList[index].getConfigSetting(eleActionTool, self.cmbPdfAlgorithmLabelName)

        #cbPdfDocAttribSet
        self.cbPdfDocAttribSetList[index].getConfigSetting(eleActionTool,self.cbPdfDocAttribSetName)
        
        #btPdfDocAttribSet
        self.btPdfDocAttribSetList[index].getConfigSetting(eleActionTool,self.btPdfDocAttribSetName)
        
        #btPdfAuthorSet
        self.btPdfAuthorSetList[index].getConfigSetting(eleActionTool,self.btPdfAuthorSetName)
        
        #gbEncrypt
        self.gbEncryptList[index].getConfigSetting(eleActionTool,self.gbEncryptName)



        return
        
    def outputConfigSetting(self, eleActionToolList:Element) -> None:

        if self.menubarList is None:
            return

        for index,  actionToolName in enumerate(self.menubarList.actionToolNameList):
            comment = ET.Comment( actionToolName + 'GUI設定')
            eleActionToolList.append(comment)
            eleActionTool =self.addEleLabel(eleActionToolList, "actionTool" + str(index))
            self.__outputConfigSetting(eleActionTool, index)
        return
        
    def __outputConfigSetting(self, eleActionTool:Element, index:int = 0) -> None:
        
        #lbObjFileName
        self.lbObjFileNameList[index].outputConfigSetting(eleActionTool)
        #txObjFileName
        self.txObjFileNameList[index].outputConfigSetting(eleActionTool)
        #btObjFileName
        self.btObjFileNameList[index].outputConfigSetting(eleActionTool)

        #lbPdfFilePath
        self.lbPdfFilePathList[index].outputConfigSetting(eleActionTool)
        #txPdfFilePath
        self.txPdfFilePathList[index].outputConfigSetting(eleActionTool)
        #cbPdfFilePath
        self.cbPdfFilePathList[index].outputConfigSetting(eleActionTool)
        #btPdfFilePath
        self.btPdfFilePathList[index].outputConfigSetting(eleActionTool)

        #lbPdfFileName
        self.lbPdfFileNameList[index].outputConfigSetting(eleActionTool)
        #txPdfFileName
        self.txPdfFileNameList[index].outputConfigSetting(eleActionTool)
        #cbPdfFileName
        self.cbPdfFileNameList[index].outputConfigSetting(eleActionTool)
        #lbPdfFileNote
        self.lbPdfFileNoteList[index].outputConfigSetting(eleActionTool)
        #cbPdfFileOverWrite
        self.cbPdfFileOverWriteList[index].outputConfigSetting(eleActionTool)
        
        #btExcelSheetSelect
        self.btExcelSheetSelectList[index].outputConfigSetting(eleActionTool)
        #btObjFile2pdfFile
        self.btObjFile2pdfFileList[index].outputConfigSetting(eleActionTool)
        
        #lbUserPassword
        self.lbUserPasswordList[index].outputConfigSetting(eleActionTool)
        #txEncryptText
        self.txEncryptList[index].outputConfigSetting(eleActionTool)
        
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithmLabelList[index].outputConfigSetting(eleActionTool)
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithmList[index].outputConfigSetting(eleActionTool)
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSetList[index].outputConfigSetting(eleActionTool)
        
        #btPdfDocAttribSet
        self.btPdfDocAttribSetList[index].outputConfigSetting(eleActionTool)
        
        #btPdfAuthorSet
        self.btPdfAuthorSetList[index].outputConfigSetting(eleActionTool)
        
        #gbEncrypt
        self.gbEncryptList[index].outputConfigSetting(eleActionTool)
        
        return
    
    def updateConfigSetting(self, pdfEditerUi:Ui_pdfEditerToolGUI, index:int  = 0 ) -> None:

        #lbObjFileName
        self.lbObjFileNameList[index].updateConfigSetting(pdfEditerUi.lbObjFileName)
        #txObjFileName
        self.txObjFileNameList[index].updateConfigSetting(pdfEditerUi.txObjFileName)
        #btObjFileName
        self.btObjFileNameList[index].updateConfigSetting(pdfEditerUi.btObjFileName)
        
        #lbPdfFilePath
        self.lbPdfFilePathList[index].updateConfigSetting(pdfEditerUi.lbPdfFilePath)
        #txPdfFilePath
        self.txPdfFilePathList[index].updateConfigSetting(pdfEditerUi.txPdfFilePath)
        #btPdfFilePath
        self.btPdfFilePathList[index].updateConfigSetting(pdfEditerUi.btPdfFilePath)
        #cbPdfFilePath
        self.cbPdfFilePathList[index].updateConfigSetting(pdfEditerUi.cbPdfFilePath)
        
        #lbPdfFileName
        self.lbPdfFileNameList[index].updateConfigSetting(pdfEditerUi.lbPdfFileName)
        #txPdfFileName
        self.txPdfFileNameList[index].updateConfigSetting(pdfEditerUi.txPdfFileName)
        #lbPdfFileNote
        self.lbPdfFileNoteList[index].updateConfigSetting(pdfEditerUi.lbPdfFileNote)
        #cbPdfFileName
        self.cbPdfFileNameList[index].updateConfigSetting(pdfEditerUi.cbPdfFileName)
        #cbPdfFileOverWrite
        self.cbPdfFileOverWriteList[index].updateConfigSetting(pdfEditerUi.cbPdfFileOverWrite)
        
        #btExcelSheetSelect
        self.btExcelSheetSelectList[index].updateConfigSetting(pdfEditerUi.btExcelSheetSelect)
        #btObjFile2pdfFile
        self.btObjFile2pdfFileList[index].updateConfigSetting(pdfEditerUi.btObjFile2pdfFile)
        
        #lbUserPassword
        self.lbUserPasswordList[index].updateConfigSetting(pdfEditerUi.lbUserPassword)
        #txEncryptText
        self.txEncryptList[index].updateConfigSetting(pdfEditerUi.txEncryptText)
        
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithmLabelList[index].updateConfigSetting(pdfEditerUi.lbPdfAlgorithmLabel)
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithmList[index].updateConfigSetting(pdfEditerUi.cmbPdfAlgorithm)

        #cbPdfDocAttribSet
        self.cbPdfDocAttribSetList[index].updateConfigSetting(pdfEditerUi.cbPdfDocAttribSet)
        
        #btPdfDocAttribSet
        self.btPdfDocAttribSetList[index].updateConfigSetting(pdfEditerUi.btPdfDocAttribSet)

        #btPdfAuthorSet
        self.btPdfAuthorSetList[index].updateConfigSetting(pdfEditerUi.btPdfAuthorSet)

        #gbEncrypt
        self.gbEncryptList[index].updateConfigSetting(pdfEditerUi.gbEncrypt)

        #暗号なし
        if (pdfEditerUi.rbEncrypt00.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 0
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return

        #rbEncrypt01
        if (pdfEditerUi.rbEncrypt01.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 1
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return

        #rbEncrypt02
        if (pdfEditerUi.rbEncrypt02.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 2
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return

        #rbEncrypt03
        if (pdfEditerUi.rbEncrypt03.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 3
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return

        #rbEncrypt04
        if (pdfEditerUi.rbEncrypt04.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 4
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return

        #rbEncrypt05
        if (pdfEditerUi.rbEncrypt05.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 5
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return

        #rbEncrypt06
        if (pdfEditerUi.rbEncrypt06.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 6
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return
       
        #rbEncrypt07
        if (pdfEditerUi.rbEncrypt07.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 7
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return
       
        #rbEncrypt09
        if (pdfEditerUi.rbEncrypt08.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 8
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return
       
        #rbEncrypt09
        if (pdfEditerUi.rbEncrypt09.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(False)
            pdfEditerUi.txEncrypt2Text.setEnabled(False)
            self.gbEncryptRbIndex[index] = 9
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
            return

        #rbEncryptOther
        if (pdfEditerUi.rbEncryptOther.isChecked()):
            pdfEditerUi.txEncryptText.setEnabled(True)
            pdfEditerUi.txEncrypt2Text.setEnabled(True)
            self.gbEncryptRbIndex[index] = 10
            self.gbEncryptList[index].addLabelProperty("gbEncryptRbIndex",self.gbEncryptRbIndex[index])
        
        return
    
    def updateGUISetting(self, pdfEditerUi:Ui_pdfEditerToolGUI, index:int  = 0 ) -> None:
        #lbObjFileName
        self.lbObjFileNameList[index].updateGUISetting(pdfEditerUi.lbObjFileName)
        #txObjFileName
        self.txObjFileNameList[index].updateGUISetting(pdfEditerUi.txObjFileName)
        #btObjFileName
        self.btObjFileNameList[index].updateGUISetting(pdfEditerUi.btObjFileName)

        #lbPdfFilePath
        self.lbPdfFilePathList[index].updateGUISetting(pdfEditerUi.lbPdfFilePath)
        #txPdfFilePath
        self.txPdfFilePathList[index].updateGUISetting(pdfEditerUi.txPdfFilePath)
        #cbPdfFilePath
        self.cbPdfFilePathList[index].updateGUISetting(pdfEditerUi.cbPdfFilePath)
        #btPdfFilePath
        self.btPdfFilePathList[index].updateGUISetting(pdfEditerUi.btPdfFilePath)
        
        #lbPdfFileName
        self.lbPdfFileNameList[index].updateGUISetting(pdfEditerUi.lbPdfFileName)
        #txPdfFileName
        self.txPdfFileNameList[index].updateGUISetting(pdfEditerUi.txPdfFileName)
        #cbPdfFileName
        self.cbPdfFileNameList[index].updateGUISetting(pdfEditerUi.cbPdfFileName)
        #lbPdfFileNote
        self.lbPdfFileNoteList[index].updateGUISetting(pdfEditerUi.lbPdfFileNote)
        #cbPdfFileOverWrite
        self.cbPdfFileOverWriteList[index].updateGUISetting(pdfEditerUi.cbPdfFileOverWrite)
        
        #btExcelSheetSelect
        self.btExcelSheetSelectList[index].updateGUISetting(pdfEditerUi.btExcelSheetSelect)
        #btObjFile2pdfFile
        self.btObjFile2pdfFileList[index].updateGUISetting(pdfEditerUi.btObjFile2pdfFile)
        
        #lbUserPassword
        self.lbUserPasswordList[index].updateGUISetting(pdfEditerUi.lbUserPassword)
        #txEncryptText
        self.txEncryptList[index].updateGUISetting(pdfEditerUi.txEncryptText)
        
        #lbPdfAlgorithmLabel
        self.lbPdfAlgorithmLabelList[index].updateGUISetting(pdfEditerUi.lbPdfAlgorithmLabel)
        #cmbPdfAlgorithm
        self.cmbPdfAlgorithmList[index].updateGUISetting(pdfEditerUi.cmbPdfAlgorithm)
        
        #cbPdfDocAttribSet
        self.cbPdfDocAttribSetList[index].updateGUISetting(pdfEditerUi.cbPdfDocAttribSet)
        
        #btPdfDocAttribSet
        self.btPdfDocAttribSetList[index].updateGUISetting(pdfEditerUi.btPdfDocAttribSet)
        
        #btPdfAuthorSet
        self.btPdfAuthorSetList[index].updateGUISetting(pdfEditerUi.btPdfAuthorSet)

        #gbEncrypt
        self.gbEncryptList[index].updateGUISetting(pdfEditerUi.gbEncrypt)
        self.gbEncryptRbIndex[index] = int(self.gbEncryptList[index].getLabelValue("gbEncryptRbIndex"))
        
        #rb Checked設定
        match(self.gbEncryptRbIndex[index]):
            case  0: pdfEditerUi.rbEncrypt00.setChecked(True)
            case  1: pdfEditerUi.rbEncrypt01.setChecked(True)
            case  2: pdfEditerUi.rbEncrypt02.setChecked(True)
            case  3: pdfEditerUi.rbEncrypt03.setChecked(True)
            case  4: pdfEditerUi.rbEncrypt04.setChecked(True)
            case  5: pdfEditerUi.rbEncrypt05.setChecked(True)
            case  6: pdfEditerUi.rbEncrypt06.setChecked(True)
            case  7: pdfEditerUi.rbEncrypt07.setChecked(True)
            case  8: pdfEditerUi.rbEncrypt08.setChecked(True)
            case  9: pdfEditerUi.rbEncrypt09.setChecked(True)
            case 10: pdfEditerUi.rbEncryptOther.setChecked(True)
            case _: 
                pdfEditerUi.rbEncrypt00.setChecked(True)
                self.gbEncryptRbIndex[index] = 0
        return
        
    def print(self) :
        return

class logList(xmlLib):
    """ log Setting"""
    #pdf変換失敗エラー
    logPdfConvertErr:xmlQLog
    #暗号無しpdf生成
    logPdfConvertWithoutEncrypt:xmlQLog
    #暗号番号が存在しているエラー
    logPdfWithEncryptErr:xmlQLog
    #暗号ありpdf生成
    logPdfConvertWithEncrypt:xmlQLog
    #暗号番号が存在していないエラー
    logPdfWithoutEncryptErr:xmlQLog
    #復唱化失敗
    logPdfDecryptErr:xmlQLog
    #復唱化成功
    logPdfDecrypt:xmlQLog
    #拡張子判定エラー
    logPdfExtensionErr:xmlQLog

    def __init__(self)-> None:
 
        super(logList, self).__init__()

        #pdf変換失敗エラー
        self.logPdfConvertErrName = "logPdfConvertErr" 
        self.logPdfConvertErrText = "対象ファイルをPDFファイルへ変換失敗\n" +"変換失敗理由:\n" + "下記のファイルが解析失敗、ファイル内容が正しいかどうかをご確認ください\n" + "__officeFileName__"

        #暗号無しpdf生成
        self.logPdfConvertWithoutEncryptName = "logPdfConvertWithoutEncrypt" 
        self.logPdfConvertWithoutEncryptText = "対象ファイルを下記のPDFファイルへ変換しました\n" + "__pdfFileName__"

        #暗号ありpdf生成
        self.logPdfConvertWithEncryptName = "logPdfConvertWithEncrypt" 
        self.logPdfConvertWithEncryptText = "生成結果詳細は以下通りです。\n" + "生成ファイル名称:__pdfFileName__\n" + "暗号化ラベル:__algorithmLabel__\n" + "user password:__encryptNumber__\n" + "owner password:__encrypt2Number__\n"

        #暗号番号が存在しているエラー
        self.logPdfWithEncryptErrName = "logPdfWithEncryptErr" 
        self.logPdfWithEncryptErrText = "下記の対象ファイルはすでに暗号された。\n"+ "ファイル名称:__pdfFileName__"

        #暗号番号が存在していないエラー
        self.logPdfWithoutEncryptErrName = "logPdfWithoutEncryptErr" 
        self.logPdfWithoutEncryptErrText = "下記の対象ファイルは暗号無し。\n"+ "ファイル名称:__pdfFileName__"

        #復唱化失敗
        self.logPdfDecryptErrName = "logPdfDecryptErr" 
        self.logPdfDecryptErrText = "復唱化実施失敗。\n" + "下記ファイルのパスワードをご確認ください\n" + "__pdfFileName__"

        #復唱化成功
        self.logPdfDecryptName = "logPdfDecrypt" 
        self.logPdfDecryptText = "復唱化されたファイルは以下通りです。\n" + "生成ファイル名称：\n" + "__pdfFileName__"

        #拡張子判定エラー
        self.logPdfExtensionErrName = "logPdfExtensionErr" 
        self.logPdfExtensionErrText = "__ObjFileTitle__" + "内容取得失敗\n" + "取得失敗理由：\n" + "下記ファイルの拡張子が間違いました：\n" + "__pdfFileName__"


        self.createConfigSetting()
        return

    def createConfigSetting(self) -> None:
        #pdf変換失敗エラー
        self.logPdfConvertErr = xmlQLog(self.logPdfConvertErrName, self.logPdfConvertErrText)
        #暗号無しpdf生成
        self.logPdfConvertWithoutEncrypt = xmlQLog(self.logPdfConvertWithoutEncryptName, self.logPdfConvertWithoutEncryptText)
        #暗号ありpdf生成
        self.logPdfConvertWithEncrypt = xmlQLog(self.logPdfConvertWithEncryptName, self.logPdfConvertWithEncryptText)
        #暗号番号が存在しているエラー
        self.logPdfWithEncryptErr = xmlQLog(self.logPdfWithEncryptErrName, self.logPdfWithEncryptErrText)
        #暗号番号が存在していないエラー
        self.logPdfWithoutEncryptErr = xmlQLog(self.logPdfWithoutEncryptErrName, self.logPdfWithoutEncryptErrText)
        #復唱化失敗
        self.logPdfDecryptErr = xmlQLog(self.logPdfDecryptErrName, self.logPdfDecryptErrText)
        #復唱化成功
        self.logPdfDecrypt = xmlQLog(self.logPdfDecryptName, self.logPdfDecryptText)
        #拡張子判定エラー
        self.logPdfExtensionErr = xmlQLog(self.logPdfExtensionErrName, self.logPdfExtensionErrText) 
        return

    def getConfigSetting(self, eleTool:Element|None)-> None:

        if eleTool is None :
            return
        
        #pdf変換失敗エラー
        self.logPdfConvertErr.getConfigSetting(eleTool, self.logPdfConvertErrName)
        self.logPdfConvertErrText = self.logPdfConvertErr.getLabelValue('Text')

        #暗号無しpdf生成
        self.logPdfConvertWithoutEncrypt.getConfigSetting(eleTool, self.logPdfConvertWithoutEncryptName)
        self.logPdfConvertWithoutEncryptText = self.logPdfConvertWithoutEncrypt.getLabelValue('Text')

        #暗号ありpdf生成
        self.logPdfConvertWithEncrypt.getConfigSetting(eleTool, self.logPdfConvertWithEncryptName)
        self.logPdfConvertWithEncryptText = self.logPdfConvertWithEncrypt.getLabelValue('Text')

        #暗号番号が存在していないエラー
        self.logPdfWithoutEncryptErr.getConfigSetting(eleTool, self.logPdfWithoutEncryptErrName)
        self.logPdfWithoutEncryptErrText = self.logPdfWithoutEncryptErr.getLabelValue('Text')

        #復唱化失敗
        self.logPdfDecryptErr.getConfigSetting(eleTool, self.logPdfDecryptErrName)
        self.logPdfDecryptErrText = self.logPdfDecryptErr.getLabelValue('Text')

        #復唱化成功
        self.logPdfDecrypt.getConfigSetting(eleTool, self.logPdfDecryptName)
        self.logPdfDecryptText = self.logPdfDecrypt.getLabelValue('Text')

        #拡張子判定エラー
        self.logPdfExtensionErr.getConfigSetting(eleTool, self.logPdfExtensionErrName)
        self.logPdfExtensionErrText = self.logPdfExtensionErr.getLabelValue('Text')
        return
    
    def outputConfigSetting(self, eleLogList:Element)-> None:
        comment = ET.Comment('ログ内容設定')
        eleLogList.append(comment)
        self.logPdfConvertErr.outputConfigSetting(eleLogList)
        self.logPdfConvertWithoutEncrypt.outputConfigSetting(eleLogList)
        self.logPdfWithEncryptErr.outputConfigSetting(eleLogList)
        self.logPdfConvertWithEncrypt.outputConfigSetting(eleLogList)
        self.logPdfWithoutEncryptErr.outputConfigSetting(eleLogList)
        self.logPdfDecryptErr.outputConfigSetting(eleLogList)
        self.logPdfDecrypt.outputConfigSetting(eleLogList)
        self.logPdfExtensionErr.outputConfigSetting(eleLogList)
        return
       
    def updateConfigSetting(self) -> None:
        return
    
    def updateGUISetting(self) -> None:
        return


class pdfEditerToolConfig():
    
    def __init__(self, configFileAddress:str, pdfEditerToolGUI:Ui_pdfEditerToolGUI)-> None:
        super(pdfEditerToolConfig, self).__init__()
        self.FSP = FileSysProcess()
        #self.pdfETConfig = pdfEditerToolConfig(os.getcwd() + "\Jp\pdfEditerToolGUI_Jp.xml",self)
        self.CreateFileAddress = configFileAddress + "\\pdfEditerToolGUI_Jp.xml"
        if self.FSP.judgeFileExsit(self.CreateFileAddress) :
            self.configFileAddress = self.CreateFileAddress
        else :
            self.configFileAddress = configFileAddress + "\\Jp\\pdfEditerToolGUI_Jp.xml"

        self.ui = pdfEditerToolGUI
        self.menubarList = menubarList()
        self.encryptButtonList = encryptButtonList(pdfEditerToolGUI)
        self.algorithmLabelList = algorithmLabelList()
        self.actionToolList = actionToolList(self.menubarList)
        self.logList = logList()
        return
        
    def getConfigSetting(self) -> bool:
        bResult = True
        try:
            tree = ET.parse(self.configFileAddress)
            elePdfEditerGUI =  tree.getroot()
            eleMenubarList = elePdfEditerGUI.find("menubarList")
            self.menubarList.getConfigSetting(eleMenubarList)
            eleEncryptNumberList = elePdfEditerGUI.find("encryptNumberList")
            self.encryptButtonList.getConfigSetting(eleEncryptNumberList)
            eleAlgorithmLabelList = elePdfEditerGUI.find("algorithmLabelList")
            self.algorithmLabelList.getConfigSetting(eleAlgorithmLabelList)
            eleActionToolList = elePdfEditerGUI.find("actionToolList")
            self.actionToolList.getConfigSetting(eleActionToolList)
            eleLogList = elePdfEditerGUI.find("LogList")
            self.logList.getConfigSetting(eleLogList)

        except Exception as e:
            bResult = False  
        return bResult
    
    def outputConfigSetting(self) -> None:
        #ツール名称
        elePdfEditerGUI = Element("pdfEditerGUI")

        #【メニューバー】GUI作成
        comment = ET.Comment('【メニューバー】GUI')
        elePdfEditerGUI.append(comment)
        eleMenubar = Element("menubarList")
        self.menubarList.outputConfigSetting(eleMenubar)
        elePdfEditerGUI.append(eleMenubar)

        #【暗号化設定リスト】GUI作成
        comment = ET.Comment('【暗号化設定リスト】GUI')
        elePdfEditerGUI.append(comment)
        eleEncryptButton = Element("encryptNumberList")
        self.encryptButtonList.outputConfigSetting(eleEncryptButton)
        elePdfEditerGUI.append(eleEncryptButton)

        #【暗号化ラベル】GUI作成
        comment = ET.Comment('【暗号化ラベル】GUI')
        elePdfEditerGUI.append(comment)
        eleAlgorithmLabelList = Element("algorithmLabelList")
        self.algorithmLabelList.outputConfigSetting(eleAlgorithmLabelList)
        elePdfEditerGUI.append(eleAlgorithmLabelList)

        #【各pdfツール設定】GUI作成
        comment = ET.Comment('【各pdfツール設定】GUI')
        elePdfEditerGUI.append(comment)
        eleActionToolList = Element("actionToolList")
        self.actionToolList.outputConfigSetting(eleActionToolList)
        elePdfEditerGUI.append(eleActionToolList)

        #【LogList】設定
        comment = ET.Comment('【LogList】設定')
        elePdfEditerGUI.append(comment)
        eleLogList = Element("LogList")
        self.logList.outputConfigSetting(eleLogList)
        elePdfEditerGUI.append(eleLogList)

        #ElementTreeを追加
        ET.indent(elePdfEditerGUI)
        tree = ElementTree(elePdfEditerGUI)
    
        #ファイル出力
        with open (self.CreateFileAddress, "wb") as xmlFileAddr :
            tree.write(xmlFileAddr, encoding='utf-8', xml_declaration=True)
        return
        
    def updateConfigSetting(self, pdfEditerToolType:int = 0) -> None:
        self.menubarList.updateConfigSetting(self.ui, pdfEditerToolType)
        self.actionToolList.updateConfigSetting(self.ui, pdfEditerToolType)
        self.algorithmLabelList.updateConfigSetting(self.ui, pdfEditerToolType)
        self.encryptButtonList.updateConfigSetting(self.ui, pdfEditerToolType)
        self.logList.updateConfigSetting()
        return

    def updateGUISetting(self, pdfEditerToolType:int = 0) -> None:
        self.menubarList.updateGUISetting(self.ui)
        self.encryptButtonList.updateGUISetting(self.ui)
        self.algorithmLabelList.updateGUISetting(self.ui)
        self.actionToolList.updateGUISetting(self.ui, pdfEditerToolType)
        self.logList.updateGUISetting()
        return
        
    def print(self)-> None:
        #self.menubarList.print()
        return
        
