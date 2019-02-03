import sys
# while line no empty:

    # while not at end of line
    # check first non whitespace character
    #     store counter value
    #     ###2 possible option --> alpha, digit

    # elif isalpha and !endofLine
        #keep reading until first digit or end of line
                # push string to stack

    # elif isDigit  and ! endofLine--> need to check price or not
        #keep reading until first alpha or period or end of line
                    #if period, read the next four, space, digit, digit, nondigit
                        # if all of the above true push to parallel stack
                        # set counter

                    #elif alpha , read till next number or end of line
                        # push this to stack

                    #elif end of line
                        # discard

    # read new line (outside end of line while)



def output_read(items, prices):
    f = open('out.txt')
    line = f.readline()
    while line:
        i = 0
        length = len(line)
        while line[i] != '\n':
            if line[i] == ' ':
                i += 1
            elif line[i] != '\n':
                checkpoint = i
                if line[i].isalpha():
                    while not ((line[i].isdigit()) or (line[i] == '\n')):
                        i += 1
                        if line[i] == '\n':
                            break
                    items.append(line[checkpoint:i])
                elif line[i].isdigit():
                    while (((not line[i].isalpha()) and (not line[i] == '.') and (not line[i] == '\n'))):
                        i += 1
                        if line[i] == '\n':
                            break
                    if line[i] == '.':
                        if i + 4 <= length - 1:
                            if ((line[i+1] == ' ') and (line[i+2].isdigit()) and (line[i+3].isdigit()) and (not line[i+4].isdigit())):
                                i += 4
                                word = line[checkpoint:i]
                                word = word.replace(' ','')
                                prices.append(float(word))
                        else:
                            i = length - 1
                    elif line[i].isalpha():
                        while not ((line[i].isdigit()) or (line[i] == '\n')):
                            i += 1
                            if line[i] == '\n':
                                break
                        items.append(line[checkpoint:i])
                    elif line[i] == '\n':
                        pass
        line = f.readline()


items = []
prices = []
output_read(items, prices)
d = dict(zip(items,prices))
print(d)
