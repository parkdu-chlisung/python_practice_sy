# 문제 12 : 게임 캐릭터 클래스 만들기
# 다음 소스 코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '파이어볼'이 출력되게 만드시오.
# 주어진 소스 코드를 수정해선 안됩니다.


class Wizard:
    # 매직매소드
    # init은 클래스가 인스턴스가 될때 무조건 처음에 한 번 실행하는 것
    # 인스턴스화 될 때, 인스턴스의 영역을 나타내는 것이 self임 -> 반드시 필요
    def __init__(self,health,mana,armor):
        self.health = health #self.health에 입력된 health 넣기
        self.mana = mana
        self.armor = armor

    # 매서드는 self가 꼭 있어야함
    def attack(self):
        print("파이어볼")


x = Wizard(health = 545, mana = 210, armor=10)
print(x.health, x.mana , x.armor)
x.attack()