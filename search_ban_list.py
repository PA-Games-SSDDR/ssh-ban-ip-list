import argparse

file_in_2 = open("ip-only-list.txt", "r+")
ip_strings_2 = file_in_2.read()
ip_list_2 = ip_strings_2.split('\n')
IP_DICT = {}
for ip in ip_list_2:
    if ip not in IP_DICT:
        IP_DICT[ip] = 1


def fin_ip(ip_addr):
    if ip_addr in IP_DICT:
        return True
    else:
        return False


parser = argparse.ArgumentParser(
                    prog='SearchIP',
                    description='Search if an IP is in ban list')
parser.add_argument('ip', type=str,
                    help='An IPv4/IPv6 address')

if __name__ == "__main__":
    args = parser.parse_args()
    print(fin_ip(args.ip))
