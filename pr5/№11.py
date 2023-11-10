a="Строка: ннн.ук.ннннн.нн"
import re
b = re.findall(r'н+', a)
s = max(b, key=len)
x = s.replace('!', '.')
print(x)
