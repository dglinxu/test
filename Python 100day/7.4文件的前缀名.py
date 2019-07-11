def get_fn(filename):
    pos=filename.find('.')
    return filename[:pos]

def get_suffix(filename):
    pos=filename.find('.')
    
fn='待装清理汇总表.xls'
print('%s的前缀名字是：%s'%(fn,get_fn(fn)))