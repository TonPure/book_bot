from tex import _get_part_text

book: dict[int,str] = {}
PAGE_SIZE = 1050

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
            print(book)
            c += res[1]
            p+=1
        else:
            res = _get_part_text(data, 0, len(data)-1)
            book[p] = res[0]
            c = res[1]-1
            p+=1

if __name__ == '__main__':
    prepare_book('book.txt')
