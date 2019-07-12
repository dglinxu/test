def get_fn(filename):
    pos = filename.find('.')
    if pos > 0:
        return filename[:pos]
    elif pos==0:
        return '没有前缀'
    else:
        return filename


def get_suffix(filename):
    pos = filename.find('.')
    if pos >= 0:
        return filename[pos:]
    else:
        return '文件没有后缀'


fn = '.待装清理汇总表'
print('%s 的前缀名字是：%s' % (fn, get_fn(fn)))
print('%s 的后缀名字是：%s' % (fn, get_suffix(fn)))
