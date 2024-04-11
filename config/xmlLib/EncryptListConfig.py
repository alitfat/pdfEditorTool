import xml.etree.ElementTree as ET
from xml.etree.ElementTree import  ElementTree,Element
from config.xmlLib.xmlLib import xmlLib
from config.xmlLib.xmlQtLib import xmlQWidget, xmlQTextEdit,xmlQLabel,xmlQPushButton, xmlQCheckBox
from GUI.pdfEditerToolGUI_EncryptListSetting import pdfEditorTool_EncryptListSetting as EncryptListUi

from Lib.FileSysProcess import FileSysProcess

class toolNameLib(xmlLib):
    #ツール名称
    widTool:xmlQWidget
    """ toolName Setting"""
    def __init__(self)-> None:
 
        super(toolNameLib, self).__init__()

        #ツール名称
        self.toolName = "widTool" 
        self.toolTitle = "EncryptListSetting"
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
       
    def updateConfigSetting(self, encryptListUi:EncryptListUi) -> None:
        toolNameText = encryptListUi.windowTitle()
        self.widTool.modifyLabelProperty('WindowTitle', toolNameText)
        return
    
    def updateGUISetting(self, encryptListUi:EncryptListUi) -> None:
        toolNameText = self.widTool.getLabelValue('WindowTitle')
        encryptListUi.setWindowTitle(toolNameText)
        return

