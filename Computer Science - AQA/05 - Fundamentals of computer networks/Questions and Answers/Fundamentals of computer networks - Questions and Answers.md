# Fundamentals of computer networks questions & answers

## 1 mark

**1.** Define a computer network.

**Answer:** Two or more computers or devices connected so they can communicate and share resources.

**2.** Which network type uses Bluetooth in this specification?

**Answer:** Personal Area Network (PAN).

**3.** Which protocol is used to send email?

**Answer:** SMTP.

**4.** Which protocol addresses and routes packets?

**Answer:** IP.

**5.** At which TCP/IP layer does TCP operate?

**Answer:** Transport layer.

**6.** Which cable type carries data as light?

**Answer:** Fibre-optic cable.

## 2 marks

**7.** Give two advantages of networking computers in a school.

**Answer:** Any two of sharing files/printers, central accounts, communication, central backups, shared internet access or central software management.

**8.** Explain the difference between a LAN and a WAN.

**Answer:**

- A LAN covers a relatively small area and is usually managed by one organisation.
- A WAN covers a wide area and often uses infrastructure under distributed ownership.

**9.** Explain the difference between HTTP and HTTPS.

**Answer:**

- Both transfer web data.
- HTTPS encrypts the connection and supports authentication, making data in transit more secure.

**10.** Explain the difference between SMTP and IMAP.

**Answer:**

- SMTP sends email to a mail server or between servers.
- IMAP accesses and manages email stored on a server.

**11.** Give one advantage and one disadvantage of a wireless network.

**Answer:**

- It supports mobility and avoids a cable to each device.
- It may suffer interference, reduced range/performance or greater interception risk.

**12.** Explain why authentication and encryption are both useful.

**Answer:**

- Authentication checks the identity of someone requesting access.
- Encryption makes intercepted data unreadable without the required key.

## 3 marks

**13.** Explain why fibre-optic cable may be chosen for a long, high-traffic network link.

**Answer:**

- Fibre supports high bandwidth.
- It can carry signals over long distances.
- It is not affected by electromagnetic interference in the way copper can be.

**14.** Describe what a firewall does.

**Answer:**

- It monitors incoming and outgoing network traffic.
- It compares traffic with defined security rules.
- It allows or blocks traffic according to those rules.

**15.** Explain how MAC address filtering controls network access and give one limitation.

**Answer:**

- It compares a device's network-adapter address with an allow/block list.
- The network permits or rejects the device based on the rule.
- A MAC address can be copied or spoofed, so filtering should not be used alone.

**16.** State the job of the application, transport and internet layers.

**Answer:**

- Application: provides services used by network applications.
- Transport: sets up end-to-end communication and manages packet delivery.
- Internet: addresses and routes packets across networks.

**17.** Explain why protocols are needed.

**Answer:**

- Devices may use different hardware and software.
- Protocols provide agreed rules for formatting, addressing and transmitting data.
- Following the same rules allows devices to understand one another.

**18.** Give three disadvantages of computer networks.

**Answer:** Any three of setup/maintenance cost, dependence on shared services, security risk, malware spread, congestion, privacy concerns or need for skilled administration.

## 4 marks

**19.** Compare wired and wireless connections for classroom computers.

**Answer:**

- Wired links are normally stable, low latency and less affected by radio interference.
- They restrict device location and require cable installation.
- Wireless links support mobile devices and are easier to extend.
- Wireless performance can fall because of distance, obstacles, interference and congestion, and strong security is required.

**20.** Describe how the four TCP/IP layers take part when a browser requests a web page.

**Answer:**

- The application layer creates an HTTP or HTTPS request.
- TCP at the transport layer manages the end-to-end communication.
- IP at the internet layer adds addressing and routes packets.
- The link layer transmits data using the local NIC and network hardware.

**21.** Explain how several network-security methods work together.

**Answer:**

- Authentication limits access to recognised users.
- Encryption protects data if traffic is intercepted.
- A firewall blocks traffic that breaks defined rules.
- MAC filtering can restrict devices, so the combined controls cover identity, data, connections and hardware access.

**22.** A business has offices in two cities. Explain why its internal city-office networks are LANs while the connection between cities forms part of a WAN.

**Answer:**

- Each office LAN covers a relatively small local area.
- Each LAN can be owned and managed by the business.
- The inter-city connection spans a wide geographical area.
- It is likely to use telecommunications infrastructure owned or managed by other organisations.

## 6 marks

**23.** A school is deciding whether student laptops should use wired or wireless networking. Evaluate the options.

**Answer:**

- Wireless allows students to move devices and connect without a cable at every desk.
- It is easier to add laptops and supports flexible classroom layouts.
- Signal quality may fall through walls or when many devices share an access point.
- Wireless traffic needs strong authentication and encryption because signals extend beyond the room.
- Wired links usually provide stable performance and low latency but restrict movement and cost more to install at every seat.
- A mixed design is sensible: wireless for student mobility and wired connections for access points, servers and fixed high-demand devices.

