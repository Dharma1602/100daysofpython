# 1st input: enter height in meters e.g: 1.65
height = input("Please enter your height meters\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Please enter your weight\n")
weight_as_int = int(weight)
height_as_float = float(height)
BMI = weight_as_int / height_as_float ** 2
BMI_as_int = int(BMI)
print(BMI_as_int)