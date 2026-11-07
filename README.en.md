# skills

[中文](README.md) | **English**

A collection of practical, easy-to-configure skills and reference packs. Updated from time to time, and PRs are welcome.

## Contents

| Name | Description |
| --- | --- |
| [anti-api](anti-api/SKILL.md) | Set up a local API bridge that routes models from multiple accounts through one endpoint |
| [apple-home-without-gateway](apple-home-without-gateway/README.md) | Control Apple Home accessories from a local Mac without a gateway (direct toggle and automation stack layouts) |
| [claude-ui](claude-ui/SKILL.md) | Apply a Claude-style visual language to an interface |
| [pdf-to-epub](pdf-to-epub/SKILL.md) | Convert PDF files to EPUB with Calibre |
| [safe-mac-openclaw](safe-mac-openclaw/SKILL.md) | Harden a personal OpenClaw setup on macOS |
| [stripe-payments-risk](stripe-payments-risk/SKILL.md) | Answer Stripe payment and risk-control questions from user-provided reference material |
| [yetone-workflow](yetone-workflow/SKILL.md) | On-demand AI development workflow: define tasks clearly, record decisions, verify by risk, and run event-driven retrospectives |

## Directory layout change

All skills have moved from a nested directory under `Desktop/` to the repository root. If you installed or linked them using the old path, please update it.

## Validation

```bash
python3 scripts/validate_skills.py
```

CI runs this check and ShellCheck on every push and PR.

## License

Unless a subdirectory states otherwise, the contents of this repository are licensed under the [MIT License](LICENSE).
