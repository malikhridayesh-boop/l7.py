medical_cause = input("do you have a medical cause for your absence? (yes/no) ")
if medical_cause == "yes":
    print("You are allowed to give the exam.")
else:
    atten = int(input("enter the attendance of the student in percentage: "))
    if atten >= 75:
        print("You are allowed to give the exam.")
    else:
        print("You are not allowed to give the exam.")