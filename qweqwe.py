
def test(test_num: int):
    ch = [i for i in range(0, test_num) if i % 2 == 0]
    for i in ch:
        b = str({f'{i}: {i+1}'})
        print(str(b))



a = int(input())
test(a)

