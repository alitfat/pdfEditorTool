import xml.etree.ElementTree as ET
from xml.etree.ElementTree import  ElementTree,Element
from config.xmlLib.xmlLib import xmlLib
from config.xmlLib.xmlQtLib import xmlQWidget,xmlQTextEdit,xmlQLabel,xmlQPushButton, xmlQCheckBox
from GUI.pdfEditerToolGUI_PdfInfoSetting import pdfEditorTool_PdfInfoSetting

from Lib.FileSysProcess import FileSysProcess

class toolNameLib(xmlLib):
    #ツール名称
    widTool:xmlQWidget
    """ toolName Setting"""
    def __init__(self)-> None:
 
        super(toolNameLib, self).__init__()

        #ツール名称
        self.toolName = "widTool" 
        self.toolTitle = "PDF Information Setting"
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
       
    def updateConfigSetting(self, PdfInfoSetting:pdfEditorTool_PdfInfoSetting) -> None:
        toolNameText = PdfInfoSetting.windowTitle()
        self.widTool.modifyLabelProperty('WindowTitle', toolNameText)
        return
    
    def updateGUISetting(self, PdfInfoSetting:pdfEditorTool_PdfInfoSetting) -> None:
        toolNameText = self.widTool.getLabelValue('WindowTitle')
        PdfInfoSetting.setWindowTitle(toolNameText)
        return


