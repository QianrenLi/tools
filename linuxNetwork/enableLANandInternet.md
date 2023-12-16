# Enable LAN and Internet Connection in Two NICs

Assume that we have two NICs which connect independently to a LAN (e.g company inner net) and the internet, the default linux route will confict the two connection and only one subnet is accessable.

## Approach 1 - Change Metric
The metric of the routing table determines the order of routing that the system will apply. With metric operation, the key is to configure the LAN route with lower metric compared to the internet routing metric.

``` bash
sudo ip route del default dev <NIC>
sudo ip route add default via <NIC GATEWAY> dev <NIC> metric <METRIC VAL> 
```

This approach, through, suffers from weak connection stability. Therefore, here the a route table configuration is introduced.
## Approach 2 - Change Route Table
``` bash
  sudo route add -net <LAN ID> netmask <LAN MASK> gw <LAN GATEWAY> dev <LAN NIC>
  sudo route del default gw <LAN GATEWAT>
  sudo route add default gw <INTENET GATEWAY> dev <INTENET NIC>
```

# Enable same subnet multiple connection:
The linux system automatically will redirect the transmission in the same BSS which might not be helpful, especially when we need to expand the transmission ability with multiple connections.

The implementation procedure mainly contains two parts:
+ First modify the ARP setting `arp_filter` and `arp_ignore` to make the kernel to identify the ip address with specific interface rather than device it self. 
+ Secondly, make sure two interfaces sperated from each other which can be done by creating multiple different route table.