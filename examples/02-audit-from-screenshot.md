# Example: critique of a screenshot

**Request:** a screenshot of a SaaS settings page for team members, with "Review this."

**Good response (abridged):**

**Summary.** The page is clean and the member list scans well. The main problems are a destructive action styled as primary, an unclear role model, and no visible state for pending invites. Behaviour (keyboard, screen reader, confirmations) can't be judged from a still image.

**Findings, by severity**

1. **Major: "Remove" looks like the main action.** Each row has a filled blue "Remove" button, the strongest element on the page. People scanning for "Invite" may hit it, and it is the action you least want them to take by accident. *Fix:* make Remove a row overflow menu item in danger color, keep "Invite member" as the only filled button, and confirm removal with the person's name and what they lose access to.
2. **Major: roles are unexplained.** "Admin", "Editor" and "Member" have no description and appear as plain text, so it is unclear whether they can be changed here. *Fix:* a role dropdown per row (for those allowed to change it) and a short "What can each role do?" link opening a comparison.
3. **Minor: no pending invite state.** Invited people who haven't joined aren't shown, so admins may invite twice. *Fix:* list them with a "Pending" tag, the date sent, and "Resend" and "Revoke".
4. **Minor: secondary text contrast.** The gray emails look around #9CA3AF on white, roughly 2.5:1, below the 4.5:1 needed. *Fix:* darken to about #6B7280 or darker and measure.
5. **Polish: inconsistent avatar fallbacks.** Some rows have initials, some a generic icon. Use initials everywhere.

**What works:** clear page title, sensible column order (name, role, last active), generous row height.

**Needs runtime or user check:** keyboard access to row actions, focus return after removal, screen-reader labels for icon buttons, what happens when the last admin tries to remove themselves.

**Why this is a good example:**
- Ordered by severity, each finding has where, issue, why, and fix.
- The contrast estimate is labelled as an estimate from pixels.
- It doesn't claim anything about behaviour it can't see.
- It names what works, briefly.
