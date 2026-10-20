# Fundamentals of computer networks

## Networks, benefits and risks

A **computer network** is two or more computers or devices connected so they can communicate and share resources.

Think of a network as a transport system: devices are destinations, links are roads and protocols are agreed traffic rules.

Advantages include:

- sharing files, printers and internet connections
- communication and collaboration
- central user accounts, updates and backups
- access to shared services from different devices

Disadvantages include:

- setup and maintenance cost
- dependence on network equipment and services
- security and privacy risks
- malware or faults spreading between connected devices
- congestion reducing performance

## PAN, LAN and WAN

| Type | Scale and ownership | Example |
|---|---|---|
| PAN | Very short range around one person; Bluetooth is required here | Phone connected to wireless earbuds |
| LAN | Small geographical area, often owned and managed by one person or organisation | School or home network |
| WAN | Wide geographical area, often using third-party infrastructure and distributed ownership | The Internet |

Classify a network using **geographical scale**, how devices connect and who owns or manages the infrastructure.

## Wired and wireless networks

### Wired

- Usually stable, low latency and less affected by radio interference.
- Physical access makes interception harder, although it is not automatically secure.
- Devices are restricted by cables and installation can be disruptive.
- **Copper cable** is common and relatively inexpensive for shorter links.
- **Fibre-optic cable** carries light, supports high bandwidth and long distances, and resists electromagnetic interference, but can cost more to install.

### Wireless

- Supports mobility and is convenient where cables are difficult.
- Easier to add mobile devices.
- Signal quality may fall with distance, obstacles, interference or congestion.
- Signals can extend beyond a building, increasing the need for authentication and encryption.

Choose a connection for the situation: fixed high-demand devices may benefit from wired links, while phones and tablets need wireless mobility.

## Protocols

A **network protocol** is an agreed set of rules for communication. Both ends must agree how data is formatted, addressed, sent and received.

| Protocol | Full name | Purpose |
|---|---|---|
| TCP | Transmission Control Protocol | Sets up reliable communication, divides data into packets and supports checking/reassembly |
| IP | Internet Protocol | Addresses and routes packets between networks |
| HTTP | Hypertext Transfer Protocol | Transfers web pages and related web data |
| HTTPS | Hypertext Transfer Protocol Secure | Encrypted, authenticated version of HTTP for more secure web communication |
| SMTP | Simple Mail Transfer Protocol | Sends email from a client to a server and between mail servers |
| IMAP | Internet Message Access Protocol | Accesses and manages email kept on a mail server, synchronising folders and status |

Do not write that HTTPS makes a website completely safe. It protects data in transit and helps authenticate the connection; the site or user's device could still be harmful or compromised.

## Why network security matters

Network security protects systems and data from unauthorised access, alteration, damage and disruption. A strong design uses several controls because each deals with different risks.

Possible consequences of weak security include data theft, changed files, unavailable services, financial loss and damage to reputation.

## Authentication and encryption

- **Authentication** checks identity before granting access, for example username/password or another factor.
- **Encryption** transforms readable plaintext into ciphertext using a key. An authorised recipient uses the required key to recover the plaintext.

Authentication controls who enters. Encryption protects data if traffic is intercepted. They work together but solve different problems.

## Firewalls and MAC address filtering

A **firewall** monitors incoming and outgoing traffic and allows or blocks it using security rules. It can reduce unwanted connections, but incorrect rules may block legitimate traffic or allow threats.

**MAC address filtering** allows or blocks a device using the physical address associated with its network adapter. It can restrict known devices, but addresses may be copied or spoofed, so it should not be the only defence.

Use layered security: authentication, encryption, firewall rules and device controls support one another.

## The four-layer TCP/IP model

Layering divides networking into manageable jobs. Each layer provides services to the layer above and uses the layer below.

| Layer | Main job | Named protocols/components |
|---|---|---|
| Application | Network applications and user-facing services | HTTP, HTTPS, SMTP, IMAP; browsers and email programs |
| Transport | Sets up end-to-end communication and agrees details such as packet size | TCP |
| Internet | Addresses, packages and routes packets across networks | IP |
| Link | Works with local network hardware and transmission | NIC and operating-system device drivers |

When data is sent, each layer adds information needed for its job. At the destination, layers process and remove the relevant information. This separation makes protocols easier to develop and replace without redesigning the whole system.

## Following a web request

1. At the application layer, the browser creates an HTTP or HTTPS request.
2. TCP at the transport layer manages the connection and packet delivery.
3. IP at the internet layer adds addressing and routes packets.
4. The link layer sends data using the local network hardware.
5. The destination processes the layers in reverse to deliver the request to the web service.

Packets may take different routes. TCP helps the receiving host detect missing data and put received data into the correct order.

## Comparison checklist

- Link each advantage or disadvantage to the stated user and task.
- For PAN/LAN/WAN, mention scale and management, not speed alone.
- Distinguish sending email with SMTP from accessing server-held email with IMAP.
- Distinguish identity checking from protecting intercepted data.
- Name the TCP/IP layer and then state its job.

## Sources

- AQA GCSE Computer Science 8525 specification, section 3.5.
