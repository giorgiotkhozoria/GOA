
def bichebtan_misalmeba():
    print("hello gio")
    print("hello nika")
    print("hello tornike")
    print("hello luka")

print("dila")
bichebtan_misalmeba()
print("shuadge")
bichebtan_misalmeba()
print("sagamo")
bichebtan_misalmeba()

def misalmeba(saxeli, age):
    print("mogesalmebi " + saxeli)
    print("sheni asakia" +str(age))

misalmeba("nika", 50)
misalmeba("luka", 10)
misalmeba("gabriel", 6)
misalmeba("sandro", 2)

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2]) #ორი ნაბიჯით გამოტოვება
print(squares[2:8:3]) #2-იდან 8-მდე ყოველი მესამე დაიპრინტოს
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4]) #1-იდან დაიწყებს, ბოლომდე წავა და 4-ს გამოტოვებს

squares1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares1[1:-1]) #1-დან 64-ის ჩათვლით - მეორე ელემენტიდან ბოლოს წინის ჩათვლით
#-1 არის ნეგატიური ინდექსი

nums = [5, 42, 7, 1, 0]
res = nums[::-1] #::-1 არის სიის შეტრიალება
print(res)