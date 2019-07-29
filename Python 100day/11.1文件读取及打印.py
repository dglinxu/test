import time
def main():
    f=open('d:\\temp\\唐诗两首.txt','r')
    print(f.read())
    f.close()

    f1=open('d:\\temp\\唐诗两首.txt','+')
    f2=open('d:\\temp\\唐诗另两首.txt','r')
    f=f1.read()+f2.read()
    print(f)
    # for line1,line2 in f1,f2:
    #     line=line1+'   '+line2
    #     for l in line:
    #         print(l,end='')
    #         time.sleep(0.2)
    f1.close
    f2.close

if __name__=='__main__':
    main()