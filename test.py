import os

os.system('sudo apt update')
os.system('sudo apt install docker.io -y')
os.system('sudo chown ubuntu /var/run/docker.sock')
os.system('sudo apt install docker-compose -y')
os.system('sudo mkdir projectOK')
os.system('cd projectOK')
os.system('git clone https://github.com/damini111294/Modifiyfontend.git')
os.system('git clone https://github.com/damini111294/Quantumsoft_backend.git')
print("Your machine is ready to use")
