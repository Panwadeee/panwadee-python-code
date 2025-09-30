import random

def test_random():
    #สุ่มเลขระหว่าง1-10 เก็บไว้ในชื่อตัวแปร random_number
    random_number = random.randint(1, 10)
    #รับค่าการทายเลขจากผู้ใช้ เก็บค่าไว้ในตัวแปร number
    number=(input("What is number do you think: ?"))
    number=int(number)
    if random_number == number:
        print("Congratulations")
    
    if random_number < number:
        print("Too much")

    if random_number > number:
        print("Too low")

    print(random_number)
    
test_random()