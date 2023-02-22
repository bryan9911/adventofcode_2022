

def mix(files: list, order: list, size: int):
    ret = files[:]
    for i in range(size):
        cur = order[i % len(order)]
        cur_ind = ret.index(cur)
        ret.remove(cur)
        new_ind = (cur_ind+cur[1]) % (len(order)-1)
        ret.insert(new_ind, cur)
    return ret


Lines = open('Day20.txt').readlines()
digits = [int(line) for line in Lines]
Encrypted = [dig for dig in enumerate(digits)]
zero = (digits.index(0), 0)
size = len(Encrypted)

# part1
decrypted1 = mix(Encrypted, Encrypted, size)
new_zero1 = decrypted1.index(zero)
print(decrypted1[(new_zero1+1000) % size][1]+decrypted1[(new_zero1+2000) % size][1]+decrypted1[(new_zero1+3000) % size][1])

# part2
dec_key = 811589153
digits2 = [int(line)*dec_key for line in Lines]
Encrypted2 = [dig for dig in enumerate(digits2)]
decrypted2 = mix(Encrypted2, Encrypted2, size*10)
new_zero2 = decrypted2.index(zero)
print(decrypted2[(new_zero2+1000) % size][1]+decrypted2[(new_zero2+2000) % size][1]+decrypted2[(new_zero2+3000) % size][1])
