Transfer files privately between instances or from local host to instance
---

SSH into destination instance
1. sudo su
2. navigate to /etc/ssh
3. edit sshd_config file with nano or vim, find `PasswordAuthentication` and replace `no to yes` next to it, save the file.
4. now run `passwd ec2-user`
5. enter your password of choice
6. restart sshd service by running `service sshd restart` or `systemctl restart ssh`
7. ssh to source instance where you have the files and run below command, it will ask you for password, type the password you entered at step 5
8. `scp -rp foldername ec2-user@privatedestinationip:/home/ec2-user`


If you want to transfer files from your local machine to instance, you have to use public ip address of the destination instance. It will ask you for password, type the password you entered at step 5 

`scp -rp foldername ec2-user@publicdestinationip:/home/ec2-user` 
