# Set the user that will run tcpdump
export TCPDUMP_USER=pcap
#change the ownership of specific folder
sudo chown pcap:pcap ~/sandbox_becu/malware_detonation/uploads
# Set the permissions for tcpdump
sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
