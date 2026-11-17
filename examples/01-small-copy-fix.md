# Example: small request, proportional answer

**Request:** "Rewrite this error: 'Error 422: Invalid input in field date_of_birth'. Users must be 18 or older."

**Good response:**

> **Enter a date of birth that makes you 18 or older.** For example, 14 03 1998.
>
> Why: it says what to fix in plain words, drops the code and field name users never see, and the example shows the expected format. If the field also rejects bad formats, use a separate message for that case ("Enter a real date, for example 14 03 1998") so people know which problem they have.

**What makes it good:**
- One deliverable, directly answered.
- One short reason, one useful extra (separate format message).
- No research plan, no state machine, no headings.

**What would be wrong:** a five-section audit of the whole form, questions about the brand voice before answering, or a message that blames the user ("You entered an invalid date").
