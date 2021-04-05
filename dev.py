from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

# Kill the gphoto2 process that starts whenever we connect the camera:
def killgphoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # Search for the line that has the process we want to kill:
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # Kill the process!
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)

shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiShots"

clearCommand = ["--folder", "/store_00020001/DCIM/100CANON", "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]

save_location = "/home/pi/data"

def createSaveFolder():
    try:
        os.makedirs(save_locaiton)
    except:
        print(save_location + " already exists.")
    os.chdir(save_location)

def captureImages():
    gp(triggerCommand)
    sleep(3) #TODO Consider removing?
    gp(downloadCommand)
    gp(clearCommand)

def renameFiles(ID):
    for filename in os.listdir("."):
        if len(filename) < 13
            if filename.endswith(".CR3"):
                os.rename(filename, (shot_time + ID + ".CR3"))
                print("Renamed the Image")

killgphoto2Process()
gp(clearCommand)
createSaveFolder()
captureImages()
renameFiles(picID)

