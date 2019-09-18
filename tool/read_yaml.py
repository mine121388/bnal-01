# 导包
import yaml


def read_yaml(filename):
    """参数化读取yaml文件并使用数据"""
    with open("./data/" + filename, "r", encoding="utf-8")as f:
        arr = []
        for i in yaml.load(f).values():
            arr.append(tuple(i.values()))
        return arr


def read_yaml1(filename):
    """参数化读取yaml文件并使用数据"""
    with open("./data/" + filename, "r", encoding="utf-8")as f:
        return yaml.load(f)


if __name__ == '__main__':
    # print(read_yaml("address.yaml"))
    print(tuple(read_yaml1("address.yaml").get("address_add")))
