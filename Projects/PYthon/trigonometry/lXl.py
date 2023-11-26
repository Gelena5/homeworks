hipotenuza = float(input("ჰიპოთენუზა გვერდის ზომა: "))
mopirdapire = float(input("მოპირდაპირე გვერდის ზომა: "))
mosazgvre = float(input("მოსაზღვრე გვერდის ზომა: "))
if hipotenuza + mopirdapire > mosazgvre and hipotenuza + mosazgvre > hipotenuza and mopirdapire + mosazgvre > mopirdapire:
    print("ასეთი სამკუთხედი იარსებებს")
    print("გაიგე სამკუტხედის sin, cos, tan.")
    print("sin(A) = ", mopirdapire / hipotenuza )
    print("cos(A) = ", mosazgvre / hipotenuza)
    print("tan(A) = ", mopirdapire / mosazgvre)
else:
    print("ასეთი სამკუთხედი ვერ იარსებებს")