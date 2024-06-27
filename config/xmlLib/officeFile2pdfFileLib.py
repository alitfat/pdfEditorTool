import os
import win32com.client

from enum import Enum
from pathlib import Path

from Lib.ExcelSheetSelect import ExcelSheetSelect as excelSheetSelectProcess
from Lib.FileSysProcess import FileSysProcess
from Lib.pdfFileLib import pdfFileLib

class eOfficeFileType(Enum):
    Powerpoint = 0
    Excel = 1
    Word = 2
    OfficeFileTypeMax = 3


class office2PDFLib():
    
    class officeFileTypeValue:
        
        fileAppName:dict[eOfficeFileType, str] = {}
        saveIndex:dict[eOfficeFileType, int] = {}
        
        def __new__(cls, name):
            return super().__new__(cls)
        
        def __init__(self, name)->None:
            #print("id:", str(id(self)), "name:", name)
            self.name = name # インスタンス変数
            self.fileAppName.clear()
            self.saveIndex.clear()
            return
          
        @classmethod
        def addSetting(cls, fileType:eOfficeFileType, fileAppName:str, saveIndex:int )->None:
            cls.fileAppName[fileType] = fileAppName
            cls.saveIndex[fileType] = saveIndex
            return

        @classmethod
        def getOfficeApplicationName(cls, officeFileTypeValue : eOfficeFileType )->str:
            applicationName:str = cls.fileAppName.get(officeFileTypeValue, '')
            return applicationName
        
        @classmethod
        def getOfficeSaveIndex(cls, officeFileTypeValue : eOfficeFileType )->int:
            saveIndex:int =  cls.saveIndex.get(officeFileTypeValue, 0)
            return saveIndex

    
    objFullFileAddr:str = ""
    excelSheetFileList: list[str]=[]
    excelSelectSheetList: list[str]=[]
    officeFileExtList:dict[str, eOfficeFileType] = {}
    
    def __init__(self)->None:
        super(office2PDFLib, self).__init__()
        self.excelSelectSheetList.clear()
        self.excelSheetSelectPs =  excelSheetSelectProcess()
        self.excelSheetSelectPs.setui()
        self.pdfPs =  pdfFileLib()
        self.fsps = FileSysProcess()
        
        self.officeFileExtList.clear()
        self.officeFileExtList["ppt" ]= eOfficeFileType.Powerpoint
        self.officeFileExtList["pptx"]= eOfficeFileType.Powerpoint
        self.officeFileExtList["pptm"]= eOfficeFileType.Powerpoint
        
        self.officeFileExtList["xls" ]= eOfficeFileType.Excel
        self.officeFileExtList["xlsx"]= eOfficeFileType.Excel
        self.officeFileExtList["xlsm"]= eOfficeFileType.Excel
        
        self.officeFileExtList["doc" ]= eOfficeFileType.Word
        self.officeFileExtList["docx"]= eOfficeFileType.Word
        self.officeFileExtList["docm"]= eOfficeFileType.Word
        
        self.officeFileTypeValue("officeType")
        self.officeFileTypeValue.addSetting(eOfficeFileType.Powerpoint,        'Powerpoint.Application', 32 )
        self.officeFileTypeValue.addSetting(eOfficeFileType.Excel,             'Excel.Application',       0 )
        self.officeFileTypeValue.addSetting(eOfficeFileType.Word,              'Word.Application',       17 )
        self.officeFileTypeValue.addSetting(eOfficeFileType.OfficeFileTypeMax, '',                        0 )
        return
    

    def GetOfficeFileTypeByFileAddr(self, officeFullFileAddr : str) -> eOfficeFileType:
        """
        -----------------------------------------------------------------
        OfficeFileType取得処理\n
        【引数 】\n
            officeFullFileAddr:ファイルフルアドレス\n
        【戻り値】eOfficeFileType値\n
        -----------------------------------------------------------------
        """
        objFileName: list[str] = []
        bResult = self.fsps.getFileNameInfoByFileFullAddr(officeFullFileAddr, objFileName)
        if ( bResult  == False ) :
            return eOfficeFileType.OfficeFileTypeMax
        
        return self.officeFileExtList.get(objFileName[3], eOfficeFileType.OfficeFileTypeMax)
    

    def JudgeOfficeFileByFileAddr(self, officeFullFileAddr : str) -> bool:
        """
        -----------------------------------------------------------------
        OfficeFileType判定処理\n
        【引数 】\n
            officeFullFileAddr:ファイルフルアドレス\n
        【戻り値】判定結果\n
        -----------------------------------------------------------------
        """
        bResult:bool = True
        officeFiletype = self.GetOfficeFileTypeByFileAddr(officeFullFileAddr)
        #print(f'officeFiletype= {officeFiletype}')
        if officeFiletype == eOfficeFileType.OfficeFileTypeMax :
            bResult = False
        
        return bResult
    
    
    def GetOfficeFileName(self, officeFullFileAddr : str) -> str:
        """
        ------------------------------------------------------------
        対象Officeファイルアドレス取得処理\n
        【引数 】\n
            officeFullFileAddr:デフォルトファイルアドレス\n
        【戻り値】\n
            str:ファイルアドレス文字列\n
        ------------------------------------------------------------
        """
        officeFilePath = os.getcwd()
        officeFFileAddr = officeFullFileAddr
        resultList = self.fsps.getDirByFileFullAddr(officeFFileAddr)
        
        if resultList[0] == True :
            officeFilePath = resultList[1]

        objtype = [('All Office File','.ppt .pptx .pptm .doc .docx .docm .xls .xlsx .xlsm'),
                   ('Powerpoint File','.ppt .pptx .pptm'),
                   ('Excel File', '.xls .xlsx .xlsm'),
                   ('Word File', '.doc .docx .docm') ]
        
        #ファイルパス指定（絶対パスをPathメソッドでWindowsPath型に変換要）
        fileAddr = self.fsps.getFileFullAddrByFileDialog(objtype, officeFilePath)
        if fileAddr != "":
            officeFFileAddr = fileAddr
        return officeFFileAddr
    

    def ConvertofficeFile2pdfFile(self, officeFullFileAddr:str, pdfFullFileAddr:str) -> bool:
        """
        -----------------------------------------------------------------
        OfficeファイルをPDFファイルへ変換する処理\n
        【引数 】\n
            officeFullFileAddr:対象officeファイルフルアドレス\n
            pdfFullFileAddr:生成されたpdfファイル格納アドレス\n
        【戻り値】変換実施結果\n
        -----------------------------------------------------------------
        """
        officeFiletype = self.GetOfficeFileTypeByFileAddr(officeFullFileAddr)
        
        if officeFiletype == eOfficeFileType.OfficeFileTypeMax :
            return False
        
        bResult = True
        try:
            match(officeFiletype):
                case eOfficeFileType.Powerpoint: bResult = self.ConvertpptFile2pdfFile(officeFullFileAddr, pdfFullFileAddr)
                case eOfficeFileType.Word:       bResult = self.ConvertWordFile2pdfFile(officeFullFileAddr, pdfFullFileAddr)
                case eOfficeFileType.Excel:      bResult = self.ConvertExcelFile2pdfFile(officeFullFileAddr, pdfFullFileAddr)
                case _:
                    pass
        except Exception as e:
            bResult = False
           
        return bResult
    
    
    def ConvertpptFile2pdfFile(self, pptFileAddr:str, pdfFullFileAddr:str) -> bool:
        """
        -----------------------------------------------------------------
        PowerpointファイルをPDFファイルへ変換する処理\n
        【引数 】\n
            pptFileAddr:対象Powerpointファイルフルアドレス\n
            pdfFullFileAddr:生成されたpdfファイル格納アドレス\n
        【戻り値】変換実施結果\n
        -----------------------------------------------------------------
        """
        objFileApplication = self.officeFileTypeValue.getOfficeApplicationName(eOfficeFileType.Powerpoint)
        objFileSaveIndex = self.officeFileTypeValue.getOfficeSaveIndex(eOfficeFileType.Powerpoint)

        #対象アプリケーションの準備
        application = win32com.client.DispatchEx(objFileApplication)
        
        bResult =  True
        try:
            # PowerpointファイルをPDF形式で保存
            """
            ------------------------------------------------------------------------------
            application.Presentations.Open説明
                Filename:pptFileAddr
                ReadyOnly:True
                Untitled:False
                WithWindow:False
            注: 下記資料を参考
                https://learn.microsoft.com/ja-jp/office/vba/api/powerpoint.presentations.open
            ------------------------------------------------------------------------------
            """
            presentation = application.Presentations.Open(pptFileAddr, True, False, False)
            presentation.SaveAs(Path(pdfFullFileAddr), objFileSaveIndex)
        except Exception as e:
            bResult = False
        
        # アプリケーション終了処理
        presentation.Close()
        presentation = None
        application.Quit()
        application = None
        
        return bResult
    
    
    def ConvertWordFile2pdfFile(self, wordFileAddr:str, pdfFullFileAddr:str) -> bool:
        """
        -----------------------------------------------------------------
        WordファイルをPDFファイルへ変換する処理\n
        【引数 】\n
            wordFileAddr:対象Wordファイルフルアドレス\n
            pdfFullFileAddr:生成されたpdfファイル格納アドレス\n
        【戻り値】変換実施結果\n
        -----------------------------------------------------------------
        """
        bResult = True
        objFileApplication = self.officeFileTypeValue.getOfficeApplicationName(eOfficeFileType.Word)
        objFileSaveIndex = self.officeFileTypeValue.getOfficeSaveIndex(eOfficeFileType.Word)
        #対象アプリケーションの準備
        application = win32com.client.DispatchEx(objFileApplication)

        # WordファイルをPDF形式で保存
        try:
            """
            ------------------------------------------------------------------------------
            application.Documents.Open説明
                Filename:wordFileAddr
                ConfirmConversions:False
                ReadyOnly:True
            注: 下記資料を参考
                https://learn.microsoft.com/ja-jp/office/vba/api/word.documents.open
            ------------------------------------------------------------------------------
            """
            document = application.Documents.Open(wordFileAddr, False, True)
            document.SaveAs(pdfFullFileAddr, objFileSaveIndex)
        except Exception as e:
            bResult = False

        # アプリケーション終了処理
        document.Close()
        document = None
        application.Quit()
        application = None
        return bResult
    
    
    def SelectExcelSheetFile(self, excelFileAddr :str ="") -> None:
        """
        -----------------------------------------------------------------
        Excel Sheet選択処理\n
        【引数 】\n
            excelFileAddr:対象Excelファイルフルアドレス\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        #対象アプリケーションの準備
        application = win32com.client.DispatchEx('Excel.Application')
        # Excelファイルを開く
        """
        -------------------------------------------------------------------------------------------------------------------
        application.Workbooks.Open説明
            Filename:excelFileAddr
            UpdateLinks:None
            ReadyOnly:True
        注: 下記資料を参考
            https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.excel.workbooks.open?view=excel-pia
        -------------------------------------------------------------------------------------------------------------------
        """
        workbook = application.Workbooks.Open(excelFileAddr, None, True)
        self.excelSheetFileList.clear()
        for sheet in workbook.Sheets :
            self.excelSheetFileList.append(sheet.Name)
        workbook.Close()
        workbook = None

        self.excelSheetSelectPs.showGUI(excelFileAddr, self.excelSheetFileList)
        return 
    

    def ConvertExcelFile2pdfFile(self, excelFileAddr: str, pdfFullFileAddr: str) -> bool:
        """
        -----------------------------------------------------------------
        ExcelファイルをPDFファイルへ変換する処理\n
        【引数 】\n
            excelFileAddr:対象Excelファイルフルアドレス\n
            pdfFullFileAddr:生成されたpdfファイル格納アドレス\n
        【戻り値】変換実施結果\n
        -----------------------------------------------------------------
        """
        bResult = False
        objFileApplication = self.officeFileTypeValue.getOfficeApplicationName(eOfficeFileType.Excel)
        #対象アプリケーションの準備
        application = win32com.client.DispatchEx(objFileApplication)
        """
        -------------------------------------------------------------------------------------------------------------------
        application.Workbooks.Open説明
            Filename:excelFileAddr
            UpdateLinks:None
            ReadyOnly:True
        注: 下記資料を参考
            https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.excel.workbooks.open?view=excel-pia
        -------------------------------------------------------------------------------------------------------------------
        """
        workbook = application.Workbooks.Open(excelFileAddr, None, True)
        pdfFileList: list[str]=[]
        excelSheetFileList: list[str]=[]
        selectSheetList: list[str]=[]
        for sheet in workbook.Sheets :
            excelSheetFileList.append(sheet.Name)
            
        self.excelSheetSelectPs.getSelectSheetList(excelFileAddr, excelSheetFileList,  selectSheetList)
        num = len(selectSheetList)
        if (num == 0 ):
            selectSheetList = excelSheetFileList
        
        #全てのシートをループ
        self.__SaveExcelFileSheets(workbook, application, pdfFileList, selectSheetList, pdfFullFileAddr)

        num = len(pdfFileList)
        if (num != 0 ):
            self.pdfPs.MergepdfFile(pdfFileList, pdfFullFileAddr)
            bResult = True
        
        # アプリケーション終了処理
        workbook.Close()
        workbook = None
        application.Quit()
        application = None
        
        for pdfFileName in pdfFileList:
            self.fsps.delFile(pdfFileName)

        return bResult
    
    def __SaveExcelFileSheets(self, workbook, application, pdfFileList: list[str], selectSheetList:list[str], pdfFullFileAddr: str)->None:
        #全てのシートをループ
        for sheetName in selectSheetList :
            self.__SaveExcelFileSheet(workbook, application, pdfFileList, sheetName, pdfFullFileAddr)     
        return

    def __SaveExcelFileSheet(self,workbook, application, pdfFileList: list[str], sheetName:str, pdfFullFileAddr: str)->None:
        #ファイルを選択
        application.Worksheets(sheetName).Activate()
        activesheet = application.ActiveSheet
        pdfFileWithSheetName = self.fsps.getRandomValue()
        pdfFileWithSheetName = pdfFullFileAddr.replace('.pdf', '_' + pdfFileWithSheetName  + '.pdf')
            
        #PDF変換
        try:
            workbook.ActiveSheet.ExportAsFixedFormat(0, pdfFileWithSheetName)
            pdfFileList.append(pdfFileWithSheetName)
        except Exception as e:
            pass
        return
            
    