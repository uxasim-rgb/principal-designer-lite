# Example: flow and state specification

**Request:** "Spec the 'Export report' action in our analytics app. Exports can take a few minutes."

**Good response (abridged):**

**Assumptions:** web app; exports run on the server as background jobs; files are kept 7 days; users can leave the page while it runs; a file is all or nothing (an export either contains every matching row or fails, never a file with rows silently missing). Confirm the retention period, size limits and the all-or-nothing rule with engineering.

| State | User sees | Available actions | Next |
| --- | --- | --- | --- |
| Idle | "Export" button with format menu (CSV, XLSX, PDF) | Choose format | Requesting |
| Requesting | Button shows spinner, disabled to prevent duplicates. The request carries a request ID made on the client | None | Queued, Failed to start, or Unknown |
| Queued / running | Toast: "Preparing your export. We'll notify you when it's ready." Job appears in an Exports panel with progress if known, "Running" if not | Cancel, keep working, leave page | Ready, Failed, Cancellation requested |
| Ready | Notification and Exports panel entry: file name, size, created time, "Download" | Download, Dismiss | Downloaded, Expired |
| Failed | Panel entry: "Export failed. The report has more rows than the 1 million row limit." (or the real reason) | Retry, Change filters, Contact support | Requesting |
| Cancellation requested | Panel entry: "Cancelling..." until the server answers, because the job may finish first | None | Cancelled, or Ready if it finished first |
| Cancelled | Panel entry: "Export cancelled" | Export again | Idle |
| Expired | "This file has expired. Export again to get current data." | Export again | Requesting |
| Unknown | Connection lost while requesting: "Checking whether your export started..." The app asks the server for the job by its request ID when the connection returns | Open Exports | Queued or running if the server has the job; Idle with "Your export did not start. Try again." if it does not |

**Rules**
- Exports reflect filters at the time of request; show those filters on the panel entry.
- Retries are safe: the server treats a repeated request ID as the same job, so a refresh, a lost connection or a second tab cannot create a duplicate. A new job is created only after the old one is Failed, Cancelled or Expired, or the person changes the filters or format.
- Leaving the page does not cancel the job.
- If permissions change before download, the download checks access again.
- Screen readers announce "Export ready" through a polite live region; the notification also persists in the panel.

**Acceptance checks:** no duplicate jobs on double-click, refresh, reconnect or a second tab; a request that timed out but actually succeeded shows the real job; a cancel that arrives after the file is ready shows Ready; status survives refresh; failure messages name the real cause; download works by keyboard.

**Why this is a good example:**
- Covers pending, failure, cancellation and its race with completion, expiry and unknown outcome, not just success. Partial files are ruled out by an explicit assumption rather than left undefined.
- States assumptions up front and who confirms them.
- Includes accessibility and acceptance checks without becoming a full audit.
