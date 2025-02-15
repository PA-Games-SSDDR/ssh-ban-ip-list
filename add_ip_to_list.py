# Run this file to add new ips you have listed to existing list
# first enter the new ips in new_list.txt , every ip in new line
# then run this python script
file_in = open("new_list.txt", "r+")
ip_strings = file_in.read()
ip_list = ip_strings.split('\n')
file_in_2 = open("ip-only-list.txt", "r+")
ip_strings_2 = file_in_2.read()
ip_list_2 = ip_strings_2.split('\n')
new_dict = {}
for ip in ip_list_2:
    if ip not in new_dict:
        new_dict[ip] = 1
for ip in ip_list:
    if ip not in new_dict:
        new_dict[ip] = 1
file_in.close()
file_in_2.close()
file_out = open("ip-only-list.txt", "w+")
file_out.write("\n".join(new_dict.keys()))
file_out.close()
file_in = open("new_list.txt", "w")
file_in.close()
