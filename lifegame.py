import time
import sys
args = sys.argv

def ume(sta):
    vsta = "00000000"
    for i, char in enumerate(sta):
        vsta += char
        if i % 5 == 4:
            vsta += "00"
    vsta += "000000"
    return vsta

def show(sta):
    for i, char in enumerate(sta):
        if char == '0':
            print('□ ', end='')
        else:
            print('■ ', end='')
        if i % 5 == 4:
            print()

def daytime(vsta):
    sur = ""
    for turn in list(range(9, 14)) + list(range(16, 21)) + list(range(23, 28)) + list(range(30, 35)) + list(range(37, 42)):
        count = 0
        for p in [-8, -7, -6, -1, 1, 6, 7, 8]:
            if vsta[turn-1+p] == '1':
                count += 1
        sur += str(count)
    return sur

def night(sta, sur):
    nsta = ""
    for i, char in enumerate(sur):
        if char == '2':
            nsta += sta[i]
        elif char == '3':
            nsta += '1'
        else:
            nsta += '0'
    return nsta

def main():
    sta = args[1]
    vsta = ume(sta)
    gen = 1
    while True:
        print(f"gen {gen}")
        gen += 1

        show(sta)
        vsta = ume(sta)
        sur = daytime(vsta)
        sta = night(sta, sur)

        time.sleep(1.5)
        print("="*15)

if __name__ == "__main__":
    main()
