def _get_part_text(t: str, st: int, si: int) -> tuple[str, int]:
    s=[]
    c=[',','.','!',':',';','?']
    print(len(t))
    print(t[st:st+si])
    for i in range(st+si-1, st, -1):
        print('i = ', i)
        if i+3<=len(t):
            s.append(t[i+1])
            s.append(t[i+2])
            s.append(t[i+3])
        else:
            print('i+3 = ', i+3)
            print((i+3),' > ',len(t))
            for j in range(3-(len(t)-i)):
                print('j = ', j)
                s.append(t[j])
                print('t[j]==', t[j])
        if (x for x in s) not in c:
            for ch in range(i, st, -1):
                if t[ch] in c:
                    print('t[ch]= ', t[ch])
                    res = [t[st:ch+1], len(t[st:ch+1])]
                    print('res - ',res)
                    break
        break

t='- Я амн очень тщательно проверил, - сказал компьютер, - и со всей определенностью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсо'
_get_part_text(t,54,70)
