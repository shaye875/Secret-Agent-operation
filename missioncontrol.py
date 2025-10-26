from report import *
from Agent import *
from Mission import *
class MissionControl:
    def analyze_report(r:Report):
        if r.urgency_level >= 4:
            print("Immresponse response required.")
        elif r.urgency_level == 3:
            print("High priority Monitor closely")
        else:
            print("Routine analysis")
