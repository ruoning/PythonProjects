

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


user_dict = {}
for user in users:
    user_dict[user["id"]] = user
    user_dict[user["id"]]["friends"] = []

print(user_dict)
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

for i, j in friendships:
    user_dict[i]["friends"].append(j)
    user_dict[j]["friends"].append(i)

print(user_dict)

#找到拥有最多朋友个数与id的对应关系
count_to_id = {}
for key in user_dict.keys():

    length = len(user_dict[key]["friends"])
    lst = count_to_id.get(length, [])
    lst.append(key)
    count_to_id[length] = lst
print(count_to_id)

#排序
sorted_list = sorted(count_to_id)
max_count = sorted_list[-1]
friends_list = count_to_id.get(max_count)
print(friends_list)

#通过ID找到用户姓名
print("The user which has the most friends:")
for id in friends_list:
    print(user_dict[id]["name"])

#按朋友个数排序输出
print("Users sorted by friends count: (max to min)")
for i in sorted_list:
    lst = sorted_list[i]
    for j in lst:
        print(user_dict[j]["names"])

if __name__ == "__main__":
    print("start do hw1.py")
    open_test_file()
