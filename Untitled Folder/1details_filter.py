import xlrd
import pandas as pd

def details_filter (brand, date):
    
    #--------------#
    basic = pd.read_excel('..\\\\%sbasic_%s.xlsx'%(brand,date))
    basic = basic.replace({'productName': r'[(グリーン購入適合商品)]'},{'productName':''},regex=True)
    basic = basic.sort_values('monotaroNo', ascending=True)
    basic.to_excel('..\\\\%sbasic_%s.xlsx'%(brand,date), index=None)
    
    #--------------#
    mono = pd.read_excel('..\\\\%smono_%s.xlsx'%(brand,date))
    mono = mono.query('attrName not in ("グリーン購入法", "エコマーク認定番号")')
    mono = mono.sort_values('monotaroNo', ascending=True)
    mono.to_excel('..\\\\%smono_%s.xlsx'%(brand,date), index=None)
    
    #--------------#
    gc = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date))
    gc = gc.replace(r'[\※]|[\◆]|[\■]|[\●]|[\▲]','',regex=True)

    attention = gc['attention'].dropna(how='any')
    attention = attention.drop_duplicates()
    attention = attention.values.tolist()
    found_list = []
    gc_del=['エコマーク','メーカー直送商品','MonotaRo','配送','別途送料']
    for tosplit in attention:
            sentences = tosplit.split('。')
            for onesen in sentences:
                for onedel in gc_del:
                    if onedel in onesen:
                        found_list.append(onesen)
     
    for onefound in found_list:
        gc['attention'] = gc['attention'].str.replace(pat='%s。'%onefound,repl='',regex=False) 
        gc['attention'] = gc['attention'].str.replace(pat='%s'%onefound,repl='',regex=False) 
    
    gc = gc.sort_values('pC', ascending=True)
    gc.to_excel('..\\\\%sgc_%s.xlsx'%(brand,date), index=True)
