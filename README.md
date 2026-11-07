# skills

收录高实用性、配置简单的 skills 和参考资料包，不定期更新，欢迎 PR。

## 目录

| 名称 | 说明 |
| --- | --- |
| [anti-api](anti-api/SKILL.md) | 配置本地 API 桥接，统一路由多个账号的模型 |
| [apple-home-without-gateway](apple-home-without-gateway/README.md) | 无网关时用本地 Mac 控制 Apple Home 配件（直接控制、自动化编排两种布局） |
| [claude-ui](claude-ui/SKILL.md) | 为界面应用 Claude 风格的视觉语言 |
| [pdf-to-epub](pdf-to-epub/SKILL.md) | 用 Calibre 将 PDF 转换为 EPUB |
| [safe-mac-openclaw](safe-mac-openclaw/SKILL.md) | 加固 macOS 上的个人 OpenClaw 环境 |
| [stripe-payments-risk](stripe-payments-risk/SKILL.md) | 按用户提供的参考资料回答 Stripe 支付与风控问题 |
| [yetone-workflow](yetone-workflow/SKILL.md) | 按需 AI 开发工作流：明确任务、记录决策、按风险验证和事件驱动复盘 |

## 目录结构变更

所有 skill 已从 `Desktop/` 下的嵌套目录移到仓库根目录。如果你按旧路径安装或链接过，请更新路径。

## 校验

```bash
python3 scripts/validate_skills.py
```

CI 会在每次 push 和 PR 时运行该校验和 ShellCheck。

## 许可证

除非子目录另有说明，本仓库内容采用 [MIT 许可证](LICENSE)。
