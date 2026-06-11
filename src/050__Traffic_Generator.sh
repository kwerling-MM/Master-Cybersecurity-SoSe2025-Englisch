CLONE_IP="192.168.100.13"  # IP-Adresse von 

while (true); do
    curl -s http://$CLONE_IP
    sleep 1
    
done