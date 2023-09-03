## Install

To install Samba, follow these steps:

1. Update package lists:
    
    ```bash
    sudo apt update
    ```
    
2. Install the Samba package:
    
    ```bash
    sudo apt install samba
    ```
    
3. Verify the installation:
    
    ```bash
    whereis samba
    ```
    
    You should see output similar to the following:
    
    ```
    samba: /usr/sbin/samba /usr/lib/samba /etc/samba /usr/share/samba /usr/share/man/man7/samba.7.gz /usr/share/man/man8/samba.8.gz
    ```
    

## Setup

### Create directory to share:

```bash
mkdir /home/<username>/<sambashare>/
```

### Configuration:

```bash
sudo nano /etc/samba/smb.conf
```

Scroll to the bottom and add the following lines:

```bash
[<sambashare>]
    comment = Samba on Ubuntu
    path = /home/<username>/<sambashare>
    read only = no
    browsable = yes
```

1. **Note**: Replace **`<username>`** with your actual username.
- **`comment`**: A brief description of the share.
- **`path`**: The directory of our share.
- **`read only`**: Permission to modify the contents of the share folder; set to **`no`**.
- **`browsable`**: When set to **`yes`**, the share will appear in file managers.

Save and close the file (Ctrl-O to save, Ctrl-X to exit).

Restart the Samba service to apply the changes:

```bash
sudo service smbd restart
```

Update the firewall rules to allow Samba traffic:

```bash
sudo ufw allow samba
```

# Accounts

### User password

**Note**: Make sure the username belongs to a system account.

```bash
sudo smbpasswd -a <username>
```

### Connect from Windows

1. Open File Manager on your Windows machine.
2. In the address bar, type:

```bash
\\<IP-Address>\<sambashare>
```
