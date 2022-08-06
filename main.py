# variables

a = 2
b = 10.00
c = 'blue'
d,e = (True, 1), (False, 0)
f = ['tulip', 'rose', 'daisy', 'fern']
g = {
    0: 'closed',
    1: 'closed',
    2: 'closed',
    4: 'open',
}

h = False
i = 'animal'
j = [
    ({
        'name': 'jeff',
        'age': 34,
    },
    {
        'job': ('programmer', 24501),
        'interests': ['fishing', 'hiking']
    })
]
k = 0b10101010
l = 0b10000000
m = 0b10101010

# code stack
output = []

spF = f.copy()
if a >= b:
    h = not h
    output.append('Lamp')
else:
    b -= a
    f.sort()

if len(j) > 1:
    for staff in j:
        if 'boring forms' in staff['interests']:
            staff['job']['role'] = 'admin'
            staff['job']['ID'] = '6345789'
        