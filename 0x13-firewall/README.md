0x13. Firewall
DevOps
SysAdmin
Security

0. Block all incoming traffic but
mandatory
Score: 0.0% (Checks completed: 0.0%)
Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:

The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)
Share the ufw commands that you used in your answer file
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x13-firewall
File: 0-block_all_incoming_traffic_but