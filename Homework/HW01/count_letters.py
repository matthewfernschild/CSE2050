def count_letters(data):
    """Data is put into lowercase, then if i in data is an alpha(bet)
    character, it is put into the dictionary. other chars are ignored"""

    data = data.lower

    letter_dict = {}

    for i in data:
        if i.isalpha(): # is in string.ascii_lowercase  
            if i not in letter_dict:
                letter_dict[i] = 1
            elif i in letter_dict:
                letter_dict[i] += 1

    return letter_dict
#print(count_letters("#$Fire and IceSome say the world will end in fire,Some say in ice.From what I've tasted of desireI hold with those who favor fire.But if it had to perish twice,I think I know enough of hateTo say that for destruction iceIs also greatAnd would suffice.-Robert Frost"))
a = (1,2,3,4,4,4,2,3,4)
print(a)
print(set(a))
print({a})