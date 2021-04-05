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

triggerCommand = ["gphoto2 --capture-image-and-download"]

save_location = "/home/pi/data"

def captureImages(ID):
    gp(triggerCommand)
    os.rename('capt0000.cr3', '~/data/image_{}.cr3'.format(ID))

killgphoto2Process()
captureImages()

for ii in range(0,3):
    captureImages(ii)