import psutil
from ipaddress import ip_network
import os

def arp_setup():
    cmd =  os.system("echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore")
    cmd =  cmd + os.system("echo 1 > /proc/sys/net/ipv4/conf/all/arp_filter")
    return cmd

def route_table_setup(interface:str, routeMetric:int):
    cmds = []
    cmds.append(os.system(f'sudo sed -i "/{interface}t/d" /etc/iproute2/rt_tables'))
    cmds.append(os.system(f'echo {routeMetric} {interface}t >> /etc/iproute2/rt_tables'))
    return cmds

def route_table_rule_setup(interface:str, info:dict):
    ipv4 = info[interface]
    maskId = 24
    gateway = str(ip_network(ipv4 + "/" + str(maskId), strict=False)[0])
    cmds = []
    cmds.append(os.system(f'ip rule add from {ipv4} table {interface}t'))
    cmds.append(os.system(f'ip route add {gateway}/{maskId} dev {interface} table {interface}t'))

def setip_test(interface:str, info:dict):
    ipv4 = info[interface]
    maskId = 24
    gateway = str(ip_network(ipv4 + "/" + str(maskId), strict=False)[1])
    cmd = f'ip route get {gateway} from {ipv4}'
    return os.system(cmd)


def main(target_interfaces : list):
    print("Arp setup: ", arp_setup())
    ## get ip information
    addrs = psutil.net_if_addrs()
    info = {} ## interface -- key
    for key in addrs.keys():
        for addr in addrs[key]:
            if addr.family == 2:
                info[key] = addr.address
    ## 
    for target_interface in target_interfaces:
        if target_interface not in info.keys():
            print("Setup fail: Invaid interface or interface has no ipv4: ", target_interface)
            return None
    ##
    metric = 200
    for idx, target_interface in enumerate(target_interfaces):
        print( route_table_setup(target_interface, metric + idx) )
    
    for target_interface in target_interfaces:
        route_table_rule_setup(target_interface, info)

    for target_interface in target_interfaces:
        setip_test(target_interface, info)
    return info

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', nargs='+', required=True, help='interface name')
    args = parser.parse_args()

    main(args.interface)