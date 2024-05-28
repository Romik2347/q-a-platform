def parse_fullname(fullname):
    names = dict()
    splited = fullname.split()
    names[second_name] = splited[1]
    names[first_name] = splited[0]
    return names