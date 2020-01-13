import pandas as pd
def data_validation(data):
    try:
        assert 100<data.价格<120
    except:
        print(f'#{data.ID}的商品{data.商品}是不合理的价格{data.价格}')
data=pd.read_excel('output2.xlsx')
data.apply(data_validation,axis=1)
