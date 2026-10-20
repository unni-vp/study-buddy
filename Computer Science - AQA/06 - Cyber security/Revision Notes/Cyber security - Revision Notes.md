# Cyber security

## What cyber security protects

**Cyber security** means protecting computers, networks, programs and data from attacks, damage and unauthorised access.

Think of a school building: locks control entry, staff check visitors, and repairs fix broken doors. Computer security also needs **technology, people and procedures** working together.

Its main purposes are to:

- **Keep information private:** stop someone reading data they should not see.
- **Prevent unwanted changes or damage:** protect files, programs and equipment.
- **Keep systems usable:** help legitimate users access services when needed.

A stolen password can expose private records. Malware may change or destroy files. An attack that stops a school network working can disrupt lessons even if no records are stolen.

Security therefore includes procedures such as checking sensitive requests, people following those procedures, and technical controls such as updates and account permissions. Buying a security product alone does not address every weak point.

## Weak passwords and access rights

### Weak and default passwords

A **weak password** is easy to guess or discover, such as a common word or a person's name. A **default password** is supplied with a device or service; attackers may already know it.

- Use **long, unique passwords** rather than common or reused ones.
- Change default passwords when setting up equipment.
- Keep passwords private and protect accounts that can change system settings.
- Limit repeated login attempts to make automated guessing harder.

Using the same password everywhere creates a link between accounts: one stolen password may unlock several services.

### Misconfigured access rights

**Access rights** control what an account is allowed to read, change or delete. They are **misconfigured** when someone receives inappropriate permissions.

Imagine every pupil receiving a key to the school office. The problem is the permission, even if each key works correctly.

- A pupil may need to read their own marks, but should not be able to change everyone else's.
- Give each account **only the permissions it needs**.
- Review permissions when a person's role changes or they leave.
- Restrict administrator rights because these allow powerful changes.

| Feature | Authentication | Access rights |
|---|---|---|
| Question | Who is trying to use the system? | What is that account allowed to do? |
| Example | Check a pupil’s username and password. | Allow the pupil to read their own marks, but not change everyone else’s. |
| Key distinction | A successful login accepts the claimed identity. | Successful login does not justify unrestricted permissions. |

### Two different account problems

If an attacker guesses a staff password, the problem begins with **authentication**: someone is using another person's identity. If a correctly logged-in pupil can edit all marks, the problem is **access rights**: the account itself has too much permission.

Give each role the minimum access needed for its work. A read-only permission can allow a user to see information without changing it. Remove or revise permissions when a user leaves or changes roles, instead of leaving old access in place.

## Removable media and outdated software

### Removable media

USB drives and other removable storage can carry infected files between devices. A lost drive may also expose the information stored on it.

- Avoid connecting unknown devices.
- Scan files with updated **anti-malware software**.
- Restrict removable-media use where sensitive systems need extra protection.
- Encrypt sensitive stored data so losing the device does not immediately reveal readable files.

### Unpatched and outdated software

A **vulnerability** is a weakness that an attacker could exploit. A **patch** is an update that fixes a problem, which may include a security weakness.

- Delaying updates leaves known weaknesses available to attackers.
- **Automatic updates** reduce the chance that users forget important patches.
- Software that is no longer supported may stop receiving security fixes.

Updating software reduces risk; it does not automatically remove every infection or prevent every future attack.

A drive can create two different risks: it can **bring infected files in**, or it can **take confidential copies out**. Restricting unknown drives reduces the first route. Access controls and policies on copying data help address the second. Encrypting a lost drive protects its contents, but does not make an infected program safe to run.

Patches repair known software weaknesses. Attackers may learn about a weakness after it is published, so delaying the fix leaves a known route open. Automatic updating reduces reliance on each user remembering to install fixes. Unsupported software may need replacement because the developer no longer supplies patches.

## Pharming and fake destinations

**Pharming** redirects a user's website request to a fake website. The user may have typed the correct address but still reach the wrong destination because the system locating or directing the request has been compromised.

It is like replacing a road sign so drivers who chose the right route arrive at a fraudulent shop.

