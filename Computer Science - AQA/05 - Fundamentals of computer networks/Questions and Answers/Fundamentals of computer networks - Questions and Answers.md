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
