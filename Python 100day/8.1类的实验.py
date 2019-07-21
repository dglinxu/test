class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

    def p_name(self, name):
        print('%s,你好！' % name)


def main():
    test = Test('hello')
    # t=Test()
    # t('阿土仔')
    # t.__bar()
    test._Test__bar()
    print(test._Test__foo)
    test.p_name('阿土仔')


if __name__ == "__main__":
    main()
