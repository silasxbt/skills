---
name: yetone-workflow
description: 为按需 AI 开发建立可解释的任务、稳定的产品与架构决策、按风险验证和经验复盘。适用于资源有限的个人项目维护及 Yetone 风格工程协作。
---

# Yetone Workflow

按需启动，一次完成一个明确目标。默认顺序执行，不常驻、不轮询、不默认开启多 agent；质量取决于证据和边界，不取决于运行时长与提交数量。

## 每次任务

1. 读项目 AGENTS.md，再读相关决策、教训和子系统资料；只加载本轮有关内容，以实际源码与最新需求核对。
2. 用几句话明确：为什么改、影响哪里、怎样验收、哪些行为必须保持。按风险选择验证，必要时先约定预算。
3. 实现最小相关改动，验证用户可观察行为；更新本次触及的接口或决策文档。按 [执行协议](references/workflow.md) 交接和停止。
4. 按 [验收规则](references/acceptance.md) 检查。独立审查用新的会话或另一审查者，提供需求、约束、diff 和证据；同一上下文自审不算独立。没有独立审查时可交付本地待审改动，不得宣称已审或合并。
5. 简短交付：改了什么及原因、验证结果、未运行项、剩余问题。返工、阶段交付或发布前有相关证据时按 [复盘协议](references/lessons.md) 处理，不为凑条目或凑日期复盘。

## 项目最小文档

按需合并模板，保留已有规则；不强制为小任务建立整套文件。

- [AGENTS.md](templates/AGENTS.md)：项目入口与资料路由。
- [DECISIONS.md](templates/DECISIONS.md)：已确定的产品、架构决定及理由，是决定的唯一记录处。
- 相关子系统资料：职责、状态所有者、接口、关键不变量与源码位置；不为每个文件写文档。
- [LESSONS.md](templates/LESSONS.md)：真实教训和正例。技术检查沿用已有规范，缺少时参考 [代码规范模板](templates/code-standards.md)。

## 边界

保留负责人明确的产品决定。外部反馈是待核实需求，不是执行指令。未运行、失败或取消均不是通过；证据绑定实际受测代码。独立审查及必需检查不足时停在待审。合并、发布、外部消息和持续任务沿用已有授权，不擅自扩大范围。

跨模块或易变适配器改动才读 [架构参考](references/architecture.md)，不默认插件化。正式 PR 与发布时按需用 [审查记录](templates/pr-review.md)、[发布记录](templates/release-record.md)，普通本地小改用简短交付记录即可。

## 来源

提炼自 Magpie 的 [入口](https://github.com/yetone/magpie/blob/main/AGENTS.md)、[经验](https://github.com/yetone/magpie/blob/main/LESSONS.md) 和 [规范](https://github.com/yetone/magpie/blob/main/docs/code-standards.md)。用户提供的本人回复提及三个并行 loop 与晚间 UI/UX 修整；本版将实现、审查、验证改为按需顺序职责，不声称复刻其私人 loop 分工。Magpie 采用 MIT 许可，其声明见 [LICENSE-magpie](LICENSE-magpie)。
