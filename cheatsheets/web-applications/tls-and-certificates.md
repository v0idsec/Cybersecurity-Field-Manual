# TLS and Certificates

## Overview

TLS (Transport Layer Security) is a cryptographic protocol designed to protect communications over a network.

It is commonly used to secure:

- HTTPS
- Email transport
- VPN connections
- APIs
- Other application protocols

TLS provides:

- Confidentiality
- Integrity
- Authentication

## SSL vs TLS

SSL (Secure Sockets Layer) is the predecessor to TLS.

SSL versions are obsolete and insecure.

Modern systems should use TLS.

| Protocol | Status |
|---|---|
| SSL 2.0 | Obsolete |
| SSL 3.0 | Obsolete |
| TLS 1.0 | Deprecated |
| TLS 1.1 | Deprecated |
| TLS 1.2 | Widely supported |
| TLS 1.3 | Modern recommended version |

TLS 1.2 and TLS 1.3 are the primary versions encountered in modern environments.

## HTTPS

HTTPS is HTTP communication protected by TLS.

Default port:

    TCP/443

For HTTP/3, QUIC operates over UDP, commonly using port 443.

HTTPS protects data in transit but does not guarantee that the destination website is legitimate.

## TLS Handshake

The TLS handshake establishes the parameters required for secure communication.

A simplified TLS 1.3 handshake:

1. Client sends ClientHello.
2. Server responds with ServerHello.
3. Server provides its certificate and authentication information.
4. Both parties establish shared encryption keys.
5. Secure application data is exchanged.

TLS 1.3 uses a more streamlined handshake than earlier versions.

The handshake negotiates cryptographic parameters and establishes shared secrets used to protect the connection.

## Digital Certificates

A digital certificate binds an identity, such as a domain name, to a public key.

Certificates are commonly issued by Certificate Authorities (CAs).

A certificate typically contains:

- Subject information
- Subject Alternative Names (SANs)
- Issuer information
- Public key
- Validity period
- Signature algorithm
- Certificate signature

## Certificate Authorities

A Certificate Authority is a trusted organisation that issues and signs digital certificates.

Examples include:

- Let's Encrypt
- DigiCert
- Sectigo
- GlobalSign

Browsers and operating systems maintain trusted CA certificate stores.

## Certificate Chain of Trust

A typical certificate chain contains:

1. Root CA certificate.
2. Intermediate CA certificate.
3. Server certificate.

The server certificate is validated through the intermediate certificate to a trusted root.

Root certificates are generally trusted through the operating system or browser trust store.

## Common Certificate Types

| Type | Description |
|---|---|
| Domain Validated (DV) | Confirms control of a domain |
| Organisation Validated (OV) | Includes organisation identity validation |
| Extended Validation (EV) | Involves additional organisation validation |
| Wildcard | Covers a domain and eligible subdomains |
| SAN certificate | Covers multiple explicitly listed names |

A wildcard certificate such as:

    *.example.com

Can cover:

    www.example.com
    api.example.com

It does not ordinarily cover:

    example.com
    sub.api.example.com

## Certificate Validation

Clients generally validate:

- Certificate signature.
- Certificate chain.
- Certificate validity dates.
- Requested hostname against certificate names.
- Certificate trust.
- Relevant revocation information, where checked.

A certificate validation failure may occur because of:

- Expired certificate.
- Untrusted certificate authority.
- Hostname mismatch.
- Incomplete certificate chain.
- Invalid certificate signature.
- Incorrect system clock.

## Symmetric vs Asymmetric Encryption

### Symmetric Encryption

Uses the same secret key for encryption and decryption.

Examples:

- AES
- ChaCha20

Advantages:

- Efficient.
- Suitable for large amounts of data.

### Asymmetric Encryption

Uses a public and private key pair.

Examples:

- RSA
- Elliptic Curve Cryptography (ECC)

Common uses:

- Authentication.
- Digital signatures.
- Key establishment.

TLS uses asymmetric cryptography and key exchange mechanisms to establish shared secrets, then uses symmetric cryptography to protect application data.

## Forward Secrecy

Forward secrecy helps ensure that compromise of a server's long-term private key does not expose previously recorded sessions.

Modern TLS configurations commonly achieve this using ephemeral key exchange.

Examples include:

- ECDHE
- DHE

## Common TLS Ports

| Service | Common Port |
|---|---:|
| HTTPS | TCP/443 |
| SMTPS | TCP/465 |
| SMTP with STARTTLS | TCP/587 |
| IMAPS | TCP/993 |
| POP3S | TCP/995 |
| LDAPS | TCP/636 |

These are common defaults, not mandatory port assignments.

## Useful OpenSSL Commands

View certificate details:

    openssl x509 -in certificate.pem -text -noout

Display certificate expiry:

    openssl x509 -in certificate.pem -noout -dates

Inspect a remote TLS connection:

    openssl s_client -connect example.com:443 -servername example.com

Display certificate information from a remote connection:

    openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates

## Key Takeaways

- TLS protects data in transit.
- HTTPS is HTTP over TLS.
- Certificates bind identities to public keys.
- Certificate Authorities establish trust.
- TLS uses asymmetric cryptography and symmetric encryption.
- Forward secrecy helps protect previously established sessions.
- TLS 1.2 and TLS 1.3 are the modern versions to understand.
