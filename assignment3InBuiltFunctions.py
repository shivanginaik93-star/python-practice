from sys import getsizeof # imported getSizeOf method from in built module sys

def main():
    var = input("Enter value : ")

    print("Entered Value's information as follows : ")
    print("Data Type : ",type(var))
    print("Memory Address : ",id(var))
    print("Size in Bytes : ",getsizeof(var))

if __name__ == "__main__":
    main()
