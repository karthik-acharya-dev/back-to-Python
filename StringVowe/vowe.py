string="hell"
empty=''

lowerConvert=string.lower()
for item in lowerConvert:
  if item=='a'or item=='e'or item=='i'or item=='o'or item=='u':
    empty+=item
s=''
if len(empty)>1:
  s='s'

print(string,'string contains',empty,'vowel'+s)