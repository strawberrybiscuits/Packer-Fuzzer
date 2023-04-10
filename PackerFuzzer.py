# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

from lib.Controller import Project
from lib.TestProxy import testProxy
from lib.common.banner import RandomBanner
from lib.common.cmdline import CommandLines
from lib.common.readConfig import ReadConfig
from lib.common.FileRead import FileRead
from concurrent.futures import ThreadPoolExecutor,wait, ALL_COMPLETED

class Program():
    def __init__(self,options):
        self.options = options

    def check(self):
        url = self.options.url
        if url != None:
            t = Project(url,self.options)
            t.parseStart()
        else :
            #不能放循环，循环内多线程无法控制。循环结束漏洞无法分析、报告无法生成
            file = self.options.file
            urlLists = FileRead(file).getUrlLists()
            pool = ThreadPoolExecutor(10)
            allTask = [pool.submit(self.worker, domain) for domain in urlLists]
            wait(allTask, return_when=ALL_COMPLETED)
                
    def worker(self,url):
        try:
            t = Project(url,self.options)
            t.parseStart()
        except Exception as e:
            print("error :%s" % e)
            

if __name__ == '__main__':
    cmd = CommandLines().cmd()
    testProxy(cmd,1)
    PackerFuzzer = Program(cmd)
    PackerFuzzer.check()
