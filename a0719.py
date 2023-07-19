# class method1 -> 設定血量 , method2 -> 顯示血量
class method:
    def set_blood(self,hp):
        self.blood1 = int(hp) #設定血量
    def show_blood(self):
        hp = self.blood1
        return (hp)
# class method1 -> 設定攻擊力 , method2 -> 顯示攻擊力
    def set_attack(self,atk):
        self.attack = int(atk)
    def show_attack(self):
        show_atk = self.attack
        return (show_atk)
# class method1 -> 設定防禦力 , method2 -> 顯示防禦力
    def set_defense(self,def_):
        self.defense = int(def_)
    def show_defense(self):
        show_def = self.defense
        return (show_def)
if __name__ == "__main__":
    hp = method()
    hp.set_blood(1)
    my_blood = hp.show_blood()  #要有人去接他。用ＭＥ接
    print(my_blood)
    # ------------------------------------------------------------------------------------------
    atk = method()
    atk.set_attack(100)
    my_atk = atk.show_attack()
    print(my_atk)
    # ------------------------------------------------------------------------------------------
    def_ = method()
    def_.set_defense(20)
    show_def1 = def_.show_defense()
    print(show_def1)




