# 编码 Skills 与 Rules 审查任务

只保留尚未执行或尚未确认的事项。完成一项后删除对应任务及说明，让文档持续变短；优先级只在分组标题中表达。

## P0｜全局 Rules 迁移与常驻行为

- [ ] 执行本节方案，把 Codex 和 Pi 收敛为“最小全局入口 + 共享工程 Skills”。
  - 范围：本仓库 Skills、`/Users/edison/.codex/AGENTS.md`、其引用的 7 份 Markdown、`/Users/edison/.pi/agent/AGENTS.md` 和 Ponytail plugin 的退出。
  - 不包含：本节不顺带审查 P1/P2 的全部第三方 Skills，也不把仓库级构建、测试和架构规则搬进全局配置。
  - 完成条件：按下述顺序实现、发布、安装、切换和验收；通过后删除本节。

### 已定结论

Codex 的 `AGENTS.md` 会确定性进入每次任务；Skill 只在显式调用或 description 命中时加载正文。因此，长期不变且每次都必须成立的底线留在 `AGENTS.md`，任务型流程进入 Skill。这个边界符合 [Codex 的 AGENTS.md 说明](https://learn.chatgpt.com/docs/agent-configuration/agents-md) 和 [Skill 渐进加载模型](https://learn.chatgpt.com/docs/build-skills)。

最终结构如下：

- 全局底线
  - 所有者：Codex、Pi 各自的 `AGENTS.md`。
  - 内容：正确性与安全、用户范围、最小修改、验证诚实、破坏性操作边界、项目规则归属、Skill 缺失时的保守行为。
  - 加载：每次任务确定性加载。

- Feature 与 enhancement 开发
  - 所有者：本仓库 `feature-development`。
  - 内容：非平凡实现的目标、风险、方案、执行、验证和交付流程。
  - 加载：任务命中时加载。

- 专项工程流程
  - 所有者：本仓库现有工程 Skills。
  - 内容：bug、兼容性、迁移、性能、分布式可靠性、可观测性、重构和工程审查。
  - 加载：对应任务命中时加载。

- 代码库导航
  - 所有者：本仓库 `codebase-navigation`。
  - 内容：CodeGraph 可用时做结构分析，否则使用 `rg` 和精确读取。
  - 加载：代码理解、调用链和影响分析时加载。

- 软件设计
  - 所有者：本仓库 `software-design`。
  - 内容：模块边界、接口、信息隐藏、状态所有权、生命周期、失败模型和 deep-module 原则。
  - 加载：设计问题具有实质结构权衡时加载；`feature-development` 用它指导实现，`code-review` 用同一标准检查结果。

- 外部文档
  - 所有者：第三方 `context7-mcp`。
  - 内容：库、框架、SDK、API 和 CLI 的当前文档。
  - 加载：外部技术文档任务命中时加载。

- 活动任务文档
  - 所有者：本仓库 `write-great-document`。
  - 内容：未完成队列、分组、任务子项、阻塞和验证。
  - 加载：创建或维护 todo 文档时加载。

- 仓库约束
  - 所有者：各项目 `AGENTS.md`。
  - 内容：构建、测试、lint、布局、生成文件、兼容性、发布和完成标准。
  - 加载：进入对应项目时确定性加载。

- 命令策略
  - 所有者：Codex `.rules` 或 hook。
  - 内容：只用于可机械判断的命令前缀和外部副作用。
  - 加载：执行命令时判断。

当前 Markdown Rules 描述的是工程判断，不是命令前缀策略；这次不新增 `.rules` 或 hook。官方 [Codex Rules](https://learn.chatgpt.com/docs/agent-configuration/rules) 与这里的 Markdown “rules” 不是同一机制。

### 最小全局入口

Codex 和 Pi 使用完全相同的正文；不再通过链接加载其他规则文件。

```md
# AGENTS.md

Global defaults for this agent.

## Boundaries

- Preserve correctness, safety, security, and data integrity before speed or convenience.
- Follow the user's requested scope and externally visible behavior. Preserve compatibility unless the user asks to break it.
- Repository `AGENTS.md` files own project build, test, lint, layout, generated-file, compatibility, migration, release, and done criteria. They may specialize these defaults without weakening safety or verification honesty.

## Work

- Inspect relevant code and instructions before editing. Make the smallest clear change; do not include unrelated cleanup.
- Use applicable installed Skills for task workflows. User and repository instructions override Skill defaults. If a required Skill is unavailable, say so and continue conservatively.
- Never claim a check passed unless it ran. Report the command, result, partial coverage, and remaining risk accurately.
- Assess new or updated dependencies for maintenance, license, security, build, and runtime risk; proceed when the risk is acceptable. Ask before destructive or irreversible actions, unrequested external-state changes, unresolved material dependency risk, or weakening authentication, authorization, validation, sandboxing, or encryption.
- Lead with the outcome. Include only information needed to understand the result, evidence, risk, or next action; omit pleasantries, request restatements, meta-commentary, fixed templates, and empty summaries.
```

这段内容故意不保留任务规模表、调试步骤、性能清单、工具名和输出模板。它们不是每个任务都需要，应该由项目规则、系统能力或对应 Skill 提供。

### 执行顺序

1. 发布远端，再从远端安装。
   - 只提交本方案涉及的仓库文件，不夹带无关改动。
   - 固定顺序：`commit → push → 核对远端 SHA → 安装`。

     ```sh
     git add -A README.md coding-skills-review.md daily-engineering-skills-plan.md skills/ scripts/ tests/
     git commit -m "refactor skills-based engineering guidance"
     git push origin HEAD
     test "$(git rev-parse HEAD)" = "$(git ls-remote origin "refs/heads/$(git branch --show-current)" | cut -f1)"
     skills add https://github.com/3AceShowHand/agent-skills.git -g -a codex pi --skill '*' -y
     skills list -g -a codex --json
     skills list -g -a pi --json
     ```

   - 两个 agent 都必须显示来自该远端的完整自有 Skill 集合；任一安装失败都不切换全局入口。

2. 切换常驻行为。
   - Ponytail 已经是 `defaultMode: off`；新流程的验收不依赖其显式命令。
   - 用“最小全局入口”替换 Codex 和 Pi 的 `AGENTS.md`。
   - 旧 Rules 在新入口生效后停止使用；验收不通过时修正新入口和 Skills，不恢复旧架构。

3. 分别启动新的 Codex 和 Pi 会话做验收。
   - 小型单文件修改：不应加载 `feature-development` 或专项 Skill。
   - 非平凡 feature/enhancement：应加载 `feature-development`，并给出目标、风险和验证计划。
   - 实质性模块、接口、所有权或生命周期设计：由 `software-design` 统一原则；实现仍由 `feature-development` 编排，审查仍由 `code-review` 汇总 findings。
   - bug、兼容性、迁移、性能、分布式、可观测性、重构和深度 review：应由对应专项 Skill 主导，通用 Skill 不重复长检查表。
   - 架构、调用链和影响分析：有现成 CodeGraph 索引时走图工具；没有时退回 `rg`/读取，不自动建索引。
   - 库或 SDK 文档：由 `context7-mcp` 处理；业务逻辑和普通重构不得触发它。
   - todo 文档：有清晰分组和任务子项，完成项会被删除。
   - 项目内存在 `AGENTS.md` 时，仍能读取并遵守项目的构建、测试和完成标准。
   - 不调用 Ponytail 时，仍能保持最小 diff、YAGNI、必要测试和交付前复杂度检查。

4. 收尾。
   - 两个 agent 全部通过后，卸载整个 Ponytail plugin，并确认新会话不再加载其 Skills。
   - 两个 agent 全部通过后，永久删除 7 份旧 Codex Rule 文件，不保留 `retired/` 或迁移副本。
   - 从本文删除整个 P0 迁移任务，只留下尚未审查的 Skills。
   - 任一验收不通过：修正新的 Skills 或 `AGENTS.md` 后重新验收，不恢复旧 Rules、Ponytail 默认模式或已卸载 Skills。

### 验收标准

- Codex 和 Pi 各自只常驻一份短 `AGENTS.md`，正文没有外部 Markdown include。
- 两个 agent 通过 `skills` CLI 使用同一远端、同一版本的自有 Skills；没有手工复制或孤立符号链接。
- 通用 Skill 与专项 Skill 的触发边界通过正反样例；普通小任务没有额外流程负担。
- 审查、迁移和非平凡实施任务首次交付完整方案；“完成后报告下一项”不会再退化成逐步向用户索取决定。
- 验证结果只报告实际执行过的命令；项目 `AGENTS.md` 的约束没有丢失。
- 自有工程流程在不调用 Ponytail 的情况下保持最小改动和 YAGNI；验收后卸载整个插件并永久删除旧 Rules。

### 尚待移除的常驻插件

- [ ] 自有工作流通过最小改动和 YAGNI 场景验证后，卸载 Ponytail plugin（`/Users/edison/.codex/plugins/cache/ponytail/ponytail/4.8.4/skills/ponytail/SKILL.md:1`）。
  - 引入目的：约束最小改动、YAGNI 和过度设计。
  - 当前状态：插件版本为 `4.8.4`，共享配置是 `defaultMode: off`，普通编码任务不再由它控制。
  - 替代方式：`feature-development` 在实现前限制范围和设计复杂度，`code-review` 在交付前检查无关改动、提前抽象和可删除复杂度。
  - 完成条件：Codex 和 Pi 不调用 Ponytail 也能通过相应场景测试；随后卸载插件并验证新会话。

## P1｜直接影响代码与交付

### 我们自己的 Skills

- [ ] `compatibility-check`（`/Users/edison/workspace/agent-skills/skills/compatibility-check/SKILL.md:1`）。
- [ ] `diagnose-and-fix-bugs`（`/Users/edison/workspace/agent-skills/skills/diagnose-and-fix-bugs/SKILL.md:1`）。
- [ ] `distributed-systems-reliability`（`/Users/edison/workspace/agent-skills/skills/distributed-systems-reliability/SKILL.md:1`）。
- [ ] `migration-safety`（`/Users/edison/workspace/agent-skills/skills/migration-safety/SKILL.md:1`）。
- [ ] `observability-readiness`（`/Users/edison/workspace/agent-skills/skills/observability-readiness/SKILL.md:1`）。
- [ ] `performance-engineering`（`/Users/edison/workspace/agent-skills/skills/performance-engineering/SKILL.md:1`）。
- [ ] `project-agents-bootstrap`（`/Users/edison/workspace/agent-skills/skills/project-agents-bootstrap/SKILL.md:1`）。
- [ ] `refactor`（`/Users/edison/workspace/agent-skills/skills/refactor/SKILL.md:1`）。
