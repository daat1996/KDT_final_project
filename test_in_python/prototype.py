from ai_hard import find_all_numbers, print_all_numbers
import random
import pandas as pd
import time


# 플레이 함수
def play_game(turnkey,cardturn,myforce,yourforce):
    if turnkey % 2 == 0:
        print('<당신의 차례입니다>-----------------------------------------------------------------')
        # plague = 1
        while True:
            answer=input('=을 제외한 계산식을 입력해 주세요: ')
            try:
                fin = input(f'예상 결과 값 [{eval(answer)}]이 맞습니까?(y/n)')
                if fin == 'y':
                    if calculright(answer,cardturn,yourforce):
                        print('게임에서 승리하셨습니다!')
                        return False

                    else:
                        print('포스가 다릅니다!')
                        print('차례가 넘어갑니다.')
                        return 2
                else:
                    print('계산식을 다시 입력합니다.')

            except:
                print('계산식에 문제가 있습니다')
                print('차례가 넘어갑니다.')
                return 2

    else:
        print('<상대의 차례입니다>-----------------------------------------------------------------')
        _,algorythm_dict = find_all_numbers(cardturn)
        time.sleep(1)
        if myforce in algorythm_dict:
            print(f'목표 포스:{myforce}')
            time.sleep(0.5)
            print(f'계산 과정: {algorythm_dict[myforce]}')
            time.sleep(0.5)
            print('당신은 패배하였습니다.')
            return False
        else:
            print('차례를 넘깁니다.')
            return 2



# 계산 검증 함수
def calculright(answer,cardturn, force):
    anslist = list(answer)
    alist = []
    for i in anslist:
        if i.isdigit():
            if i =='0':
                alist[-1]=10
            else:
                alist.append(int(i))

    if all(e in cardturn for e in alist):

        if eval(answer) == force:
            return True
        else:
            return False

    else:
        print('사용하신 숫자 중 카드에 없는 것이 있습니다')
        # print(type(alist[0]))
        # print(type(cardturn[0]))
        return False








key = 1
while True:
    while key == 1:
        print('-'*70)
        print('1.게임 방법')
        print('2.게임 시작')
        print('3.종료')
        print('-'*70)
        process = input('명령 번호 입력: ')

        if not process in ['1','2','3']:
            print('잘못 입력하셨습니다. 다시 입력하세요')
        else:
            if process == '1':
                print("""게임 방법
                1. 플레이어와 상대방은 캐릭터카드를 하나 랜덤으로 배정받는다.(시험판기준 1장)
                2. 캐릭터 카드는 좌측위의 레벨, 포스, 필살기포인트를 갖는다.
                3. 중앙에는 1~10의 숫자카드 2장과 X카드 1장이 뒤집어 섞여 있는 카드뭉치가 있다.
                4. 게임 시작 시 숫자카드가 랜덤으로 1장 뒤집혀 공개된다.
                5. 캐릭터카드의 좌측 상단의 레벨을 보고 레벨이 더 높은 플레이어가 선이 된다.
                6. 턴이 바뀌고 시작할 때 마다 숫자카드가 1장씩 앞면으로 공개된다.
                7. 공개된 숫자를 1번씩만 사용하여 사칙연산을 사용해 상대의 포스를 먼저 맞추면 승리한다.
                8. 공격이 힘들거나 불가능할 경우 턴을 넘길 수 있다.
                9. 제한시간이 지나거나 계산을 틀려 실패한 경우 턴이 넘어간다.
                10. (시험판에서는 불가능)일부 카드는 특수한 기능의 필살기포인트를 갖는다.""")



            elif process == '2':
                key = 2
                print('카드를 섞습니다.')
                deckDF = pd.read_csv('../data/character.csv', index_col=0)
                deck = random.sample(deckDF.index.tolist(), 2)
                my_card=deckDF.loc[deck[0]]
                your_card=deckDF.loc[deck[1]]
                cardList = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
                random.shuffle(cardList)
                cardturn = []
                card = cardList.pop()
                cardturn.append(card)
                book = f"""                                                                 _______________________   _______________________
                                                             .-/| 나의 카드             \ / 상대의 카드            |\-.
                                                             |||| no:{deck[0]:^5}               | no:{deck[1]:^5}               ||||
                                                             |||| level:{my_card.level:^5}            | level:{your_card.level:^5}            ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             |||| 포스:{my_card.force:^7}           |   포스:{your_card.force:^7}         ||||
                                                             ||||                        |                        ||||
                                                             ||||                        |                        ||||
                                                             ||||_______________________ | _______________________||||
                                                             ||/========================\|/========================\||
                                                             `-------------------------~___~-----------------------'''"""
                print(book)
                card = cardList.pop()
                cardturn.append(card)
                print(f'현재 숫자 카드 : {cardturn}')
                if my_card.level >= your_card.level:
                    turnkey = len(cardturn)

                    time.sleep(1)
                else:
                    # 상대 차례 부터면 turnkey 홀수
                    turnkey = len(cardturn) + 1

                    time.sleep(1)
                key = play_game(turnkey, cardturn, my_card.force, your_card.force)
                while key == 2:

                    card = cardList.pop()
                    cardturn.append(card)
                    print(book)
                    print(f'현재 숫자 카드 : {cardturn}')
                    turnkey += 1
                    key = play_game(turnkey, cardturn, my_card.force, your_card.force)
                    time.sleep(1)



            elif process == '3':
                print('종료합니다')
                key = 0







    if key == 0:
        break