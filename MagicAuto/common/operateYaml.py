#! -*- coding:utf-8 -*-
import yaml

def getyaml(fileName):
    try:
        with open(fileName,'r',encoding='utf-8') as f:
            ret = yaml.load(f)
            print(ret)
            return ret
    except FileNotFoundError:
        print(u"找不到文件")

if __name__ == "__main__":
    getyaml(r"D:\AutoEnvironment\MagicAuto\devices\devices.yaml")