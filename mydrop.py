import os

DIR = ".\\drop"

file_info = {}

def main():
    refresh = True
    while(refresh):
        files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(DIR)) for f in fn]

        for f in files:
            new_time = os.path.getmtime(f)
            if f in file_info:
                if file_info[f] != new_time:
                    print("File " + f + " modified")
            else:
                print(f + " is a new file")
            file_info[f] = os.path.getmtime(f)

        print(file_info)
        i = input("refresh (Y/n): ")
        refresh = i != 'n'

def fat(n):
    prod = 1
    for i in range(2,n):
        prod *= i
    return prod

if __name__ == "__main__":
    # execute only if run as a script
    print(fat(4))
    #main()
