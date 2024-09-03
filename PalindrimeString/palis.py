DummyString="Hih"
lowerConversion=DummyString.lower()
print(lowerConversion)
reverseString=lowerConversion[::-1]
print(reverseString)
if lowerConversion==reverseString:
  print("YEAH! , string is Palindrome")
else:
  print("OH!, string lost")