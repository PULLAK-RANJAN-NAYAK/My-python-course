def main():
    try:
        a = int(input("Enter a number : "))  # Take integer input
        print(a)
        return

    except Exception as e:
        print(e)  # Print error message
        return
    
    finally:    # Finally will definitely run if the try runs correct or it fails 
        print("Hey I am inside of finally")

main()