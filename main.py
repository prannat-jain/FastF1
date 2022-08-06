import fastf1

from fastf1 import plotting
from matplotlib import pyplot as plt
plotting.setup_mpl()

fastf1.Cache.enable_cache('C:/Users/ASUS/Desktop/cacheFastF1')  # optional but recommended


race = fastf1.get_session(2022, 'Hungarian Grand Prix', 'R')
race.load()

lec = race.laps.pick_driver('LEC')
ver = race.laps.pick_driver('VER')
ham = race.laps.pick_driver('HAM')

fig, ax = plt.subplots()
ax.plot(lec['LapNumber'], lec['SpeedST'], color='red')
ax.plot(ver['LapNumber'], ver['SpeedST'], color='blue')
ax.plot(ham['LapNumber'], ham['SpeedST'], color='cyan')
ax.set_title("LEC vs VER vs HAM")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Speed Trap")
plt.show()

