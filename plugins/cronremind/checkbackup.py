import re
import os
import paramiko
import socket

list_instance_ips = {
    'SWEB-42': '94.237.79.22',
    'SWEB-44': '144.217.86.73',
    'SWEB-36': '178.238.226.42',
    'SWEB-37': '178.238.226.43',
    'TDA-50': '185.207.250.94',
    'TDA-51': '130.185.118.54',
    'TDA-dedi': '209.126.6.116',
    'TDA-52': '213.136.92.122',
}



def check_telnet(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((ip, 22))
        sock.close()
        return result == 0
    except Exception:
        return False

def main():
    USERNAME = "deploy"
    REMOTE_SSH_COMMAND = "sudo cat /var/log/backup_bin.log"
    OUTPUT_FILE = "output.txt"
    new_instance_ips = {}

    for hostname, instance_ip in list_instance_ips.items():
        if check_telnet(instance_ip):
            new_instance_ips[hostname] = instance_ip
        else:
            print(f"Telnet connection to {instance_ip} failed. Skipping {hostname}...")
            continue
    print(new_instance_ips)
    for hostname, instance_ip in new_instance_ips.items():
        try:
            REMOTE_SERVER_IP=instance_ip

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #private_key_path = '/home/tritran/.ssh/deploy_rsa.pem'
            private_key_path = './id_rsa_deploy'
            private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
            client.connect(hostname='{}'.format(REMOTE_SERVER_IP), username='{}'.format(USERNAME), pkey=private_key)
            stdin, stdout, stderr = client.exec_command('{}'.format(REMOTE_SSH_COMMAND))

            output = stdout.read().decode('utf-8')
            with open(OUTPUT_FILE, "w") as f:
                f.write(output)
            client.close()
            domain_pattern = r'^(\S+)'

            # Open the file for reading
            with open("output.txt", "r") as file:
                # Process each line in the file
                for line in file:
                    line = line.strip()  # Remove leading/trailing whitespaces

                    # Extract the domain name from the first element
                    domain_match = re.match(domain_pattern, line)
                    if domain_match:
                        domain = domain_match.group(1)
                    else:
                        domain = ""

                    # Check if "db1" exists in the line
                    if "db1" in line:
                        print("Failed: Backup DB - {} on {} IP {}".format(domain, hostname, instance_ip))
                    # Check if "source1" exists in the line
                    if "source1" in line:
                        print("Failed: Backup Source - {} on {} IP {}".format(domain, hostname, instance_ip))

                    # Check if "cloud1" exists in the line
                    if "cloud1" in line:
                        print("Failed: Upload to Cloud - {} on {} IP {}".format(domain, hostname, instance_ip))
        except paramiko.AuthenticationException as auth_exc:
            print(f"Authentication failed for {hostname}: {str(auth_exc)}")
        except paramiko.SSHException as ssh_exc:
            print(f"Unable to establish SSH connection with {hostname}: {str(ssh_exc)}")
        except Exception as e:
            print(f"An error occurred while connecting to {hostname}: {str(e)}")

if __name__ == "__main__":
    main()
    os.remove("output.txt")