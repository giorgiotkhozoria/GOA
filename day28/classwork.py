
x =int(input("Choose a number")) #x ის მაგივრად შეიყვანეთ ნებისმიერი რიცხვი


y = input("what math operation do you want to choose : - or + or / or ^")#y ის მაგივრად აირჩიეთ და შეიყვანეთ ამ მათემატიკური ელემენტებებიდან ერთერთი


z =int(input("Choose a number"))#z ის მაგივრად აირჩიეთ ნებისმიერი რიცხვი


if y == "-": print(x-z) #თუ yის გრაფაში ავირჩიეთ - მაშინ შესრულდება x და z ის გამოკლება.


elif y == "+": print(x+z) #თუ yის გრაფაში ავირჩიეთ + მაშინ შესრულდება x და z ის მიმატება.


elif y == "/": print(x/z) #თუ yის გრაფაში ავირჩიეთ / მაშინ შესრულდება x და z ის გაყოფა.


elif y == "^": print(x^z) #თუ yის გრაფაში ავირჩიეთ ^ მაშინ შესრულდება x და z ის გამრავლება.


else: print("wrong answer")#თუ პირობები არ შესრულდა მაშინ დაეწერება "wrong answer".