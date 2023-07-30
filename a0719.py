# class method1 -> 設定血量 , method2 -> 顯示血量
# class 要先set 在get
# class method:
#     def set_blood(self,hp):
#         self.blood1 = int(hp) #設定血量
#     def show_blood(self):
#         hp = self.blood1
#         return (hp)
# # class method1 -> 設定攻擊力 , method2 -> 顯示攻擊力
#     def set_attack(self,atk):
#         self.attack = int(atk)
#     def show_attack(self):
#         show_atk = self.attack
#         return (show_atk)
# # class method1 -> 設定防禦力 , method2 -> 顯示防禦力
#     def set_defense(self,def_):
#         self.defense = int(def_)
#     def show_defense(self):
#         show_def = self.defense
#         return (show_def)
# if __name__ == "__main__":
#     hp = method()
#     hp.set_blood(1)
#     my_blood = hp.show_blood()  #要有人去接他。用ＭＥ接
#     print(my_blood)
#     # ------------------------------------------------------------------------------------------
#     atk = method()
#     atk.set_attack(100)
#     my_atk = atk.show_attack()
#     print(my_atk)
#     # ------------------------------------------------------------------------------------------
#     def_ = method()
#     def_.set_defense(20)
#     my_def = def_.show_defense()
#     print(my_def)


class Person:
    def __init__(self,hp):
        self.hp = hp 
        print("person")

    def set_hp(self,hp):
        self.hp = hp 
        return self.hp
    
    def get_hp(self):
        print(self.hp)
        return self.hp
if __name__ == "__main__":
    hp = Person(4)
    # hp.set_hp(100)
    my_hp = hp.get_hp()
    print (my_hp)


