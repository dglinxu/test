# -*- coding: utf-8 -*-
import time
def jindu(delay=0.25): 
    s='=='
    for i in range(50): 
        if i%5==4: 
            s=str((i//5)+1)+'0% '
        else: 
            s='= '
        print('\b%s'%s,end='',flush=True)
        for ch in ['-','\\','|','/']:
            print('\b%s'%ch,end='',flush=True)
            time.sleep(delay)
    
jindu()