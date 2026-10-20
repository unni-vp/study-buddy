# Fundamentals of computer networks

## Networks, benefits and risks

A **computer network** is two or more computers or devices connected so they can communicate and share resources.

Think of a network as a transport system: devices are destinations, links are roads and protocols are agreed traffic rules.

| Aspect | Benefit | Possible disadvantage |
|---|---|---|
| Shared resources | Users can share files, printers and an internet connection. | Setup, equipment and maintenance cost money. |
| Communication | Users can collaborate and access shared services from different devices. | Congestion can reduce performance. |
| Central management | Accounts, updates and backups can be managed centrally. | Users may depend on network equipment and services remaining available. |
| Connected devices | Information is easier to exchange. | Malware or faults can spread; security and privacy need protection. |

### Linking the benefit to the reason

A shared printer can serve several computers, so an organisation may need fewer printers. Shared files let users work from a common version rather than repeatedly exchange separate copies. Central administration lets an administrator install updates or manage accounts across many computers.

These services create dependencies. If a file server becomes unavailable, users may temporarily lose access to shared documents even though their own computers still work. This is not necessarily permanent file loss; recovery depends on the fault and the backups.

Networks also need equipment, installation, maintenance and trained administration. A useful evaluation balances those costs against the number of users and the services they need.

## PAN, LAN and WAN

| Type | Scale and ownership | Example |
|---|---|---|
| PAN | Very short range around one person; Bluetooth is required here | Phone connected to wireless earbuds |
| LAN | Small geographical area, often owned and managed by one person or organisation | School or home network |
| WAN | Wide geographical area, often using third-party infrastructure and distributed ownership | The Internet |

Classify a network using **geographical scale**, how devices connect and who owns or manages the infrastructure.

**PAN** means Personal Area Network. A phone communicating with a smartwatch by Bluetooth is a PAN around one person. It does not become a WAN simply because the phone can also access the internet.

**LAN** means Local Area Network. A school's computers, shared printers and local servers can form a LAN controlled by that school. A LAN can contain many devices; “local” describes its geographical area, not a fixed maximum number of computers.

**WAN** means Wide Area Network. A business may connect offices in different cities using communication links provided by other organisations. The internet connects networks worldwide and has distributed ownership.

Scale and management identify these categories. Speed alone cannot reliably distinguish them: performance depends on the actual links and equipment.

## Wired and wireless networks

| Feature | Wired network | Wireless network |
|---|---|---|
| Connection | A cable connects each device. | Radio signals connect devices without a cable to each one. |
| Mobility | Movement is restricted by cables. | Users can move around within coverage. |
| Installation | Cabling can cost money and disrupt a building. | Convenient where cables are difficult; mobile devices are easier to add. |
| Performance | Usually stable, with low latency and less radio interference. | Distance, obstacles, interference and congestion can reduce signal quality. |
| Security | Physical access makes interception harder, but a cable does not guarantee security. | Signals may extend beyond a building, so authentication and encryption are important. |
| Suitable use | Fixed devices needing a stable connection. | Phones and tablets needing mobility. |


### Copper and fibre-optic cable

| Feature | Copper cable | Fibre-optic cable |
|---|---|---|
| Signal | Carries electrical signals. | Carries light. |
| Suitable use | Common, relatively inexpensive shorter links. | High-bandwidth links over long distances. |
| Trade-off | Can be affected by electromagnetic interference. | Resists electromagnetic interference, but installation can cost more. |


Choose a connection for the stated situation. Do not assume one option is always faster or more secure in every installation.

### Making a justified connection choice

A fixed desktop used for large transfers may benefit from a stable wired connection. A tablet carried around a classroom needs mobility, so wireless access is more practical. Wireless performance can fall when walls weaken the signal or many nearby devices compete for access.

Copper carries electrical signals and is often economical for shorter connections within a building. Fibre carries light, supports high bandwidth over longer distances and resists electromagnetic interference. Fibre installation and the equipment at its ends may cost more.

Neither connection automatically makes transmitted information private. Wired access can still be compromised, and wireless signals may be received outside the intended room. Authentication and encryption address risks that a speed comparison alone does not cover.

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

### TCP and IP

| Feature | TCP | IP |
|---|---|---|
| Main job | Manages reliable end-to-end communication, including ordering data and detecting missing data. | Addresses and routes packets between networks. |
| TCP/IP layer | **Transport**. | **Internet**. |
| How they work together | Helps the destination reconstruct the correct data stream. | Gets addressed packets towards the destination. |


### HTTP and HTTPS

| Feature | HTTP | HTTPS |
|---|---|---|
| Use | Transfers web pages and related web data. | Performs web communication using an encrypted connection. |
| Data in transit | Does not itself encrypt the connection. | Protects transmitted data against being read by an interceptor. |
| Authentication | Does not itself authenticate the server through a certificate. | Uses certificates to help authenticate the server connection. |


Do not write that HTTPS makes a website completely safe. It protects data in transit and helps authenticate the connection; the site or user's device could still be harmful or compromised.

### SMTP and IMAP

