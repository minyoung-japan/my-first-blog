import pandas as pd

def SKU_filter (brand,date):
    #-----------------------#
    basic_csv = pd.read_csv('..\\\\%sbasic_%s.csv'%(brand,date), encoding='UTF-8')
    basic_csv = basic_csv.query('shipType in ("在庫")') #in, notin, ==, != 사용
    basic_csv = basic_csv.query('C_1 not in ("21862")') 
    basic_csv = basic_csv.query('C_2 not in ("87331", "423", "59607", "422", "68299", "420", "87251")') 
    basic_csv = basic_csv.query('C_3 not in ("43422", "122179", "68174", "122181", "23736")') 
    
    monotaroNo_list = basic_csv['monotaroNo']
    basic_csv.to_excel('..\\\\%sbasic_%s.xlsx'%(brand,date), index=None)
    
    
    mono_csv = pd.read_csv('..\\\\%smono_%s.csv'%(brand,date), encoding='UTF-8')
    mono_csv = mono_csv.query('monotaroNo in @monotaroNo_list')
    mono_csv.to_excel('..\\\\%smono_%s.xlsx'%(brand,date), index=None)
    
    gc_csv = pd.read_csv('..\\\\%sgc_%s.csv'%(brand,date), encoding='UTF-8')
    gc_csv = gc_csv.query('mN in @monotaroNo_list')
    gc_csv.to_excel('..\\\\%sgc_%s.xlsx'%(brand,date), index=None)
    
    #-----------------------#
    mono_xls = pd.read_excel('..\\\\%smono_%s.xlsx'%(brand,date))
    
    attr_del = ['AC100','電池','1年延長ライセンス','豚毛','馬毛','鶏尾毛','ポリイミド','ワケあり']
    name_del = mono_xls.query('attrName.str.contains("|".join(@attr_del))', engine='python') 
    name_del = name_del['monotaroNo']
    value_del = mono_xls.query('attrValue.str.contains("|".join(@attr_del))', engine='python') 
    value_del = value_del['monotaroNo']
    
    mono_xls = mono_xls.query('monotaroNo not in @name_del') 
    mono_xls = mono_xls.query('monotaroNo not in @value_del') 
    
    monotaroNo_list = mono_xls['monotaroNo']
    mono_xls.to_excel('..\\\\%smono_%s.xlsx'%(brand,date), index=None)  
    
    basic_xls = pd.read_excel('..\\\\%sbasic_%s.xlsx'%(brand,date))
    basic_xls = basic_xls.query('monotaroNo not in @monotaroNo_list')
    basic_xls.to_excel('..\\\\%sbasic_%s.xlsx'%(brand,date), index=None)
    
    gc_xls = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date))
    gc_xls = gc_xls.query('mN not in @monotaroNo_list')
    gc_xls = gc_xls.sort_values('pC', ascending=True)
    gc_xls.to_excel('..\\\\%sgc_%s.xlsx'%(brand,date), index=None)

    
    