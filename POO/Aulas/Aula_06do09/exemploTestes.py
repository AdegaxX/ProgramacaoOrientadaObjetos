from exemplos import Student

class TesteStudent:
    if __name__ == '__main__':
        std = Student('Swati', 20)
        print(std._name)
        std.name = 'Dipa'
        print(std.name)
    def __display(self):
        print('This is private method.')