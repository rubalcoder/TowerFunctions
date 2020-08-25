import os
from pathlib import Path


class Flashing:
    def __init__(self):
        self.ftpPath = "\\\\fijyvvrcis07\\deliveries\\firmware\\"
        self.flashFileDestination = "c:\\nb_flash_files"
        self.branchCount = 0
        self.VariantCount = 0
        self.buildCount = 0

    def FlashFilesPath(self,project,branch,variant,build='Latest'):
        self.project = project
        self.branch = branch
        self.variant = variant
        self.project = project
        self.build = str(build)
        if self.project.casefold() == "picasso".casefold():
            self.ftpPath=self.ftpPath+self.project+"\\nightly-builds\\"
            self.branchList = os.listdir(self.ftpPath)

            for branches in self.branchList:
                if branches.casefold() == self.branch.casefold():
                    global branchCount
                    self.branchCount = self.branchCount+1
                    self.ftpPath = self.ftpPath+"\\"+branches+"\\"+self.build

                    if os.path.isdir(self.ftpPath):
                        global buildCount
                        self.buildCount=self.buildCount+1
                        self.ftpPath = self.ftpPath+'\\publish'
                        self.variantList=os.listdir(self.ftpPath)

                        for variants in self.variantList:
                            if variants.casefold() == self.variant.casefold():
                                global VariantCount
                                self.VariantCount=self.VariantCount+1
                                self.ftpPath = self.ftpPath+"\\"+variants+"\\Release\\Flash"
                                self.flashfilesPath = self.ftpPath
                                #return flashfilesPath



        if self.project.casefold() == "Picasso_Products".casefold():
            self.ftpPath = self.ftpPath+self.project+"\\nightly-builds\\"
            self.branchList = os.listdir(self.ftpPath)
            for branches in self.branchList:
                if branches.casefold() == self.branch.casefold():
                    global branchCount
                    self.branchCount=self.branchCount+1
                    self.ftpPath = self.ftpPath+"\\"+branches+"\\"+self.build


                    if os.path.isdir(self.ftpPath):
                        global buildCount
                        self.buildCount=self.buildCount+1
                        self.ftpPath = self.ftpPath+'\\publish'
                        self.variantList=os.listdir(self.ftpPath)


                        for variants in self.variantList:
                            if variants.casefold() == self.variant.casefold():
                                global VariantCount
                                self.VariantCount=self.VariantCount+1
                                self.ftpPath = self.ftpPath+"\\"+variants+"\\Release\\Flash"
                                if variants.casefold() == "E360LTE3Ph".casefold():
                                    self.ftpPath = self.ftpPath+"\\"+"_hw5"
                                    self.flashfilesPath=self.ftpPath
                                    #return flashfilesPath
                                elif variants.casefold() == "E360LTE1Ph".casefold():
                                    self.ftpPath = self.ftpPath + "\\"+"_hw4"
                                    self.flashfilesPath = self.ftpPath
                                    #return flashfilesPath
                                else:
                                    pass


        if self.branchCount == 0:
            print("Incorrect Branch specified or branch does not exist")
        elif self.buildCount == 0:
            print("Incorrect Build specfied or Hex build is not successfull")
        elif self.VariantCount == 0:
            print("Incorrect Variant specified or Variant does not exist")
        else:
            pass

        def firmwareFlash(self):
            self.filespath=self.flashfilesPath
            if os.path.exists(self.flashFileDestination+"\\"+self.build):
                os.system("xcopy /e /h /y"+" "+self.filespath+" "+self.flashFileDestination+"\\"+self.build)
            else:
                os.makedirs(self.flashFileDestination+"\\"+self.build)
                os.system("xcopy /e /h /y" + " " + self.filespath + " " + self.flashFileDestination + "\\" + self.build)

        firmwareFlash(self)



flash1=Flashing()
flash1.FlashFilesPath(project="picasso_products",variant="E360LTE3Ph",branch="E360_Picasso",build=818)