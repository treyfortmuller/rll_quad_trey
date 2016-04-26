""" attempt to connect to RLL SOLO 1, reads battery voltage. """

from dronekit import connect


# Connect to the Vehicle (in this case a UDP endpoint)
print "Connecting to Solo"
vehicle = connect('udpin:0.0.0.0:14550', wait_ready=True)

print "Get some vehicle attribute values:"
print " Battery: %s" % vehicle.battery