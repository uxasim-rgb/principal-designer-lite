# Example: flow and state specification

**Request:** "Spec the 'Export report' action in our analytics app. Exports can take a few minutes."

**Good response (abridged):**

**Assumptions:** web app; exports run on the server as background jobs; files are kept 7 days; users can leave the page while it runs. Confirm the retention period and size limits with engineering.

| State | User sees | Available actions | Next |
| --- | --- | --- | --- |
| Idle | "Export" button with format menu (CSV, XLSX, PDF) | Choose format | Requesting |
| Requesting | Button shows spinner, disabled to prevent duplicates | None | Queued, or Failed to start |
| Queued / running | Toast: "Preparing your export. We'll notify you when it's ready." Job appears in an Exports panel with progress if known, "Running" if not | Cancel, keep working, leave page | Ready, Failed, Cancelled |
| Ready | Notification and Exports panel entry: file name, size, created time, "Download" | Download, Dismiss | Downloaded, Expired |
| Failed | Panel entry: "Export failed. The report has more rows than the 1 million row limit." (or the real reason) | Retry, Change filters, Contact support | Requesting |
| Cancelled | Panel entry: "Export cancelled" | Export again | Idle |
| Expired | "This file has expired. Export again to get current data." | Export again | Requesting |
| Unknown | Connection lost while requesting: "We couldn't confirm your export started. Check Exports before trying again." | Open Exports | Any |

**Rules**
- Exports reflect filters at the time of request; show those filters on the panel entry.
- Leaving the page does not cancel the job.
- If permissions change before download, the download checks access again.
- Screen readers announce "Export ready" through a polite live region; the notification also persists in the panel.

**Acceptance checks:** no duplicate jobs on double-click; status survives refresh; failure messages name the real cause; download works by keyboard.

**Why this is a good example:**
- Covers pending, partial, failure, cancellation, expiry and unknown outcome, not just success.
- States assumptions up front and who confirms them.
- Includes accessibility and acceptance checks without becoming a full audit.
