# TrustVault — Threat Model

## Project Scope

TrustVault is a Django document-storage application. The current implementation supports user login, document uploads, a personal document dashboard, owner-protected downloads, and audit logging for successful document uploads.

## Assets to Protect

- Uploaded documents and their contents
- User accounts and authentication sessions
- Document titles and descriptions
- Document ownership records
- Audit-log records

## Threats and Mitigations

### 1. Unauthorized Document Access

**Threat:** A logged-in user changes a document ID in a download URL to access another user's file.

**Mitigation:** The download view retrieves documents using both the document ID and the logged-in user's ownership. A request for another user's document returns a 404 response.

**Verification:** An automated test confirms that another user cannot download a document they do not own.

### 2. Unauthorized Dashboard Access

**Threat:** A user attempts to view another user's documents through the dashboard.

**Mitigation:** The dashboard filters documents by the currently authenticated user.

**Verification:** An automated test confirms that another user's private document does not appear on the dashboard.

### 3. Malicious or Unsupported Uploads

**Threat:** A user attempts to upload an executable or an unsupported file type.

**Mitigation:** The upload view checks file extensions against an allowlist of PDF, TXT, DOC, and DOCX files and limits file size to 5 MB.

**Limitation:** Extension checks alone do not prove that a file's actual contents match its extension. File content validation and malware scanning are not currently implemented.

### 4. Cross-Site Request Forgery

**Threat:** A malicious website attempts to submit an upload request using an authenticated user's browser.

**Mitigation:** The upload form includes Django's CSRF token, and uploads use POST requests.

### 5. Accidental Exposure of Uploaded Files

**Threat:** Uploaded files become publicly accessible through an exposed media directory or an insecure hosting configuration.

**Mitigation:** Downloads are handled through an authenticated view that checks document ownership. Production hosting must also ensure uploaded files are not exposed through a public media URL.

### 6. Incomplete Audit Logging

**Threat:** Security-relevant document activity may be difficult to investigate if actions are not recorded.

**Mitigation:** TrustVault records successful document uploads, including the acting user, document reference, action, and document title.

**Limitation:** Document downloads and other actions are not currently logged. Audit-log integrity and access restrictions also require further review before production deployment.

## Remaining Risks

- Document sharing and permission management are not yet implemented in the user interface.
- Audit logging currently covers successful uploads only; downloads and other document actions are not logged.
- File content validation and malware scanning are not implemented.
- Production deployment settings, file-storage security, and hosting configuration still require verification.
- Audit-log integrity and access controls need further review before production use.

## Security Testing

Run the automated tests with:

`python manage.py test documents`

The current test suite covers:

- Successful document downloads by the owner.
- Denial of downloads by another user.
- Dashboard isolation between users.
- Rejection of unsupported file extensions.
- Creation of an audit-log entry after a successful upload.

The five automated tests passed in the current development environment. Production security has not yet been independently verified.