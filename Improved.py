while True:
    X = float(input("Please enter distance in kilometers: " ))
    Y = 0.621371
    Z = X*Y
    print("The distance in miles is: ", Z)
    
    compute_again = input("Do you want to convert again? (yes/no): ").lower()   
    if compute_again != 'yes':
        print("Goodbye!")
        break