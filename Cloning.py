import os
from git import Repo


class cloning:
    def __init__(self, **kwargs):
        self.PlatformRepository="Picasso_Test"
        self.ProductRepository="PPT"
        for i, v in kwargs.items():
            if i.casefold() == "slotLookup".casefold():
                self.slotLookup = v
            elif i.casefold() == "slots".casefold():
                self.slots = v
                self.slots = self.slots.split(",")
            elif i.casefold() == "branch".casefold():
                self.branch = v
            elif i.casefold() == "variant".casefold():
                self.variant = v
            elif i.casefold() == "project".casefold():
                self.project = v
            elif i.casefold() == "user".casefold():
                self.user = 'jhaabhis'
            else:
                pass


    def platformClone(self):
        for self.slot in self.slots:
            if os.path.isdir(self.slotLookup+"\\"+self.slot+"\\"+self.project+"\\"+self.variant+"\\"+self.PlatformRepository):
                self.repo = Repo(self.slotLookup+"\\"+self.slot+"\\"+self.project+"\\"+self.variant+"\\"+self.PlatformRepository)
                self.repositorybranch = self.repo.active_branch

                if str(self.repositorybranch).casefold() == self.branch.casefold():
                    os.chdir(self.slotLookup+"\\"+self.slot+"\\"+self.project+"\\"+self.variant+"\\"+self.PlatformRepository)
                    os.system("git pull")
                    os.chdir(self.slotLookup + "\\" + self.slot + "\\" + self.project + "\\" + self.variant + "\\" + self.PlatformRepository + "\\Setups\\ATS\\"+self.variant)
                    os.system("call Setup_ATS_"+self.variant+".bat")
                    break

                else:
                    os.chdir(self.slotLookup + "\\" + self.slot + "\\" + self.project + "\\" + self.variant)
                    os.system ("rmdir "+self.PlatformRepository+" /s /q")
                    os.system("git clone ssh://"+self.user+"@gerrit-eu.landisgyr.net:29418/Picasso_Test --branch "+self.branch)
                    os.system("cd "+self.PlatformRepository)
                    os.chdir(self.slotLookup + "\\" + self.slot + "\\" + self.project + "\\" + self.variant + "\\" + self.PlatformRepository + "\\Setups\\ATS\\" + self.variant)
                    os.system("call Setup_ATS_" + self.variant + ".bat")
                    break

            else:
                os.chdir(self.slotLookup + "\\" + self.slot + "\\" + self.project + "\\" + self.variant)
                os.system("git clone ssh://" + self.user + "@gerrit-eu.landisgyr.net:29418/Picasso_Test --branch "+self.branch)
                os.system("cd "+self.PlatformRepository)
                os.chdir(self.slotLookup + "\\" + self.slot + "\\" + self.project + "\\" + self.variant + "\\" + self.PlatformRepository + "\\Setups\\ATS\\" + self.variant)
                os.system("call Setup_ATS_" + self.variant + ".bat")
                break


    def productclone(self):
        for self.slot in self.slots:
            if os.path.isdir(self.slotLookup + "\\" + self.slot + "\\" + self.project + "\\" + self.ProductRepository):
                os.system("rmdir " + self.ProductRepository + " /s /q")
                os.chdir(self.slotLookup + "\\" + self.slot + "\\" + self.project)
                os.system("git clone ssh://"+self.user+"@gerrit-eu.landisgyr.net:29418/Picasso_Products_Tests PPT")
                os.system("cd PPT")
                os.system("git checkout E360_Picasso")
                os.system("git config --local --replace-all submodule.Picasso_Test.url ssh://inampbsuser@gerrit-eu.landisgyr.net:29418/Picasso_Test")
                os.system("git submodule update --init")
                os.system("cd Picasso_Test")
                os.system("git checkout master")

            else:
                os.chdir(self.slotLookup + "\\" + self.slot + "\\" + self.project)
                os.system("git clone ssh://" + self.user + "@gerrit-eu.landisgyr.net:29418/Picasso_Products_Tests PPT")
                os.system("cd PPT")
                os.system("git checkout E360_Picasso")
                os.system("git config --local --replace-all submodule.Picasso_Test.url ssh://"+self.user+"@gerrit-eu.landisgyr.net:29418/Picasso_Test")
                os.system("git submodule update --init")
                os.system("cd Picasso_Test")
                os.system("git checkout master")


#s=cloning(slotLookup="D:\Slots",slots="slot_D",branch="master",variant="Ref_NMS2",project='e360 emea',user='jhaabhis')
#s.productclone()