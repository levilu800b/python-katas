# Write a simple parser that will parse and run Deadfish.
#
# Deadfish has 4 commands, each 1 character long:
#
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.
#
# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    result = []
    value = 0
    for i in data:
        if i == 'i':
            value += 1
        elif i == 'd':
            value -= 1
        elif i == 's':
            value **= 2
        elif i == 'o':
            result.append(value)
    return result

if __name__ == '__main__':
    print(parse('iiisdoso'))