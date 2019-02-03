class Base(object):

    def __init__(self, m):
        self.msg = m

    def validate(self):
        return len(self.msg) > 3


class Hoge(Base):

    def __init__(self, m):
        super(Hoge, self).__init__(m)

    def show(self):
        print('hoge msg is "{}"'.format(self.msg))


class Piyo(Base):

    def __init__(self, m):
        super(Piyo, self).__init__(m)

    def show(self):
        print('piyo msg is "{}"'.format(self.msg))


def check(target):
    if target.validate():
        target.show()
        return
    print 'NG'


if __name__ == '__main__':
    targets = [Hoge('hello'), Piyo('world'), Piyo('!!')]

    for target in targets:
        check(target)
