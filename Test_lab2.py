import Lab2
num1,num2,num3,num4 = 23,54,34,23
 
def test_calc_average():
    
    expected_result = 33.5
    
    result = Lab2.calc_average(num1 = 23, num2 = 54, num3 = 34, num4 = 23)
    
    assert result == expected_result
    
def test_find_min_max():
    
    min_num,max_num = Lab2.find_min_max(num1,num2,num3,num4)
    
    assert min_num == min(num1,num2,num3,num4)
    assert max_num == max(num1,num2,num3,num4)
    
def test_calculate_medain_temperature():
    
    medain_temp = Lab2.calc_median_temperature([num1,num2,num3,num4])
    
    expected_result = 28.5
    
    assert expected_result == medain_temp
    
  
    
    
     