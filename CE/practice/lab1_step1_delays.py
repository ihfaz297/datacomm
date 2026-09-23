# LAB 1 STEP 1 / 2  -  transmission delay, propagation delay, header overhead
#
# Formulas:
#   transmission delay = total bits / data rate (bits per second)
#   propagation delay  = distance (m) / propagation speed (m/s)
#   efficiency         = payload / (payload + header) * 100
#
# Units are the whole game:  MB -> bytes x 1e6,  bytes -> bits x 8,
#                            Mbps -> bps x 1e6,   km -> m x 1000

video_size_mb     = 20
data_rate_mbps    = 5
distance_km       = 1500
propagation_speed = 2e8          # m/s   (2e8 means 200,000,000)

# TODO: convert units
video_size_bits = video_size_mb * 1e6 * 8           # MB -> bytes -> bits
data_rate_bps   = data_rate_mbps * 1e6           # Mbps -> bps
distance_m      = distance_km * 1000           # km -> m

# TODO: the three delays
transmission_delay = video_size_bits / data_rate_bps
propagation_delay  = distance_m / propagation_speed
total_delay        = transmission_delay + propagation_delay

# TODO: packets with a 100-byte header on every 1000-byte payload
payload, header = 1000, 100
number_of_packets  = video_size_bits / (8 * payload)        # video bytes / payload bytes
effective_time     = number_of_packets * (payload + header) * 8 / data_rate_bps
efficiency         = (payload / (payload + header)) * 100        # payload / (payload + header) * 100


# ---------------- checker: don't edit below ----------------
got = (transmission_delay, propagation_delay, total_delay, number_of_packets, effective_time, efficiency)
exp = (32.0, 0.0075, 32.0075, 20000, 35.2, 90.9090909)
names = ("transmission delay", "propagation delay", "total delay", "packets", "effective time", "efficiency %")
ok = True
for n, g, e in zip(names, got, exp):
    good = g is not None and abs(g - e) < 1e-4
    ok &= good
    print(f"{n:20s}: {g}   {'ok' if good else f'expected {e}'}")
print("PASS  ->  open lab1_step2_bitstuff.py" if ok else "FAIL")
