import os

os.system('sudo apt update')
os.system('sudo apt install docker.io -y')
os.system('sudo chown ubuntu /var/run/docker.sock')
os.system('sudo apt install docker-compose -y')
os.system('docker-compose up')
