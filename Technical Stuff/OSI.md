

### OSI Model Cheatsheet

#### Layer 7: Application Layer
- **Role**: Provides end-user services and application-to-application communication.
- **Protocols**: HTTP, HTTPS, FTP, SMTP, POP3, IMAP, Telnet, SSH
- **Key Concepts**: User interface, end-user services, API

#### Layer 6: Presentation Layer
- **Role**: Translates, encrypts, and compresses data.
- **Protocols**: JPEG, GIF, MPEG, SSL, TLS
- **Key Concepts**: Data translation (ASCII, EBCDIC), data compression, data encryption

#### Layer 5: Session Layer
- **Role**: Manages sessions or connections between applications.
- **Protocols**: NetBIOS, RPC, PPTP
- **Key Concepts**: Session establishment, maintenance, and termination

#### Layer 4: Transport Layer
- **Role**: Provides reliable data transport services.
- **Protocols**: TCP, UDP
- **Key Concepts**: Segmentation and reassembly, error checking, flow control

#### Layer 3: Network Layer
- **Role**: Routes data from one network node to the destination node.
- **Protocols**: IP, ICMP, OSPF, RIP, BGP
- **Key Concepts**: Routing, IP addressing, packet forwarding

#### Layer 2: Data Link Layer
- **Role**: Transfers data between network interfaces on the same network.
- **Protocols**: Ethernet, Wi-Fi, Frame Relay, PPP
- **Key Concepts**: MAC addressing, error detection, frames

#### Layer 1: Physical Layer
- **Role**: Transmits raw bits over a physical medium.
- **Protocols**: USB, Bluetooth, Ethernet
- **Key Concepts**: Bitrate, modulation, physical medium (cables, switches)

---

### Key Points
- Each layer serves the layer above it and is served by the layer below it.
- Data encapsulation adds headers and trailers as data moves down the layers.
- Data decapsulation removes headers and trailers as data moves up the layers.

---