| Feature | SMTP | IMAP |
|---|---|---|
| Main job | **Sends email.** | **Accesses and manages email stored on a server.** |
| Communication | Client to outgoing mail server, and between mail servers. | An email client communicates with the server holding the mailbox. |
| Example action | Send a new message to somebody else. | Read a message or synchronise folders and read/unread status across devices. |
| What to distinguish | Sending a message does not replace mailbox access. | Reading or organising a mailbox is different from sending a message. |

### Following an email

1. A sender's email application submits an outgoing message using **SMTP**.
2. Mail servers use **SMTP** to pass the message towards the recipient's mail server.
3. The recipient's application uses **IMAP** to access the stored mailbox and manage messages.
4. Server-held folders and read/unread status can then be reflected on the recipient's other devices.

SMTP and IMAP are not alternative names for the same step. One handles sending; the other handles access to the mailbox.

### Reliable delivery and addressing

**IP** identifies destinations and supports routing packets between networks. Different packets may travel by different routes. IP alone does not guarantee that all data arrives in order.

**TCP** manages reliable end-to-end communication. It supports sequencing, detects missing data and arranges retransmission where necessary, helping the receiver reconstruct the data correctly. A destination address answers “where?”, while reliable delivery answers “has the complete data arrived correctly?”.

An **HTTPS** connection protects web data while it travels and helps authenticate the server connection. That matters when submitting login or payment details. It does not prove that every claim on a website is truthful or that a downloaded file is harmless.

## Why network security matters

Network security protects systems and data from unauthorised access, alteration, damage and disruption. A strong design uses several controls because each deals with different risks.

Possible consequences of weak security include data theft, changed files, unavailable services, financial loss and damage to reputation.

## Authentication and encryption

| Feature | Authentication | Encryption |
|---|---|---|
| Purpose | Checks identity before access is granted. | Makes data unreadable without the appropriate key. |
| Example | Check a username/password or another identity factor. | Transform plaintext into ciphertext before transmission. |
| Limitation | Checking identity does not itself hide intercepted traffic. | An authorised recipient still needs the required key; encryption does not decide account permissions. |


Authentication controls who enters. Encryption protects data if traffic is intercepted. They work together but solve different problems.

### Protecting a school record system

Authentication asks the user to prove their claimed identity before access is accepted. For example, a username identifies an account and a password provides a secret associated with that account. A further factor, such as access to an authenticator device, can add protection if a password is stolen.

Encryption transforms readable **plaintext** into **ciphertext** using a key. The intended recipient uses the appropriate decryption process and key to recover readable data. It protects the contents of intercepted communication rather than preventing interception itself.

A user can pass authentication and still have permission only to read their own record. Identity checking, data encryption and access permissions have related but distinct jobs.

## Firewalls and MAC address filtering

| Feature | Firewall | MAC address filtering |
|---|---|---|
| What is checked? | Incoming and outgoing network traffic. | The physical address associated with a device’s network adapter. |
| Decision | Allows or blocks traffic using defined security rules. | Allows or blocks devices using their MAC addresses. |
| Limitation | Incorrect rules may block legitimate traffic or allow threats. | Addresses can be copied or spoofed, so this should not be the only defence. |


Use **layered security**: authentication, encryption, firewall rules and device controls support one another.

**MAC** means Media Access Control. A network adapter has a physical address that a filtering rule can compare with an allow list or block list. For example, a school can restrict a network to the addresses registered for its managed devices.

A copied or spoofed address can weaken this control, so MAC filtering should not replace authentication and encryption. It also does not prove which person is currently using an allowed device.

A firewall can allow the traffic needed for a school website while blocking traffic that breaks its configured rules. It monitors incoming and outgoing traffic; it does not simply reject every connection. A badly chosen rule may block legitimate work or allow an unwanted connection.

Together, identity checks restrict account access, encryption protects data in transit, firewall rules filter traffic, and MAC filtering controls permitted adapters. Each contributes a different part of the defence.

## The four-layer TCP/IP model

Layering divides networking into manageable jobs. Each layer provides services to the layer above and uses the layer below.

| Layer | Main job | Named protocols/components |
|---|---|---|
| Application | Network applications and user-facing services | HTTP, HTTPS, SMTP, IMAP; browsers and email programs |
| Transport | Sets up end-to-end communication and agrees details such as packet size | TCP |
| Internet | Addresses, packages and routes packets across networks | IP |
| Link | Works with local network hardware and transmission | NIC and operating-system device drivers |

When data is sent, each layer adds information needed for its job. At the destination, layers process and remove the relevant information. This separation makes protocols easier to develop and replace without redesigning the whole system.

### Why separate the jobs?

Think of sending a parcel: writing its contents, preparing its delivery, choosing a route and physically moving it are separate responsibilities. The networking layers similarly let specialists change one part without redesigning every application.

On the sender, application data passes **down** through transport, internet and link processing. On the receiver, the corresponding processing happens **upwards** until the data reaches the application. Each layer uses the services below it and offers a service to the layer above.

The link layer deals with the local connection and its hardware. The internet layer deals with addressing and routing between networks. Keeping those roles separate explains why changing the local connection does not require rewriting the email application's rules.

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

- [PMT Education: original Summary Notes](../Reference Materials/PMT - Summary Notes.pdf). Unmodified source retained with its printed attribution and licence.
- [AQA specification for first exams in 2027](../../00 - Specification/AQA-8525-specification-2027.pdf).
