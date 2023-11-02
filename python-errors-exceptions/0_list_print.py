#!/usr/bin/python3
def list_print(lst=[], i=0):
    new_count = 0
    for d in range(i):
        try:
            print("{}".format(lst[d]), end="")
            new_count += 1
        except:
            break
    print("")
    return (new_count)
  

if __name__=="__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_print(list_, 4)
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
