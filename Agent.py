class Agent:
    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self.__clearance_level = clearance_level

    def report(self):
        print(f"Agent {self.code_name} reporting clearance level:{self.clearance_level}")
    def set_clearance_level(self,clearance_level):
        if clearance_level > 0 <= 5:
           self.__clearance_level = clearance_level
           print("done")
        else:
            print("just 1-5")
    def get_clearance_level(self,level):
        print(self.__clearance_level)
    @staticmethod
    def sd():
        print("hello")
a1 = Agent("d","g")