f = open("major-chords-compre-set-train.csv","w")

#major chords - root position
x,y,z = 0, 4, 7
answer = 9

array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for el in range(0,81):
    current_array = list(array)
    answer = (9+el)%12
    current_array[x+el] = 1
    current_array[y+el] = 1
    current_array[z+el] = 1
    current_array_str = str(current_array)[1:-1]
    f.write('%s, %d \n' % (current_array_str, answer))


#major chord first inversion
x,y,z = 0, 3, 8
answer = 5

for el in range(0,80):
    current_array = list(array)
    answer = (5+el)%12
    current_array[x+el] = 1
    current_array[y+el] = 1
    current_array[z+el] = 1
    current_array_str = str(current_array)[1:-1]
    f.write('%s, %d \n' % (current_array_str, answer))

#major chord second inversion
x,y,z = 0, 5, 9
answer = 2

for el in range(0,79):
    current_array = list(array)
    answer = (2+el)%12
    current_array[x+el] = 1
    current_array[y+el] = 1
    current_array[z+el] = 1
    current_array_str = str(current_array)[1:-1]
    f.write('%s, %d \n' % (current_array_str, answer))

f.close()

import random
lines = open('major-chords-compre-set-train.csv').readlines()
random.shuffle(lines)
open('major-chords-compre-set-train.csv','w').writelines(lines)

validate_lines = open('major-chords-compre-set-train.csv').readlines()
random.shuffle(validate_lines)
open('major-chords-compre-set-validate.csv','w').writelines(validate_lines)
