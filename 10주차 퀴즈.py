import random
def generate_lotto_numbers():
    numbers=[]
    while len(numbers)<6:
        num= random.randint(1,45)
        if num not in numbers:
            numbers.append(num)
            numbers.sort()
            return "생성된 로또번호는 "+','.join(map(str,numbers))+"입니다."
        print(generate_lotto_numbers())
