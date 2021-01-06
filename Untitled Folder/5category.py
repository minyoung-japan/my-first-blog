import pandas as pd

def category(brand,date,csv,xlsx):
    encoding = pd.read_csv(csv,encoding="cp932")
    encoding.to_excel(xlsx, Index=None)
    
    xlsx = pd.read_excel(xlsx,index=False, Usecols="B,C,D")
    xlsx.colums=["code","name","productCode"]
    
    basic = pd.read_excle('..\\\\%basic_%s.xlsx'%(brand,date),usecols="B,C,D")
    basic = basic.sort_values("productCode", ascending=True)
    
    compiled = pd.merge(basic, xlsx, how="left",on="productCode")
    compiled = compiled.drop_duplicates(['productCode'],keep='first')
    compiled.to_excel(xlsx, index=None, header=True)
    
def category_dic(xlsx,dic):
    
    dic = pd.read_excel(dic,sheet_name='VLOOK')
    dic = dic.to_dict(into=OrderedDict)
    
    category = pd.read_excel(xlsx)
    category = category.insert(4,'cate_dic')
    replaced = category['code'].replace(dic, regex=True, inplace=True)
    category['cate_dic'] = replaced['code']
    category.to_excel(category, Index=None)