- The fake site may copy the real site's appearance.
- Entered login or payment details may be stolen.
- Updated security software and secure configuration help protect the device and address lookup.
- Browser certificate warnings can reveal a problem; they should not be ignored.

| Feature | Phishing | Pharming |
|---|---|---|
| Mechanism | A fraudulent message tricks the person into revealing information or opening something unsafe. | A website request is redirected to a fraudulent destination. |
| Correctly typed address | The victim may be persuaded to follow a deceptive link instead. | The victim may type the correct address and still be redirected. |
| Possible result | A fake login page steals details. | A fake login page steals details. |
| Suitable response | Verify unexpected messages independently and use a known address or app. | Protect software and address lookup; do not ignore certificate warnings. |


The result may look similar, but explain the **different mechanism** when comparing these attacks.

## Social engineering

**Social engineering** manipulates people into revealing confidential information or taking actions that help an attacker. It targets human trust rather than relying only on a technical weakness.

### Blagging, also called pretexting

An attacker invents a believable situation or identity. For example, a caller pretends to be school IT support and claims they need a password to repair an account.

- **The mechanism:** a false story makes an unusual request seem reasonable.
- **Protection:** check the person's identity using a known contact route, and follow procedures for sensitive requests.
- Pressure or urgency is a reason to check carefully, rather than skip the checks.

### Phishing

A fraudulent email or text impersonates a trusted organisation. It may ask for private information, direct the victim to a fake login page, or encourage them to open a harmful attachment.

- **The mechanism:** the victim trusts the message and reveals data or opens something unsafe.
- **Protection:** check the sender and destination; verify unexpected requests independently.
- Open the service using a known address or app instead of relying on an unexpected message's link.

An email's logo or professional wording does not prove that it is genuine.

### Shouldering, also called shoulder surfing

Someone observes private information directly, such as a PIN being entered, a password on a screen or confidential work in a public place.

- **The mechanism:** information is seen rather than obtained by guessing a password.
- **Protection:** shield the keypad, position screens carefully, and use privacy screens where appropriate.

### Choosing the response that breaks the deception

An urgent request to transfer money should be checked through a previously known contact route. Replying to the suspicious message only asks the possible attacker to confirm their own story.

For shouldering, the attacker may not need to send any message or install software. A person watching a PIN entry can obtain the secret directly, so shielding the keypad and checking the surroundings address that particular method.

Strong passwords do not prevent a photographed or disclosed password being used. The response must address how the information is obtained.

## Malware

**Malware** is malicious software designed to cause harm or perform unwanted actions.

| Type | How it works | Possible consequence |
|---|---|---|
| **Computer virus** | Attaches to a host file or program and copies itself when the infected host is run | Infection spreads; files may be damaged or altered |
| **Trojan** | Pretends to be useful or legitimate software, concealing a malicious purpose | The user installs or runs something that steals data or gives unwanted access |
| **Spyware** | Secretly monitors activity or collects information | Private information, browsing activity or keystrokes may be captured |

**A virus is a type of malware.** The terms are not interchangeable. A trojan's defining feature is its disguise; it does not need to replicate like a virus.

| Measure | How it helps | Important limitation |
|---|---|---|
| Updated **anti-malware** | Scans files and detects or blocks known malicious activity. | It cannot guarantee detection of every threat. |
| Trusted downloads | Reduce the chance of installing disguised malicious programs. | A convincing appearance alone does not prove a download is trustworthy. |
| Software updates | Close vulnerabilities that malware might exploit. | Updating does not automatically remove every infection. |
| Attachment and USB precautions | Reduce routes by which infected files reach the system. | Users still need to follow the procedures. |
| Restricted permissions | Limit what a compromised account or program can change. | They do not make the account immune to compromise. |
| **Backups** | Help recover damaged or lost data. | They do not prevent theft of readable data that has already been exposed. |

A disguised game could be a trojan because it persuades the user to run software with a hidden malicious purpose. If it secretly records keystrokes, that activity is spyware. These descriptions concern different features, so a malicious program can fit more than one description.