**24.** Explain how protocols and layers allow an email message to travel across different networks.

**Answer:**

- The email application uses SMTP at the application layer to send the message.
- TCP at the transport layer establishes communication and supports reliable delivery.
- IP at the internet layer addresses and routes packets across interconnected networks.
- The link layer uses the current local network hardware to transmit each packet.
- Routers can forward IP packets across different link technologies.
- At the destination, the layers process the data in reverse, and IMAP may later let the recipient access server-held mail.

**25.** A college links two buildings, equips fixed desktop rooms and provides access for students carrying laptops. Recommend suitable connection types for these three uses. Explain your choices, including installation, mobility and performance limitations.

**Answer:**

**Between buildings:** fibre can provide high-capacity links over longer distances and is not affected by electrical interference in the way copper can be. Installation and suitable equipment cost more, so the choice should reflect the distance and required capacity.

**Fixed desktops:** copper Ethernet is practical where desks are near the network equipment. It gives a stable connection without sharing a radio channel, but each position needs cable installation and movement is restricted.

**Student laptops:** wireless access supports movement and avoids a cable at every seat. Coverage, walls, interference and the number of simultaneous users affect performance, so access-point placement and capacity must be planned.

A **mixed network** matches the connection to its job. No connection guarantees the same speed in every installation.

**26.** A school uses a wireless network for staff devices. Explain how authentication, encryption, a firewall and MAC address filtering protect different aspects of access. Give limitations and explain why using only one control would be inadequate.

**Answer:**

- **Authentication** checks a user's claimed identity before allowing access. A stolen password can still let an attacker impersonate that user.
- **Encryption** makes intercepted traffic unreadable without the appropriate key. It does not stop an authorised user from mishandling information or make a deceptive website trustworthy.
- A **firewall** monitors incoming and outgoing traffic and applies rules to permit or block it. Its protection depends on suitable rules; permitted traffic can still contain a threat.
- **MAC filtering** permits or blocks devices using their network-adapter addresses. An address can be copied, so this is not reliable proof of a user's identity.

Together, the controls cover **identity, transmitted information, network traffic and devices**. For example, encryption protects an intercepted message even though it cannot decide whether the user should have logged in. The different controls reduce different risks; none removes the need for the others.

**27.** A student accesses a school web page and sends an email that a teacher later reads on two devices. Explain the purposes of HTTP, HTTPS, TCP, IP, SMTP and IMAP in these activities. Distinguish the two web protocols and the two email protocols.

**Answer:**

| Protocol | Purpose in these activities |
|---|---|
| HTTP | Transfers web requests and responses between browser and web server |
| HTTPS | Provides a protected, encrypted version of web communication, suitable for login and personal information |
| TCP | Sets up end-to-end communication and supports reliable, ordered delivery of data |
| IP | Provides addressing and routing so packets can cross interconnected networks |
| SMTP | Sends email from a client to a server and between mail servers |
| IMAP | Lets the teacher access server-held email and synchronise its state across devices |

**HTTPS adds protection to web communication**; HTTP alone does not encrypt it. **SMTP sends email; IMAP accesses and manages stored email**. They are not interchangeable names for the same job.

## 7 marks

**28.** A student's headphones connect to a phone using Bluetooth. Their laptop connects to the college network, which links a second campus in another city. Classify these three networks as PAN, LAN or WAN, with reasons. Then explain the four TCP/IP layers involved when the laptop requests an HTTPS web page.

**Answer:**

- **PAN:** the Bluetooth phone–headphones link serves one person's nearby devices.
- **LAN:** the local campus network covers a relatively small area and is managed by the college.
- **WAN:** the inter-city connection spans a wide area, normally using telecommunications infrastructure beyond a single local network.
- **Application layer:** the browser uses HTTPS to request the page using protected web communication.
- **Transport layer:** TCP sets up and manages communication between the hosts, supporting reliable delivery.
- **Internet layer:** IP addresses and routes the packets towards the destination network.
- **Link layer:** the network interface and local network hardware transmit data across the current link; drivers support this hardware access.

The **network type describes its scope**; a **protocol layer describes a communication role**. PAN, LAN and WAN are not extra layers of the TCP/IP model.

## Past-paper sources

Original practice questions and tutor answers. Longer questions use tutor practice mark allocations, with independent checks against the current specification. They are not official marked questions or a prediction of future paper structure.

- [Current specification](../../00%20-%20Specification/AQA-8525-specification-2027.pdf)
- [AQA assessment resources](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/assessment-resources)
- [June 2022 Paper 2](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN22.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN22.PDF)
- [June 2023 Paper 2](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN23.PDF) and [mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN23.PDF)

The added 6–7 mark tasks are original consolidation and application practice. Mark values are tutor allocations rather than evidence that every topic has that exact mark value in official papers. Extended explanations need connected reasoning and, where requested, a justified judgement; a list of isolated words is insufficient.
