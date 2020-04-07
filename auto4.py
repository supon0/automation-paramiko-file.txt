#import Library
import paramiko
import time
import sys

try:
#variabel ip (untuk ip yang diremote), username (untuk masuk ssh), password (password ssh)
    ip_address = ["192.168.122.100","192.168.122.223","192.168.122.140","192.168.122.127",
                  "192.168.122.83","192.168.122.69","192.168.122.66","192.168.122.220"  
                 ]
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
        my_config.seek(0)
        config_list = my_config.readlines()
        for command in config_list:
            ssh_client.exec_command(command)
            print (command)
        print (f"Konfigurasi Router dengan identity : R{i} dan IP Address : {ip} Berhasil")
        time.sleep(0.5)
    sys.exit()

except KeyboardInterrupt:
    print ("\n Exit \n")
    sys.exit()