A virus needs a host file or program and spreads through infected hosts. Calling every harmful program a virus loses this distinction. Updated scanning, cautious downloads and restricted permissions reduce risk, while a protected backup provides a recovery route if files are damaged.

## Authentication and automated-abuse checks

Think of access to an account as a doorway. Different checks ask different questions: do you know a secret, do you have access to an email account, or do you match a stored physical characteristic?

| Method | What it checks | Strength or limitation |
|---|---|---|
| **Password** | A secret entered by the user. | Simple to use, but weak, reused or disclosed passwords undermine it. |
| **Biometrics** | A physical characteristic, such as a fingerprint or face, against stored information. | Convenient on mobile devices, but recognition can fail and compromised biometric information is difficult to replace. |
| **CAPTCHA** | Whether activity appears to come from a human rather than automation. | Can reduce automated registration or guessing, but does not establish real identity and may create accessibility difficulties. |
| **Email confirmation** | Access to the mailbox receiving a link or code. | An attacker controlling that mailbox may pass the check. |


**Biometrics identify a characteristic, not a permission.** The account still needs suitable access rights after authentication.

### What each check can establish

A fingerprint or face check compares a measured characteristic with enrolled data. It can be convenient for unlocking a mobile device, but recognition may fail and it is difficult to replace a compromised physical characteristic in the way a password can be changed.

A CAPTCHA aims to distinguish automated activity from human activity. It can slow bulk registration or password attempts; passing it does not prove that the person is the account owner.

An email confirmation link or code shows that someone can access the receiving mailbox. It does not independently prove their legal identity. If an attacker already controls that mailbox, the email check may also be defeated.

## Layered protection and penetration testing

### Use measures together

No single measure addresses every threat.

- A strong password is useful against guessing, but can still be disclosed during phishing.
- Training and independent identity checks reduce social-engineering risks.
- Updates and anti-malware reduce technical risks.
- Appropriate access rights limit what an account can do.

Combining measures protects different weak points, like having a lock, a visitor check and a working alarm rather than relying on one door alone.

### Penetration testing

**Penetration testing** is an authorised, controlled attempt to find security weaknesses by testing how an attacker might gain access. Its purpose is to discover problems so they can be fixed.

| Test situation | What the testers know | What it helps reveal |
|---|---|---|
| **Insider simulation** | Some knowledge of the system, and possibly ordinary user credentials | Whether an insider can exceed their intended permissions or exploit internal weaknesses |
| **External simulation** | No prior knowledge of access credentials | How someone outside the system might gain unauthorised access |

A test report identifies weaknesses, their consequences and recommended fixes. The organisation should **correct the weaknesses and retest**. Testing finds problems; it does not itself repair them.

### Detection, prevention and recovery

| Job | Example | Why the distinction matters |
|---|---|---|
| Prevention | Installing a patch closes a known vulnerability. | This reduces an attack route before it is exploited. |
| Detection | Anti-malware identifies a suspicious file. | Finding a threat allows action, but detection alone is not the same as preventing every infection. |
| Recovery | A protected backup restores damaged records. | Restoring files does not undo confidential data already stolen. |

An insider-style test can explore what an ordinary account can reach beyond its intended permissions. An external-style test starts without credentials and investigates access from outside. Both need agreed authorisation and scope.

## Applying a security explanation

### A fake IT-support call

**Threat:** blagging. The caller invents an identity to obtain a staff password.

**Suitable response:** verify the request by contacting IT using the school's known number. This breaks the attack's reliance on trusting the caller's story. A firewall alone would not stop a staff member voluntarily revealing their password.

### A pupil can change other pupils' marks

**Threat:** misconfigured access rights. The account has permission to change records it should not control.

**Suitable response:** change the account's permissions to match the pupil's role. Making the password stronger would not remove the excessive permission.

**A strong explanation connects the threat, the measure and the reason it reduces that particular risk.**

## Sources

- [PMT Education: original Summary Notes](../Reference Materials/PMT - Summary Notes.pdf). Unmodified source retained with its printed attribution and licence.
- [AQA specification for first exams in 2027](../../00 - Specification/AQA-8525-specification-2027.pdf).
