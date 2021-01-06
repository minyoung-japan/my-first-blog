import pandas as pd

def image(csv,xlsx):
    
    encoding = pd.read_csv(csv,encoding="cp932")
    encoding.to_excel(xlsx, Index=None)
    
    xlsx = pd.read_excel(xlsx,encoding="cp932",usecols='B.G')
    xlsx.colums = ['monoatroNo','img']
    xlsx = xlsx.unstack(level='monotaroNo')
    xlsx.to_excel(xlsx, index=None)
    
    