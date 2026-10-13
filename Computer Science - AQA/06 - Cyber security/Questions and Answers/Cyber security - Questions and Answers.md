# Cyber security questions & answers

## 1 mark

**1.** Which kind of malware pretends to be useful software?

**Answer:** Trojan.

**2.** Which kind of malware secretly monitors activity such as keystrokes?

**Answer:** Spyware.

**3.** Which kind of malware attaches to files or programs and copies itself when they run?

**Answer:** Virus.

**4.** Name the attack in which a genuine-looking message asks somebody to reveal a password.

**Answer:** Phishing.

**5.** Name the attack that redirects somebody towards a fake website even after they try to visit the correct address.

**Answer:** Pharming.

**6.** What is the main purpose of a CAPTCHA?

**Answer:** To distinguish likely human users from automated programs.

**7.** Name a biometric feature that a phone could use to authenticate its user.

**Answer:** Fingerprint.

**8.** What do access rights control?

**Answer:** Which data and actions a user is authorised to access.

## 2 marks

**9.** Explain what cyber security protects against.

**Answer:**

- It protects **systems, networks and data**.
- It aims to prevent unauthorised access, attacks, damage and disruption.

**10.** Explain why keeping a router's default password creates a risk.

**Answer:**

- The default password may be widely known or easy to find.
- An attacker could use it to access the settings and change the network's configuration.

**11.** Explain how a weak password could expose a private account.

**Answer:**

- A common or predictable password is easier to guess.
- Successful guessing lets the attacker authenticate as the account holder.

**12.** An ordinary employee can delete payroll records. Explain the security problem.

**Answer:**

- Their **access rights are too broad** for the job.
- They could accidentally or deliberately delete sensitive records that they should not be allowed to change.

**13.** Explain the difference between authentication and access rights.

**Answer:**

- **Authentication** checks the identity a user claims.
- **Access rights** determine what that authenticated user may do.

**14.** Give two reasons automatic security updates can be more effective than relying on users to update manually.

**Answer:**

- Updates are less likely to be forgotten.
- Patches can be installed sooner, reducing the time known vulnerabilities remain available to attackers.

**15.** Explain why a copied fingerprint image is not a password reset.

**Answer:**

- A biometric check compares a physical feature with a registered reference.
- A password reset changes a secret credential; it does not change the person's actual fingerprint.

**16.** Explain how checking an email confirmation link can help with account registration.

**Answer:**

- Sending a unique link to the claimed address checks whether the registrant can access that mailbox.
- It reduces registrations using addresses the person does not control, but does not prove their legal identity.

**17.** What is penetration testing?

**Answer:**

- It is an **authorised attempt to find or exploit security weaknesses**.
- Findings are reported so the organisation can improve its defences.

**18.** Explain why malware scanning alone does not stop all social engineering.

**Answer:**

- A person may be persuaded to reveal genuine credentials without downloading malware.
- Staff awareness and verification procedures are also needed to resist the deception.

## 3 marks

**19.** A visitor claims to be an IT technician and asks for a staff password. Identify and explain the threat, and one appropriate response.

**Answer:**

- This is **blagging**: inventing an identity or story to gain trust.
- The visitor could use the password to gain access as the staff member.
- Verify the request through a known official contact and do not disclose the password.

**20.** A passenger watches somebody unlock a phone and later steals it. Explain the attack and a suitable precaution.

**Answer:**

- Watching the PIN is **shouldering**.
- Knowing the PIN may let the thief unlock the stolen device.
- Shield the keypad or use an appropriate biometric lock so the secret is not visible during entry.

**21.** Explain how an unknown USB drive could put an office computer at risk.

**Answer:**

- It may contain malware.
- Opening an infected file or running a disguised program can execute that malware.
- The malware could steal data, damage files or spread to other computers.

**22.** Explain how a phishing message could compromise a school account.

**Answer:**

- The message impersonates a trusted sender and prompts the pupil to visit a fake login page.
- The pupil enters credentials that the attacker records.
- The attacker then uses them to access the real account.

**23.** Explain why a pharming attack can be harder to spot than a visibly suspicious message.

