#! /bin/sh

### BEGIN INIT INFO
# Provides:          gpio_relays_off.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting gpio_relays_on.py"
    /home/dan/scripts/gpio_relays_on.py &
    ;;
  stop)
    echo "Starting gpio_relays_off.py"
    /home/dan/scripts/gpio_relays_off.py &
    #pkill -f /home/dan/listen-for-shutdown.py
    ;;
  *)
    echo "Usage: /etc/init.d/listen-for-shutdown.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
