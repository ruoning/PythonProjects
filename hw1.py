

PATH = "data/hw1.txt"


def open_test_file(path=PATH):
    """打开测试文件"""
    lines = 0
    age = 0
    birth = 0
    greatest_age = ""
    greatest_birth = ""
    with open(path) as file_doc:
        for data in file_doc.readlines():
            if data == "\n":
                continue
            lines += 1
            print(data)
            words = data.split(',')
            if words[1] > age:
                age = words[1]
                greatest_age = words[0]
            dates = words[2].split('-')
            if dates[2] > birth:
                birth = dates[2]
            greatest_birth = words[0]


if __name__ == "__main__":
    print("start do hw1.py")
    open_test_file()
