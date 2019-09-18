import logging

fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.INFO, filename="./log/file2.log", format=fm)

def get_log():
    return logging

if __name__ == '__main__':
    get_log().info("测试1")