from gps3 import gps3


gpsd_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gpsd_socket.connect()
gpsd_socket.watch()
for new_data in gpsd_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = ',data_stream.TPV['alt'])
        print('Latitude = ',data_stream.TPV['lat'])