

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


# 用户
users = [
    {"id": 0, "name": "l"},
    {"id": 1, "name": "li"},
    {"id": 2, "name": "x2"},
    {"id": 3, "name": "x1"},
    {"id": 4, "name": "x"},
    {"id": 5, "name": "xu"},
    {"id": 6, "name": "xy"},

]


# 朋友关系
friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6)
]


if __name__ == "__main__":
    print("start do hw1.py")
    open_test_file()
