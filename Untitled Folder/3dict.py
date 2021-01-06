import pandas as pd
dic = pd.read_excel('//fss0201/Marketing/overseas/輸出関連プロセス/商品情報抽出/Navi/◆商品情報提供/ptthon_work/chk_Kwords.xlsx')    
dic_j = dic['origin'].to_string(index=False)
dic_t = dic['right'].to_string(index=False)
dictor = str.maketrans(dic_j, dic_t)

def all_dic(brand,date):    
    
    basic = pd.read_excel('..\\\\%basic_%s.xlsx'%(brand,date))
    #dic~~~~~~~#
    dicted = []
    for index, text in basic['productName_K'].iteritems():
        text = str(text)
        item = text.translate(dictor)
        dicted.append(item)
    basic['dic'] = pd.Series(dicted)
    #dic~~~~~~~#
    basic.to_excel('..\\\\%basic_%s.xlsx'%(brand,date), Index=None)
    
    #--------------#
    mono = pd.read_excel('..\\\\%smono_%s.xlsx'%(brand,date),sheet_name='attrValue')
    #dic~~~~~~~#
    dicted = []
    for index, text in basic['attrValue_K'].iteritems():
        text = str(text)
        item = text.translate(dictor)
        dicted.append(item)
    mono['dic'] = pd.Series(dicted)
    #dic~~~~~~~#
    mono.to_excel('..\\\\%smono_%s.xlsx'%(brand,date), Index=None)
    
    #--------------#
    gc = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date),sheet_name='attention')
    #dic~~~~~~~#
    dicted = []
    for index, text in basic['attention_K'].iteritems():
        text = str(text)
        item = text.translate(dictor)
        dicted.append(item)
    gc['dic'] = pd.Series(dicted)
    #dic~~~~~~~#
    
    gc = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date),sheet_name='useable')
    #dic~~~~~~~#
    dicted = []
    for index, text in basic['useable_K'].iteritems():
        text = str(text)
        item = text.translate(dictor)
        dicted.append(item)
    gc['dic'] = pd.Series(dicted)
    #dic~~~~~~~#
    
    gc = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date),sheet_name='feature')
    #dic~~~~~~~#
    dicted = []
    for index, text in basic['feature_K'].iteritems():
        text = str(text)
        item = text.translate(dictor)
        dicted.append(item)
    gc['dic'] = pd.Series(dicted)
    #dic~~~~~~~#
    
    gc.to_excel('..\\\\%sgc_%s.xlsx'%(brand,date), Index=True)

import pandas as pd
dic = pd.read_excel('//fss0201/Marketing/overseas/輸出関連プロセス/商品情報抽出/Navi/◆商品情報提供/ptthon_work/dict_attrName.xlsx')
dic_j = dic['origin'].to_string(index=False)
dic_t = dic['right'].to_string(index=False)
dictor = str.maketrans(dic_j, dic_t)

def attrname_dic(brand,date):
    
    mono = pd.read_excel('..\\\\%mono_%s.xlsx'%(brand,date),sheet_name='attrName')
    #dic~~~~~~~#
    dicted = []
    for index, text in basic['feature_K'].iteritems():
        text = str(text)
        item = text.translate(dictor)
        dicted.append(item)
    gc['dic'] = pd.Series(dicted)
    #dic~~~~~~~#
    mono.to_excel('..\\\\%mono_%s.xlsx'%(brand,date), Index=None)
    