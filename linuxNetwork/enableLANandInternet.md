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


# Enable two same NICs
The WiFi system generally providing a co-service set on 5G and 2.4G which not interferes with each other. Nevertheless, the linux driver will automatically use one NIC as proxy and thus reduce the channel capacity available. To enable these such connection, we can set the route table rule as done in the `set_route.py`.

In `set_route.py`, a simple example offers to set route for Interfaces in the same subnet (started with `192.168`) is provided.
