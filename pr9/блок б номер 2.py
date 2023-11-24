a='девятая практическая работа'
b=a.split()
c=''.join([''.join(sorted(a)) for a in b])
print(c)
