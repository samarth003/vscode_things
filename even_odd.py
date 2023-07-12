def even_nums(arr):
    #placeholder var
    even_num_arr = []
    for i in arr:
        if i%2 == 0:
            even_num_arr.append(i)
        else:
            pass
    return even_num_arr

def main():
    val = input("Enter an array to your liking\n")
    #convert string to list
    in_list = list(val.split(","))
    #convert list of strings to ints 
    arg_list = [eval(i) for i in in_list]
    #pass argument to func
    retArr = even_nums(arg_list)
    print(retArr)

if __name__ == "__main__":
    main()