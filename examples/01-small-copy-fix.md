# Example: small request, proportional answer

**Request:** "Rewrite this error: 'Error 422: Invalid input in field date_of_birth'. Users must be 18 or older."

**Good response:**

> **You must be 18 or older to create an account.**
>
> Why: the person's date may be correct, so the message states the rule instead of asking them to change their birth date. It drops the code and the field name people never see.
>
> If the same 422 also covers other problems, give each its own message:
> - Bad format: "Enter a real date of birth, for example 14 03 1998."
> - Field left empty: "Enter your date of birth."
>
> Show the one that matches the actual validation reason.

**What makes it good:**
- One deliverable, directly answered.
- One short reason, one useful extra (the other two cases, kept separate).
- No research plan, no state machine, no headings.

**What would be wrong:** a five-section audit of the whole form, questions about the brand voice before answering, a message that blames the user ("You entered an invalid date"), or one that tells an underage person to enter a different birth date.
