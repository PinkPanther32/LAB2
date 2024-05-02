def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    #Add code here to caculate the bmi
    bmi = float(weight / (height*height))
    
    #add code here to print the bmi
    print ("Hence your bmi is " + str(bmi))
    
    #conditional operaters to test if determine the weight classification of bmi
    if bmi > 25.0:
        print ("1")
    elif bmi <= 25.0 and bmi >= 18.5:
        print("0") 
    else:
        print("-1")
            
        
calculate_bmi(weight = 57, height = 1.73)