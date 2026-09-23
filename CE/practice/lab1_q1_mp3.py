import os
def transmission_time(mp3_file, data_rate):
    file_size_bytes = os.path.getsize(mp3_file)
    message_size_bits = file_size_bytes * 8
    time_in_sec = message_size_bits / data_rate
    return time_in_sec

mp3_file = "CE/saint.mp3"
data_rate = 12800

file_size = os.path.getsize(mp3_file)
time = transmission_time(mp3_file, data_rate)

print(f"Transmission time: {time} seconds")
print(f"Message size: {file_size} bytes")