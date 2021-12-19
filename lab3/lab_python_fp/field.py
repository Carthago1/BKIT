def field(col, *args):
    if len(args) == 1:
        for i in col:
            if args[0] in i:
                yield i[args[0]]
    else:
        for i in col:
            d = {}
            for j in args:
                if j in i:
                    d[j] = i[j]    
            yield d

goods = [{'title' : 'Ковер', 'price' : 2000, 'color' : 'green'},
         {'title' : 'Диван для отдыха', 'color' : 'black'}]

field_gen = field(goods, 'title', 'price')

for i in field_gen: 
    print(i)
