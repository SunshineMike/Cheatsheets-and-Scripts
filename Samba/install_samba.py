import subprocess
import os

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

def main():
    # Step 1: Update package list and install Samba
    print("Updating package lists...")
    run_command("sudo apt update")

    print("Installing Samba...")
    run_command("sudo apt install -y samba")

    # Step 2: Create the directory to be shared
    username = os.getlogin()
    share_name = input("Share name: ")
    directory_path = f"/home/{username}/{share_name}"
  
    print(f"Creating directory {directory_path}...")
    run_command(f"mkdir -p {directory_path}")

    # Step 3: Configure Samba settings
    samba_config = "/etc/samba/smb.conf"
    print(f"Configuring Samba settings in {samba_config}...")

    with open(samba_config, 'a') as f:
        f.write(f"\n[{share_name}]\n")
        f.write("  comment = Samba\n")
        f.write(f"  path = {directory_path}\n")
        f.write("  read only = no\n")
        f.write("  browsable = yes\n")

    print("Restarting Samba service...")
    run_command("sudo service smbd restart")

    # Step 4: Update firewall rules to allow Samba traffic
    print("Updating firewall rules...")
    run_command("sudo ufw allow samba")

    # Step 5: Set up Samba password for the user
    print("Setting up Samba user password...")
    run_command(f"sudo smbpasswd -a {username}")

    print("Samba setup completed.")
    print("Connect from Windows: \\<IP-Address>\<Share-Name>")

if __name__ == "__main__":
    main()
