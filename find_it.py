def find_it(seq):
    for i in range(len(seq)):
        if seq.count(seq[i]) % 2 != 0:
            return seq[i]
a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(a))
