#Match all the phone numbers listed with a regular expression.

import re

text="555.123.4565,+1-(800)-545-2468,2-(800)-545-2468, 3-800-545-2468, 555-123-3456, 555 222 3342, (234) 234 2442, (234)-234-2342,
      1234567890, 123.456.7890, 123.4567, 123-4567, 1234567900, 12345678900"
      
p=re.findall(r'\+?\d?\-?\(?\d{3}\)?[\-\.\s]?\d{3}?[\-\.\s]?\d{4}?|\d{3}[\s\.\-]?\d{4}?',text)

for i in range(0,len(a)):
    print(p[i],"[]", a[i])
    
print(p)
