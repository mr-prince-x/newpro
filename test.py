import os

os.system('sudo apt update')
os.system('sudo apt install docker.io -y')
os.system('sudo chown ubuntu /var/run/docker.sock')
os.system('sudo apt install docker-compose -y')
os.system('sudo mkdir projectOK')
os.system('sudo apt install maven -y')
#os.system('cd projectOK')
os.system('git clone https://github.com/damini111294/Modifiyfontend.git')
os.system('git clone https://github.com/damini111294/Quantumsoft_backend.git')
os.system('sudo mv Modifiyfontend/ /home/ubuntu/newpro/projectOK/ && sudo mv Quantumsoft_backend/ /home/ubuntu/newpro/projectOK/')
print("Your machine is ready to use")
