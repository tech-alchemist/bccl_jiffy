## AutoJiffy
Automatic attendance marking at BCCL - [Timescape Jiffy](https://jiffy.timesgroup.com/)

### Initial Setup `(After git clone)`
 ```
cd Project_Directory
sudo apt install python3-venv python3 python3-pip curl git libssl-dev
python3 -m venv venv
. venv/bin/activate
pip install wheel
pip install -r requirements.txt
cp config.ini.example config.ini
vim config.ini
```

### Usage
```
cd Project_Directory
. venv/bin/activate
python jiffy.py <in/out>
```
