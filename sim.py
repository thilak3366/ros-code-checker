import subprocess, time, os

print("Launching Gazebo...")
subprocess.Popen(["gazebo"])
time.sleep(10)

print("Capturing screenshot...")
os.system("gnome-screenshot -f screenshots/sim_preview.png")

print("Simulation finished")
