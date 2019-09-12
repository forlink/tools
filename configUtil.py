# -*- coding:utf-8 -*-
import configparser


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Settings(object):
    def __init__(self):
        self.cf = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation())
        self.cf.read("config.cfg")
        for section in self.cf.sections():
            for k, v in self.cf.items(section):
                setattr(self, k, v)


def test():
    cfg = Settings()
    # print(cfg.cf.get('db', 'db_name'))
    print(cfg)
