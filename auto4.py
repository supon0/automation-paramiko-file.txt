#import Library
import paramiko
import time
import sys

try:
#variabel ip (untuk ip yang diremote), username (untuk masuk ssh), password (password ssh)
    my_ip = open ('ip_address.txt','r')
    ip_address = my_ip.readlines()
    username = "admin"
    password = ""
    i = 0

#perintah untuk melakukan koneksi ssh client ke mikrotik
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for ip in ip_address :
        i += 1
        ssh_client.connect(hostname=ip,username=username,password=password)
        print (f"sukses login to {ip}")
        my_config = open ('perintah.txt','r')
        config_list = my_config.readlines()
        ssh_client.exec_command(f'system identity set name=Router{i}')
        for command in config_list:
            ssh_client.exec_command(command)
            print (command)
        print (f"Konfigurasi Router dengan identity : Router{i} dan IP Address : {ip} Berhasil")
        time.sleep(0.5)
    sys.exit()

except KeyboardInterrupt:
    print ("\n Exit \n")
    sys.exit()
