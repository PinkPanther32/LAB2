def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    #Add code here to caculate the bmi
    bmi = float(weight / (height*height))
    
    #add code here to print the bmi
    print ("Hence your bmi is " + str(bmi))
    
    #conditional operaters to test if determine the weight classification of bmi
    if bmi > 25.0:
        print ("Your weight classification would be Over Weight")
    elif bmi <= 25.0 and bmi >= 18.5:
        print("Your weight classification would be Normal Weight") 
    else:
        print("YOur weight classification would be Under Weight")
            
        
calculate_bmi(weight = 57, height = 1.73)