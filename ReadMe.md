## AutoJiffy
Automatic attendance marking at BCCL - [Timescape Jiffy](https://jiffy.timesgroup.com/)

### Initial Setup `(After git clone)`
 ```
sudo apt install python3-venv python3 python3-pip curl git libssl-dev gdebi
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/gc.deb
sudo gdebi /tmp/gc.deb ; rm -f /tmp/gc.deb

cd Project_Directory
python3 -m venv venv
. venv/bin/activate
pip install wheel
pip install -r requirements.txt
cp config.ini.example config.ini
vim config.ini
google-chrome # Remove 2 Checkboxes @ Initial start & Click OK
```

### Usage
```
cd Project_Directory
. venv/bin/activate
python jiffy.py <in/out>
```