**Answer:**

- The user may type a genuine address.
- Altered name-resolution information redirects the request to the attacker's site.
- The destination may copy the real site's appearance, so the user can disclose details despite initially choosing the right address.

**24.** A company wants to test the risk from a malicious employee. Explain a suitable penetration-testing scenario.

**Answer:**

- Give the authorised tester an agreed level of internal access, such as a normal staff account.
- Test whether they can reach or alter resources beyond those permissions.
- Report weaknesses so the company can restrict access and correct the configuration.

**25.** A company wants to test attacks by somebody with no account. Explain a suitable penetration-testing scenario.

**Answer:**

- Start the authorised tester outside the organisation with no internal account.
- Attempt to identify exposed weaknesses within the agreed testing scope.
- Report any route to unauthorised access so it can be fixed.

## 4 marks

**26.** Compare viruses and trojans.

**Answer:**

- A **virus** attaches to files or programs and can make copies when the infected code runs.
- A **trojan** disguises malicious software as something useful or legitimate.
- A virus spreads by infecting other files; a trojan depends on being accepted or run and need not copy itself.
- Both can cause harm such as damaging files or allowing information theft.

**27.** Evaluate using a fingerprint instead of only a password on a staff phone.

**Answer:**

- It can be convenient because the user need not remember or type a secret.
- It reduces the opportunity to watch a password being entered.
- Recognition can fail, for example if the finger is damaged, so a secure fallback is needed.
- A compromised biometric cannot be changed as easily as a password; suitable protection of the registered data still matters.

**28.** A school installs CAPTCHA on its sign-up page. Explain its benefit and two limitations.

**Answer:**

- It can reduce **automated bulk registrations**, lowering spam and server load.
- It does not establish which real person is completing the challenge.
- It does not prevent a genuine user from choosing a weak password or falling for phishing.
- Difficult challenges can also hinder legitimate users, so accessible alternatives are needed.

## 6 marks

**29.** A small business has outdated software, shared passwords and excessive access rights. Explain a suitable layered defence.

**Answer:**

- Install security patches promptly, preferably using managed automatic updates, so known software weaknesses are closed.
- Replace shared credentials with individual accounts and strong passwords. This reduces guessing and makes access easier to manage.
- Give each user only the permissions needed, limiting the damage from a compromised account.
- Train staff to verify unexpected requests so attackers cannot simply persuade them to disclose credentials.
- Use suitable malware detection and controls on removable media to reduce malicious execution.
- Test the measures through authorised penetration testing. Different controls address different routes of attack.

## 9 marks

**30.** A design company stores confidential client files. Staff use predictable passwords, all accounts can edit every project, and software updates are often postponed. Discuss how attackers could exploit these weaknesses and how the company should respond.

**Answer:**

Predictable passwords could be guessed, giving an attacker a genuine staff login. Because every account can edit all projects, one compromised account could expose or damage far more client work than the staff member needs. Postponed updates leave known software vulnerabilities open, potentially giving an attacker another route into the system.

The company should use individual accounts with strong passwords and an additional suitable identity check for sensitive access. It should restrict permissions by role so a stolen account has a smaller reach, and apply security updates promptly. Staff should verify unusual requests and report suspicious activity; technical controls alone do not remove deception. Authorised testing should cover both an external attacker and misuse of an internal account.

The priority is to combine these measures. Fixing only passwords would leave broad permissions and software weaknesses in place. Regular review is needed as staff roles and threats change.

## Past-paper sources

These are original practice questions and tutor answers. Question types were checked against AQA Paper 2 from June 2022 and June 2023 and the revised course content. The marks are practice allocations. No frequency ranking is claimed from this two-paper sample.

- [June 2022 question paper](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN22.PDF)

- [June 2022 mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN22.PDF)

- [June 2023 question paper](../../00%20-%20Past%20papers/Paper%202/AQA-85252-QP-JUN23.PDF)

- [June 2023 mark scheme](../../00%20-%20Past%20papers/Paper%202/AQA-85252-MS-JUN23.PDF)

- [Official AQA assessment resource directory](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/assessment-resources)
