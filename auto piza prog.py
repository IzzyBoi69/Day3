print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
s_pizza = 15
m_pizza = 20
l_pizza = 25

if(size == "S"):
    if(add_pepperoni == "Y"):
        s_pizza += 2
    else:
        s_pizza +=0
    if(extra_cheese == "Y"):
        s_pizza += 1
        print(f"Your final bill is ${s_pizza}")
    else:
        s_pizza +=0
        print(f"Your final bill is ${s_pizza}")

if(size == "M"):
    if(add_pepperoni == "Y"):
        m_pizza += 3
    else:
        m_pizza += 0
    if(extra_cheese == "Y"):
        m_pizza += 1
        print(f"Your final bill is ${m_pizza}")
    else:
        m_pizza += 0
        print(f"Your final bill is ${m_pizza}")
if(size == "L"):
    if(add_pepperoni == "Y"):
        l_pizza += 3
    else:
        l_pizza +=0
    if(extra_cheese == "Y"):
        l_pizza += 1
        print(f"Your final bill is ${l_pizza}")
    else:
        l_pizza +=0
        print(f"Your final bill is ${l_pizza}")













