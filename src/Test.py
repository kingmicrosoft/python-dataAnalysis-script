def gettale(uid, seed):
    return "user_%d" % (uid >> seed)

if __name__ == '__main__':
   print gettale(123344, 3)
