#Match all the following currencies £50,000, 30p, 500m euro, $5000.00 , £50.00 , 30.0bn.


import re
text="£50,000, 30p, 500m euro, $5000.00 , £50.00 , 30.0bn"

m=re.findall(r'(?:[\£\$]?\d+[\,\.]?\d+[p|m|bn]?\s?\w+[euros|euro|pounds|pound|dollars|dollar]?)',text)

print(m)
