
#간략한 프로그램 의도 소개

print("안녕하세요! 당신의 기분에 도움이 되어드릴게요!^^")

mood=['행복','우울']
say=['네','아니오']


mymood=input(str(list(mood))+"당신의 기분은?? ")

print("")

if mymood=="행복":
    import random
    행복=['기쁘게 일하고, 자신이 한 일을 기뻐하는 사람은 행복하다.-괴테',
        '오래가는 행복은 정직한 것 속에서만 발견할 수 있다. -리히텐베르히',
        '행복은 무엇보다 건강속에서 찾을 수 있다.-커티스']
    def selectRandom(행복):
        return random.choice(행복)
    print("행복한 당신에게 주는 명언: ",selectRandom(행복))
    

    yousay=input(str(list(say))+"노래 추천해드릴까요??")
    if yousay=="네":
        import random
        네=['"행복한 순간이야! Happy days!" 엄정화-Festival',
           '"하이얀 우리 봄날의 Climax! 얼마나 기쁜 일이야" 아이유-라일락',
           '"사소한 게 사소하지 않게 만들어버린 너라는 별" BTS-작은 것들을 위한 시']
        def selcetRandom(네):
            return random.choice(네)
        print("행복할 때 추천노래: ",selectRandom(네))
        
    else: print("안녕히계세요!")

if mymood=="우울":
    import random
    우울=['아름다운 장미는 가시 위에서 피고, 슬픔 뒤에는 반드시 기쁨이 있다.-윌리엄 스미스',
        '너의 점이 조금이라도 가벼워 지기를.. 될 수 있다면 아주 많이 가벼워 지기를 바란다.-빈센트 반 고흐',
        '세상 모든 일은 여러분이 무엇을 생각하느냐에 따라 일어납니다.-오프라 윈프리']
    def selectRandom(우울):
        return random.choice(우울)
    print("우울한 당신에게 주는 명언: ", selectRandom(우울))

    yousay=input(str(list(say))+"노래 추천해드릴까요?")

    if yousay=="네":
        import random
        네=['"원하는 대로만 살수는 없지만 알 수 없는 내일이 있다는 건 설레는 일이야 두렵기는 해도" 산다는건 다 그런게 아니겠니-여치',
           '"하지만 힘을 내 이만큼 왔잖아 이것쯤은 정말 별거 아냐" 힘내-소녀시대',
           '"아무노력 말아요 버거울 땐 언제든 나의 이름을 잊어요" 눈사람-정승환']
        def selectRandom(네):
            return random.choice(네)
        print("우울할 때 추천노래: ",selectRandom(네))

    else: print("안녕히계세요!")
    

 
    
