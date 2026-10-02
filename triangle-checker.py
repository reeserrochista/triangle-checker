s1 = float(input('Say the  first segment:'))
s2 = float(input('Say the second segment:'))
s3 = float(input('Say the third segment:'))
if s1+s2 > s3 and s2+s3 > s1 and s1+s3 > s2:
    print('The segments can do a triangle')
else:
    print('The segments cannot do a triangle')
