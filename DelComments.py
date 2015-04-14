#!/usr/bin/python
# -*- coding: GB18030 -*-
#ȥ��C\C++�ļ��е�ע�͡�����

import os,sys
import time

#c/c++�ļ���չ���б�
cppFileExtList = ['.h', '.c', '.cpp', '.xx']

#����һ���ļ���ȥ��ע��
def ProcessFile(Filename):
    
    strFilename = Filename
    
    FileObj = open(strFilename, 'r')
    
    if os.path.exists("mod_src") == False:
        os.mkdir("mod_src")
    
    DstFileobj = open("mod_src\\" + strFilename, 'w+')
    
    #��һ���ǲ���ע��
    isLastLineAComment = False
    
    line = ""
    for line in  FileObj.readlines():
        #ȥ��β�ո�\Tab etc
        NewLine = line.strip(' \t\n\r')
    
        #ȥ����
        if NewLine == "":
            continue    
        
        if NewLine[0:2] == "//":
            #print '����һ��ע��'    
            continue
        if NewLine[0:2] == "/*":
            isLastLineAComment = True
            
        if isLastLineAComment == True:
            nIndex = NewLine.find('*/')
            if nIndex != -1:
                if NewLine[-2:] != "*/":
                    print '���г���ע�ͻ��д��룡����',NewLine[-2:]
                    strWrite = NewLine[nIndex+2:].strip()
                    DstFileobj.write(strWrite +'\n')
                isLastLineAComment = False
            #��������
            continue
        
        #�������������ע��
        nIndex = NewLine.find('//')
        if nIndex != -1:
            #����������ߵ������ȷ��ţ�ȥ���ұߵ�
            strWrite = line[:nIndex].rstrip()
            DstFileobj.write(strWrite +'\n')
            continue
        
        DstFileobj.write(line)
        
    FileObj.close()
    DstFileobj.close()

def IsCorCppSrc(filename):
    for strExt in cppFileExtList:
        nPos = filename.rfind(strExt)
        #�ļ���������Ӧ��չ���ַ����������ж�һ���Ƿ���ĩβ
        #if nPos != -1: 
        if filename[-len(strExt):] == strExt:
            print '�ļ� %s ��һ��C/C++Դ���ļ�������֮' %filename
            return True
    
if __name__=="__main__":
    #������ǰĿ¼�е�C/C++�ļ�    
    for dirpath, dirnames, filenames in os.walk(os.curdir):
        #print dirpath, dirnames, filenames
        for curfile in filenames:
            if IsCorCppSrc(curfile):
                #print "�ҵ�һ��C/C++Դ���ļ�...",curfile
                ProcessFile(curfile)
        #ֻ������ǰĿ¼�����ٱ����¼�Ŀ¼
        break
    print '��������ˣ�ȥmod_srcȥ�����ɣ�'