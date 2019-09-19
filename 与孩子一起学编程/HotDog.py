class HotDog:
    def __init__(self):
        self.cooked_level=0
        self.cooked_string="Raw"
        self.condiments=[]
        
    def cook(self,time):
        self.cookled_level=self.cooked_level+time
        if self.cooked_level>8:
            self.cooked_string="Charcoal"
        elif self.cooked_level>5:
            self.cooked_string="Well-done"
        elif self.cooked_level>3:
            self.cooked_string="Medium"
        else:
            self.cooked_string="Raw"
            
myDog=HotDog()
print myDog.cooked_level
print myDog.cooked_string
print myDog.condiments
print "Now I'm going to cook the hot dog"
myDog.cook(4)
print myDog.cooked_level
print myDog.cooked_string

            
