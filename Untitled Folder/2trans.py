import pandas as pd
from google_trans_new import google_translator
translator = google_translator() 
#--------------------------------#
def basic(brand,date,trans):
    basic = pd.read_excel('..\\\\%sbasic_%s.xlsx'%(brand,date))
    basic.insert(3,'productName_K','')
    basic.to_excel('..\\\\%sbasic_%s.xlsx'%(brand,date), index=None)
    
    trans = pd.read_excel('..\\\\%sbasic_%s.xlsx'%(brand,date), usecols='C,D')
    trans = trans.drop_duplicates(keep='first', subset='productName')
    trans = trans.sort_values('productName', ascending=True)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    translated = []
    japanese = trans['productName']
    for oneja in japanese:
        ontrans = translator.translate(oneja,dest='ko').text
        translated.append(onetrans)
    for onetranslated in translated:
        trans['productName_K'] = pd.Series(onetranslated)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    trans.to_excel(trans, index=None, header=True)
#--------------------------------#
def gc(brand,date,trans):
    gc = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date))
    gc.insert(4,'feature_K','')
    gc.insert(6,'useable_K','')
    gc.insert(8,'attention_K','')
    gc.to_excel('..\\\\%sgc_%s.xlsx'%(brand,date), index=None)
    
    trans1 = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date), usecols='C:E')
    trans1 = trans1.query('feature == feature')
    trans1 = trans1.drop_duplicates(keep='first', subset='productCode')
    trans1 = trans1.sort_values('productCode', ascending=True)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    translated = []
    japanese = trans['feature']
    for oneja in japanese:
        ontrans = translator.translate(oneja,dest='ko').text
        translated.append(onetrans)
    for onetranslated in translated:
        trans1['feature_K'] = pd.Series(onetranslated)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   

    trans2 = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date), usecols='C,F,G')
    trans2 = trans2.query('useable_K == useable_K')
    trans2 = trans2.drop_duplicates(keep='first', subset='productCode')
    trans2 = trans2.sort_values('productCode', ascending=True)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    translated = []
    japanese = trans['useable']
    for oneja in japanese:
        ontrans = translator.translate(oneja,dest='ko').text
        translated.append(onetrans)
    for onetranslated in translated:
        trans2['useable_K'] = pd.Series(onetranslated)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
    
    trans3 = pd.read_excel('..\\\\%sgc_%s.xlsx'%(brand,date), usecols='C,H,I')
    trans3 = trans3.query('attention_K == attention_K')
    trans3 = trans3.drop_duplicates(keep='first', subset='productCode')
    trans3 = trans3.sort_values('productCode', ascending=True)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    translated = []
    japanese = trans['attention']
    for oneja in japanese:
        ontrans = translator.translate(oneja,dest='ko').text
        translated.append(onetrans)
    for onetranslated in translated:
        trans3['attention_K'] = pd.Series(onetranslated)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
    
    with pd.ExcelWriter(trans) as writer:
        trans1.to_excel(writer, sheet_name='feature', index=None, header=True)
        trans2.to_excel(writer, sheet_name='useable', index=None, header=True)
        trans3.to_excel(writer, sheet_name='attention', index=None, header=True)
#--------------------------------#   
def mono(brand,date,trans):

    mono = pd.read_excel('..\\\\%smono_%s.xlsx'%(brand,date))
    mono.insert(3,'attrName_K','')
    mono.insert(5,'attrValue_K','')
    
    mono = mono.query('attrValue.str.contains(pat=r"[ぁ-んァ-ヶ亜-熙]")')
#    attrvalue_define = pd.concat([mono,attrvalue_define],axis=1,join='outer',keys=['define'])  
#    attrvalue_define = attrvalue_define.query('define == "False"') 
    mono = mono.update(attrvalue_define,join='left')
        
    mono.to_excel('..\\\\%smono_%s.xlsx'%(brand,date), index=None)
    
    trans1 = pd.read_excel('..\\\\%smono_%s.xlsx'%(brand,date), usecols='A,C,D')
    trans1 = trans1.drop_duplicates(keep='first', subset='attrName')
    trans1 = trans1.sort_values('attrName', ascending=True)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    translated = []
    japanese = trans['attrName']
    for oneja in japanese:
        ontrans = translator.translate(oneja,dest='ko').text
        translated.append(onetrans)
    for onetranslated in translated:
        trans1['attrName_K'] = pd.Series(onetranslated)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
    
    trans2 = pd.read_excel('..\\\\%smono_%s.xlsx'%(brand,date), usecols='A,E,F')
    trans2 = trans2.query('attrValue == attrValue')
    trans2 = trans2.drop_duplicates(keep='first', subset='attrValue')
    trans2 = trans2.sort_values('attrValue', ascending=True)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    translated = []
    japanese = trans['attrValue']
    for oneja in japanese:
        ontrans = translator.translate(oneja,dest='ko').text
        translated.append(onetrans)
    for onetranslated in translated:
        trans2['attrValue_K'] = pd.Series(onetranslated)
    #Google Trans~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
    
    with pd.ExcelWriter(trans) as writer:
        trans1.to_excel(writer, sheet_name='attrName', index=None, header=True)
        trans2.to_excel(writer, sheet_name='attrValue', index=None, header=True)
                              