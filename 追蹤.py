from a0719 import method
    
hp = method()
hp.set_blood(200)
my_blood = hp.show_blood()  #要有人去接他。用ＭＥ接
print(my_blood)
# ------------------------------------------------------------------------------------------
atk = method()
atk.set_attack(20000)
my_atk = atk.show_attack()
print(my_atk-my_blood)
# ------------------------------------------------------------------------------------------
def_ = method()
def_.set_defense(20)
my_def = def_.show_defense()
print(my_def)