class actionToolList(xmlLib):

    #タイトル
    #lbRbIndex(Index)
    lbRbIndex:xmlQLabel
    #lbRbComment(表示内容)b 
    lbRbComment:xmlQLabel
    #lbRbUserPassword(UserPassword)
    lbRbUserPassword:xmlQLabel
    #lbRbOwnerPassword(OwnerPassword)
    lbRbOwnerPassword:xmlQLabel
    #lbRbProHidden(表示/非表示)
    lbRbProHidden:xmlQLabel
    
    
    #Rb0
    #lbRb0Index(Index)
    lbRb0Index:xmlQLabel
    #txRb0Comment(表示内容)
    txRb0Comment:xmlQTextEdit
    #txRb0UserPassword(UserPassword)
    txRb0UserPassword:xmlQTextEdit
    #txRb0OwnerPassword(OwnerPassword)
    txRb0OwnerPassword:xmlQTextEdit
    #cbRb0ProHidden(表示/非表示)
    cbRb0ProHidden:xmlQCheckBox
    
    #Rb1
    #lbRb1Index(Index)
    lbRb1Index:xmlQLabel
    #txRb1Comment(表示内容)
    txRb1Comment:xmlQTextEdit
    #txRb1UserPassword(UserPassword)
    txRb1UserPassword:xmlQTextEdit
    #txRb1OwnerPassword(OwnerPassword)
    txRb1OwnerPassword:xmlQTextEdit
    #cbRb1ProHidden(表示/非表示)
    cbRb1ProHidden:xmlQCheckBox
    
    #Rb2
    #lbRb2Index(Index)
    lbRb2Index:xmlQLabel
    #txRb2Comment(表示内容)
    txRb2Comment:xmlQTextEdit
    #txRb2UserPassword(UserPassword)
    txRb2UserPassword:xmlQTextEdit
    #txRb2OwnerPassword(OwnerPassword)
    txRb2OwnerPassword:xmlQTextEdit
    #cbRb2ProHidden(表示/非表示)
    cbRb2ProHidden:xmlQCheckBox
    
    #Rb3
    #lbRb3Index(Index)
    lbRb3Index:xmlQLabel
    #txRb3Comment(表示内容)
    txRb3Comment:xmlQTextEdit
    #txRb3UserPassword(UserPassword)
    txRb3UserPassword:xmlQTextEdit
    #txRb3OwnerPassword(OwnerPassword)
    txRb3OwnerPassword:xmlQTextEdit
    #cbRb3ProHidden(表示/非表示)
    cbRb3ProHidden:xmlQCheckBox
    
    #Rb4
    #lbRb4Index(Index)
    lbRb4Index:xmlQLabel
    #txRb4Comment(表示内容)
    txRb4Comment:xmlQTextEdit
    #txRb4UserPassword(UserPassword)
    txRb4UserPassword:xmlQTextEdit
    #txRb4OwnerPassword(OwnerPassword)
    txRb4OwnerPassword:xmlQTextEdit
    #cbRb4ProHidden(表示/非表示)
    cbRb4ProHidden:xmlQCheckBox

    #Rb5
    #lbRb5Index(Index)
    lbRb5Index:xmlQLabel
    #txRb5Comment(表示内容)
    txRb5Comment:xmlQTextEdit
    #txRb5UserPassword(UserPassword)
    txRb5UserPassword:xmlQTextEdit
    #txRb5OwnerPassword(OwnerPassword)
    txRb5OwnerPassword:xmlQTextEdit
    #cbRb5ProHidden(表示/非表示)
    cbRb5ProHidden:xmlQCheckBox

    #Rb6
    #lbRb6Index(Index)
    lbRb6Index:xmlQLabel
    #txRb6Comment(表示内容)
    txRb6Comment:xmlQTextEdit
    #txRb6UserPassword(UserPassword)
    txRb6UserPassword:xmlQTextEdit
    #txRb6OwnerPassword(OwnerPassword)
    txRb6OwnerPassword:xmlQTextEdit
    #cbRb6ProHidden(表示/非表示)
    cbRb6ProHidden:xmlQCheckBox

    #Rb7
    #lbRb7Index(Index)
    lbRb7Index:xmlQLabel
    #txRb7Comment(表示内容)
    txRb7Comment:xmlQTextEdit
    #txRb7UserPassword(UserPassword)
    txRb7UserPassword:xmlQTextEdit
    #txRb7OwnerPassword(OwnerPassword)
    txRb7OwnerPassword:xmlQTextEdit
    #cbRb7ProHidden(表示/非表示)
    cbRb7ProHidden:xmlQCheckBox

    #Rb8
    #lbRb8Index(Index)
    lbRb8Index:xmlQLabel
    #txRb8Comment(表示内容)
    txRb8Comment:xmlQTextEdit
    #txRb8UserPassword(UserPassword)
    txRb8UserPassword:xmlQTextEdit
    #txRb8OwnerPassword(OwnerPassword)
    txRb8OwnerPassword:xmlQTextEdit
    #cbRb8ProHidden(表示/非表示)
    cbRb8ProHidden:xmlQCheckBox

    #Rb9
    #lbRb9Index(Index)
    lbRb9Index:xmlQLabel
    #txRb9Comment(表示内容)
    txRb9Comment:xmlQTextEdit
    #txRb9UserPassword(UserPassword)
    txRb9UserPassword:xmlQTextEdit
    #txRb9OwnerPassword(OwnerPassword)
    txRb9OwnerPassword:xmlQTextEdit
    #cbRb9ProHidden(表示/非表示)
    cbRb9ProHidden:xmlQCheckBox

    #Rb10
    #lbRb10Index(Index)
    lbRb10Index:xmlQLabel
    #txRb10Comment(表示内容)
    txRb10Comment:xmlQTextEdit
    #txRb10UserPassword(UserPassword)
    txRb10UserPassword:xmlQTextEdit
    #txRb10OwnerPassword(OwnerPassword)
    txRb10OwnerPassword:xmlQTextEdit
    #cbRb10ProHidden(表示/非表示)
    cbRb10ProHidden:xmlQCheckBox


    #btExecution(確定)
    btExecution:xmlQPushButton
    
    def __init__(self)-> None:
        super(actionToolList, self).__init__()
        #タイトル設定
        self.__init_title()

        #Rb設定
        self.__init_Rb0()
        self.__init_Rb1()
        self.__init_Rb2()
        self.__init_Rb3()
        self.__init_Rb4()
        self.__init_Rb5()
        self.__init_Rb6()
        self.__init_Rb7()
        self.__init_Rb8()
        self.__init_Rb9()
        self.__init_Rb10()

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

        #Rb設定
        self.__createConfigSetting_Rb0()
        self.__createConfigSetting_Rb1()
        self.__createConfigSetting_Rb2()
        self.__createConfigSetting_Rb3()
        self.__createConfigSetting_Rb4()
        self.__createConfigSetting_Rb5()
        self.__createConfigSetting_Rb6()
        self.__createConfigSetting_Rb7()
        self.__createConfigSetting_Rb8()
        self.__createConfigSetting_Rb9()
        self.__createConfigSetting_Rb10()

        #btExecution(確定)
        self.__createConfigSetting_Execution()
        return
        
        
    def getConfigSetting(self, eleActionTool:Element|None)-> None:
        if eleActionTool is None :
            return
        #タイトル設定
        self.__getConfigSetting_title(eleActionTool)

        #Rb設定
        self.__getConfigSetting_Rb0(eleActionTool)
        self.__getConfigSetting_Rb1(eleActionTool)
        self.__getConfigSetting_Rb2(eleActionTool)
        self.__getConfigSetting_Rb3(eleActionTool)
        self.__getConfigSetting_Rb4(eleActionTool)
        self.__getConfigSetting_Rb5(eleActionTool)
        self.__getConfigSetting_Rb6(eleActionTool)
        self.__getConfigSetting_Rb7(eleActionTool)
        self.__getConfigSetting_Rb8(eleActionTool)
        self.__getConfigSetting_Rb9(eleActionTool)
        self.__getConfigSetting_Rb10(eleActionTool)

        #btExecution(確定)
        self.__getConfigSetting_Execution(eleActionTool)
        return
        
    def outputConfigSetting(self, eleActionTool:Element) -> None:
        #タイトル設定
        self.__outputConfigSetting_title(eleActionTool)

        #Rb設定
        self.__outputConfigSetting_Rb0(eleActionTool)
        self.__outputConfigSetting_Rb1(eleActionTool)
        self.__outputConfigSetting_Rb2(eleActionTool)
        self.__outputConfigSetting_Rb3(eleActionTool)
        self.__outputConfigSetting_Rb4(eleActionTool)
        self.__outputConfigSetting_Rb5(eleActionTool)
        self.__outputConfigSetting_Rb6(eleActionTool)
        self.__outputConfigSetting_Rb7(eleActionTool)
        self.__outputConfigSetting_Rb8(eleActionTool)
        self.__outputConfigSetting_Rb9(eleActionTool)
        self.__outputConfigSetting_Rb10(eleActionTool)


        #btExecution(確定)
        self.__outputConfigSetting_Execution(eleActionTool)
        return
    
    def updateConfigSetting(self, encryptListUi:EncryptListUi) -> None:
        #タイトル設定
        self.__updateConfigSetting_title(encryptListUi)

        #Rb設定
        self.__updateConfigSetting_Rb0(encryptListUi)
        self.__updateConfigSetting_Rb1(encryptListUi)
        self.__updateConfigSetting_Rb2(encryptListUi)
        self.__updateConfigSetting_Rb3(encryptListUi)
        self.__updateConfigSetting_Rb4(encryptListUi)
        self.__updateConfigSetting_Rb5(encryptListUi)
        self.__updateConfigSetting_Rb6(encryptListUi)
        self.__updateConfigSetting_Rb7(encryptListUi)
        self.__updateConfigSetting_Rb8(encryptListUi)
        self.__updateConfigSetting_Rb9(encryptListUi)
        self.__updateConfigSetting_Rb10(encryptListUi)


        #btExecution(確定)
        self.__updateConfigSetting_Execution(encryptListUi)
        return
    
    def updateGUISetting(self, encryptListUi:EncryptListUi) -> None:
        #タイトル設定
        self.__updateGUISetting_title(encryptListUi)

        #Rb設定
        self.__updateGUISetting_Rb0(encryptListUi)
        self.__updateGUISetting_Rb1(encryptListUi)
        self.__updateGUISetting_Rb2(encryptListUi)
        self.__updateGUISetting_Rb3(encryptListUi)
        self.__updateGUISetting_Rb4(encryptListUi)
        self.__updateGUISetting_Rb5(encryptListUi)
        self.__updateGUISetting_Rb6(encryptListUi)
        self.__updateGUISetting_Rb7(encryptListUi)
        self.__updateGUISetting_Rb8(encryptListUi)
        self.__updateGUISetting_Rb9(encryptListUi)
        self.__updateGUISetting_Rb10(encryptListUi)

        #btExecution(確定)
        self.__updateGUISetting_Execution(encryptListUi)
        return

    def __init_title(self) -> None:
        #lbRbIndex(Index)
        self.lbRbIndexName = "lbRbIndex" 
        self.lbRbIndexText = "Index"
        self.lbRbIndexHidden = False

        #lbRbComment(表示内容)
        self.lbRbCommentName = "lbRbComment" 
        self.lbRbCommentText = "ShowComment"
        self.lbRbCommentHidden = False

        #lbRbUserPassword(UserPassword)
        self.lbRbUserPasswordName = "lbRbUserPassword" 
        self.lbRbUserPasswordText = "UserPassword"
        self.lbRbUserPasswordHidden = False
        
        #lbRbOwnerPassword(OwnerPassword)
        self.lbRbOwnerPasswordName = "lbRbOwnerPassword" 
        self.lbRbOwnerPasswordText = "OwnerPassword"
        self.lbRbOwnerPasswordHidden = False
        
        #lbRbProHidden(表示/非表示)
        self.lbRbProHiddenName = "lbRbProHidden" 
        self.lbRbProHiddenText = "HiddenSetting"
        self.lbRbProHiddenHidden = False
        
        return

    def __createConfigSetting_title(self) -> None:
        
        #lbRbIndex(Index)
        self.lbRbIndex = xmlQLabel(self.lbRbIndexName,
                                   self.lbRbIndexText,
                                   self.lbRbIndexHidden)
        
        #lbRbComment(表示内容)
        self.lbRbComment = xmlQLabel(self.lbRbCommentName,
                                     self.lbRbCommentText,
                                     self.lbRbCommentHidden)

        #lbRbUserPassword(UserPassword)
        self.lbRbUserPassword = xmlQLabel(self.lbRbUserPasswordName,
                                          self.lbRbUserPasswordText,
                                          self.lbRbUserPasswordHidden)

        #lbRbOwnerPassword(OwnerPassword)
        self.lbRbOwnerPassword = xmlQLabel(self.lbRbOwnerPasswordName,
                                           self.lbRbOwnerPasswordText,
                                           self.lbRbOwnerPasswordHidden)

        #lbRbProHidden(表示/非表示)
        self.lbRbProHidden = xmlQLabel(self.lbRbProHiddenName,
                                       self.lbRbProHiddenText,
                                       self.lbRbProHiddenHidden)
        
        return
    
    def __getConfigSetting_title(self, eleActionTool:Element)-> None:

        #lbRbIndex(Index)
        self.lbRbIndex.getConfigSetting(eleActionTool, self.lbRbIndexName)
        
        #lbRbComment(表示内容)
        self.lbRbComment.getConfigSetting(eleActionTool, self.lbRbCommentName)
        
        #lbRbUserPassword(UserPassword)
        self.lbRbUserPassword.getConfigSetting(eleActionTool, self.lbRbUserPasswordName)
        
        #lbRbOwnerPassword(OwnerPassword)
        self.lbRbOwnerPassword.getConfigSetting(eleActionTool, self.lbRbOwnerPasswordName)
        
        #lbRbProHidden(表示/非表示)
        self.lbRbProHidden.getConfigSetting(eleActionTool, self.lbRbProHiddenName)

        return
    
    def __outputConfigSetting_title(self, eleActionTool:Element) -> None:
        #タイトル
        comment = ET.Comment('【タイトル】設定')
        eleActionTool.append(comment)

        #lbRbIndex(Index)
        self.lbRbIndex.outputConfigSetting(eleActionTool)
        
        #lbRbComment(表示内容)
        self.lbRbComment.outputConfigSetting(eleActionTool)
        
        #lbRbUserPassword(UserPassword)
        self.lbRbUserPassword.outputConfigSetting(eleActionTool)
        
        #lbRbOwnerPassword(OwnerPassword)
        self.lbRbOwnerPassword.outputConfigSetting(eleActionTool)
        
        #lbRbProHidden(表示/非表示)
        self.lbRbProHidden.outputConfigSetting(eleActionTool)

        return
    
    def __updateConfigSetting_title(self, encryptListUi:EncryptListUi) -> None:
        
        #lbRbIndex(Index)
        self.lbRbIndex.updateConfigSetting(encryptListUi.lbRbIndex)
        #lbRbComment(表示内容)
        self.lbRbComment.updateConfigSetting(encryptListUi.lbRbComment)
        #lbRbUserPassword(UserPassword)
        self.lbRbUserPassword.updateConfigSetting(encryptListUi.lbRbUserPassword)
        #lbRbOwnerPassword(OwnerPassword)
        self.lbRbOwnerPassword.updateConfigSetting(encryptListUi.lbRbOwnerPassword)
        #lbRbProHidden(表示/非表示)
        self.lbRbProHidden.updateConfigSetting(encryptListUi.lbRbProHidden)

        return
    
    def __updateGUISetting_title(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRbIndex(Index)
        self.lbRbIndex.updateGUISetting(encryptListUi.lbRbIndex)
        #lbRbComment(表示内容)
        self.lbRbComment.updateGUISetting(encryptListUi.lbRbComment)
        #lbRbUserPassword(UserPassword)
        self.lbRbUserPassword.updateGUISetting(encryptListUi.lbRbUserPassword)
        #lbRbOwnerPassword(OwnerPassword)
        self.lbRbOwnerPassword.updateGUISetting(encryptListUi.lbRbOwnerPassword)
        #lbRbProHidden(表示/非表示)
        self.lbRbProHidden.updateGUISetting(encryptListUi.lbRbProHidden)
        return

    def __init_Rb0(self) -> None:

        #lbRb0Index(Index)
        self.lbRb0IndexName = "lbRb0Index" 
        self.lbRb0IndexText = "Rb0"
        self.lbRb0IndexHidden = False

        #txRb0Comment(表示内容)
        self.txRb0CommentName = "txRb0Comment"
        self.txRb0CommentText = ""
        self.txRb0CommentEnabled = True
        self.txRb0CommentHidden = False

        #txRb0UserPassword(UserPassword)
        self.txRb0UserPasswordName = "txRb0UserPassword"
        self.txRb0UserPasswordText = ""
        self.txRb0UserPasswordEnabled = True
        self.txRb0UserPasswordHidden = False
        
        #txRb0OwnerPassword(OwnerPassword)
        self.txRb0OwnerPasswordName = "txRb0OwnerPassword"
        self.txRb0OwnerPasswordText = ""
        self.txRb0OwnerPasswordEnabled = True
        self.txRb0OwnerPasswordHidden = False
        
        #cbRb0ProHidden(表示/非表示)
        self.cbRb0ProHiddenName = "cbRb0ProHidden"
        self.cbRb0ProHiddenText = "select"
        self.cbRb0ProHiddenChecked = False
        self.cbRb0ProHiddenEnabled = True
        self.cbRb0ProHiddenHidden = False

        return

    def __createConfigSetting_Rb0(self) -> None:
        #lbRb0Index(Index)
        self.lbRb0Index = xmlQLabel(self.lbRb0IndexName,
                                    self.lbRb0IndexText,
                                    self.lbRb0IndexHidden)

        #txRb0Comment(表示内容)
        self.txRb0Comment = xmlQTextEdit(self.txRb0CommentName,
                                         self.txRb0CommentText,
                                         self.txRb0CommentEnabled,
                                         self.txRb0CommentHidden)
        self.txRb0Comment.delLabelProperty("Text")

        #txRb0UserPassword(UserPassword)
        self.txRb0UserPassword = xmlQTextEdit(self.txRb0UserPasswordName,
                                              self.txRb0UserPasswordText,
                                              self.txRb0UserPasswordEnabled,
                                              self.txRb0UserPasswordHidden)
        self.txRb0UserPassword.delLabelProperty("Text")

        #txRb0OwnerPassword(OwnerPassword)
        self.txRb0OwnerPassword = xmlQTextEdit(self.txRb0OwnerPasswordName,
                                               self.txRb0OwnerPasswordText,
                                               self.txRb0OwnerPasswordEnabled,
                                               self.txRb0OwnerPasswordHidden)
        self.txRb0OwnerPassword.delLabelProperty("Text")

        #cbRb0ProHidden(表示/非表示)
        self.cbRb0ProHidden = xmlQCheckBox(self.cbRb0ProHiddenName,
                                           self.cbRb0ProHiddenText,
                                           self.cbRb0ProHiddenChecked,
                                           self.cbRb0ProHiddenEnabled,
                                           self.cbRb0ProHiddenHidden)
        self.cbRb0ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb0(self, eleActionTool:Element)-> None:
        #lbRb0Index(Index)
        self.lbRb0Index.getConfigSetting(eleActionTool, self.lbRb0IndexName)
        #txRb0Comment(表示内容)
        self.txRb0Comment.getConfigSetting(eleActionTool, self.txRb0CommentName)
        #txRb0UserPassword(UserPassword)
        self.txRb0UserPassword.getConfigSetting(eleActionTool, self.txRb0UserPasswordName)
        #txRb0OwnerPassword(OwnerPassword)
        self.txRb0OwnerPassword.getConfigSetting(eleActionTool, self.txRb0OwnerPasswordName)
        #cbRb0ProHidden(表示/非表示)
        self.cbRb0ProHidden.getConfigSetting(eleActionTool, self.cbRb0ProHiddenName)
        return
    
    def __outputConfigSetting_Rb0(self, eleActionTool:Element) -> None:

        #【Rb0】設定
        comment = ET.Comment('【Rb0】設定')
        eleActionTool.append(comment)
        #lbRb0Index(Index)
        self.lbRb0Index.outputConfigSetting(eleActionTool) 
        #txRb0Comment(表示内容)
        self.txRb0Comment.outputConfigSetting(eleActionTool) 
        #txRb0UserPassword(UserPassword)
        self.txRb0UserPassword.outputConfigSetting(eleActionTool) 
        #txRb0OwnerPassword(OwnerPassword)
        self.txRb0OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb0ProHidden(表示/非表示)
        self.cbRb0ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb0(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb0Index(Index)
        self.lbRb0Index.updateConfigSetting(encryptListUi.lbRb0Index)
        #txRb0Comment(表示内容)
        self.txRb0Comment.updateConfigSetting(encryptListUi.txRb0Comment)
        #txRb0UserPassword(UserPassword)
        self.txRb0UserPassword.updateConfigSetting(encryptListUi.txRb0UserPassword)
        #txRb0OwnerPassword(OwnerPassword)
        self.txRb0OwnerPassword.updateConfigSetting(encryptListUi.txRb0OwnerPassword)
        #cbRb0ProHidden(表示/非表示)
        self.cbRb0ProHidden.updateConfigSetting(encryptListUi.cbRb0ProHidden)
        return
    
    def __updateGUISetting_Rb0(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb0Index(Index)
        self.lbRb0Index.updateGUISetting(encryptListUi.lbRb0Index)
        #txRb0Comment(表示内容)
        self.txRb0Comment.updateGUISetting(encryptListUi.txRb0Comment)
        #txRb0UserPassword(UserPassword)
        self.txRb0UserPassword.updateGUISetting(encryptListUi.txRb0UserPassword)
        #txRb0OwnerPassword(OwnerPassword)
        self.txRb0OwnerPassword.updateGUISetting(encryptListUi.txRb0OwnerPassword)
        #cbRb0ProHidden(表示/非表示)
        self.cbRb0ProHidden.updateGUISetting(encryptListUi.cbRb0ProHidden)
        return


    def __init_Rb1(self) -> None:

        #lbRb1Index(Index)
        self.lbRb1IndexName = "lbRb1Index" 
        self.lbRb1IndexText = "Rb1"
        self.lbRb1IndexHidden = False

        #txRb1Comment(表示内容)
        self.txRb1CommentName = "txRb1Comment"
        self.txRb1CommentText = ""
        self.txRb1CommentEnabled = True
        self.txRb1CommentHidden = False

        #txRb1UserPassword(UserPassword)
        self.txRb1UserPasswordName = "txRb1UserPassword"
        self.txRb1UserPasswordText = ""
        self.txRb1UserPasswordEnabled = True
        self.txRb1UserPasswordHidden = False
        
        #txRb1OwnerPassword(OwnerPassword)
        self.txRb1OwnerPasswordName = "txRb1OwnerPassword"
        self.txRb1OwnerPasswordText = ""
        self.txRb1OwnerPasswordEnabled = True
        self.txRb1OwnerPasswordHidden = False
        
        #cbRb1ProHidden(表示/非表示)
        self.cbRb1ProHiddenName = "cbRb1ProHidden"
        self.cbRb1ProHiddenText = "select"
        self.cbRb1ProHiddenChecked = False
        self.cbRb1ProHiddenEnabled = True
        self.cbRb1ProHiddenHidden = False

        return

    def __createConfigSetting_Rb1(self) -> None:
    
        #lbRb1Index(Index)
        self.lbRb1Index = xmlQLabel(self.lbRb1IndexName,
                                    self.lbRb1IndexText,
                                    self.lbRb1IndexHidden)

        #txRb1Comment(表示内容)
        self.txRb1Comment = xmlQTextEdit(self.txRb1CommentName,
                                         self.txRb1CommentText,
                                         self.txRb1CommentEnabled,
                                         self.txRb1CommentHidden)
        self.txRb1Comment.delLabelProperty("Text")

        #txRb1UserPassword(UserPassword)
        self.txRb1UserPassword = xmlQTextEdit(self.txRb1UserPasswordName,
                                              self.txRb1UserPasswordText,
                                              self.txRb1UserPasswordEnabled,
                                              self.txRb1UserPasswordHidden)
        self.txRb1UserPassword.delLabelProperty("Text")

        #txRb1OwnerPassword(OwnerPassword)
        self.txRb1OwnerPassword = xmlQTextEdit(self.txRb1OwnerPasswordName,
                                               self.txRb1OwnerPasswordText,
                                               self.txRb1OwnerPasswordEnabled,
                                               self.txRb1OwnerPasswordHidden)
        self.txRb1OwnerPassword.delLabelProperty("Text")

        #cbRb1ProHidden(表示/非表示)
        self.cbRb1ProHidden = xmlQCheckBox(self.cbRb1ProHiddenName, 
                                           self.cbRb1ProHiddenText,
                                           self.cbRb1ProHiddenChecked,
                                           self.cbRb1ProHiddenEnabled,
                                           self.cbRb1ProHiddenHidden)
        self.cbRb1ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb1(self, eleActionTool:Element)-> None:
    
        #lbRb1Index(Index)
        self.lbRb1Index.getConfigSetting(eleActionTool, self.lbRb1IndexName)
        #txRb1Comment(表示内容)
        self.txRb1Comment.getConfigSetting(eleActionTool, self.txRb1CommentName)
        #txRb1UserPassword(UserPassword)
        self.txRb1UserPassword.getConfigSetting(eleActionTool, self.txRb1UserPasswordName)
        #txRb1OwnerPassword(OwnerPassword)
        self.txRb1OwnerPassword.getConfigSetting(eleActionTool, self.txRb1OwnerPasswordName)
        #cbRb1ProHidden(表示/非表示)
        self.cbRb1ProHidden.getConfigSetting(eleActionTool, self.cbRb1ProHiddenName)
        return
    
    def __outputConfigSetting_Rb1(self, eleActionTool:Element) -> None:

        #【Rb1】設定
        comment = ET.Comment('【Rb1】設定')
        eleActionTool.append(comment)
        #lbRb1Index(Index)
        self.lbRb1Index.outputConfigSetting(eleActionTool) 
        #txRb1Comment(表示内容)
        self.txRb1Comment.outputConfigSetting(eleActionTool) 
        #txRb1UserPassword(UserPassword)
        self.txRb1UserPassword.outputConfigSetting(eleActionTool) 
        #txRb1OwnerPassword(OwnerPassword)
        self.txRb1OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb1ProHidden(表示/非表示)
        self.cbRb1ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb1(self, encryptListUi:EncryptListUi) -> None:
        #lbRb1Index(Index)
        self.lbRb1Index.updateConfigSetting(encryptListUi.lbRb1Index)
        #txRb1Comment(表示内容)
        self.txRb1Comment.updateConfigSetting(encryptListUi.txRb1Comment)
        #txRb1UserPassword(UserPassword)
        self.txRb1UserPassword.updateConfigSetting(encryptListUi.txRb1UserPassword)
        #txRb1OwnerPassword(OwnerPassword)
        self.txRb1OwnerPassword.updateConfigSetting(encryptListUi.txRb1OwnerPassword)
        #cbRb1ProHidden(表示/非表示)
        self.cbRb1ProHidden.updateConfigSetting(encryptListUi.cbRb1ProHidden)
        return
    
    def __updateGUISetting_Rb1(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb1Index(Index)
        self.lbRb1Index.updateGUISetting(encryptListUi.lbRb1Index)
        #txRb1Comment(表示内容)
        self.txRb1Comment.updateGUISetting(encryptListUi.txRb1Comment)
        #txRb1UserPassword(UserPassword)
        self.txRb1UserPassword.updateGUISetting(encryptListUi.txRb1UserPassword)
        #txRb1OwnerPassword(OwnerPassword)
        self.txRb1OwnerPassword.updateGUISetting(encryptListUi.txRb1OwnerPassword)
        #cbRb1ProHidden(表示/非表示)
        self.cbRb1ProHidden.updateGUISetting(encryptListUi.cbRb1ProHidden)
        return

    def __init_Rb2(self) -> None:

        #lbRb2Index(Index)
        self.lbRb2IndexName = "lbRb2Index" 
        self.lbRb2IndexText = "Rb2"
        self.lbRb2IndexHidden = False

        #txRb2Comment(表示内容)
        self.txRb2CommentName = "txRb2Comment"
        self.txRb2CommentText = ""
        self.txRb2CommentEnabled = True
        self.txRb2CommentHidden = False

        #txRb2UserPassword(UserPassword)
        self.txRb2UserPasswordName = "txRb2UserPassword"
        self.txRb2UserPasswordText = ""
        self.txRb2UserPasswordEnabled = True
        self.txRb2UserPasswordHidden = False
        
        #txRb2OwnerPassword(OwnerPassword)
        self.txRb2OwnerPasswordName = "txRb2OwnerPassword"
        self.txRb2OwnerPasswordText = ""
        self.txRb2OwnerPasswordEnabled = True
        self.txRb2OwnerPasswordHidden = False
        
        #cbRb2ProHidden(表示/非表示)
        self.cbRb2ProHiddenName = "cbRb2ProHidden"
        self.cbRb2ProHiddenText = "select"
        self.cbRb2ProHiddenChecked = False
        self.cbRb2ProHiddenEnabled = True
        self.cbRb2ProHiddenHidden = False

        return

    def __createConfigSetting_Rb2(self) -> None:
        #lbRb2Index(Index)
        self.lbRb2Index = xmlQLabel(self.lbRb2IndexName,
                                    self.lbRb2IndexText,
                                    self.lbRb2IndexHidden)

        #txRb2Comment(表示内容)
        self.txRb2Comment = xmlQTextEdit(self.txRb2CommentName,
                                         self.txRb2CommentText,
                                         self.txRb2CommentEnabled,
                                         self.txRb2CommentHidden)
        self.txRb2Comment.delLabelProperty("Text")

        #txRb2UserPassword(UserPassword)
        self.txRb2UserPassword = xmlQTextEdit(self.txRb2UserPasswordName,
                                              self.txRb2UserPasswordText,
                                              self.txRb2UserPasswordEnabled,
                                              self.txRb2UserPasswordHidden)
        self.txRb2UserPassword.delLabelProperty("Text")

        #txRb2OwnerPassword(OwnerPassword)
        self.txRb2OwnerPassword = xmlQTextEdit(self.txRb2OwnerPasswordName,
                                               self.txRb2OwnerPasswordText,
                                               self.txRb2OwnerPasswordEnabled,
                                               self.txRb2OwnerPasswordHidden)
        self.txRb2OwnerPassword.delLabelProperty("Text")

        #cbRb2ProHidden(表示/非表示)
        self.cbRb2ProHidden = xmlQCheckBox(self.cbRb2ProHiddenName, 
                                           self.cbRb2ProHiddenText,
                                           self.cbRb2ProHiddenChecked,
                                           self.cbRb2ProHiddenEnabled,
                                           self.cbRb2ProHiddenHidden)
        self.cbRb2ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb2(self, eleActionTool:Element)-> None:
        #lbRb2Index(Index)
        self.lbRb2Index.getConfigSetting(eleActionTool, self.lbRb2IndexName)
        #txRb2Comment(表示内容)
        self.txRb2Comment.getConfigSetting(eleActionTool, self.txRb2CommentName)
        #txRb2UserPassword(UserPassword)
        self.txRb2UserPassword.getConfigSetting(eleActionTool, self.txRb2UserPasswordName)
        #txRb2OwnerPassword(OwnerPassword)
        self.txRb2OwnerPassword.getConfigSetting(eleActionTool, self.txRb2OwnerPasswordName)
        #cbRb2ProHidden(表示/非表示)
        self.cbRb2ProHidden.getConfigSetting(eleActionTool, self.cbRb2ProHiddenName)
        return
    
    def __outputConfigSetting_Rb2(self, eleActionTool:Element) -> None:

        #【Rb2】設定
        comment = ET.Comment('【Rb2】設定')
        eleActionTool.append(comment)
        #lbRb2Index(Index)
        self.lbRb2Index.outputConfigSetting(eleActionTool) 
        #txRb2Comment(表示内容)
        self.txRb2Comment.outputConfigSetting(eleActionTool) 
        #txRb2UserPassword(UserPassword)
        self.txRb2UserPassword.outputConfigSetting(eleActionTool) 
        #txRb2OwnerPassword(OwnerPassword)
        self.txRb2OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb2ProHidden(表示/非表示)
        self.cbRb2ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb2(self, encryptListUi:EncryptListUi) -> None:
        #lbRb2Index(Index)
        self.lbRb2Index.updateConfigSetting(encryptListUi.lbRb2Index)
        #txRb2Comment(表示内容)
        self.txRb2Comment.updateConfigSetting(encryptListUi.txRb2Comment)
        #txRb2UserPassword(UserPassword)
        self.txRb2UserPassword.updateConfigSetting(encryptListUi.txRb2UserPassword)
        #txRb2OwnerPassword(OwnerPassword)
        self.txRb2OwnerPassword.updateConfigSetting(encryptListUi.txRb2OwnerPassword)
        #cbRb2ProHidden(表示/非表示)
        self.cbRb2ProHidden.updateConfigSetting(encryptListUi.cbRb2ProHidden)
        return
    
    def __updateGUISetting_Rb2(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb2Index(Index)
        self.lbRb2Index.updateGUISetting(encryptListUi.lbRb2Index)
        #txRb2Comment(表示内容)
        self.txRb2Comment.updateGUISetting(encryptListUi.txRb2Comment)
        #txRb2UserPassword(UserPassword)
        self.txRb2UserPassword.updateGUISetting(encryptListUi.txRb2UserPassword)
        #txRb2OwnerPassword(OwnerPassword)
        self.txRb2OwnerPassword.updateGUISetting(encryptListUi.txRb2OwnerPassword)
        #cbRb2ProHidden(表示/非表示)
        self.cbRb2ProHidden.updateGUISetting(encryptListUi.cbRb2ProHidden)
        return

    def __init_Rb3(self) -> None:

        #lbRb3Index(Index)
        self.lbRb3IndexName = "lbRb3Index" 
        self.lbRb3IndexText = "Rb3"
        self.lbRb3IndexHidden = False

        #txRb3Comment(表示内容)
        self.txRb3CommentName = "txRb3Comment"
        self.txRb3CommentText = ""
        self.txRb3CommentEnabled = True
        self.txRb3CommentHidden = False

        #txRb3UserPassword(UserPassword)
        self.txRb3UserPasswordName = "txRb3UserPassword"
        self.txRb3UserPasswordText = ""
        self.txRb3UserPasswordEnabled = True
        self.txRb3UserPasswordHidden = False
        
        #txRb3OwnerPassword(OwnerPassword)
        self.txRb3OwnerPasswordName = "txRb3OwnerPassword"
        self.txRb3OwnerPasswordText = ""
        self.txRb3OwnerPasswordEnabled = True
        self.txRb3OwnerPasswordHidden = False
        
        #cbRb3ProHidden(表示/非表示)
        self.cbRb3ProHiddenName = "cbRb3ProHidden"
        self.cbRb3ProHiddenText = "select"
        self.cbRb3ProHiddenChecked = False
        self.cbRb3ProHiddenEnabled = True
        self.cbRb3ProHiddenHidden = False

        return

    def __createConfigSetting_Rb3(self) -> None:
        #lbRb3Index(Index)
        self.lbRb3Index = xmlQLabel(self.lbRb3IndexName,
                                    self.lbRb3IndexText,
                                    self.lbRb3IndexHidden)

        #txRb3Comment(表示内容)
        self.txRb3Comment = xmlQTextEdit(self.txRb3CommentName,
                                         self.txRb3CommentText,
                                         self.txRb3CommentEnabled,
                                         self.txRb3CommentHidden)
        self.txRb3Comment.delLabelProperty("Text")

        #txRb3UserPassword(UserPassword)
        self.txRb3UserPassword = xmlQTextEdit(self.txRb3UserPasswordName,
                                              self.txRb3UserPasswordText,
                                              self.txRb3UserPasswordEnabled,
                                              self.txRb3UserPasswordHidden)
        self.txRb3UserPassword.delLabelProperty("Text")

        #txRb3OwnerPassword(OwnerPassword)
        self.txRb3OwnerPassword = xmlQTextEdit(self.txRb3OwnerPasswordName,
                                               self.txRb3OwnerPasswordText,
                                               self.txRb3OwnerPasswordEnabled,
                                               self.txRb3OwnerPasswordHidden)
        self.txRb3OwnerPassword.delLabelProperty("Text")

        #cbRb3ProHidden(表示/非表示)
        self.cbRb3ProHidden = xmlQCheckBox(self.cbRb3ProHiddenName, 
                                           self.cbRb3ProHiddenText,
                                           self.cbRb3ProHiddenChecked,
                                           self.cbRb3ProHiddenEnabled,
                                           self.cbRb3ProHiddenHidden)
        self.cbRb3ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb3(self, eleActionTool:Element)-> None:
        #lbRb3Index(Index)
        self.lbRb3Index.getConfigSetting(eleActionTool, self.lbRb3IndexName)
        #txRb3Comment(表示内容)
        self.txRb3Comment.getConfigSetting(eleActionTool, self.txRb3CommentName)
        #txRb3UserPassword(UserPassword)
        self.txRb3UserPassword.getConfigSetting(eleActionTool, self.txRb3UserPasswordName)
        #txRb3OwnerPassword(OwnerPassword)
        self.txRb3OwnerPassword.getConfigSetting(eleActionTool, self.txRb3OwnerPasswordName)
        #cbRb3ProHidden(表示/非表示)
        self.cbRb3ProHidden.getConfigSetting(eleActionTool, self.cbRb3ProHiddenName)
        return
    
    def __outputConfigSetting_Rb3(self, eleActionTool:Element) -> None:

        #【Rb3】設定
        comment = ET.Comment('【Rb3】設定')
        eleActionTool.append(comment)
        #lbRb3Index(Index)
        self.lbRb3Index.outputConfigSetting(eleActionTool) 
        #txRb3Comment(表示内容)
        self.txRb3Comment.outputConfigSetting(eleActionTool) 
        #txRb3UserPassword(UserPassword)
        self.txRb3UserPassword.outputConfigSetting(eleActionTool) 
        #txRb3OwnerPassword(OwnerPassword)
        self.txRb3OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb3ProHidden(表示/非表示)
        self.cbRb3ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb3(self, encryptListUi:EncryptListUi) -> None:
        #lbRb3Index(Index)
        self.lbRb3Index.updateConfigSetting(encryptListUi.lbRb3Index)
        #txRb3Comment(表示内容)
        self.txRb3Comment.updateConfigSetting(encryptListUi.txRb3Comment)
        #txRb3UserPassword(UserPassword)
        self.txRb3UserPassword.updateConfigSetting(encryptListUi.txRb3UserPassword)
        #txRb3OwnerPassword(OwnerPassword)
        self.txRb3OwnerPassword.updateConfigSetting(encryptListUi.txRb3OwnerPassword)
        #cbRb3ProHidden(表示/非表示)
        self.cbRb3ProHidden.updateConfigSetting(encryptListUi.cbRb3ProHidden)
        return
    
    def __updateGUISetting_Rb3(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb3Index(Index)
        self.lbRb3Index.updateGUISetting(encryptListUi.lbRb3Index)
        #txRb3Comment(表示内容)
        self.txRb3Comment.updateGUISetting(encryptListUi.txRb3Comment)
        #txRb3UserPassword(UserPassword)
        self.txRb3UserPassword.updateGUISetting(encryptListUi.txRb3UserPassword)
        #txRb3OwnerPassword(OwnerPassword)
        self.txRb3OwnerPassword.updateGUISetting(encryptListUi.txRb3OwnerPassword)
        #cbRb3ProHidden(表示/非表示)
        self.cbRb3ProHidden.updateGUISetting(encryptListUi.cbRb3ProHidden)
        return

    def __init_Rb4(self) -> None:

        #lbRb4Index(Index)
        self.lbRb4IndexName = "lbRb4Index" 
        self.lbRb4IndexText = "Rb4"
        self.lbRb4IndexHidden = False

        #txRb4Comment(表示内容)
        self.txRb4CommentName = "txRb4Comment"
        self.txRb4CommentText = ""
        self.txRb4CommentEnabled = True
        self.txRb4CommentHidden = False

        #txRb4UserPassword(UserPassword)
        self.txRb4UserPasswordName = "txRb4UserPassword"
        self.txRb4UserPasswordText = ""
        self.txRb4UserPasswordEnabled = True
        self.txRb4UserPasswordHidden = False
        
        #txRb4OwnerPassword(OwnerPassword)
        self.txRb4OwnerPasswordName = "txRb4OwnerPassword"
        self.txRb4OwnerPasswordText = ""
        self.txRb4OwnerPasswordEnabled = True
        self.txRb4OwnerPasswordHidden = False
        
        #cbRb4ProHidden(表示/非表示)
        self.cbRb4ProHiddenName = "cbRb4ProHidden"
        self.cbRb4ProHiddenText = "select"
        self.cbRb4ProHiddenChecked = False
        self.cbRb4ProHiddenEnabled = True
        self.cbRb4ProHiddenHidden = False

        return

    def __createConfigSetting_Rb4(self) -> None:
        #lbRb4Index(Index)
        self.lbRb4Index = xmlQLabel(self.lbRb4IndexName,
                                    self.lbRb4IndexText,
                                    self.lbRb4IndexHidden)

        #txRb4Comment(表示内容)
        self.txRb4Comment = xmlQTextEdit(self.txRb4CommentName,
                                         self.txRb4CommentText,
                                         self.txRb4CommentEnabled,
                                         self.txRb4CommentHidden)
        self.txRb4Comment.delLabelProperty("Text")

        #txRb4UserPassword(UserPassword)
        self.txRb4UserPassword = xmlQTextEdit(self.txRb4UserPasswordName,
                                              self.txRb4UserPasswordText,
                                              self.txRb4UserPasswordEnabled,
                                              self.txRb4UserPasswordHidden)
        self.txRb4UserPassword.delLabelProperty("Text")

        #txRb4OwnerPassword(OwnerPassword)
        self.txRb4OwnerPassword = xmlQTextEdit(self.txRb4OwnerPasswordName,
                                               self.txRb4OwnerPasswordText,
                                               self.txRb4OwnerPasswordEnabled,
                                               self.txRb4OwnerPasswordHidden)
        self.txRb4OwnerPassword.delLabelProperty("Text")

        #cbRb4ProHidden(表示/非表示)
        self.cbRb4ProHidden = xmlQCheckBox(self.cbRb4ProHiddenName, 
                                           self.cbRb4ProHiddenText,
                                           self.cbRb4ProHiddenChecked,
                                           self.cbRb4ProHiddenEnabled,
                                           self.cbRb4ProHiddenHidden)
        self.cbRb4ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb4(self, eleActionTool:Element)-> None:
        #lbRb4Index(Index)
        self.lbRb4Index.getConfigSetting(eleActionTool, self.lbRb4IndexName)
        #txRb4Comment(表示内容)
        self.txRb4Comment.getConfigSetting(eleActionTool, self.txRb4CommentName)
        #txRb4UserPassword(UserPassword)
        self.txRb4UserPassword.getConfigSetting(eleActionTool, self.txRb4UserPasswordName)
        #txRb4OwnerPassword(OwnerPassword)
        self.txRb4OwnerPassword.getConfigSetting(eleActionTool, self.txRb4OwnerPasswordName)
        #cbRb4ProHidden(表示/非表示)
        self.cbRb4ProHidden.getConfigSetting(eleActionTool, self.cbRb4ProHiddenName)
        return
    
    def __outputConfigSetting_Rb4(self, eleActionTool:Element) -> None:

        #【Rb4】設定
        comment = ET.Comment('【Rb4】設定')
        eleActionTool.append(comment)
        #lbRb4Index(Index)
        self.lbRb4Index.outputConfigSetting(eleActionTool) 
        #txRb4Comment(表示内容)
        self.txRb4Comment.outputConfigSetting(eleActionTool) 
        #txRb4UserPassword(UserPassword)
        self.txRb4UserPassword.outputConfigSetting(eleActionTool) 
        #txRb4OwnerPassword(OwnerPassword)
        self.txRb4OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb4ProHidden(表示/非表示)
        self.cbRb4ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb4(self, encryptListUi:EncryptListUi) -> None:
        #lbRb4Index(Index)
        self.lbRb4Index.updateConfigSetting(encryptListUi.lbRb4Index)
        #txRb4Comment(表示内容)
        self.txRb4Comment.updateConfigSetting(encryptListUi.txRb4Comment)
        #txRb4UserPassword(UserPassword)
        self.txRb4UserPassword.updateConfigSetting(encryptListUi.txRb4UserPassword)
        #txRb4OwnerPassword(OwnerPassword)
        self.txRb4OwnerPassword.updateConfigSetting(encryptListUi.txRb4OwnerPassword)
        #cbRb4ProHidden(表示/非表示)
        self.cbRb4ProHidden.updateConfigSetting(encryptListUi.cbRb4ProHidden)
        return
    
    def __updateGUISetting_Rb4(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb4Index(Index)
        self.lbRb4Index.updateGUISetting(encryptListUi.lbRb4Index)
        #txRb4Comment(表示内容)
        self.txRb4Comment.updateGUISetting(encryptListUi.txRb4Comment)
        #txRb4UserPassword(UserPassword)
        self.txRb4UserPassword.updateGUISetting(encryptListUi.txRb4UserPassword)
        #txRb4OwnerPassword(OwnerPassword)
        self.txRb4OwnerPassword.updateGUISetting(encryptListUi.txRb4OwnerPassword)
        #cbRb4ProHidden(表示/非表示)
        self.cbRb4ProHidden.updateGUISetting(encryptListUi.cbRb4ProHidden)
        return

    def __init_Rb5(self) -> None:

        #lbRb5Index(Index)
        self.lbRb5IndexName = "lbRb5Index" 
        self.lbRb5IndexText = "Rb5"
        self.lbRb5IndexHidden = False

        #txRb5Comment(表示内容)
        self.txRb5CommentName = "txRb5Comment"
        self.txRb5CommentText = ""
        self.txRb5CommentEnabled = True
        self.txRb5CommentHidden = False

        #txRb5UserPassword(UserPassword)
        self.txRb5UserPasswordName = "txRb5UserPassword"
        self.txRb5UserPasswordText = ""
        self.txRb5UserPasswordEnabled = True
        self.txRb5UserPasswordHidden = False
        
        #txRb5OwnerPassword(OwnerPassword)
        self.txRb5OwnerPasswordName = "txRb5OwnerPassword"
        self.txRb5OwnerPasswordText = ""
        self.txRb5OwnerPasswordEnabled = True
        self.txRb5OwnerPasswordHidden = False
        
        #cbRb5ProHidden(表示/非表示)
        self.cbRb5ProHiddenName = "cbRb5ProHidden"
        self.cbRb5ProHiddenText = "select"
        self.cbRb5ProHiddenChecked = False
        self.cbRb5ProHiddenEnabled = True
        self.cbRb5ProHiddenHidden = False

        return

    def __createConfigSetting_Rb5(self) -> None:
    
        #lbRb5Index(Index)
        self.lbRb5Index = xmlQLabel(self.lbRb5IndexName,
                                    self.lbRb5IndexText,
                                    self.lbRb5IndexHidden)

        #txRb5Comment(表示内容)
        self.txRb5Comment = xmlQTextEdit(self.txRb5CommentName,
                                         self.txRb5CommentText,
                                         self.txRb5CommentEnabled,
                                         self.txRb5CommentHidden)
        self.txRb5Comment.delLabelProperty("Text")

        #txRb5UserPassword(UserPassword)
        self.txRb5UserPassword = xmlQTextEdit(self.txRb5UserPasswordName,
                                              self.txRb5UserPasswordText,
                                              self.txRb5UserPasswordEnabled,
                                              self.txRb5UserPasswordHidden)
        self.txRb5UserPassword.delLabelProperty("Text")

        #txRb5OwnerPassword(OwnerPassword)
        self.txRb5OwnerPassword = xmlQTextEdit(self.txRb5OwnerPasswordName,
                                               self.txRb5OwnerPasswordText,
                                               self.txRb5OwnerPasswordEnabled,
                                               self.txRb5OwnerPasswordHidden)
        self.txRb5OwnerPassword.delLabelProperty("Text")

        #cbRb5ProHidden(表示/非表示)
        self.cbRb5ProHidden = xmlQCheckBox(self.cbRb5ProHiddenName, 
                                           self.cbRb5ProHiddenText,
                                           self.cbRb5ProHiddenChecked,
                                           self.cbRb5ProHiddenEnabled,
                                           self.cbRb5ProHiddenHidden)
        self.cbRb5ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb5(self, eleActionTool:Element)-> None:
        #lbRb5Index(Index)
        self.lbRb5Index.getConfigSetting(eleActionTool, self.lbRb5IndexName)
        #txRb5Comment(表示内容)
        self.txRb5Comment.getConfigSetting(eleActionTool, self.txRb5CommentName)
        #txRb5UserPassword(UserPassword)
        self.txRb5UserPassword.getConfigSetting(eleActionTool, self.txRb5UserPasswordName)
        #txRb5OwnerPassword(OwnerPassword)
        self.txRb5OwnerPassword.getConfigSetting(eleActionTool, self.txRb5OwnerPasswordName)
        #cbRb5ProHidden(表示/非表示)
        self.cbRb5ProHidden.getConfigSetting(eleActionTool, self.cbRb5ProHiddenName)
        return
    
    def __outputConfigSetting_Rb5(self, eleActionTool:Element) -> None:

        #【Rb5】設定
        comment = ET.Comment('【Rb5】設定')
        eleActionTool.append(comment)
        #lbRb5Index(Index)
        self.lbRb5Index.outputConfigSetting(eleActionTool) 
        #txRb5Comment(表示内容)
        self.txRb5Comment.outputConfigSetting(eleActionTool) 
        #txRb5UserPassword(UserPassword)
        self.txRb5UserPassword.outputConfigSetting(eleActionTool) 
        #txRb5OwnerPassword(OwnerPassword)
        self.txRb5OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb5ProHidden(表示/非表示)
        self.cbRb5ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb5(self, encryptListUi:EncryptListUi) -> None:
        #lbRb5Index(Index)
        self.lbRb5Index.updateConfigSetting(encryptListUi.lbRb5Index)
        #txRb5Comment(表示内容)
        self.txRb5Comment.updateConfigSetting(encryptListUi.txRb5Comment)
        #txRb5UserPassword(UserPassword)
        self.txRb5UserPassword.updateConfigSetting(encryptListUi.txRb5UserPassword)
        #txRb5OwnerPassword(OwnerPassword)
        self.txRb5OwnerPassword.updateConfigSetting(encryptListUi.txRb5OwnerPassword)
        #cbRb5ProHidden(表示/非表示)
        self.cbRb5ProHidden.updateConfigSetting(encryptListUi.cbRb5ProHidden)
        return
    
    def __updateGUISetting_Rb5(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb5Index(Index)
        self.lbRb5Index.updateGUISetting(encryptListUi.lbRb5Index)
        #txRb5Comment(表示内容)
        self.txRb5Comment.updateGUISetting(encryptListUi.txRb5Comment)
        #txRb5UserPassword(UserPassword)
        self.txRb5UserPassword.updateGUISetting(encryptListUi.txRb5UserPassword)
        #txRb5OwnerPassword(OwnerPassword)
        self.txRb5OwnerPassword.updateGUISetting(encryptListUi.txRb5OwnerPassword)
        #cbRb5ProHidden(表示/非表示)
        self.cbRb5ProHidden.updateGUISetting(encryptListUi.cbRb5ProHidden)
        return

    def __init_Rb6(self) -> None:

        #lbRb6Index(Index)
        self.lbRb6IndexName = "lbRb6Index" 
        self.lbRb6IndexText = "Rb6"
        self.lbRb6IndexHidden = False

        #txRb6Comment(表示内容)
        self.txRb6CommentName = "txRb6Comment"
        self.txRb6CommentText = ""
        self.txRb6CommentEnabled = True
        self.txRb6CommentHidden = False

        #txRb6UserPassword(UserPassword)
        self.txRb6UserPasswordName = "txRb6UserPassword"
        self.txRb6UserPasswordText = ""
        self.txRb6UserPasswordEnabled = True
        self.txRb6UserPasswordHidden = False
        
        #txRb6OwnerPassword(OwnerPassword)
        self.txRb6OwnerPasswordName = "txRb6OwnerPassword"
        self.txRb6OwnerPasswordText = ""
        self.txRb6OwnerPasswordEnabled = True
        self.txRb6OwnerPasswordHidden = False
        
        #cbRb6ProHidden(表示/非表示)
        self.cbRb6ProHiddenName = "cbRb6ProHidden"
        self.cbRb6ProHiddenText = "select"
        self.cbRb6ProHiddenChecked = False
        self.cbRb6ProHiddenEnabled = True
        self.cbRb6ProHiddenHidden = False

        return

    def __createConfigSetting_Rb6(self) -> None:
        #lbRb6Index(Index)
        self.lbRb6Index = xmlQLabel(self.lbRb6IndexName,
                                    self.lbRb6IndexText,
                                    self.lbRb6IndexHidden)

        #txRb6Comment(表示内容)
        self.txRb6Comment = xmlQTextEdit(self.txRb6CommentName,
                                         self.txRb6CommentText,
                                         self.txRb6CommentEnabled,
                                         self.txRb6CommentHidden)
        self.txRb6Comment.delLabelProperty("Text")

        #txRb6UserPassword(UserPassword)
        self.txRb6UserPassword = xmlQTextEdit(self.txRb6UserPasswordName,
                                              self.txRb6UserPasswordText,
                                              self.txRb6UserPasswordEnabled,
                                              self.txRb6UserPasswordHidden)
        self.txRb6UserPassword.delLabelProperty("Text")

        #txRb6OwnerPassword(OwnerPassword)
        self.txRb6OwnerPassword = xmlQTextEdit(self.txRb6OwnerPasswordName,
                                               self.txRb6OwnerPasswordText,
                                               self.txRb6OwnerPasswordEnabled,
                                               self.txRb6OwnerPasswordHidden)
        self.txRb6OwnerPassword.delLabelProperty("Text")

        #cbRb6ProHidden(表示/非表示)
        self.cbRb6ProHidden = xmlQCheckBox(self.cbRb6ProHiddenName, 
                                           self.cbRb6ProHiddenText,
                                           self.cbRb6ProHiddenChecked,
                                           self.cbRb6ProHiddenEnabled,
                                           self.cbRb6ProHiddenHidden)
        self.cbRb6ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb6(self, eleActionTool:Element)-> None:
        #lbRb6Index(Index)
        self.lbRb6Index.getConfigSetting(eleActionTool, self.lbRb6IndexName)
        #txRb6Comment(表示内容)
        self.txRb6Comment.getConfigSetting(eleActionTool, self.txRb6CommentName)
        #txRb6UserPassword(UserPassword)
        self.txRb6UserPassword.getConfigSetting(eleActionTool, self.txRb6UserPasswordName)
        #txRb6OwnerPassword(OwnerPassword)
        self.txRb6OwnerPassword.getConfigSetting(eleActionTool, self.txRb6OwnerPasswordName)
        #cbRb6ProHidden(表示/非表示)
        self.cbRb6ProHidden.getConfigSetting(eleActionTool, self.cbRb6ProHiddenName)
        return
    
    def __outputConfigSetting_Rb6(self, eleActionTool:Element) -> None:

        #【Rb6】設定
        comment = ET.Comment('【Rb6】設定')
        eleActionTool.append(comment)
        #lbRb6Index(Index)
        self.lbRb6Index.outputConfigSetting(eleActionTool) 
        #txRb6Comment(表示内容)
        self.txRb6Comment.outputConfigSetting(eleActionTool) 
        #txRb6UserPassword(UserPassword)
        self.txRb6UserPassword.outputConfigSetting(eleActionTool) 
        #txRb6OwnerPassword(OwnerPassword)
        self.txRb6OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb6ProHidden(表示/非表示)
        self.cbRb6ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb6(self, encryptListUi:EncryptListUi) -> None:
        #lbRb6Index(Index)
        self.lbRb6Index.updateConfigSetting(encryptListUi.lbRb6Index)
        #txRb6Comment(表示内容)
        self.txRb6Comment.updateConfigSetting(encryptListUi.txRb6Comment)
        #txRb6UserPassword(UserPassword)
        self.txRb6UserPassword.updateConfigSetting(encryptListUi.txRb6UserPassword)
        #txRb6OwnerPassword(OwnerPassword)
        self.txRb6OwnerPassword.updateConfigSetting(encryptListUi.txRb6OwnerPassword)
        #cbRb6ProHidden(表示/非表示)
        self.cbRb6ProHidden.updateConfigSetting(encryptListUi.cbRb6ProHidden)
        return
    
    def __updateGUISetting_Rb6(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb6Index(Index)
        self.lbRb6Index.updateGUISetting(encryptListUi.lbRb6Index)
        #txRb6Comment(表示内容)
        self.txRb6Comment.updateGUISetting(encryptListUi.txRb6Comment)
        #txRb6UserPassword(UserPassword)
        self.txRb6UserPassword.updateGUISetting(encryptListUi.txRb6UserPassword)
        #txRb6OwnerPassword(OwnerPassword)
        self.txRb6OwnerPassword.updateGUISetting(encryptListUi.txRb6OwnerPassword)
        #cbRb6ProHidden(表示/非表示)
        self.cbRb6ProHidden.updateGUISetting(encryptListUi.cbRb6ProHidden)
        return

    def __init_Rb7(self) -> None:

        #lbRb7Index(Index)
        self.lbRb7IndexName = "lbRb7Index" 
        self.lbRb7IndexText = "Rb7"
        self.lbRb7IndexHidden = False

        #txRb7Comment(表示内容)
        self.txRb7CommentName = "txRb7Comment"
        self.txRb7CommentText = ""
        self.txRb7CommentEnabled = True
        self.txRb7CommentHidden = False

        #txRb7UserPassword(UserPassword)
        self.txRb7UserPasswordName = "txRb7UserPassword"
        self.txRb7UserPasswordText = ""
        self.txRb7UserPasswordEnabled = True
        self.txRb7UserPasswordHidden = False
        
        #txRb7OwnerPassword(OwnerPassword)
        self.txRb7OwnerPasswordName = "txRb7OwnerPassword"
        self.txRb7OwnerPasswordText = ""
        self.txRb7OwnerPasswordEnabled = True
        self.txRb7OwnerPasswordHidden = False
        
        #cbRb7ProHidden(表示/非表示)
        self.cbRb7ProHiddenName = "cbRb7ProHidden"
        self.cbRb7ProHiddenText = "select"
        self.cbRb7ProHiddenChecked = False
        self.cbRb7ProHiddenEnabled = True
        self.cbRb7ProHiddenHidden = False

        return

    def __createConfigSetting_Rb7(self) -> None:
        #lbRb7Index(Index)
        self.lbRb7Index = xmlQLabel(self.lbRb7IndexName,
                                    self.lbRb7IndexText,
                                    self.lbRb7IndexHidden)

        #txRb7Comment(表示内容)
        self.txRb7Comment = xmlQTextEdit(self.txRb7CommentName,
                                         self.txRb7CommentText,
                                         self.txRb7CommentEnabled,
                                         self.txRb7CommentHidden)
        self.txRb7Comment.delLabelProperty("Text")

        #txRb7UserPassword(UserPassword)
        self.txRb7UserPassword = xmlQTextEdit(self.txRb7UserPasswordName,
                                              self.txRb7UserPasswordText,
                                              self.txRb7UserPasswordEnabled,
                                              self.txRb7UserPasswordHidden)
        self.txRb7UserPassword.delLabelProperty("Text")

        #txRb7OwnerPassword(OwnerPassword)
        self.txRb7OwnerPassword = xmlQTextEdit(self.txRb7OwnerPasswordName,
                                               self.txRb7OwnerPasswordText,
                                               self.txRb7OwnerPasswordEnabled,
                                               self.txRb7OwnerPasswordHidden)
        self.txRb7OwnerPassword.delLabelProperty("Text")

        #cbRb7ProHidden(表示/非表示)
        self.cbRb7ProHidden = xmlQCheckBox(self.cbRb7ProHiddenName, 
                                           self.cbRb7ProHiddenText,
                                           self.cbRb7ProHiddenChecked,
                                           self.cbRb7ProHiddenEnabled,
                                           self.cbRb7ProHiddenHidden)
        self.cbRb7ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb7(self, eleActionTool:Element)-> None:
        #lbRb7Index(Index)
        self.lbRb7Index.getConfigSetting(eleActionTool, self.lbRb7IndexName)
        #txRb7Comment(表示内容)
        self.txRb7Comment.getConfigSetting(eleActionTool, self.txRb7CommentName)
        #txRb7UserPassword(UserPassword)
        self.txRb7UserPassword.getConfigSetting(eleActionTool, self.txRb7UserPasswordName)
        #txRb7OwnerPassword(OwnerPassword)
        self.txRb7OwnerPassword.getConfigSetting(eleActionTool, self.txRb7OwnerPasswordName)
        #cbRb7ProHidden(表示/非表示)
        self.cbRb7ProHidden.getConfigSetting(eleActionTool, self.cbRb7ProHiddenName)
        return
    
    def __outputConfigSetting_Rb7(self, eleActionTool:Element) -> None:

        #【Rb7】設定
        comment = ET.Comment('【Rb7】設定')
        eleActionTool.append(comment)
        #lbRb7Index(Index)
        self.lbRb7Index.outputConfigSetting(eleActionTool) 
        #txRb7Comment(表示内容)
        self.txRb7Comment.outputConfigSetting(eleActionTool) 
        #txRb7UserPassword(UserPassword)
        self.txRb7UserPassword.outputConfigSetting(eleActionTool) 
        #txRb7OwnerPassword(OwnerPassword)
        self.txRb7OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb7ProHidden(表示/非表示)
        self.cbRb7ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb7(self, encryptListUi:EncryptListUi) -> None:
        #lbRb7Index(Index)
        self.lbRb7Index.updateConfigSetting(encryptListUi.lbRb7Index)
        #txRb7Comment(表示内容)
        self.txRb7Comment.updateConfigSetting(encryptListUi.txRb7Comment)
        #txRb7UserPassword(UserPassword)
        self.txRb7UserPassword.updateConfigSetting(encryptListUi.txRb7UserPassword)
        #txRb7OwnerPassword(OwnerPassword)
        self.txRb7OwnerPassword.updateConfigSetting(encryptListUi.txRb7OwnerPassword)
        #cbRb7ProHidden(表示/非表示)
        self.cbRb7ProHidden.updateConfigSetting(encryptListUi.cbRb7ProHidden)
        return
    
    def __updateGUISetting_Rb7(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb7Index(Index)
        self.lbRb7Index.updateGUISetting(encryptListUi.lbRb7Index)
        #txRb7Comment(表示内容)
        self.txRb7Comment.updateGUISetting(encryptListUi.txRb7Comment)
        #txRb7UserPassword(UserPassword)
        self.txRb7UserPassword.updateGUISetting(encryptListUi.txRb7UserPassword)
        #txRb7OwnerPassword(OwnerPassword)
        self.txRb7OwnerPassword.updateGUISetting(encryptListUi.txRb7OwnerPassword)
        #cbRb7ProHidden(表示/非表示)
        self.cbRb7ProHidden.updateGUISetting(encryptListUi.cbRb7ProHidden)
        return


    def __init_Rb8(self) -> None:

        #lbRb8Index(Index)
        self.lbRb8IndexName = "lbRb8Index" 
        self.lbRb8IndexText = "Rb8"
        self.lbRb8IndexHidden = False

        #txRb8Comment(表示内容)
        self.txRb8CommentName = "txRb8Comment"
        self.txRb8CommentText = ""
        self.txRb8CommentEnabled = True
        self.txRb8CommentHidden = False

        #txRb8UserPassword(UserPassword)
        self.txRb8UserPasswordName = "txRb8UserPassword"
        self.txRb8UserPasswordText = ""
        self.txRb8UserPasswordEnabled = True
        self.txRb8UserPasswordHidden = False
        
        #txRb8OwnerPassword(OwnerPassword)
        self.txRb8OwnerPasswordName = "txRb8OwnerPassword"
        self.txRb8OwnerPasswordText = ""
        self.txRb8OwnerPasswordEnabled = True
        self.txRb8OwnerPasswordHidden = False
        
        #cbRb8ProHidden(表示/非表示)
        self.cbRb8ProHiddenName = "cbRb8ProHidden"
        self.cbRb8ProHiddenText = "select"
        self.cbRb8ProHiddenChecked = False
        self.cbRb8ProHiddenEnabled = True
        self.cbRb8ProHiddenHidden = False

        return

    def __createConfigSetting_Rb8(self) -> None:
        #lbRb8Index(Index)
        self.lbRb8Index = xmlQLabel(self.lbRb8IndexName,
                                    self.lbRb8IndexText,
                                    self.lbRb8IndexHidden)

        #txRb8Comment(表示内容)
        self.txRb8Comment = xmlQTextEdit(self.txRb8CommentName,
                                         self.txRb8CommentText,
                                         self.txRb8CommentEnabled,
                                         self.txRb8CommentHidden)
        self.txRb8Comment.delLabelProperty("Text")

        #txRb8UserPassword(UserPassword)
        self.txRb8UserPassword = xmlQTextEdit(self.txRb8UserPasswordName,
                                              self.txRb8UserPasswordText,
                                              self.txRb8UserPasswordEnabled,
                                              self.txRb8UserPasswordHidden)
        self.txRb8UserPassword.delLabelProperty("Text")

        #txRb8OwnerPassword(OwnerPassword)
        self.txRb8OwnerPassword = xmlQTextEdit(self.txRb8OwnerPasswordName,
                                               self.txRb8OwnerPasswordText,
                                               self.txRb8OwnerPasswordEnabled,
                                               self.txRb8OwnerPasswordHidden)
        self.txRb8OwnerPassword.delLabelProperty("Text")

        #cbRb8ProHidden(表示/非表示)
        self.cbRb8ProHidden = xmlQCheckBox(self.cbRb8ProHiddenName, 
                                           self.cbRb8ProHiddenText,
                                           self.cbRb8ProHiddenChecked,
                                           self.cbRb8ProHiddenEnabled,
                                           self.cbRb8ProHiddenHidden)
        self.cbRb8ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb8(self, eleActionTool:Element)-> None:
        #lbRb8Index(Index)
        self.lbRb8Index.getConfigSetting(eleActionTool, self.lbRb8IndexName)
        #txRb8Comment(表示内容)
        self.txRb8Comment.getConfigSetting(eleActionTool, self.txRb8CommentName)
        #txRb8UserPassword(UserPassword)
        self.txRb8UserPassword.getConfigSetting(eleActionTool, self.txRb8UserPasswordName)
        #txRb8OwnerPassword(OwnerPassword)
        self.txRb8OwnerPassword.getConfigSetting(eleActionTool, self.txRb8OwnerPasswordName)
        #cbRb8ProHidden(表示/非表示)
        self.cbRb8ProHidden.getConfigSetting(eleActionTool, self.cbRb8ProHiddenName)
        return
    
    def __outputConfigSetting_Rb8(self, eleActionTool:Element) -> None:

        #【Rb8】設定
        comment = ET.Comment('【Rb8】設定')
        eleActionTool.append(comment)
        #lbRb8Index(Index)
        self.lbRb8Index.outputConfigSetting(eleActionTool) 
        #txRb8Comment(表示内容)
        self.txRb8Comment.outputConfigSetting(eleActionTool) 
        #txRb8UserPassword(UserPassword)
        self.txRb8UserPassword.outputConfigSetting(eleActionTool) 
        #txRb8OwnerPassword(OwnerPassword)
        self.txRb8OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb8ProHidden(表示/非表示)
        self.cbRb8ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb8(self, encryptListUi:EncryptListUi) -> None:
        #lbRb8Index(Index)
        self.lbRb8Index.updateConfigSetting(encryptListUi.lbRb8Index)
        #txRb8Comment(表示内容)
        self.txRb8Comment.updateConfigSetting(encryptListUi.txRb8Comment)
        #txRb8UserPassword(UserPassword)
        self.txRb8UserPassword.updateConfigSetting(encryptListUi.txRb8UserPassword)
        #txRb8OwnerPassword(OwnerPassword)
        self.txRb8OwnerPassword.updateConfigSetting(encryptListUi.txRb8OwnerPassword)
        #cbRb8ProHidden(表示/非表示)
        self.cbRb8ProHidden.updateConfigSetting(encryptListUi.cbRb8ProHidden)
        return
    
    def __updateGUISetting_Rb8(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb8Index(Index)
        self.lbRb8Index.updateGUISetting(encryptListUi.lbRb8Index)
        #txRb8Comment(表示内容)
        self.txRb8Comment.updateGUISetting(encryptListUi.txRb8Comment)
        #txRb8UserPassword(UserPassword)
        self.txRb8UserPassword.updateGUISetting(encryptListUi.txRb8UserPassword)
        #txRb8OwnerPassword(OwnerPassword)
        self.txRb8OwnerPassword.updateGUISetting(encryptListUi.txRb8OwnerPassword)
        #cbRb8ProHidden(表示/非表示)
        self.cbRb8ProHidden.updateGUISetting(encryptListUi.cbRb8ProHidden)
        return


    def __init_Rb9(self) -> None:

        #lbRb9Index(Index)
        self.lbRb9IndexName = "lbRb9Index" 
        self.lbRb9IndexText = "Rb9"
        self.lbRb9IndexHidden = False

        #txRb9Comment(表示内容)
        self.txRb9CommentName = "txRb9Comment"
        self.txRb9CommentText = ""
        self.txRb9CommentEnabled = True
        self.txRb9CommentHidden = False

        #txRb9UserPassword(UserPassword)
        self.txRb9UserPasswordName = "txRb9UserPassword"
        self.txRb9UserPasswordText = ""
        self.txRb9UserPasswordEnabled = True
        self.txRb9UserPasswordHidden = False
        
        #txRb9OwnerPassword(OwnerPassword)
        self.txRb9OwnerPasswordName = "txRb9OwnerPassword"
        self.txRb9OwnerPasswordText = ""
        self.txRb9OwnerPasswordEnabled = True
        self.txRb9OwnerPasswordHidden = False
        
        #cbRb9ProHidden(表示/非表示)
        self.cbRb9ProHiddenName = "cbRb9ProHidden"
        self.cbRb9ProHiddenText = "select"
        self.cbRb9ProHiddenChecked = False
        self.cbRb9ProHiddenEnabled = True
        self.cbRb9ProHiddenHidden = False

        return

    def __createConfigSetting_Rb9(self) -> None:
        #lbRb9Index(Index)
        self.lbRb9Index = xmlQLabel(self.lbRb9IndexName,
                                    self.lbRb9IndexText,
                                    self.lbRb9IndexHidden)

        #txRb9Comment(表示内容)
        self.txRb9Comment = xmlQTextEdit(self.txRb9CommentName,
                                         self.txRb9CommentText,
                                         self.txRb9CommentEnabled,
                                         self.txRb9CommentHidden)
        self.txRb9Comment.delLabelProperty("Text")

        #txRb9UserPassword(UserPassword)
        self.txRb9UserPassword = xmlQTextEdit(self.txRb9UserPasswordName,
                                              self.txRb9UserPasswordText,
                                              self.txRb9UserPasswordEnabled,
                                              self.txRb9UserPasswordHidden)
        self.txRb9UserPassword.delLabelProperty("Text")

        #txRb9OwnerPassword(OwnerPassword)
        self.txRb9OwnerPassword = xmlQTextEdit(self.txRb9OwnerPasswordName,
                                               self.txRb9OwnerPasswordText,
                                               self.txRb9OwnerPasswordEnabled,
                                               self.txRb9OwnerPasswordHidden)
        self.txRb9OwnerPassword.delLabelProperty("Text")

        #cbRb9ProHidden(表示/非表示)
        self.cbRb9ProHidden = xmlQCheckBox(self.cbRb9ProHiddenName, 
                                           self.cbRb9ProHiddenText,
                                           self.cbRb9ProHiddenChecked,
                                           self.cbRb9ProHiddenEnabled,
                                           self.cbRb9ProHiddenHidden)
        self.cbRb9ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb9(self, eleActionTool:Element)-> None:
        #lbRb9Index(Index)
        self.lbRb9Index.getConfigSetting(eleActionTool, self.lbRb9IndexName)
        #txRb9Comment(表示内容)
        self.txRb9Comment.getConfigSetting(eleActionTool, self.txRb9CommentName)
        #txRb9UserPassword(UserPassword)
        self.txRb9UserPassword.getConfigSetting(eleActionTool, self.txRb9UserPasswordName)
        #txRb9OwnerPassword(OwnerPassword)
        self.txRb9OwnerPassword.getConfigSetting(eleActionTool, self.txRb9OwnerPasswordName)
        #cbRb9ProHidden(表示/非表示)
        self.cbRb9ProHidden.getConfigSetting(eleActionTool, self.cbRb9ProHiddenName)
        return
    
    def __outputConfigSetting_Rb9(self, eleActionTool:Element) -> None:

        #【Rb9】設定
        comment = ET.Comment('【Rb9】設定')
        eleActionTool.append(comment)
        #lbRb9Index(Index)
        self.lbRb9Index.outputConfigSetting(eleActionTool) 
        #txRb9Comment(表示内容)
        self.txRb9Comment.outputConfigSetting(eleActionTool) 
        #txRb9UserPassword(UserPassword)
        self.txRb9UserPassword.outputConfigSetting(eleActionTool) 
        #txRb9OwnerPassword(OwnerPassword)
        self.txRb9OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb9ProHidden(表示/非表示)
        self.cbRb9ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb9(self, encryptListUi:EncryptListUi) -> None:
        #lbRb9Index(Index)
        self.lbRb9Index.updateConfigSetting(encryptListUi.lbRb9Index)
        #txRb9Comment(表示内容)
        self.txRb9Comment.updateConfigSetting(encryptListUi.txRb9Comment)
        #txRb9UserPassword(UserPassword)
        self.txRb9UserPassword.updateConfigSetting(encryptListUi.txRb9UserPassword)
        #txRb9OwnerPassword(OwnerPassword)
        self.txRb9OwnerPassword.updateConfigSetting(encryptListUi.txRb9OwnerPassword)
        #cbRb9ProHidden(表示/非表示)
        self.cbRb9ProHidden.updateConfigSetting(encryptListUi.cbRb9ProHidden)
        return
    
    def __updateGUISetting_Rb9(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb9Index(Index)
        self.lbRb9Index.updateGUISetting(encryptListUi.lbRb9Index)
        #txRb9Comment(表示内容)
        self.txRb9Comment.updateGUISetting(encryptListUi.txRb9Comment)
        #txRb9UserPassword(UserPassword)
        self.txRb9UserPassword.updateGUISetting(encryptListUi.txRb9UserPassword)
        #txRb9OwnerPassword(OwnerPassword)
        self.txRb9OwnerPassword.updateGUISetting(encryptListUi.txRb9OwnerPassword)
        #cbRb9ProHidden(表示/非表示)
        self.cbRb9ProHidden.updateGUISetting(encryptListUi.cbRb9ProHidden)
        return


    def __init_Rb10(self) -> None:

        #lbRb10Index(Index)
        self.lbRb10IndexName = "lbRb10Index" 
        self.lbRb10IndexText = "Rb10"
        self.lbRb10IndexHidden = False

        #txRb10Comment(表示内容)
        self.txRb10CommentName = "txRb10Comment"
        self.txRb10CommentText = ""
        self.txRb10CommentEnabled = True
        self.txRb10CommentHidden = False

        #txRb10UserPassword(UserPassword)
        self.txRb10UserPasswordName = "txRb10UserPassword"
        self.txRb10UserPasswordText = ""
        self.txRb10UserPasswordEnabled = True
        self.txRb10UserPasswordHidden = False
        
        #txRb10OwnerPassword(OwnerPassword)
        self.txRb10OwnerPasswordName = "txRb10OwnerPassword"
        self.txRb10OwnerPasswordText = ""
        self.txRb10OwnerPasswordEnabled = True
        self.txRb10OwnerPasswordHidden = False
        
        #cbRb10ProHidden(表示/非表示)
        self.cbRb10ProHiddenName = "cbRb10ProHidden"
        self.cbRb10ProHiddenText = "select"
        self.cbRb10ProHiddenChecked = False
        self.cbRb10ProHiddenEnabled = True
        self.cbRb10ProHiddenHidden = False

        return

    def __createConfigSetting_Rb10(self) -> None:
        #lbRb10Index(Index)
        self.lbRb10Index = xmlQLabel(self.lbRb10IndexName,
                                    self.lbRb10IndexText,
                                    self.lbRb10IndexHidden)

        #txRb10Comment(表示内容)
        self.txRb10Comment = xmlQTextEdit(self.txRb10CommentName,
                                         self.txRb10CommentText,
                                         self.txRb10CommentEnabled,
                                         self.txRb10CommentHidden)
        self.txRb10Comment.delLabelProperty("Text")

        #txRb10UserPassword(UserPassword)
        self.txRb10UserPassword = xmlQTextEdit(self.txRb10UserPasswordName,
                                              self.txRb10UserPasswordText,
                                              self.txRb10UserPasswordEnabled,
                                              self.txRb10UserPasswordHidden)
        self.txRb10UserPassword.delLabelProperty("Text")

        #txRb10OwnerPassword(OwnerPassword)
        self.txRb10OwnerPassword = xmlQTextEdit(self.txRb10OwnerPasswordName,
                                               self.txRb10OwnerPasswordText,
                                               self.txRb10OwnerPasswordEnabled,
                                               self.txRb10OwnerPasswordHidden)
        self.txRb10OwnerPassword.delLabelProperty("Text")

        #cbRb10ProHidden(表示/非表示)
        self.cbRb10ProHidden = xmlQCheckBox(self.cbRb10ProHiddenName, 
                                           self.cbRb10ProHiddenText,
                                           self.cbRb10ProHiddenChecked,
                                           self.cbRb10ProHiddenEnabled,
                                           self.cbRb10ProHiddenHidden)
        self.cbRb10ProHidden.delLabelProperty("Checked")
        
        return
    
    def __getConfigSetting_Rb10(self, eleActionTool:Element)-> None:
        #lbRb10Index(Index)
        self.lbRb10Index.getConfigSetting(eleActionTool, self.lbRb10IndexName)
        #txRb10Comment(表示内容)
        self.txRb10Comment.getConfigSetting(eleActionTool, self.txRb10CommentName)
        #txRb10UserPassword(UserPassword)
        self.txRb10UserPassword.getConfigSetting(eleActionTool, self.txRb10UserPasswordName)
        #txRb10OwnerPassword(OwnerPassword)
        self.txRb10OwnerPassword.getConfigSetting(eleActionTool, self.txRb10OwnerPasswordName)
        #cbRb10ProHidden(表示/非表示)
        self.cbRb10ProHidden.getConfigSetting(eleActionTool, self.cbRb10ProHiddenName)
        return
    
    def __outputConfigSetting_Rb10(self, eleActionTool:Element) -> None:

        #【Rb10】設定
        comment = ET.Comment('【Rb10】設定')
        eleActionTool.append(comment)
        #lbRb10Index(Index)
        self.lbRb10Index.outputConfigSetting(eleActionTool) 
        #txRb10Comment(表示内容)
        self.txRb10Comment.outputConfigSetting(eleActionTool) 
        #txRb10UserPassword(UserPassword)
        self.txRb10UserPassword.outputConfigSetting(eleActionTool) 
        #txRb10OwnerPassword(OwnerPassword)
        self.txRb10OwnerPassword.outputConfigSetting(eleActionTool) 
        #cbRb10ProHidden(表示/非表示)
        self.cbRb10ProHidden.outputConfigSetting(eleActionTool)  
        return
    
    def __updateConfigSetting_Rb10(self, encryptListUi:EncryptListUi) -> None:
        #lbRb10Index(Index)
        self.lbRb10Index.updateConfigSetting(encryptListUi.lbRb10Index)
        #txRb10Comment(表示内容)
        self.txRb10Comment.updateConfigSetting(encryptListUi.txRb10Comment)
        #txRb10UserPassword(UserPassword)
        self.txRb10UserPassword.updateConfigSetting(encryptListUi.txRb10UserPassword)
        #txRb10OwnerPassword(OwnerPassword)
        self.txRb10OwnerPassword.updateConfigSetting(encryptListUi.txRb10OwnerPassword)
        #cbRb10ProHidden(表示/非表示)
        self.cbRb10ProHidden.updateConfigSetting(encryptListUi.cbRb10ProHidden)
        return
    
    def __updateGUISetting_Rb10(self, encryptListUi:EncryptListUi) -> None:
    
        #lbRb10Index(Index)
        self.lbRb10Index.updateGUISetting(encryptListUi.lbRb10Index)
        #txRb10Comment(表示内容)
        self.txRb10Comment.updateGUISetting(encryptListUi.txRb10Comment)
        #txRb10UserPassword(UserPassword)
        self.txRb10UserPassword.updateGUISetting(encryptListUi.txRb10UserPassword)
        #txRb10OwnerPassword(OwnerPassword)
        self.txRb10OwnerPassword.updateGUISetting(encryptListUi.txRb10OwnerPassword)
        #cbRb10ProHidden(表示/非表示)
        self.cbRb10ProHidden.updateGUISetting(encryptListUi.cbRb10ProHidden)
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
    
    def __updateConfigSetting_Execution(self, encryptListUi:EncryptListUi) -> None:
        
        #btExecution(確定)
        self.btExecution.updateConfigSetting(encryptListUi.btExecution)
        return
    
    def __updateGUISetting_Execution(self, encryptListUi:EncryptListUi) -> None:
    
        #btExecution(確定)
        self.btExecution.updateGUISetting(encryptListUi.btExecution)
        return

    def print(self) :
        return
        
class EncryptListConfig():
    
    def __init__(self, configFileAddress:str, PdfInfoSetting:EncryptListUi)-> None:
        super(EncryptListConfig, self).__init__()
        self.FSP = FileSysProcess()
        self.CreateFileAddress = configFileAddress + "\\config2.xml"
        if self.FSP.judgeFileExsit(self.CreateFileAddress) :
            self.configFileAddress = self.CreateFileAddress
        else :
            self.configFileAddress = configFileAddress + "\\Jp\\EncryptListSetting_Jp.xml"
        
        self.toolName = toolNameLib()
        self.ui = PdfInfoSetting
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
        eleEncryptListGUI = Element("EncryptList")

        #ツール名称GUI作成
        eleTool = Element("ToolName")
        self.toolName.outputConfigSetting(eleTool)
        eleEncryptListGUI.append(eleTool)

        #【各pdfツール設定】GUI作成
        comment = ET.Comment('【暗号化リスト情報設定】GUI')
        eleEncryptListGUI.append(comment)
        eleActionToolList = Element("actionToolList")
        self.actionToolList.outputConfigSetting(eleActionToolList)
        eleEncryptListGUI.append(eleActionToolList)

        #ElementTreeを追加
        ET.indent(eleEncryptListGUI)
        tree = ElementTree(eleEncryptListGUI)
    
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
        
