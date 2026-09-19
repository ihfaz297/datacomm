# Lab 1 Exam Guide — Transmission Time, Delays, Encapsulation, Bit Stuffing

Five tiny programs. All of them are **unit conversion + one formula + print**.
The marks are in: (a) converting units correctly, (b) printing with labels and units.

---

## 0. The formulas (this is the entire theory you need)

| Quantity | Formula | Units to watch |
|---|---|---|
| Message size in bits | `bytes x 8` | 1 MB = 1,000,000 bytes (lab uses decimal, NOT 1024) |
| **Transmission delay** (a.k.a. transmission time) | `T_t = bits / data_rate_bps` | Mbps -> x1,000,000 ; kbps -> x1,000 |
| **Propagation delay** | `T_p = distance_m / speed` | km -> x1,000 ; speed usually 2e8 or 3e8 m/s |
| Total delay (latency) | `T_t + T_p` (+ queuing + processing if given) | |
| Number of packets | `data_bytes / payload_bytes` | |
| Effective time with headers | `packets x (payload+header) x 8 / bps` | |
| **Efficiency** | `payload / (payload + overhead) x 100 %` | overhead = all headers + trailers |
| Ethernet frame | `6 + 6 + 2 + payload + 4` | header = 14, trailer (FCS) = 4, overhead = 18 |
| Bit stuffing | after every **five consecutive 1s**, insert a **0** | flag is `01111110` |

Sanity check you can do in your head: 20 MB at 5 Mbps -> 160 Mbit / 5 = **32 s**.
1500 km at 2e8 m/s -> 1.5e6 / 2e8 = **0.0075 s**.

> WARNING: Your notebook run typed `2000000` (2e6) for speed and printed 0.75 s. With the
> example's `200000000` (2e8) the answer is **0.0075 s** and total = **32.0075 s**.
> Type the zeros carefully, or write `2e8`.

---

## Q1 — WAV file transmission time

