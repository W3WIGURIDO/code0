import os

if __name__ == "__main__":
    dir = './data/train'
    files = os.listdir(dir)
    f = open('list0.txt', 'w')
    f1 = open('list0_1.txt', 'w')
    f2 = open('cifar_map.txt', 'w')
    f3 = open('cifar_map_1.txt', 'w')
    num = 0
    num1 = 0
    for file in files:
        dir2 = file
        f3.write(file + ",")
        files2 = os.listdir(dir + '/' + file)
        for file in files2:
            dir3 = file
            f2.write(file + ",")
            files3 = os.listdir(dir + "/" + dir2 + "/" + file)
            for file in files3:
                f.write(dir + '/' + dir2 + '/' + dir3 + "/" + file + ' ' + str(num) + '\n')
                f1.write(dir + '/' + dir2 + '/' + dir3 + "/" + file + ' ' + str(num1) + '\n')
                print "wrote"
            num += 1
        num1 += 1
            
    f.close()
            