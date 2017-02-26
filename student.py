class Boy:
    def __init__(self,name,attractiv,intel,budget,min_girlAttract):
        self.name=name
        self.attractiv=attractiv
        self.intel=intel
        self.budget=budget
        self.min_girlAttract=min_girlAttract
        self.status = 'single'
        self.gf = ''
        self.budget=budget

    def checkElligible(self, girl):
        if (self.budget >= girl.main and self.min_girlAttract >= girl.attractiv):
            return True
        return False
class Girl:
    girls_count = 0
    def __init__(self, name, attractiv, main, budget):
        self.name = name
        self.attractiv = attractiv
        self.main = main
        self.status = 'single'
        self.bf = ''
        self.type=''
        self.happinessLevel = 0
        Girl.girls_count += 1
    def checkElligible( self, boy):
        if (self.main <= boy.budget ):
            return True
        return False