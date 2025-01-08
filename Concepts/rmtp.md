03.01.2025 03:45
Tags: #concept

---
# Real Time Messaging Protocol

RTMP is a TCP-based protocol which maintains persistent connections and allows low-latency communication.

At a higher level, RTMP encapsulates:

- MP3 or AAC audio
- FLV1 video multimedia streams
- Remote Procedure Calls (RPCs) using the Action Message Format
## Fragments

To deliver streams smoothly and transmit as much information as possible, it splits streams into fragments, and their size is negotiated dynamically between the client and server.

Fragments from different streams may then be interleaved, and multiplexed over a single connection.

- **Interleaving**: arranging video data in an alternating pattern, typically mixing different types of frames or fields.
- **Multiplexing**: combining multiple data streams into a single transmission channel.

With longer data chunks, the protocol thus carries only a one-byte header per fragment

```ad-note
However, in practice, individual fragments are not typically 
interleaved.

Instead, the interleaving and multiplexing is done at the packet level, with RTMP packets across several different active channels being interleaved in such a way as to ensure that each channel meets its bandwidth, latency, and other quality-of-service requirements.

Packets interleaved in this fashion are treated as indivisible, and are not interleaved on the fragment level.
```

## Channels

RTMP defines several virtual channels on which packets may be sent and received, and which operate independently of each other and simultaneously at any given time.

- RPC requests and responses
- Video stream data
- Audio stream data
- out-of-band control messages
- …

## Packets
### Headers
When RTMP data is encoded, a packet header is generated. The packet header specifies, amongst other matters:

- The ID of the channel on which it is to be sent.
- A timestamp of when it was generated (if necessary).
- The size of the packet’s payload.

This header is then followed by the actual payload content of the packet, which is fragmented according to the currently agreed-upon fragment size before it is sent over the connection.

The packet header itself is never fragmented, and its size does not count towards the data in the packet's first fragment.

In other words, only the actual packet payload (the media data) is subject to fragmentation.


