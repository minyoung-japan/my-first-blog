import pandas as pd

def trans_combine(brand,date,b_trans, g_trans, m_trans):
    basic = pd.read_excel('..\\\\%basic_%s.xlsx'%(brand,date))
    b_trans = pd.read_excel(b_trans)
    basic = basic.update(b_trans)
    basic.to_excel('..\\\\%basic_%s.xlsx'%(brand,date))

    gc = pd.read_excel('..\\\\%gc_%s.xlsx'%(brand,date))
    g_trans = pd.read_excel(g_trans)
    gc = gc.update(g_trans)
    gc.to_excel('..\\\\%gc_%s.xlsx'%(brand,date))
    
    mono = pd.read_excel('..\\\\%mono_%s.xlsx'%(brand,date))
    m_trans = pd.read_excel(m_trans)
    mono = mono.update(m_trans)
    mono.to_excel('..\\\\%mono_%s.xlsx'%(brand,date))

def gc_add(brand,date):
    
    gc = pd.read_excel('..\\\\%gc_%s.xlsx'%(brand,date))
    gc['combined'] = "특징|| " + gc[['attention_K', 'useable_K','feature_K']].agg('|'.join, axis=1)
    gc.to_excel('..\\\\%gc_%s.xlsx'%(brand,date))

def mono_add(brand,date):

    mono = pd.read_excel('..\\\\%mono_%s.xlsx'%(brand,date))
    p_mono = mono.unstack(level='monotaroNo')    
    for index_row in p_mono.index():
        maxcol = p_mono.count(axis='columns')
        for col_cnt in maxcol.index():
            p_mono.iloc[index,col_cnt+1] = "원산지"
            p_mono.iloc[index,col_cnt+2] = "다국적"
    p_mono.to_excel('mono_processed.xlsx')

    