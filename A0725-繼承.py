class OzToGram:
    def set_oz(self,oz):
        self.Oz = oz
class GoldOz(OzToGram):
    def get_gram(self):
        print(self.Oz *31)
# 30G        

class steak(OzToGram):
    def get_gram(self):
        print(self.Oz *28)
# 28G


oz = GoldOz()
oz.set_oz(1)
oz.get_gram()

oz = steak()
oz.set_oz(1)
oz.get_gram()