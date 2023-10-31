#!/usr/bin/python3
def calc_weight(list_=[]):
    avg = 0
    size = 0
    for x in list_:
        avg += (x[0] * x[1])
        size += x[1]
    return (avg / size)

  

if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
