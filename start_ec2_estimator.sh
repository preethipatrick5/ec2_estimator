sudo apt-get -y update
sudo apt-get -y install git
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
sudo git clone https://github.com/preethipatrick5/ec2_estimator.git
cd ec2_estimator
sudo pip3 install -r requirements.txt
sudo python3 estimator_ec2.py
