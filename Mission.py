class Mission:
    def __init__(self,mission_name,target_location):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent =   None
    def brief(self):
        print(f"mission: {self.mission_name} target {self.target_location} ")
    def assigned_agent(self,assigned_agent):
        self.assigned_agent = assigned_agent
    @staticmethod
    def encrypt_message(msg):
        return msg[::-1]
    @staticmethod
    def log_transmission(agent_name,message):
        print(f"{agent_name} sent encrypted message: {message}")