class actionToolList(xmlLib):
    #lbTitle(タイトル)
    lbTitle:xmlQLabel
    #txTitle(タイトル)
    txTitle:xmlQTextEdit
    #cbTitle(タイトル)
    cbTitle:xmlQCheckBox
    
    #lbSubject(件名)
    lbSubject:xmlQLabel
    #txSubject(件名)
    txSubject:xmlQTextEdit
    #cbSubject(件名)
    cbSubject:xmlQCheckBox
    
    #lbAuthor(作成者)
    lbAuthor:xmlQLabel
    #txAuthor(作成者)
    txAuthor:xmlQTextEdit
    #cbAuthor(作成者)
    cbAuthor:xmlQCheckBox

    #lbKeywords(タグ)
    lbKeywords:xmlQLabel
    #txKeywords(タグ)
    txKeywords:xmlQTextEdit
    #cbKeywords(タグ)
    cbKeywords:xmlQCheckBox
    
    #lbProducer(Producer)
    lbProducer:xmlQLabel
    #txProducer(Producer)
    txProducer:xmlQTextEdit
    #cbProducer(Producer)
    cbProducer:xmlQCheckBox
    
    #lbCreator(Creator)
    lbCreator:xmlQLabel
    #txCreator(Creator)
    txCreator:xmlQTextEdit
    #cbCreator(Creator)
    cbCreator:xmlQCheckBox

    #btExecution(確定)
    btExecution:xmlQPushButton
    
    def __init__(self)-> None:
        super(actionToolList, self).__init__()
        #lbTitle(タイトル)
        self.lbTitleName = "lbTitle" 
        self.lbTitleText = "Title"
        self.lbTitleHidden = False
        
        #txTitle(タイトル)
        self.txTitleName = "txTitle"
        self.txTitleText = ""
        self.txTitleEnabled = True
        self.txTitleHidden = False
        
        #cbTitle(タイトル)
        self.cbTitleName = "cbTitle"
        self.cbTitleText = "select"
        self.cbTitleChecked = False
        self.cbTitleEnabled = True
        self.cbTitleHidden = False
        
        #lbSubject(件名)
        self.lbSubjectName = "lbSubject" 
        self.lbSubjectText = "Subject"
        self.lbSubjectHidden = False
        
        #txSubject(件名)
        self.txSubjectName = "txSubject" 
        self.txSubjectText = ""
        self.txSubjectEnabled = True
        self.txSubjectHidden = False
        
        #cbSubject(件名)
        self.cbSubjectName = "cbSubject"
        self.cbSubjectText = "select"
        self.cbSubjectChecked = False
        self.cbSubjectEnabled = True
        self.cbSubjectHidden = False
        
        #lbAuthor(作成者)
        self.lbAuthorName = "lbAuthor" 
        self.lbAuthorText = "Author"
        self.lbAuthorHidden = False
        
        #txAuthor(作成者)
        self.txAuthorName = "txAuthor" 
        self.txAuthorText = ""
        self.txAuthorEnabled = True
        self.txAuthorHidden = False
        
        #cbAuthor(作成者)
        self.cbAuthorName = "cbAuthor"
        self.cbAuthorText = "select"
        self.cbAuthorChecked = False
        self.cbAuthorEnabled = True
        self.cbAuthorHidden = False

        #lbKeywords(タグ)
        self.lbKeywordsName = "lbKeywords" 
        self.lbKeywordsText = "Keywords"
        self.lbKeywordsHidden = False
        
        #txKeywords(タグ)
        self.txKeywordsName = "txKeywords" 
        self.txKeywordsText = ""
        self.txKeywordsEnabled = True
        self.txKeywordsHidden = False
        
        #cbKeywords(タグ)
        self.cbKeywordsName = "cbKeywords"
        self.cbKeywordsText = "select"
        self.cbKeywordsChecked = False
        self.cbKeywordsEnabled = True
        self.cbKeywordsHidden = False
        
        #lbProducer(Producer)
        self.lbProducerName = "lbProducer" 
        self.lbProducerText = "Producer"
        self.lbProducerHidden = False
        
        #txProducer(Producer)
        self.txProducerName = "txProducer" 
        self.txProducerText = ""
        self.txProducerEnabled = True
        self.txProducerHidden = False
        
        #cbProducer(Producer)
        self.cbProducerName = "cbProducer"
        self.cbProducerText = "select"
        self.cbProducerChecked = False
        self.cbProducerEnabled = True
        self.cbProducerHidden = False
        
        #lbCreator(Creator)
        self.lbCreatorName = "lbCreator" 
        self.lbCreatorText = "Creator"
        self.lbCreatorHidden = False
        
        #txCreator(Creator)
        self.txCreatorName = "txCreator" 
        self.txCreatorText = ""
        self.txCreatorEnabled = True
        self.txCreatorHidden = False
        
        #cbCreator(Creator)
        self.cbCreatorName = "cbCreator"
        self.cbCreatorText = "select"
        self.cbCreatorChecked = False
        self.cbCreatorEnabled = True
        self.cbCreatorHidden = False
        
        #btExecution(確定)
        self.btExecutionName = "btObjFileName"
        self.btExecutionText = "select"
        self.btExecutionEnabled = True
        self.btExecutionHidden = False

        self.clearConfigSetting()
        self.createConfigSetting()
        return
        
    def clearConfigSetting(self) -> None:
        return

    def createConfigSetting(self) -> None:
        
        #lbTitle(タイトル)
        self.lbTitle = xmlQLabel(self.lbTitleName,
                                 self.lbTitleText,
                                 self.lbTitleHidden)
        
        #txTitle(タイトル)
        self.txTitle = xmlQTextEdit(self.txTitleName,
                                    self.txTitleText,
                                    self.txTitleEnabled,
                                    self.txTitleHidden
                                    )
        
        #cbTitle(タイトル)
        self.cbTitle = xmlQCheckBox(self.cbTitleName, 
                                    self.cbTitleText,
                                    self.cbTitleChecked,
                                    self.cbTitleEnabled,
                                    self.cbTitleHidden)

        #lbSubject(件名)
        self.lbSubject = xmlQLabel(self.lbSubjectName,
                                   self.lbSubjectText,
                                   self.lbSubjectHidden)

        #txSubject(件名)
        self.txSubject = xmlQTextEdit(self.txSubjectName,
                                      self.txSubjectText,
                                      self.txSubjectEnabled,
                                      self.txSubjectHidden
                                    )

        #cbSubject(件名)
        self.cbSubject = xmlQCheckBox(self.cbSubjectName, 
                                      self.cbSubjectText,
                                      self.cbSubjectChecked,
                                      self.cbSubjectEnabled,
                                      self.cbSubjectHidden)



        #lbAuthor(作成者)
        self.lbAuthor = xmlQLabel(self.lbAuthorName,
                                  self.lbAuthorText,
                                  self.lbAuthorHidden)
        
       
        #txAuthor(作成者)
        self.txAuthor = xmlQTextEdit(self.txAuthorName,
                                     self.txAuthorText,
                                     self.txAuthorEnabled,
                                     self.txAuthorHidden
                                    )
                                    
        #cbAuthor(作成者)
        self.cbAuthor = xmlQCheckBox(self.cbAuthorName, 
                                     self.cbAuthorText,
                                     self.cbAuthorChecked,
                                     self.cbAuthorEnabled,
                                     self.cbAuthorHidden)

        #lbKeywords(タグ)
        self.lbKeywords = xmlQLabel(self.lbKeywordsName,
                                    self.lbKeywordsText,
                                    self.lbKeywordsHidden)
        
        #txKeywords(タグ)
        self.txKeywords = xmlQTextEdit(self.txKeywordsName,
                                       self.txKeywordsText,
                                       self.txKeywordsEnabled,
                                       self.txKeywordsHidden
                                       )
        
        #cbKeywords(タグ)
        self.cbKeywords = xmlQCheckBox(self.cbKeywordsName, 
                                       self.cbKeywordsText,
                                       self.cbKeywordsChecked,
                                       self.cbKeywordsEnabled,
                                       self.cbKeywordsHidden)
        
        #lbProducer(Producer)
        self.lbProducer = xmlQLabel(self.lbProducerName,
                                    self.lbProducerText,
                                    self.lbProducerHidden)
        
        #txProducer(Producer)
        self.txProducer = xmlQTextEdit(self.txProducerName,
                                       self.txProducerText,
                                       self.txProducerEnabled,
                                       self.txProducerHidden
                                      )
        
        #cbProducer(Producer)
        self.cbProducer = xmlQCheckBox(self.cbProducerName, 
                                       self.cbProducerText,
                                       self.cbProducerChecked,
                                       self.cbProducerEnabled,
                                       self.cbProducerHidden)
        
        #lbCreator(Creator)
        self.lbCreator = xmlQLabel(self.lbCreatorName,
                                   self.lbCreatorText,
                                   self.lbCreatorHidden)
       
        #txCreator(Creator)
        self.txCreator = xmlQTextEdit(self.txCreatorName,
                                      self.txCreatorText,
                                      self.txCreatorEnabled,
                                      self.txCreatorHidden
                                    )
      
        #cbCreator(Creator)
        self.cbCreator = xmlQCheckBox(self.cbCreatorName, 
                                       self.cbCreatorText,
                                       self.cbCreatorChecked,
                                       self.cbCreatorEnabled,
                                       self.cbCreatorHidden)
       
        #btExecution(確定)
        self.btExecution = xmlQPushButton(self.btExecutionName, 
                                          self.btExecutionText, 
                                          self.btExecutionEnabled, 
                                          self.btExecutionHidden)

        return
        
        
    def getConfigSetting(self, eleActionTool:Element|None)-> None:
        if eleActionTool is None :
            return
        
        #lbTitle(タイトル)
        self.lbTitle.getConfigSetting(eleActionTool, self.lbTitleName)
        #txTitle(タイトル)
        self.txTitle.getConfigSetting(eleActionTool,self.txTitleName)
        #cbTitle(タイトル)
        self.cbTitle.getConfigSetting(eleActionTool,self.cbTitleName)
        
        #lbSubject(件名)
        self.lbSubject.getConfigSetting(eleActionTool, self.lbSubjectName)
        #txSubject(件名)
        self.txSubject.getConfigSetting(eleActionTool, self.txSubjectName)
        #cbSubject(件名)
        self.cbSubject.getConfigSetting(eleActionTool, self.cbSubjectName)
        
        #lbAuthor(作成者)
        self.lbAuthor.getConfigSetting(eleActionTool, self.lbAuthorName)
        #txAuthor(作成者)
        self.txAuthor.getConfigSetting(eleActionTool, self.txAuthorName)
        #cbAuthor(作成者)
        self.cbAuthor.getConfigSetting(eleActionTool, self.cbAuthorName)
        
        #lbKeywords(タグ)
        self.lbKeywords.getConfigSetting(eleActionTool, self.lbKeywordsName)
        #txKeywords(タグ)
        self.txKeywords.getConfigSetting(eleActionTool, self.txKeywordsName)
        #cbKeywords(タグ)
        self.cbKeywords.getConfigSetting(eleActionTool, self.cbKeywordsName)
        
        #lbProducer(Producer)
        self.lbProducer.getConfigSetting(eleActionTool, self.lbProducerName)
        #txProducer(Producer)
        self.txProducer.getConfigSetting(eleActionTool, self.txProducerName)
        #cbProducer(Producer)
        self.cbProducer.getConfigSetting(eleActionTool, self.cbProducerName)
        
        #lbCreator(Creator)
        self.lbCreator.getConfigSetting(eleActionTool, self.lbCreatorName)
        #txCreator(Creator)
        self.txCreator.getConfigSetting(eleActionTool, self.txCreatorName)
        #cbCreator(Creator)
        self.cbCreator.getConfigSetting(eleActionTool, self.cbCreatorName)
        
        #btExecution(確定)
        self.btExecution.getConfigSetting(eleActionTool,self.btExecutionName)

        return
        
    def outputConfigSetting(self, eleActionTool:Element) -> None:
        
        #タイトル
        comment = ET.Comment('【'+ self.lbTitle.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #lbTitle(タイトル)
        self.lbTitle.outputConfigSetting(eleActionTool)
        #txTitle(タイトル)
        self.txTitle.outputConfigSetting(eleActionTool)
        #cbTitle(タイトル)
        self.cbTitle.outputConfigSetting(eleActionTool)
        
        #件名
        comment = ET.Comment('【'+ self.lbSubject.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #lbSubject(件名)
        self.lbSubject.outputConfigSetting(eleActionTool)
        #txSubject(件名)
        self.txSubject.outputConfigSetting(eleActionTool)
        #cbSubject(件名)
        self.cbSubject.outputConfigSetting(eleActionTool)
        
        #作成者
        comment = ET.Comment('【'+ self.lbAuthor.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #lbAuthor(作成者)
        self.lbAuthor.outputConfigSetting(eleActionTool)
        #txAuthor(作成者)
        self.txAuthor.outputConfigSetting(eleActionTool)
        #cbAuthor(作成者)
        self.cbAuthor.outputConfigSetting(eleActionTool)
        
        #タグ
        comment = ET.Comment('【'+ self.lbKeywords.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #lbKeywords(タグ)
        self.lbKeywords.outputConfigSetting(eleActionTool)
        #txKeywords(タグ)
        self.txKeywords.outputConfigSetting(eleActionTool)
        #cbKeywords(タグ)
        self.cbKeywords.outputConfigSetting(eleActionTool)
        
        #Producer
        comment = ET.Comment('【'+ self.lbProducer.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #lbProducer(Producer)
        self.lbProducer.outputConfigSetting(eleActionTool)
        #txProducer(Producer)
        self.txProducer.outputConfigSetting(eleActionTool)
        #cbProducer(Producer)
        self.cbProducer.outputConfigSetting(eleActionTool)
        
        #Creator
        comment = ET.Comment('【'+ self.lbCreator.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #lbCreator(Creator)
        self.lbCreator.outputConfigSetting(eleActionTool)
        #txCreator(Creator)
        self.txCreator.outputConfigSetting(eleActionTool)
        #cbCreator(Creator)
        self.cbCreator.outputConfigSetting(eleActionTool)
        
        #確定
        comment = ET.Comment('【'+ self.btExecution.getLabelValue('Text') + '】設定')
        eleActionTool.append(comment)
        #btExecution(確定)
        self.btExecution.outputConfigSetting(eleActionTool)
        
        return
    
    def updateConfigSetting(self, PdfInfoSetting:pdfEditorTool_PdfInfoSetting) -> None:

        #lbTitle(タイトル)
        self.lbTitle.updateConfigSetting(PdfInfoSetting.lbTitle)
        #txTitle(タイトル)
        self.txTitle.updateConfigSetting(PdfInfoSetting.txTitle)
        #cbTitle(タイトル)
        self.cbTitle.updateConfigSetting(PdfInfoSetting.cbTitle)
        
        #lbSubject(件名)
        self.lbSubject.updateConfigSetting(PdfInfoSetting.lbSubject)
        #txSubject(件名)
        self.txSubject.updateConfigSetting(PdfInfoSetting.txSubject)
        #cbSubject(件名)
        self.cbSubject.updateConfigSetting(PdfInfoSetting.cbSubject)
        
        #lbAuthor(作成者)
        self.lbAuthor.updateConfigSetting(PdfInfoSetting.lbAuthor)
        #txAuthor(作成者)
        self.txAuthor.updateConfigSetting(PdfInfoSetting.txAuthor)
        #cbAuthor(作成者)
        self.cbAuthor.updateConfigSetting(PdfInfoSetting.cbAuthor)
        
        #lbKeywords(タグ)
        self.lbKeywords.updateConfigSetting(PdfInfoSetting.lbKeywords)
        #cbKeywords(タグ)
        self.cbKeywords.updateConfigSetting(PdfInfoSetting.cbKeywords)
        #txKeywords(タグ)
        self.txKeywords.updateConfigSetting(PdfInfoSetting.txKeywords)
        
        #lbProducer(Producer)
        self.lbProducer.updateConfigSetting(PdfInfoSetting.lbProducer)
        #txProducer(Producer)
        self.txProducer.updateConfigSetting(PdfInfoSetting.txProducer)
        #cbProducer(Producer)
        self.cbProducer.updateConfigSetting(PdfInfoSetting.cbProducer)
        
        #lbCreator(Creator)
        self.lbCreator.updateConfigSetting(PdfInfoSetting.lbCreator)
        #txCreator(Creator)
        self.txCreator.updateConfigSetting(PdfInfoSetting.txCreator)
        #cbCreator(Creator)
        self.cbCreator.updateConfigSetting(PdfInfoSetting.cbCreator)
        
        #btExecution(確定)
        self.btExecution.updateConfigSetting(PdfInfoSetting.btExecution)
        
        return
    
    def updateGUISetting(self, PdfInfoSetting:pdfEditorTool_PdfInfoSetting) -> None:
    
        #lbTitle(タイトル)
        self.lbTitle.updateGUISetting(PdfInfoSetting.lbTitle)
        #txTitle(タイトル)
        self.txTitle.updateGUISetting(PdfInfoSetting.txTitle)
        #cbTitle(タイトル)
        self.cbTitle.updateGUISetting(PdfInfoSetting.cbTitle)
        
        #lbSubject(件名)
        self.lbSubject.updateGUISetting(PdfInfoSetting.lbSubject)
        #txSubject(件名)
        self.txSubject.updateGUISetting(PdfInfoSetting.txSubject)
        #cbSubject(件名)
        self.cbSubject.updateGUISetting(PdfInfoSetting.cbSubject)
        
        #lbAuthor(作成者)
        self.lbAuthor.updateGUISetting(PdfInfoSetting.lbAuthor)
        #txAuthor(作成者)
        self.txAuthor.updateGUISetting(PdfInfoSetting.txAuthor)
        #cbAuthor(作成者)
        self.cbAuthor.updateGUISetting(PdfInfoSetting.cbAuthor)
        
        #lbKeywords(タグ)
        self.lbKeywords.updateGUISetting(PdfInfoSetting.lbKeywords)
        #txKeywords(タグ)
        self.txKeywords.updateGUISetting(PdfInfoSetting.txKeywords)
        #cbKeywords(タグ)
        self.cbKeywords.updateGUISetting(PdfInfoSetting.cbKeywords)
        
        #lbProducer(Producer)
        self.lbProducer.updateGUISetting(PdfInfoSetting.lbProducer)
        #txProducer(Producer)
        self.txProducer.updateGUISetting(PdfInfoSetting.txProducer)
        #cbProducer(Producer)
        self.cbProducer.updateGUISetting(PdfInfoSetting.cbProducer)
        
        #lbCreator(Creator)
        self.lbCreator.updateGUISetting(PdfInfoSetting.lbCreator)
        #txCreator(Creator)
        self.txCreator.updateGUISetting(PdfInfoSetting.txCreator)
        #cbCreator(Creator)
        self.cbCreator.updateGUISetting(PdfInfoSetting.cbCreator)
        
        #btExecution(確定)
        self.btExecution.updateGUISetting(PdfInfoSetting.btExecution)

        return
        
    def print(self) :
        return


class pdfInfoConfig():
    
    def __init__(self, configFileAddress:str, PdfInfoSetting:pdfEditorTool_PdfInfoSetting)-> None:
        super(pdfInfoConfig, self).__init__()
        self.FSP = FileSysProcess()
        self.CreateFileAddress = configFileAddress + "\\PdfInfoSetting_Jp.xml"
        if self.FSP.judgeFileExsit(self.CreateFileAddress) :
            self.configFileAddress = self.CreateFileAddress
        else :
            self.configFileAddress = configFileAddress + "\\Jp\\PdfInfoSetting_Jp.xml"

        self.ui = PdfInfoSetting
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
        eleToolGUI = Element("pdfEditorTool")

        #ツール名称GUI作成
        eleTool = Element("ToolName")
        self.toolName.outputConfigSetting(eleTool)
        eleToolGUI.append(eleTool)

        #【各pdfツール設定】GUI作成
        comment = ET.Comment('【各pdf情報設定】GUI')
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
        
