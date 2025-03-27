#Palindrome Kelimeler

kelime=input("Bir kelime giriniz:")
tersi=kelime[::-1]
if(kelime==tersi):
    print(kelime,"palindrome kelimedir.")
else:
    print(kelime,"palindrome değildir.")