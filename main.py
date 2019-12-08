import random
base = {}


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def write_to_base(name):

    with open("Words\\" + name + ".txt", encoding="utf-8") as w:
        for line in w:
            text = line.rstrip("\n").rstrip().split("\t")
            base[text[0]] = text[1]


def Anki():
    while base:
        key = random.choice(list(base.keys()))
        print(key, end="  ->   ")
        if str(input()) != "":
            break
        print('\t'*3, base[key])
        print(Colors.FAIL + "smth\t" + Colors.OKBLUE + "nothing" + Colors.ENDC)

        if str(input()) == "":
            base.pop(key)


def write_test():
    while base:
        key = random.choice(list(base.keys()))
        print(base[key], end="  ->   ")

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
            base.pop(key)


if __name__ == "__main__":
    write_to_base("Book - Henry Ford")
    #Anki()
    print("|"*80)
    write_test()

