# ssh-ban-ip-list
List of ips port scanning ssh

The file `ip-only-list.txt` contains list of ips which were found to trying to ssh multiple times without valid credentials.

The script `add_ip_to_list.py` adds new ips you place in `new_list.txt` to existing list.

The script `search_ban_list.py` returns True/False if provided ip is in ban list.

Usage : `python search_ban_list.py x.y.z.w`
