Host simple hello world website from EC2 instance
---
Launch EC2 instance
Create security group rules

    1. SSH on PORT 22 for only from your IP
 
    2. HTTP on PORT 80 for all CIDR range 0.0.0.0/0

SSH into the instance or you can use connect option in the EC2 console and run the following commands
 
    `sudo su`

    `yum update -y`

    `yum install http -y`

    `cd /var/www/html`
    
    `vi index.html`

It will open a vi editor
 
    i - insert
 
    type <p>Hello World</p>

    :w

    :q

You will get back to shell
run `ls` command, it will show you index.html > `cat index.html` will give you `Hello World`
    `service httpd start`