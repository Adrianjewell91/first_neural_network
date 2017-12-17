#open file
f = open("major-chords-set-train.csv","w")

#the variables for major chords
x,y,z = 0, 4, 7

#the chord name, the first chord in a keyboard is A major, so n = 9
#0..11, C...B
answer = 9

#the array of all notes, whether they are played or not.
#at this point, we're just playing three notes at once.
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# print(array)
#go from 0..81, because we need to stop when the top note hits the last element.
for el in range(0,81):
    current_array = list(array)
    answer = (9+el)%12
    current_array[x+el] = 1
    current_array[y+el] = 1
    current_array[z+el] = 1
    f.write('%s, %d \n' % (current_array, answer))

#close the file.
f.close()

import random
lines = open('major-chords-set-train.csv').readlines()
random.shuffle(lines)
open('major-chords-set-train.csv','w').writelines(lines)

#now, go in and remove the brackets.
import random
validate_lines = open('major-chords-set-train.csv').readlines()
random.shuffle(validate_lines)
open('major-chords-set-validate.csv','w').writelines(validate_lines)
