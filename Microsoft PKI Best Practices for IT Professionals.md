---
title: Microsoft PKI Best Practices
layout: article
permalink: /pkibestpractices
sidebar:
  nav: header
---

## 1. **Planning and Designing**:
   Microsoft emphasizes the importance of planning and designing in implementing a PKI. Proper planning can prevent many issues that might arise during the implementation phase ([source](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/designing-and-implementing-a-pki-part-i-design-and-planning/ba-p/259730)).

## 2. **Avoiding AD CS for PKI in Cloud Migration Context**:
   - Active Directory Certificate Services (AD CS) is a server role by Microsoft that allows administrators to build a PKI and roll out certificates.
   - However, AD CS requires an on-premise server, which is not ideal for organizations looking to migrate their networks to the cloud.
   - Implementing a PKI with AD CS can be expensive as it requires a team of trained PKI experts, hardware, software, and licensing fees ([source](https://www.securew2.com/solutions/managed-pki-service/)).

## 3. **Choosing a Managed PKI Solution**:
   - A managed PKI service can be set up in a few hours at a fraction of the cost of on-prem PKIs, shifting the workload away from IT administrators.
   - Managed PKI solutions like SecureW2’s cloud-based Managed PKI can be a better choice due to their ease of implementation and cost-effectiveness ([source](https://www.securew2.com/solutions/managed-pki-service/)).

## 4. **Using 802.1X EAP-TLS Authentication**:
   - 802.1X is a network protocol for user authentication which is crucial for secure network access.
   - It's advisable to use certificate-based EAP-TLS authentication as it eliminates over-the-air credential theft. Unlike credential-based protocols like EAP-TTLS/PAP or PEAP-MSCHAPv2, EAP-TLS is much more secure as it relies on certificates for authentication ([source](https://www.securew2.com/solutions/managed-pki-service/)).

## 5. **Configuring a Cloud RADIUS Server**:
   - A Cloud RADIUS server can strengthen 802.1X EAP-TLS authentication by leveraging a Dynamic Policy Engine that can directly reference any cloud identity provider, including Microsoft Azure.
   - This setup allows for real-time referencing of directory entries to check authorization and other attached information, providing a more dynamic and secure authentication mechanism ([source](https://www.securew2.com/solutions/managed-pki-service/)).

## 6. **Deep Dive into PKI and Active Directory Certificate Services (ADCS)**:
   PKI Solutions LLC offers a course that focuses on building knowledge and skills on PKI and ADCS, emphasizing security and best practices. This course could be beneficial for IT professionals looking to deepen their understanding of Microsoft PKI and its features ([source](https://platform.pkisolutions.com/courses/microsoft-pki-in-depth)).

## 7. **Step-by-Step Guide on PKI Hierarchy Deployment**:
   There is a guide on deploying a Two Tier PKI Hierarchy, which provides best practice information for implementing a Microsoft Windows Server 2003 Public Key Infrastructure ([source](https://social.technet.microsoft.com/wiki/contents/articles/15037.ad-cs-step-by-step-guide-two-tier-pki-hierarchy-deployment.aspx)).
