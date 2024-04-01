import os
import sys

BOOK_PATH = 'book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    res=tuple()
    s=[]
    c=[',','.','!',':',';','?']
    for j in range(start+size-1,start,-1):
        if j+4<=len(text):
            s=[text[j+1],text[j+2],text[j+3]]
            cr=list(set(s) & set(c))
            if not len(cr):
                for i in range(j,start, -1):
                    if text[i] in c:
                        res=tuple([text[start:i+1], len(text[start:i+1])])
                        return res
            else:
                continue
        else:
            for i in range(0, len(text)-j,1):
                s.append(text[j+i])
            cr=list(set(s) & set(c))
            if not len(cr):
                for ch in range(j-(j-len(text))-1,start,-1):
                    if text[ch] in c:
                        res=[text[start:ch+1], len(text[start:ch+1])]
                        return(res)
        break

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        d = f.read()
        data = d.lstrip(' \n    ')
    c: int = 0
    p: int = 1
    while c<len(data):
        if len(data) > PAGE_SIZE:
            res = _get_part_text(data, c, PAGE_SIZE)
            book[p] = res[0].lstrip(' \n    ')
            c+=res[1]
            p+=1
        else:
            res = _get_part_text(data, 0, len(data)-1)
            book[p] = res[0].lstrip(' \n    ')
            c = res[1]-1
            p+=1

# Вызов функции prepare_book для подгоовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
