class base:
    def __init__(self):
        print('HEY')
    def sub_base(self, b):
        print("Printing from class base: ", b)

class site(base):
    def __init__(self):
        print('HEY')
        super().__init__()

    def sub_base(self, b):
        print('Printing from class site:', b)
        super().sub_base(b + 1)


class file(site):
    def __init__(self):
        print("HEY")
        super().__init__()

    def sub_base(self, b):
        print("Printing from class file: ", b)
        super().sub_base(b + 1)

if __name__ == '__main__':
    num = file()
    num.sub_base(2)




