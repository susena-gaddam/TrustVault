# TrustVault — AI Prompt Log

This log records selected AI-assisted development work on TrustVault. Development began on 20 October 2026 and continued on 24 October 2026. Git commit dates reflect when commits were created; they do not necessarily represent the exact date when all related work began.

## Entry 1 — 20 October 2026 — Initial project setup

- **Prompt/task:** Get help setting up a Django project for a document-storage application.
- **Tool:** ChatGPT
- **Work:** Created the Django project and `documents` app, configured the database, and started defining document-related models.
- **What needed checking:** The project configuration needed to match the installed Python and Django environment.
- **What I did:** Ran Django system checks and migrations locally.
- **Commit:** [57210b1 — Set up Django project and document models](https://github.com/susena-gaddam/TrustVault/commit/57210b1)

## Entry 2 — 24 October 2026 — Login and authentication

- **Prompt/task:** Add a login page and authentication routes.
- **Tool:** ChatGPT
- **Work:** Added the login template and authentication routing.
- **What needed checking:** Template paths, URL configuration, and protection of authenticated pages needed to be correct.
- **What I did:** Tested the login flow and protected pages locally.
- **Commit:** [6c76342 — Add login page and authentication routes](https://github.com/susena-gaddam/TrustVault/commit/6c76342)

## Entry 3 — 24 October 2026 — Document upload and dashboard

- **Prompt/task:** Build a dashboard that lets authenticated users upload and view their documents.
- **Tool:** ChatGPT
- **Work:** Added document upload functionality and a dashboard listing the current user's documents.
- **What needed checking:** Documents needed to be associated with the logged-in user and the dashboard needed to filter by ownership.
- **What I did:** Tested uploads and verified that the dashboard displayed documents belonging to the current user.
- **Commit:** [47acf58 — Add document upload and dashboard](https://github.com/susena-gaddam/TrustVault/commit/47acf58)

## Entry 4 — 24 October 2026 — Authorization and protected downloads

- **Prompt/task:** Prevent users from downloading another user's document by changing a document ID in the URL.
- **Tool:** ChatGPT
- **Work:** Implemented a download view that restricts document retrieval to the authenticated owner.
- **What needed checking:** Authentication alone is insufficient; the requested document must also belong to the current user.
- **What I did:** Used an owner-constrained database lookup and tested unauthorized download attempts.
- **Commit:** [9b8bdda — Add owner-protected document downloads](https://github.com/susena-gaddam/TrustVault/commit/9b8bdda)

## Entry 5 — 24 October 2026 — Security and access-control tests

- **Prompt/task:** Write automated tests for document ownership and unauthorized access.
- **Tool:** ChatGPT
- **Work:** Added tests for document visibility and protected downloads.
- **What needed checking:** Tests needed separate user accounts and assertions against actual responses, rather than merely checking whether a page loaded.
- **What I did:** Ran the Django test suite and verified dashboard isolation and download authorization.
- **Commit:** [6994993 — Add document access control tests](https://github.com/susena-gaddam/TrustVault/commit/6994993)

## Entry 6 — 24 October 2026 — File-upload validation

- **Prompt/task:** Restrict uploads to an allowlist of file extensions and test rejection of unsupported files.
- **Tool:** ChatGPT
- **Work:** Added file-extension validation and a test for an unsupported `.exe` upload.
- **What needed checking:** Extension validation does not prove that a file's contents are safe or match its extension.
- **What I did:** Added the validation and automated test, then ran the test suite.
- **Commit:** [91a27f7 — Validate uploaded file extensions and add security test](https://github.com/susena-gaddam/TrustVault/commit/91a27f7)

## Entry 7 — 24 October 2026 — Threat modelling

- **Prompt/task:** Document TrustVault's security threats, mitigations, and remaining risks.
- **Tool:** ChatGPT
- **Work:** Created threat documentation describing the implemented protections and limitations.
- **What needed checking:** The documentation needed to distinguish implemented features from incomplete or planned features.
- **What I did:** Documented the current protections and outstanding risks in `THREATS.md`.
- **Commit:** [ba32eca — Document TrustVault security threats](https://github.com/susena-gaddam/TrustVault/commit/ba32eca)

## Entry 8 — 24 October 2026 — Audit logging

- **Prompt/task:** Add audit logging for document uploads and update the relevant security tests.
- **Tool:** ChatGPT
- **Work:** Added an audit record for successful document uploads and updated the tests.
- **What needed checking:** Audit records needed to correspond to successful uploads. The implementation should not be described as logging every document action.
- **What I did:** Added upload audit logging and updated the security tests. The document test suite passed.
- **Commit:** [d363f14 — Add upload audit logging and update security tests](https://github.com/susena-gaddam/TrustVault/commit/d363f14)

## Entry 9 — 24 October 2026 — Deployment configuration

- **Prompt/task:** Configure the Django application for deployment on Render.
- **Tool:** ChatGPT
- **Work:** Updated deployment settings and configured static-file handling and the application startup command.
- **What needed checking:** Production settings, allowed hosts, dependencies, static files, and startup commands needed to work on the hosting platform.
- **What I did:** Deployed the application and verified that the live login page opened. I also identified the limitations of temporary SQLite and media storage on the free hosting plan.
- **Commit:** [c3a28df — Prepare Django settings for Render deployment](https://github.com/susena-gaddam/TrustVault/commit/c3a28df)

## Entry 10 — 24 October 2026 — User registration

- **Prompt/task:** Add account registration so new users can create accounts and access the application.
- **Tool:** ChatGPT
- **Work:** Added a registration view, URL route, template, and a registration link on the login page.
- **What needed checking:** The registration route and template needed to work, and users needed a way to reach registration from the login page.
- **What I did:** Ran the existing document tests, which passed, and tested registration on the deployed website.
- **Commit:** [e83f2df — Add user registration for TrustVault](https://github.com/susena-gaddam/TrustVault/commit/e83f2df)

## Current limitations and remaining risks

- **Storage persistence:** The deployed application uses SQLite and local media storage on Render's free plan. Database records and uploaded files may not persist across restarts or redeployments.
- **Audit coverage:** Uploads are logged. Download audit logging is not implemented.
- **Sharing and permissions:** Document sharing and permission-management interfaces are not implemented.
- **File security:** Extension validation is implemented, but file-content inspection and malware scanning are not.
- **Production readiness:** The deployed application is a demonstration and should not be used for confidential documents without durable storage and further security hardening.

This log records selected AI-assisted development tasks and the associated Git commits. Commit dates have not been rewritten or backdated. The application and its documentation should be evaluated against the features actually implemented.