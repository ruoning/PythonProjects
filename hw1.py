

PATH = "data/test.txt"


def open_test_file(path=PATH):
    """打开测试文件"""
    lines = 0
    age = 0
    birth = 0
    # 年纪列表
    age_list = []

    greatest_age = ""
    greatest_birth = ""
    with open(path) as file_doc:
        for data in file_doc.readlines():
            lines += 1
            words = data.split(',')
            print(words)
            age = int(words[1])
            age_list.append(age)

    print("max age is %s" % max(age_list))


if __name__ == "__main__":
    print("start do hw1.py")
    open_test_file()
