import random


class Colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Constructor():

    def __init__(self, name):
        self.base = {}
        self.write_to_base(name)

    def write_to_base(self, name):

        with open("Words\\" + name + ".txt", encoding="utf-8") as w:
            for line in w:
                text = line.rstrip("\n").rstrip().split("\t")
                self.base[text[0]] = text[1]

    def Anki(self):

        while self.base:
            key = random.choice(list(self.base.keys()))
            print(key, end="  ->   ")
            if str(input()) != "":
                break
            print('\t'*3, self.base[key])
            print(Colors.FAIL + "smth\t" + Colors.OKBLUE + "nothing" + Colors.ENDC)

            if str(input()) == "":
                self.base.pop(key)

    def write_test(self):
        while self.base:
            key = random.choice(list(self.base.keys()))
            print(self.base[key], end="  ->   ")

            answer = str(input()).lower()

            flag = True

            for i in range(len(key)-abs(len(key)-len(answer))):

                if key.lower()[i] != answer[i]:
                    flag = False
                    print(Colors.FAIL + answer[i] + Colors.ENDC, end="")
                else:
                    print(Colors.OKBLUE + answer[i] + Colors.ENDC, end="")
            print(" -> " + Colors.OKBLUE + key.lower() + Colors.ENDC)
            if flag:
                self.base.pop(key)


if __name__ == "__main__":
    new = Constructor("Book - Henry Ford")
    # new.Anki()
    new.write_test()
    print("|"*80)



