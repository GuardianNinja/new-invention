# SECURITY.md

Space Leaf Corp takes security and safety seriously. This document explains how to report vulnerabilities, our response process, and disclosure policy.

## Reporting a Vulnerability
If you discover a security issue, please report it privately to our security team:
- **Email**: security@spaceleaf.org
- **PGP Key**: Available on request via the security email for encrypted reports

When reporting, include:
- A clear summary of the issue
- Affected component or file paths
- Steps to reproduce or a minimal proof of concept
- Impact assessment and suggested mitigations if available
- Your contact information for follow up

Do not post vulnerabilities publicly until the issue is resolved.

## Response Process
1. **Acknowledgement**: We will acknowledge receipt within 72 hours.
2. **Triage**: We will triage the report and assign severity and an owner.
3. **Fix and Test**: We will develop and test a fix, prioritizing safety and minimal disruption.
4. **Patch Release**: We will publish a patch and advisory to the repository and notify the reporter.
5. **Disclosure**: We will coordinate public disclosure with the reporter.

## Timelines
- Initial acknowledgement within 72 hours.
- Preliminary triage and mitigation plan within 14 days.
- Target remediation timeline depends on severity and complexity. For critical issues we aim to release mitigations or patches within 30 days when feasible.
- If a longer timeline is required we will provide status updates.

## Severity and Supported Versions
- Security advisories will indicate severity and affected versions.
- We maintain a supported versions list in `/governance/` and will provide upgrade guidance.

## Public Disclosure Policy
- We prefer coordinated disclosure. We will not publicly disclose a vulnerability until a fix or mitigation is available, or after a mutually agreed timeline.
- Reporters who follow responsible disclosure will be credited in advisories unless they request anonymity.

## Emergency and Field Safety
- If a vulnerability poses immediate physical safety risk in a deployed demonstration or field test, contact the Stewardship Board emergency channel as documented in `/governance/emergency_protocol.md`.
- Emergency mitigation steps will be prioritized over normal timelines.

## Legal Safe Harbor
- We will not pursue legal action against good faith security researchers who follow this policy and act responsibly to avoid privacy or safety violations.

## Security Best Practices for Contributors
- Do not commit secrets, private keys, or credentials to the repository.
- Use environment variables or secret management for CI and simulations.
- Follow secure coding practices and include threat modeling for protocol changes.

## Contact
- **Security Email**: security@spaceleaf.org
- For non security questions use the general project contact in `README.md`.

Thank you for helping keep the Digital Sea safe and trustworthy.
