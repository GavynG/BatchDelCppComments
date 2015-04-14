#!/usr/bin/python
# -*- coding: GB18030 -*-
#去除C\C++文件中的注释、空行

import os,sys
import time

#c/c++文件扩展名列表
cppFileExtList = ['.h', '.c', '.cpp', '.xx']

#处理一个文件，去除注释
def ProcessFile(Filename):
    
    strFilename = Filename
    
    FileObj = open(strFilename, 'r')
    
    if os.path.exists("mod_src") == False:
        os.mkdir("mod_src")
    
    DstFileobj = open("mod_src\\" + strFilename, 'w+')
    
    #上一行是不是注释
    isLastLineAComment = False
    
    line = ""
    for line in  FileObj.readlines():
        #去首尾空格\Tab etc
        NewLine = line.strip(' \t\n\r')
    
        #去空行
        if NewLine == "":
            continue    
        
        if NewLine[0:2] == "//":
            #print '这是一行注释'    
            continue
        if NewLine[0:2] == "/*":
            isLastLineAComment = True
            
        if isLastLineAComment == True:
            nIndex = NewLine.find('*/')
            if nIndex != -1:
                if NewLine[-2:] != "*/":
                    print '这行除了注释还有代码！！！',NewLine[-2:]
                    strWrite = NewLine[nIndex+2:].strip()
                    DstFileobj.write(strWrite +'\n')
                isLastLineAComment = False
            #跳过这行
            continue
        
        #正常代码后面有注释
        nIndex = NewLine.find('//')
        if nIndex != -1:
            #保留代码左边的缩进等符号，去除右边的
            strWrite = line[:nIndex].rstrip()
            DstFileobj.write(strWrite +'\n')
            continue
        
        DstFileobj.write(line)
        
    FileObj.close()
    DstFileobj.close()

def IsCorCppSrc(filename):
    for strExt in cppFileExtList:
        nPos = filename.rfind(strExt)
        #文件名包含相应扩展名字符串，但需判断一下是否在末尾
        #if nPos != -1: 
        if filename[-len(strExt):] == strExt:
            print '文件 %s 是一个C/C++源码文件，处理之' %filename
            return True
    
if __name__=="__main__":
    #遍历当前目录中的C/C++文件    
    for dirpath, dirnames, filenames in os.walk(os.curdir):
        #print dirpath, dirnames, filenames
        for curfile in filenames:
            if IsCorCppSrc(curfile):
                #print "找到一个C/C++源码文件...",curfile
                ProcessFile(curfile)
        #只遍历当前目录，不再遍历下级目录
        break
    print '处理完毕了，去mod_src去看看吧！'