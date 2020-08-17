import sys

def main():
    wait = 0
    s = int(sys.stdin.readline().strip())
    a = []
    a = [line.strip().split() for line in sys.stdin]
    for line in a:
        d = int(line[0])
        r = int(line[1])
        g = int(line[2])
        mod = (d + wait) % (g + r)
        if mod < r:
            wait = wait + (r - mod)
    print(s + wait)

if __name__ == "__main__":
    main()
