---
created_at: 2026-10-09
updated_at: 2026-10-09
model: claude-opus-5-5
doc_type: sources
purpose: Where the procedures and evidence for this spec live.
related:
  - path: ./spec.md
    why: The spec these sources support.
---

# Sources

## Repo Guidance

- [browser-deep-research-prompts skill](../../skills/browser-deep-research-prompts/SKILL.md): procedure for writing prompt packs and runner files. Updated 2026-10-09 with the slim shape.
- [chatgpt-browser research chats](../../skills/chatgpt-browser/references/research-chats.md): starting chats, modes, effort slider, Deep research pill and plan card, pitfalls.
- [chatgpt-browser export](../../skills/chatgpt-browser/references/export.md): API-based status checks, Deep research report extraction from `widget_state`, generated-file download, stalled-run file recovery, clipboard byte transfer.

## Evidence

- B1 and B2 full reports, the scored audit and the prompt packs are kept in
  a private repo because the topic is personal.
  Exported files were also saved under the user's Downloads folder.
- Model labels come from ChatGPT's own conversation data
  (`resolved_model_slug`, and the Deep research report message's model).
  Trust: the platform's own label, not independent proof.
- Allowance figures: OpenAI publishes no numeric 6 Pro or Extra High cap
  (checked 9 October 2026). "About 50 a week" from earlier skill notes
  matches only a blog's Pro $100 figure; Business Insider (29 September
  2026) reports 100 a week for new Pro $200 subscribers. Treat both as
  press, not official.

## External / Canonical Docs

Checked live on 9 October 2026. help.openai.com blocks plain fetches; read
it through a fetch proxy.

- [GPT-6 and other models in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt): Pro effort = GPT-6 Pro on GPT-6 Astra; Instant to Extra High = GPT-6 Sol; plan table (Plus has no Extra High or Pro); Pro-model allowance rules.
- [Deep research in ChatGPT](https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt): "latest model by default", legacy models selectable, task counter that resets 30 days after first use. No model named.
- [Enterprise rate card](https://help.openai.com/en/articles/20001415-chatgpt-rate-card-enterprise-token-based-pricing): lists `o4-mini-deep-research` under Deep research.
- [About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers): $100, $200, $500 tiers; old Pro $200 allowance kept until 29 October 2026.
- [OpenAI Academy, search and deep research](https://openai.com/academy/search-and-deep-research/): Deep research "5 to 30 minutes".

## Generated Reference / Companion Docs

- ChatGPT research modes report (private, not published): verified, condensed answer from B3 Q1 (models, search, run time, caps, best uses, where OpenAI's guidance and our runs disagree).

## Weak Claims To Avoid

- Deep research is o3 or o4-mini today (those are 2025 launch facts).
- Plus gets 25 and Pro 250 Deep research tasks a month (April 2025 figures, not confirmed now).
- Chat Pro or Extra High cannot search the web, or answer "in seconds".
- Chat is fast and Deep research is slow: with slim prompts all three took 5 to 10 minutes here.

## Related Specs

- [internet-deep-research](../internet-deep-research/spec.md): agent-run search and fetch tools and providers.
- [browser-use](../browser-use/spec.md): browser safety and identity contract.
