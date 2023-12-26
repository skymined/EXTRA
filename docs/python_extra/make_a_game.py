# 첫번째 줄에 숫자 3개를 입력한다. 
# 두번째 줄에 도전 횟수를 입력한다. 
# 세번째 줄 부터 맞추는 기회가 주어진다. 

# - 숫자는 맞지만 위치가 틀렸을 때는 볼
# - 숫자와 위치가 전부 맞으면 스트라이크
# - 숫자와 위치가 전부 틀리면 아웃이 주어진다. 
# - 만약 모두 틀렸을 경우 '아웃'이 출력된다.

# 선택 사항)
# - 3S가 나올 경우 프로그램 종료
# - 입력 양식이 틀릴 경우 다시 입력
# - 숫자 3개 입력 시 값 중에 똑같은 값이 있을 경우 다시 입력

def num_game() :

    while True : 
        Correct_answer = list(map(int, input().split()))
        try_time = int(input()) # 시도할 횟수
        if len(Correct_answer) != 3 :
            print("다시 입력해주십시오.")
            continue
        elif Correct_answer[0] == Correct_answer [1] or Correct_answer[1] == Correct_answer[2] or Correct_answer[2] ==Correct_answer[0] :
            print("다른 수 3개를 입력해주십시오.")
        else : 
            break

    for x in range(try_time):
        your_answer = input("{}번째 시도 : ".format(x+1)).split()
        your_answer = list(map(int, your_answer))
        ddaddan = []
        Strike=[]
        for y in range(0,3):
            if Correct_answer[y] == your_answer[y]:
                Strike.append("S")
        if len(Strike) != 0 :
            ddaddan.append("{}S".format(len(Strike)))
        Out = [item for item in your_answer if item not in Correct_answer]
        if 3-len(Out)-len(Strike) !=0:
            ddaddan.append("{}B".format(3-len(Out)-len(ddaddan)))
        if len(Out) !=0:
            ddaddan.append("{}O".format(len(Out)))

        print(*ddaddan,end="")
        print("")
        
        if len(Strike) == 3 :
            print("정답입니다!")
            break

num_game()