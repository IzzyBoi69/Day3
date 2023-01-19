# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
body_mass_calc= weight/(height**2)
final_body_mass_calc: int= round(body_mass_calc)
if (final_body_mass_calc < 18.5):
    print(f"Your BMI is {final_body_mass_calc}, you are underweight.")
elif((final_body_mass_calc>18.5) and (final_body_mass_calc<25)):
        print(f"Your BMI is {final_body_mass_calc}, you have a normal weight.")
elif((final_body_mass_calc>25) and (final_body_mass_calc<30)):
        print(f"Your BMI is {final_body_mass_calc}, you are slightly overweight")
elif((final_body_mass_calc>30) and (final_body_mass_calc<35)):
        print(f"Your BMI is {final_body_mass_calc}, you are obese")
else:
    print(f"Your BMI is {final_body_mass_calc}, you are clinically obsese.")


