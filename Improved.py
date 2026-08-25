while True:
    KM = float(input("Please enter distance in kilometers: " ))
    #this is the user input
    Miles = 0.621371
    Converted_Distance = KM*Miles
     #We multiplied the given KM by how much 1km=mile
    print("The distance in miles is: ", Converted_Distance)
    
    compute_again = input("Do you want to convert again? (yes/no): ").lower()   
    if compute_again != 'yes':
        print("Goodbye!")
        break
