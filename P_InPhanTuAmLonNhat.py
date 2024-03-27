def find_max_negative(lst):
    return max((num for num in lst if num < 0), default=0)

def main():
    lst = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy : ").split(',')))
    print(find_max_negative(lst))

if __name__ == "__main__":
    main()

