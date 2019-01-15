string1 = "79-900"
string2 = "80-155"

def generate(arg1,arg2):
    generate_list = []
    start = arg1[0:2]
    start += arg1[3:6]
    start = int(start)
    start += 1
    end = arg2[0:2]
    end += arg2[3:6]
    end = int(end)

    for i in range(start, end, 1):
        i = str(i)
        new = i[0:2] + "-" + i[2:5]
        generate_list.append(new)
    print(generate_list)
generate(string1,string2)
