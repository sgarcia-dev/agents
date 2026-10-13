# Desktop and browser GUI fallback

Browser DOM/CDP control does not operate a native file picker, a desktop app, an OS permission prompt, or browser chrome reliably. If the requested action needs those surfaces, use a separately authorized desktop/accessibility controller, or a browser-native file-input/download method that can be independently verified. See `~/agents/capabilities/browser-desktop.md`.

A desktop screenshot of Chrome is not evidence a browser connector controls that same profile. Confirm the intended window, profile and current URL before clicking. Prefer accessible controls; coordinates are valid only for a fresh observation. Do not approve native remote-debugging, passwords, MFA, CAPTCHA or payment prompts on the owner's behalf. Hand control to the owner once, then reobserve the result. If a headless route is logged out or the connection route stalls, change approach early rather than repeatedly trying the same action.

For a state change, reload or reopen the exact target and read back the server state. A click dispatched, a picker opened, or a toast saying Saved is not enough. Close task-owned tabs, restore global clipboard/download settings when changed, and leave owner-owned windows alone.
