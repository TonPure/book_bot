import sys

def _get_part_text(t: str, st: int, si: int) -> tuple[str, int]:
    res=tuple()
    s=[]
    c=[',','.','!',':',';','?']
    for j in range(st+si-1,st,-1):
        if j+4<=len(t):
            s=[t[j+1],t[j+2],t[j+3]]
            cr=list(set(s) & set(c))
            if not len(cr):
                for i in range(j,st,-1):
                    if t[i] in c:
                        res=tuple([t[st:i+1], len(t[st:i+1])])
                        return res
            else:
                continue
        else:
            for i in range(0, len(t)-j,1):
                s.append(t[j+i])
            cr=list(set(s) & set(c)) 
            if not len(cr):
                for ch in range(j-(j-len(t))-1,st,-1):
                    if t[ch] in c:
                        res=[t[st:ch+1], len(t[st:ch+1])]
                        return res
        break