```python
import os

wav_file  = "/content/drive/My Drive/Commn Engg/sample-12s.wav"   # or any path
data_rate = 128000                                                # bps (128 kbps)

file_size_bytes = os.path.getsize(wav_file)   # size on disk
file_size_bits  = file_size_bytes * 8
time_seconds    = file_size_bits / data_rate

print(f"Message size     : {file_size_bytes:,} bytes")
print(f"Message size     : {file_size_bits:,} bits")
print(f"Data rate        : {data_rate:,} bps")
print(f"Transmission time: {time_seconds:.4f} seconds")
```
Expected (for the lab's file): 2,254,892 bytes -> 18,039,136 bits -> **140.9307 s**.

If in Colab, first: `from google.colab import drive; drive.mount('/content/drive')`.
If no file is given, upload one: `from google.colab import files; up = files.upload(); wav_file = list(up)[0]`.

Bonus if she asks for the **audio bit rate / duration** using the `wave` module:
```python
import wave
with wave.open(wav_file, 'rb') as w:
    rate, channels, width, frames = w.getframerate(), w.getnchannels(), w.getsampwidth(), w.getnframes()
duration = frames / rate                         # seconds of audio
bit_rate = rate * channels * width * 8           # bps of the audio itself
print(f"Duration: {duration:.2f} s, audio bit rate: {bit_rate:,} bps")
```

---

## Q2 — Video: transmission, propagation, total delay, header overhead, efficiency

Build it as: **inputs -> convert -> formulas -> print**.
```python
video_size_mb     = float(input("Enter video size (MB): "))
data_rate_mbps    = float(input("Enter data rate (Mbps): "))
distance_km       = float(input("Enter distance (km): "))
propagation_speed = float(input("Enter propagation speed (m/s): "))

# convert
video_size_bytes = video_size_mb * 1_000_000
video_size_bits  = video_size_bytes * 8
data_rate_bps    = data_rate_mbps * 1_000_000
distance_m       = distance_km * 1_000

# 1-3. delays
transmission_delay = video_size_bits / data_rate_bps
propagation_delay  = distance_m / propagation_speed
total_delay        = transmission_delay + propagation_delay

# 4-5. packets with header
payload_size = 1_000
header_size  = 100
packet_size  = payload_size + header_size
number_of_packets       = video_size_bytes / payload_size
total_transmitted_bits  = number_of_packets * packet_size * 8
effective_transmission_time = total_transmitted_bits / data_rate_bps
transmission_efficiency     = payload_size / packet_size * 100

print("\n========== RESULTS ==========")
print(f"Transmission delay : {transmission_delay:.4f} s")
print(f"Propagation delay  : {propagation_delay:.6f} s")
print(f"Total delay        : {total_delay:.4f} s")
print(f"Number of packets  : {number_of_packets:.0f}")
print(f"Effective tx time  : {effective_transmission_time:.4f} s")
print(f"Efficiency         : {transmission_efficiency:.2f} %")
```
Expected for 20 MB, 5 Mbps, 1500 km, 2e8 m/s:

| | |
|---|---|
| Transmission delay | 32.0000 s |
| Propagation delay | 0.0075 s |
| Total delay | 32.0075 s |
| Packets | 20000 |
| Effective tx time | 35.2000 s |
| Efficiency | 90.91 % |

Variations she may add (each is one more line):
- **Queuing / processing delay** given -> `total = T_t + T_p + T_q + T_proc`.
- **Bandwidth-delay product** -> `bps x propagation_delay` bits ("bits in flight").
- **Throughput** -> `payload_bits_total / total_time`.
- **Last packet arrives at** -> `n_packets x T_t(one packet) + T_p`.
- If she says 1 MB = 1024x1024 bytes, change the `1_000_000`.

---

## Q3 — Ethernet frame size, overhead, efficiency
```python
payload = 1000
destination_mac, source_mac, type_field, fcs = 6, 6, 2, 4

header  = destination_mac + source_mac + type_field     # 14
trailer = fcs                                           # 4
frame_size = header + payload + trailer                 # 1018
overhead   = header + trailer                           # 18
efficiency = payload / frame_size * 100                 # 98.23 %

print(f"Frame size : {frame_size} bytes")
print(f"Overhead   : {overhead} bytes")
print(f"Efficiency : {efficiency:.2f} %")
```
Variation: add preamble (7) + SFD (1) -> overhead 26, frame 1026. Add VLAN tag -> +4.

---

## Q4 — OSI encapsulation, size after each layer
```python
application_data   = 500
transport_header   = 20
network_header     = 20
data_link_header   = 14
data_link_trailer  = 4

transport_data  = application_data + transport_header                    # 520  (segment)
network_packet  = transport_data + network_header                        # 540  (packet)
data_link_frame = network_packet + data_link_header + data_link_trailer  # 558  (frame)

print(f"Application Layer : {application_data} bytes")
print(f"Transport Layer   : {transport_data} bytes")
print(f"Network Layer     : {network_packet} bytes")
print(f"Data Link Layer   : {data_link_frame} bytes")
print(f"Total overhead    : {data_link_frame - application_data} bytes")     # 58
print(f"Efficiency        : {application_data / data_link_frame * 100:.2f} %") # 89.61
```
If she asks for the reverse (**decapsulation**) just subtract in the opposite order.
If she gives all 7 layers, use a list and a loop:
```python
layers = [("Application",0),("Presentation",10),("Session",10),("Transport",20),("Network",20),("Data Link",18)]
size = 500
for name, h in layers:
    size += h
    print(f"{name:13s}: {size} bytes")
```

---

## Q5 — Bit stuffing
Rule: **count consecutive 1s; when the count hits 5, append a 0 and reset.**
```python
def bit_stuff(data):
    stuffed, ones, inserted = "", 0, 0
    for bit in data:
        stuffed += bit
        if bit == "1":
            ones += 1
            if ones == 5:
                stuffed += "0"
                inserted += 1
                ones = 0
        else:
            ones = 0
    return stuffed, inserted

data = input("Enter binary data: ")
stuffed, inserted = bit_stuff(data)
print("Original :", data, f"({len(data)} bits)")
print("Stuffed  :", stuffed, f"({len(stuffed)} bits)")
print("Inserted :", inserted)
```
Checks: `01111110` -> `011111010` (1 inserted). `0111111111` -> `01111101111` (1). `1111111111` -> `111110111110` (2).

**Unstuffing** (the reverse, in case): after seeing five 1s, **skip** the next bit.
```python
def bit_unstuff(data):
    out, ones, skip = "", 0, False
    for bit in data:
        if skip:
            skip = False; ones = 0; continue
        out += bit
        if bit == "1":
            ones += 1
            if ones == 5: skip = True
        else:
            ones = 0
    return out
```
Add flags if asked: `frame = "01111110" + stuffed + "01111110"`.

**Byte stuffing** (if she switches): insert ESC before any FLAG or ESC byte in the data.
```python
FLAG, ESC = "F", "E"
def byte_stuff(data):
    out = ""
    for ch in data:
        if ch in (FLAG, ESC):
            out += ESC
        out += ch
    return FLAG + out + FLAG
```

---

## Print-format cheat sheet (this is where "labels and units" marks come from)
- `f"{x:.4f}"` -> 4 decimals.  `f"{x:,}"` -> thousands separator.  `f"{x:.2e}"` -> scientific.
- Always print the **unit** (bytes / bits / bps / s / %).
- `input()` returns a string -> wrap in `float()` (or `int()`).
- `1_000_000` underscores are legal Python and stop you from miscounting zeros.
