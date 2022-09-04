---
permalink: vagrant-cheatsheet
categories:
    - Engineering
tags:
    - vagrant
    - automation
---



-   `vagrant` Verify vagrant installation
-   `vagrant init hashicorp/bionic64` This will create a `Vagrantfile` in current directory
-   `vagrant up` start the virtual machine from the Vagrantfile configuration
-   `vagrant halt` shutdown VM preserving content of the disk
-   `vagrant reload` This will quickly restart your virtual machine, skipping the initial import step
-   `vagrant reload --provision` The provision flag on the reload command instructs Vagrant to run the `provisioners`, since usually Vagrant will only do this on the first `vagrant up`
-   `vagrant supend` Stop the virtual machine and save the current state
-   `vagrant ssh` SSH into the machine
-   `vagrant destroy` Destroy the virtual machine
-   `vagrant box list` show the list of downloaded box
-   `vagrant box remove hashicorp/bionic64` vagrant destroy does not remove the downloaded box. remove command delete the downloaded box
-   `ls /vagrant` Explore the sync folder between host and guest machine