from Agent import *
from Mission import *
from missioncontrol import *
from report import *
Agent1 = Agent(8581722,3 )
report1 = Report("now",4,Agent1)
missioncontrol1 = MissionControl.analyze_report(report1)
print(missioncontrol1)

