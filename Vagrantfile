$script = <<-SCRIPT
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install python-bs4 python-mechanize python-cookies -y
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision "shell", inline: $script
end
