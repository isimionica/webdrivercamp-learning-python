#!/usr/bin/python3
def dict_print(dict_):
    my_list = sorted(dict_)
    for i in my_list:
        print("{}: {}".format(i, dict_[i]))
   

if __name__=="__main__":
    dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(dict_)