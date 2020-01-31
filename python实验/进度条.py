# -*- coding: utf-8 -*-
import time
def jindu(delay=0.1): 
    s='='
    for i in range(100): 
        # print('%s'%s,end='',flush=True)
        for ch in ['-','\\','|','/']:
            print('\b%s'%ch,end='',flush=True)
            time.sleep(delay)
jindu()