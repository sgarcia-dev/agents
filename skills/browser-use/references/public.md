# Public browser routes

Use a clean, isolated browser for public navigation, page inspection, and low-stakes UI checks. Search/fetch tools or an official API may be simpler when no clicks are required. The cross-harness contract lives in the browser-use spec.

- **Local isolated browser:** A browser tool, Playwright MCP's managed context, stock Jev MCP, or standalone `agent-browser` can start signed out. These are controllers and contexts, not access to the owner's Chrome logins. See `~/agents/capabilities/browser-native.md`, `~/agents/capabilities/mcp/playwright.md`, `~/agents/capabilities/mcp/jev-browser.md`, and `~/agents/capabilities/browser-cli.md`.
- **Public hosted browser:** Useful when the local host cannot run a browser or parallel jobs exceed local capacity. Each session can incur spend and starts signed out unless an explicit saved profile is bound; see `hosted.md`.
- **Blocked route:** One failed page read is not evidence every browser will fail. Check whether the failure is network, auth, bot wall, missing content, or a wrong context. Change to an authorized API/route or hand back; do not solve challenges or copy cookies to evade a block.

Set a step/time budget, open only a task-owned tab, observe controls before acting, and check final URL plus the requested content. A controller's `done`, a successful navigation call, or a page title alone is not the requested result. Close the tab or disposable session and verify it is gone. If the task later needs an account, switch to `signed-in.md` and obtain the correct identity rather than treating a logged-out run as a partial signed-in pass.
