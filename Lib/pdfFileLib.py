import os
from datetime import datetime
from pypdf  import PdfReader,PdfWriter, DocumentInformation
from typing  import Any
from pypdf.constants import UserAccessPermissions, DocumentInformationAttributes as pdfDocInfoAttr

from Lib.FileSysProcess import FileSysProcess

ALL_DOCUMENT_NoPERMISSIONS = UserAccessPermissions(0)
ALL_DOCUMENT_PERMISSIONS = UserAccessPermissions((2**31 - 1) - 3)

class pdfFileLib():

    fsps:FileSysProcess
    
    def __init__(self):
        super(pdfFileLib, self).__init__()
        self.fsps = FileSysProcess()
        return


    def MergepdfFile(self, mergepdfFileList : list[str], outputpdfFileAddr : str) -> None:
        """
        -----------------------------------------------------------------
        PDFファイル結合処理\n
        【引数 】\n
            mergepdfFileList:pdfファイルリスト\n
            outputpdfFileAddr:結合後の出力pdfファイルアドレス\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        pdf_reader = PdfReader(mergepdfFileList[0])
        pdf_writer = PdfWriter(clone_from=pdf_reader)
        for pdfFileName in mergepdfFileList [1:len(mergepdfFileList):1]:
            pdf_reader = PdfReader(pdfFileName)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
                
        with open(outputpdfFileAddr,'wb') as pdfFileObj:
            pdf_writer.write(pdfFileObj)
        pdfFileObj.close()
        return


    def AddEncrypt2pdfFiles(self, pdfFileAddrList : list[str],
                            user_password : str = "",
                            owner_password:str = "", 
                            permissions_flag:UserAccessPermissions = ALL_DOCUMENT_NoPERMISSIONS, 
                            encryptType : str = "AES-256") -> bool:
        """
        -----------------------------------------------------------------
        PDFファイル暗号化処理\n
        【引数 】\n
            pdfFileList:pdfファイルアドレスリスト\n
            user_password:パスワード文字列\n
            owner_password:権限変更パスワード文字列\n
            permissions_flag:権限設定\n
                PRINT= 4\n
                MODIFY= 8\n
                EXTRACT= 16\n
                ADD_OR_MODIFY= 32\n
                FILL_FORM_FIELDS= 256\n
                EXTRACT_TEXT_AND_GRAPHICS= 512\n
                ASSEMBLE_DOC= 1024\n
                PRINT_TO_REPRESENTATION= 2048\n
                参考先:https://pypdf.readthedocs.io/en/latest/modules/constants.html\n
            encryptType:暗号化ラベル\n
                "RC4-40"、"RC4-128"、"AES-128"、"AES-256"\n
                参考先:https://pypdf.readthedocs.io/en/latest/user/encryption-decryption.html\n
        【戻り値】実施結果\n
        -----------------------------------------------------------------
        """
        bResult = True
        for pdfFileName in pdfFileAddrList :
            bResult = self.AddEncrypt2pdfFile(pdfFileName = pdfFileName, 
                                              user_password = user_password,
                                              owner_password = owner_password,
                                              permissions_flag = permissions_flag,
                                              encryptType = encryptType)
            if ( bResult  == False ) :
                return bResult
        return bResult


    def __set_password(self, src_path : str, 
                       dst_path : str, 
                       user_password : str, 
                       owner_password:str = "", 
                       permissions_flag:UserAccessPermissions = ALL_DOCUMENT_NoPERMISSIONS, 
                       encryptType : str = "AES-256") -> None:
        """
        -----------------------------------------------------------------
        PDFファイル暗号化処理\n
        【引数 】\n
            src_path:暗号化対象pdfファイルアドレス\n
            dst_path:暗号化後pdfファイルの格納場所\n
            user_password:ドキュメントを開くパスワード文字列\n
            owner_password:権限変更パスワード文字列\n
            permissions_flag:権限設定\n
                PRINT= 4\n
                MODIFY= 8\n
                EXTRACT= 16\n
                ADD_OR_MODIFY= 32\n
                FILL_FORM_FIELDS= 256\n
                EXTRACT_TEXT_AND_GRAPHICS= 512\n
                ASSEMBLE_DOC= 1024\n
                PRINT_TO_REPRESENTATION= 2048\n
                参考先:https://pypdf.readthedocs.io/en/latest/modules/constants.html\n
            encryptType:暗号化ラベル\n
                "RC4-40"\n
                "RC4-128"\n
                "AES-128"\n
                "AES-256"\n
                参考先:https://pypdf.readthedocs.io/en/latest/user/encryption-decryption.html\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        pdf_reader = PdfReader(src_path)
        pdf_writer = PdfWriter(clone_from=pdf_reader)
        if owner_password =="":
            owner_password = user_password
        pdf_writer.encrypt(user_password=user_password,
                           algorithm= encryptType,
                           owner_password = owner_password,
                           permissions_flag = permissions_flag)

        with open(dst_path, "wb") as f:
            pdf_writer.write(f)
        return


    def AddEncrypt2pdfFile(self, 
                           pdfFileName : str, 
                           user_password : str = "", 
                           owner_password: str = "",
                           permissions_flag: UserAccessPermissions = ALL_DOCUMENT_NoPERMISSIONS,
                           encryptType : str = "AES-256") -> bool:
        """
        -----------------------------------------------------------------
        PDFファイル暗号化処理\n
        【引数 】\n
            pdfFileName:暗号化対象pdfファイルアドレス\n
            user_password:パスワード文字列\n
            owner_password:権限変更パスワード文字列\n
            permissions_flag:権限設定\n
                PRINT= 4\n
                MODIFY= 8\n
                EXTRACT= 16\n
                ADD_OR_MODIFY= 32\n
                FILL_FORM_FIELDS= 256\n
                EXTRACT_TEXT_AND_GRAPHICS= 512\n
                ASSEMBLE_DOC= 1024\n
                PRINT_TO_REPRESENTATION= 2048\n
                参考先:https://pypdf.readthedocs.io/en/latest/modules/constants.html\n
            encryptType:暗号化ラベル\n
                "RC4-40"\n
                "RC4-128"\n
                "AES-128"\n
                "AES-256"\n
                参考先:https://pypdf.readthedocs.io/en/latest/user/encryption-decryption.html\n
        【戻り値】実施結果\n
        -----------------------------------------------------------------
        """
        tmpStr = self.fsps.getRandomValue()
        tmpStr = tmpStr + '.pdf'
        
        fileTempName = pdfFileName.replace('.pdf', tmpStr)
        os.rename(pdfFileName, fileTempName) 
        self.__set_password(src_path = fileTempName, 
                            dst_path = pdfFileName, 
                            user_password = user_password,
                            owner_password = owner_password,
                            permissions_flag = permissions_flag,
                            encryptType = encryptType)
        os.remove(fileTempName) 
        return True


    def JudgePdfFileIsEncrypted(self, pdfSrcFileName : str) -> bool:
        """
        -----------------------------------------------------------------
        PDFファイルが暗号つけるかどうかを確認\n
        【引数 】\n
            pdfSrcFileName:対象pdfファイルアドレス\n
        【戻り値】判定結果\n
        -----------------------------------------------------------------
        """
        bResult = True
        
        # パスワード設定用PDFをバイナリモードで開く
        pdf_open = open(pdfSrcFileName,"rb")
        # PdfReaderオブジェクト生成
        pdf_reader = PdfReader(pdf_open)
        
        # 暗号化しているか確認
        if  not pdf_reader.is_encrypted:
            pdf_open.close()
            bResult = False
            return bResult
        
        pdf_open.close()
        return bResult


    def DecryptpdfFile(self, pdfSrcFileName : str, pdfDecryptFileName : str, password : str = "") -> bool:
        """
        -----------------------------------------------------------------
        PDFファイル復唱化処理\n
        【引数 】\n
            pdfSrcFileName:暗号化対象pdfファイルアドレス\n
            pdfDecryptFileName:復唱化後pdfファイルアドレス\n
            password:パスワード文字列\n
        【戻り値】実施結果\n
        -----------------------------------------------------------------
        """
        bResult = True
        
        # PdfReaderオブジェクト生成
        pdf_reader = PdfReader(pdfSrcFileName)
        
        # 暗号化しているか確認
        if  not pdf_reader.is_encrypted:
            bResult = False
            return bResult
        
        try:
            #パスワード解除（復号化）
            pdf_reader.decrypt(password)
            # PdfWriterオブジェクト
            pdf_writer = PdfWriter(clone_from=pdf_reader)
            # 暗号化情報を書き込み
            with open(pdfDecryptFileName,'wb') as pdfFileWithoutEncrypt:
                pdf_writer.write(pdfFileWithoutEncrypt)
        
        except Exception as e:
            bResult = False
        
        return bResult


    def JudgePdfFileByFileAddr(self, pdfFullFileAddr : str ) -> bool:
        """
        -----------------------------------------------------------------
        pdfFileType判定処理\n
        【引数 】\n
            pdfFullFileAddr:対象pdfファイルフルアドレス\n
        【戻り値】判定結果\n
        -----------------------------------------------------------------
        """
        bResult = True
        pdfFileName: list[str] = []
        bResult = self.fsps.getFileNameInfoByFileFullAddr(pdfFullFileAddr, pdfFileName)
        
        if ( bResult  == False ) :
            return bResult
            
        pdfFileType = pdfFileName[3]
        if ( pdfFileType  != "pdf" ) :
            bResult  = False

        return bResult
    
    def update_metadata(self, src_path : str, dst_path : str,
                        metadata:dict[Any, Any],
                        user_password:str= "",
                        owner_password:str = "",
                        encryptType:str = "AES-256",
                        permissions_flag: UserAccessPermissions =ALL_DOCUMENT_NoPERMISSIONS
                        ) ->None:
        """
        -----------------------------------------------------------------
        pdfファイルmetadata更新処理\n
        【引数 】\n
            src_path:対象pdfファイルフルアドレス\n
            dst_path:生成後pdfファイルフルアドレス\n
            metadata:metadata要素
                "/Author":作成者
                "/Producer":メーカ
                "/Title":タイトル
                "/Subject":サブタイトル
                "/Keywords":キーワード
                "/CreationDate":作成日時
                "/ModDate":更新日時
                "/Creator":
                "/CustomField":
            user_password:パスワード文字列\n
            owner_password:権限変更パスワード文字列\n
            encryptType:暗号化ラベル\n
                "RC4-40"\n
                "RC4-128"\n
                "AES-128"\n
                "AES-256"\n
                参考先:https://pypdf.readthedocs.io/en/latest/user/encryption-decryption.html\n
            permissions_flag:権限設定\n
                PRINT= 4\n
                MODIFY= 8\n
                EXTRACT= 16\n
                ADD_OR_MODIFY= 32\n
                FILL_FORM_FIELDS= 256\n
                EXTRACT_TEXT_AND_GRAPHICS= 512\n
                ASSEMBLE_DOC= 1024\n
                PRINT_TO_REPRESENTATION= 2048\n
                参考先:https://pypdf.readthedocs.io/en/latest/modules/constants.html\n
        【戻り値】判定結果\n
        -----------------------------------------------------------------
        """
        src_pdf = PdfReader(src_path)

        if src_pdf.is_encrypted:
            src_pdf.decrypt(password=owner_password)
            dst_pdf = PdfWriter(clone_from=src_pdf)
            if owner_password =="":
                owner_password = user_password
            dst_pdf.encrypt(user_password=user_password, 
                            owner_password=owner_password,
                            permissions_flag=permissions_flag,
                            algorithm= encryptType)
        else:
            dst_pdf = PdfWriter(clone_from=src_pdf)

        utc_time = "+09'00'"  # UTC time optional
        time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")
        metadata[pdfDocInfoAttr.CREATION_DATE] = time
        metadata[pdfDocInfoAttr.MOD_DATE] = time
        # Add the new metadata
        dst_pdf.add_metadata(metadata)
        # Save the new PDF to a file
        dst_pdf.write(dst_path)
        return


