import os,sys
from lib.common.CreatLog import creatLog

class FileRead(object):
    def __init__(self,file) -> None:
        self.log = creatLog().get_logger()
        self.filepath=file
    def getUrlLists(self):
        try:
            with open(self.filepath, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
                print(lines)
                print('\n')
            if lines == []:
                self.log.info("[Info] urlLists is empty!")
                sys.exit(0)
            return lines
        except FileNotFoundError:
            self.log.error("[Err] File not found %s" % e)
        except PermissionError:
            self.log.error("[Err] Permission denied %s" % e)
        except Exception as e:
            self.log.error("[Err] An error occurred: %s" % e)