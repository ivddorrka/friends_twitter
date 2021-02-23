"""
lab 3.1
"""
import json
import time


def redo_ever(smth):
    """To turn dict into a list of one dict"""
    if type(smth) is list:
        return smth
    else:
        return [smth]

def read_file(file):
    """
    Reads file, returns possible variants of further move
    """
    with open(file) as json_file:
        data = json.load(json_file)
    data_true = redo_ever(data)
    all_keys = []
    for i in data_true:
        res = list(i.keys())
        all_keys.append(res)
    return all_keys, data_true
# print(read_file('friends_list_AdamMGrant.json'))
# print(read_file('user_timeline_AdamMGrant.json'))


def write_to_file(what_to_write):
    """
    To write to file in process
    """
    with open("prom_results.json", "w") as file_1:
        return json.dump(what_to_write, file_1, ensure_ascii=False, indent=4)
    # return file_1


def partly_json(file):
    try:
        ret_1 = read_file(file)
        print("Choose from which list (it's index, start counting with 0)")
        time.sleep(1)
        try:
            all_keys = ret_1[0]
            print(all_keys)
            print("Choose on of {}".format(len(ret_1[0])-1))
            ans = input("Here: ")
            if ans != 'exit':
                try:
                    ans_num = int(ans)
                except ValueError:
                    print("That must've been number")
                    return partly_json(file)
            else:
                return "Thanks"
            print(ret_1[0][ans_num])
            print("choose where to move next or exit: ")
            var = input()

            # print(ret_1[1][])
            variants = read_file(file)[0][ans_num]
            data = read_file(file)[1]
            if var not in variants and var != 'exit':
                print("There's no such file or directory")
                return partly_json(file)
            elif var == 'exit':
                return "Thanks"
            else:
                if type(data[ans_num][var]) is not dict and type(data[ans_num][var]) is not list:
                    return data[ans_num][var]
                elif type(data[ans_num][var]) is dict or type(data[ans_num][var]) is list:
                    write_to_file(data[ans_num][var])
                    return partly_json("prom_results.json")
            
        except IndexError:
            print(ret_1)
            return "There's nowhere else to move"
    except AttributeError:
        return "There's nothing here"

# print(partly_json('user_timeline_obama.json'))
# print(partly_json("frienfs_list_Obama.json"))