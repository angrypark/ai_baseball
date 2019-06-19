# 인공지능 숫자야구

### 게임 방법

4자리의 숫자를 생각합니다. 겹치는 숫자가 있어서는 안됩니다. Bot이 어떤 네자리 숫자를 말하면, 어느 숫자가 내 숫자에 들어있고, 어느 숫자가 내 숫자에 들어있으면서 위치까지 동일한 지를 알려줍니다. 내 숫자에 들어있기만 하고 위치가 맞지 않으면 **Ball**이고, 숫자에 들어있으면서 위치까지 맞췄다면 **Strike**이 됩니다. 

만약 `0123` 이 나의 숫자이고 Bot이 `3178` 이라고 말했다면, `3`은 내 숫자에 있으나 위치가 틀려서 **Ball**, `1`은 내 숫자에 있고 위치까지 맞췄으므로 **Strike**, `7`, `8`은 내 숫자에 없으므로 카운트 되지 않습니다. 따라서 스코어는 1 Strike 1 Ball이 됩니다.

몇가지 알고리즘을 통해 평균 4.5회, 최악의 경우에도 7번 내로 당신의 숫자를 맞출 수 있습니다.



### 알고리즘

[Alexey Slovesnov et al 2017, Optimal Algorithms for Mastermind and Bulls-cows Games]([http://slovesnov.users.sourceforge.net/bullscows/bullscows.pdf](http://slovesnov.users.sourceforge.net/bullscows/bullscows.pdf)) 을 바탕으로 구현하였습니다.



### 해보기

페이스북 메신저로 직접 게임해볼 수 있습니다. 링크는 다음과 같습니다.

- [m.me/aibaseball](m.me/aibaseball)



#### Author

박성남, sungnam1108@naver.com, Yonsei University