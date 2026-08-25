while True:
    KM = float(input("Please enter distance in kilometers: " ))
    Miles = 0.621371
    Converted_Distance = KM*Miles
    print("The distance in miles is: ", Converted_Distance, "Miles")
    
    compute_again = input("Do you want to convert again? (yes/no): ") 
    if compute_again == 'yes' :
        print("Okay!")
    else:
        print("Goodbye!")
        break
