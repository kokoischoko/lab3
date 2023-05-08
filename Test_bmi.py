import lab2.bmi as bmi
print("test bmi")

Test_bmi_normal_weight():

result = bmi.calculate_bmi(1.73, 60)
assert(result==0)

Test_bmi_over_weight():

result = bmi.calculate_bmi(1.73, 60)
assert(result==1)

Test_bmi_under_weight():

result = bmi.calculate_bmi(1.73, 60)
assert(result==-1)
