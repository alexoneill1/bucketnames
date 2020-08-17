import sys

def main():
    errorlines = []
    errorlinecount = 0
    try:
        for line in sys.stdin:
            a = []
            line = line.strip().split()
            num = line[0]
            base = line[1]
            errorlinecount += 1
            try:
                while int(num) != 0:
                    a.append(int(num) % int(base))
                    num = (int(num) // int(base))
                total = 0
                for item in a:
                    total = total + (int(item) ** 2)
                print(total)

            except:
                errorlines.append(int(errorlinecount))

    finally:
        if sum(errorlines) > 0:
            a = ('Failed to convert line(s):' + ' ' + str(errorlines)[1:-1] + ' ')
            print(a)

if __name__ == '__main__':
    main()
