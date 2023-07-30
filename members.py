import random

members = [
            '김범수', '이승호', '승재홍', '이유빈', 
            '이윤형', '전규훈', '정구민', '주홍찬'
           ]

random.shuffle(members)
print(f'첫번째 조: {members[0:4]}')
print(f'두번째 조: {members[4:8]}')

