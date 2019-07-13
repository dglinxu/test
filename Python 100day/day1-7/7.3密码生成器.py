import random

def g_code(c_len=5):
    c_soure = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m_len = len(c_soure)
    code = ''
    for i in range(c_len):
        pos = random.randint(0, m_len-1)
        code += c_soure[pos]
    return code

print('密码是：%s' % g_code(8))
