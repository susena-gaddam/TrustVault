# TrustVault — Threat Model

## Project Scope

TrustVault is a Django document-storage application. The current implementation supports user login, document uploads, a personal document dashboard, and owner-protected downloads.

## Assets to Protect

- Uploaded documents and their contents
- User accounts and authentication sessions
- Document titles and descriptions
- Document ownership records

## Threats and Mitigations

### 1. Unauthorized Document Access

**Threat:** A logged-in user changes a document ID in a download URL to access another user's file.

**Mitigation:** The download view retrieves documents using both the document ID and the logged-in user's ownership. A request for another user's document returns 404.

**Verification:** Automated tests confirm that another user cannot download a document they do not own.

### 2. Unauthorized Dashboard Access

**Threat:** A user attempts to view another user's documents through the dashboard.

**Mitigation:** The dashboard filters documents by the current user.

**Verification:** An automated test confirms that another user's private document does not appear on the dashboard.

### 3. Malicious or Unsupported Uploads

**Threat:** A user attempts to upload an executable or an unsupported file type.

**Mitigation:** The upload view checks file extensions against an allowlist and limits file size to 5 MB.

**Limitation:** Extension checks alone do not prove that a file's actual contents match its extension. Content validation and malware scanning are not currently implemented.

### 4. Cross-Site Request Forgery

**Threat:** A malicious website attempts to submit an upload request using an authenticated user's browser.

**Mitigation:** The upload form includes Django's CSRF token, and the form uses POST for uploads.

### 5. Accidental Exposure of Uploaded Files

**Threat:** Uploaded files become publicly accessible through a directly exposed media directory.

**Mitigation:** Downloads are handled through an authenticated view that checks ownership. Production hosting must also ensure that uploaded files are not exposed through a public media URL.

## Remaining Risks

- Document sharing and permission management are not yet implemented in the user interface.
- Audit logging is not yet integrated into document actions.
- File content validation and malware scanning are not implemented.
- Production deployment settings and hosting security still require verification.

## Security Testing

Run the automated tests with:

`python manage.py test documents`

The tests cover owner downloads, denial of unauthorized downloads, dashboard isolation, and rejection of unsupported file extensions.
