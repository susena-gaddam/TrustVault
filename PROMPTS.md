# TrustVault — AI Prompt Log

This log records selected AI-assisted work on TrustVault. Development began on Tuesday, 20 October 2026, paused, and resumed on Saturday, 24 October 2026. Git commit dates reflect when the recorded commits were created, not necessarily when all related work first began.

## Entry 1 — 20 October 2026 — Initial project setup

- **Prompt/task:** Get help setting up a Django project for a document-storage application.
- **Tool:** ChatGPT
- **Work:** Created the Django project and `documents` app, configured the database, and started defining the document-related models.
- **What needed checking:** The setup needed to match the local Python and Django environment.
- **What I did:** Ran migrations and Django system checks locally.
- **Related commit:** `57210b1` — Set up Django project and document models. This commit was created on 24 October.

## Entry 2 — 24 October 2026 — Login and authentication

- **Prompt/task:** Add a login page and authentication routes.
- **Tool:** ChatGPT
- **What needed checking:** Template paths and URL configuration had to match the project.
- **What I did:** Tested the login flow and protected pages locally.
- **Commit:** `6c76342` — Add login page and authentication routes.

## Entry 3 — 24 October 2026 — Document upload and dashboard

- **Prompt/task:** Build a dashboard that lets users upload and view their own documents.
- **Tool:** ChatGPT
- **What needed checking:** Uploaded documents needed to be associated with the logged-in user.
- **What I did:** Tested uploads and verified that the dashboard filters documents by owner.
- **Commit:** `47acf58` — Add document upload and dashboard.

## Entry 4 — 24 October 2026 — Authorization and protected downloads

- **Prompt/task:** Prevent users from downloading documents belonging to other users by changing a document ID in the URL.
- **Tool:** ChatGPT
- **What needed checking:** Authentication alone is insufficient; the requested document must belong to the current user.
- **What I did:** Used an owner-constrained database lookup and tested unauthorized download attempts.
- **Commit:** `9b8bdda` — Add owner-protected document downloads.

## Entry 5 — 24 October 2026 — Security tests

- **Prompt/task:** Write automated tests for document ownership and unauthorized access.
- **Tool:** ChatGPT
- **What needed checking:** Tests needed separate user accounts and assertions against the actual responses.
- **What I did:** Ran the Django test suite and verified dashboard isolation and download authorization.
- **Commit:** `6994993` — Add document access control tests.

## Entry 6 — 24 October 2026 — File-upload validation

- **Prompt/task:** Restrict uploads to an allowlist of file extensions and test rejection of unsupported files.
- **Tool:** ChatGPT
- **What needed checking:** An extension check does not verify the actual file contents.
- **What I did:** Added an extension check and an automated test for an `.exe` upload. The test suite passed.
- **Commit:** `91a27f7` — Validate uploaded file extensions and add security test.

## Entry 7 — 24 October 2026 — Threat modelling

- **Prompt/task:** Document TrustVault's security threats, mitigations, and remaining risks.
- **Tool:** ChatGPT
- **What needed checking:** The documentation must distinguish implemented protections from planned or incomplete features.
- **What I did:** Documented the current protections and limitations in `THREATS.md`.
- **Commit:** `ba32eca` — Document TrustVault security threats.

## Next development tasks

- Implement and test audit logging for relevant document actions.
- Continue authorization and upload-security testing.
- Complete the README and deployment instructions.
- Deploy and verify the application before submitting.

This log records selected development tasks. Commit dates are preserved as recorded by Git. Further entries will be added when additional work is actually completed.
