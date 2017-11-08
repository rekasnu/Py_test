import math

def convert_number_to_base_x(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def build_the_number(temp_data):
    digit_values={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',
             20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',
             30:'u',31:'v',32:'w',33:'x',34:'y',35:'z'}
    number = ''
    for digit in temp_data:
        if digit > 9:
            number += digit_values[digit]
        else:
            number += str(digit)
    return number

def check_if_number_is_polindrom(test_num):
    if test_num == test_num[::-1]:
        return True
    else:
        return False

def check_numbers():
    final_list=[]
    for num in range (1,1001):
        for base in range (2,36):
            data =[]
            result = None
            t_num = convert_number_to_base_x(num, base)
            f_num = build_the_number(t_num)
            result = check_if_number_is_polindrom(f_num)
            if result == True:
                final_list.append([num,base])
                break
    return final_list


print 'Please wait'
mfile = open('test.txt', 'w')
fl = check_numbers()
for d in fl:
#    print d
    mfile.write("%s\n" %d)
print 'Finished'
mfile.close()