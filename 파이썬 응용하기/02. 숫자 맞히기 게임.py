import random as rd

num = rd.randint(1, 20)

for i in range(4, 0, -1): # backwards 이기 때문에 두번째 인자에 +1 한 숫자까지 반복
    user = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:"))
    if num > user:
        print("UP")
    elif num < user:
        print("DOWN")

if num == user:
    print(f"축하합니다. {4-i}번 만에 숫자를 맞히셨습니다.")
elif num != user:
    print(f"아쉽습니다. 정답은 {num}였습니다.")

