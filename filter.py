def check(x):
    for i in x:
        if i.isdigit():
            return True
        else:
            return False
    return False

seq = "hii this is a the 1wed number 12345 and 67890"
seq = seq.split()
seq = filter(lambda x:check(x) , seq)
print(list(seq))
