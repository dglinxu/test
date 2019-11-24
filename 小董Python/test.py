while True:
    try:
        n=int(input('请输入裁判数量：'))
        if n>2:
            break
        else:
            print('裁判数量太少了！')
            continue
    except:
        print('输入的不是自然数。')
        continue