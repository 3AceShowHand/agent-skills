# 编码 Skills 与 Rules 审查任务

只保留尚未执行或尚未确认的事项。完成一项后删除对应任务及说明，让文档持续变短；优先级只在分组标题中表达。

## P0｜全局 Rules 迁移与常驻行为

- [ ] 执行本节方案，把 Codex 和 Pi 收敛为“最小全局入口 + 共享工程 Skills”。
  - 范围：本仓库 Skills、`/Users/edison/.codex/AGENTS.md`、其引用的 7 份 Markdown、`/Users/edison/.pi/agent/AGENTS.md` 和 Ponytail 默认模式。
  - 不包含：本节不顺带审查 P1/P2 的全部第三方 Skills，也不把仓库级构建、测试和架构规则搬进全局配置。
  - 完成条件：按下述顺序实现、发布、安装、切换和验收；通过后删除本节。

### 已定结论

Codex 的 `AGENTS.md` 会确定性进入每次任务；Skill 只在显式调用或 description 命中时加载正文。因此，长期不变且每次都必须成立的底线留在 `AGENTS.md`，任务型流程进入 Skill。这个边界符合 [Codex 的 AGENTS.md 说明](https://learn.chatgpt.com/docs/agent-configuration/agents-md) 和 [Skill 渐进加载模型](https://learn.chatgpt.com/docs/build-skills)。

最终结构如下：

- 全局底线
  - 所有者：Codex、Pi 各自的 `AGENTS.md`。
  - 内容：正确性与安全、用户范围、最小修改、验证诚实、破坏性操作边界、项目规则归属、Skill 缺失时的保守行为。
  - 加载：每次任务确定性加载。

- 通用工程流程
  - 所有者：本仓库 `engineering-workflow`。
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

### 逐文件处理

- `/Users/edison/.codex/AGENTS.md`
  - 处理：保留并重写。
  - 最终归属：最小全局入口，不再引用其他 Markdown。

- `karpathy-coding-guidelines.md`
  - 处理：合并后移除。
  - 最终归属：真正常驻的部分并入最小 `AGENTS.md`；工程流程进入 `engineering-workflow`；不创建同名 Skill。

- `codex-core-rules.md`
  - 处理：压缩后移除。
  - 最终归属：安全、范围和验证底线并入最小 `AGENTS.md`。

- `codex-output-style.md`
  - 处理：压缩后移除。
  - 最终归属：只保留“结果优先、简洁、如实报告验证”；任务模板不保留。

- `engineering.md`
  - 处理：拆分后移除。
  - 最终归属：通用流程进入 `engineering-workflow`；专项内容由现有工程 Skills 接管。

- `todo-documents.md`
  - 处理：合并后移除。
  - 最终归属：进入 `write-great-document/references/task-lists.md`。

- `codex-tool-routing.md`
  - 处理：拆分后移除。
  - 最终归属：代码结构进入 `codebase-navigation`；Context7 由 `context7-mcp` 接管；删除没有可靠配置来源的 `context-mode` 路由。

- `codex-skill-routing.md`
  - 处理：直接移除。
  - 最终归属：Skill 的 description 和显式调用负责路由；不再强制所有 `chat/status/docs` 加载 `shuorenhua`。

- `/Users/edison/.pi/agent/AGENTS.md`
  - 处理：重写。
  - 最终归属：与 Codex 使用同一组底线，不再复制工程、工具和 todo 细则。

`engineering.md` 的专项归属固定如下：

- `diagnose-and-fix-bugs`：bug 复现、根因和回归测试。
- `api-compatibility-review`：公共 API、CLI、配置和格式兼容性。
- `performance-engineering`：性能基线、profiling 和复测。
- `distributed-systems-reliability`：分布式状态、进展、重试和恢复。
- `observability-readiness`：日志、指标、trace、告警和回滚信号。
- `migration-safety`：schema、持久化数据和不可逆状态。
- `refactor-safety`：行为保持型重构。
- `engineering-review`：合并前的深度代码与设计审查。

第三方 `implement` 不作为通用工程流程的所有者：它只有简短的 spec → TDD → review → commit 流程，依赖 slash command，并默认提交代码，无法覆盖当前规则中的风险识别、专项路由、验证诚实和回滚要求。

### 尚待执行的仓库任务

- [ ] 新增 `skills/engineering-workflow/`。
  - 目的：为非平凡、多步骤的工程实现或设计提供完整计划和执行流程。它负责目标、非目标、假设、风险、方案、验证、发布、回滚和完成标准。
  - 计划合同：开始工作前一次性给出所有已知阶段。用户要求“每完成一项告诉我下一项”时，从既有计划报告进度，不把普通阶段转换成新的用户决策点。
  - 分工：bug、重构、迁移、性能、API 兼容性、分布式可靠性和纯 review 任务优先使用对应专项 Skill。
  - 边界：不自动 commit，不重复专项 Skill 的长检查表，不接管项目 `AGENTS.md`。
  - 文件：`SKILL.md` 和 `agents/openai.yaml`；只有正文超过合理长度时才增加 `references/`。

- [ ] 新增 `skills/codebase-navigation/`。
  - 目的：处理陌生代码库理解、架构与调用链追踪、符号关系、变更影响和模块归属定位。
  - 路由：有 CodeGraph 工具且仓库已有 `.codegraph/` 时优先结构查询；工具或索引不可用时直接退回 `rg`、文件列表和精确读取。
  - 边界：不为普通精确文本查找调用 CodeGraph；不擅自初始化索引；不重复查询已由图结果回答的事实；不负责外部库文档。
  - 文件：`SKILL.md` 和 `agents/openai.yaml`。

- [ ] 更新 `README.md`，补充 `engineering-workflow` 和 `codebase-navigation`。
  - 把 Codex + Pi 的标准安装命令固定为：

     ```sh
     skills add https://github.com/3AceShowHand/agent-skills.git -g -a codex pi --skill '*' -y
     ```

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
- Ask before destructive or irreversible actions, adding production dependencies, or weakening authentication, authorization, validation, sandboxing, or encryption.
- Lead with the outcome and keep progress updates concise.
```

这段内容故意不保留任务规模表、调试步骤、性能清单、工具名和输出模板。它们不是每个任务都需要，应该由项目规则、系统能力或对应 Skill 提供。

### 执行顺序

1. 建立可恢复基线。
   - 记录 `git status --short`。
   - 用 `git diff` 检查 unstaged（工作区已修改但尚未加入下一次提交的内容），用 `git diff --cached` 检查 staged（已加入 Git index、准备进入下一次 commit 的内容）。两者都必须审查。
   - 在 `/Users/edison/.codex/backups/rules-migration-pre-switch/` 备份 Codex 的 8 份文件、Pi 的 `AGENTS.md`、`/Users/edison/.codex/config.toml` 和 `/Users/edison/.config/ponytail/config.json`。若目录已存在则停止，换一个明确的新目录，不覆盖旧备份。

2. 在本仓库实现剩余变更。
   - 新增 `engineering-workflow`。
   - 新增 `codebase-navigation`。
   - 更新 `README.md`。
   - 暂不修改全局入口，保证实现阶段仍可使用旧 Rules。

3. 验证仓库改动。
   - 对所有 `skills/*/SKILL.md` 检查 YAML frontmatter、name 与目录一致、description 清楚、相对链接存在。
   - 使用 Skill Creator 的 validator；本机有 `uv`，用临时依赖运行，避免修改仓库依赖：

     ```sh
     for skill_dir in skills/*; do
       uv run --with pyyaml python /Users/edison/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill_dir"
     done
     ```

   - 为两个新 Skill 各做至少 3 个应触发、3 个不得触发样例；检查专项任务不会被通用 `engineering-workflow` 抢占。
   - 运行 `git diff --check`，再次审查 `git diff`、`git diff --cached` 和 `git status --short`。

4. 发布远端，再从远端安装。
   - 只提交本方案涉及的仓库文件，不夹带无关改动。
   - 固定顺序：`commit → push → 核对远端 SHA → 安装`。

     ```sh
     git add README.md coding-skills-review.md skills/engineering-workflow skills/codebase-navigation
     git commit -m "refactor skills-based engineering guidance"
     git push origin HEAD
     test "$(git rev-parse HEAD)" = "$(git ls-remote origin "refs/heads/$(git branch --show-current)" | cut -f1)"
     skills add https://github.com/3AceShowHand/agent-skills.git -g -a codex pi --skill '*' -y
     skills list -g -a codex --json
     skills list -g -a pi --json
     ```

   - 两个 agent 都必须显示来自该远端的完整自有 Skill 集合；任一安装失败都不切换全局入口。

5. 切换常驻行为。
   - 把 `/Users/edison/.config/ponytail/config.json` 的 `defaultMode` 从 `lite` 改为 `off`，保留插件及其显式命令，避免它继续控制所有编码任务。Ponytail 的 review/audit 等能力仍留在后续清单单独审查。
   - 用“最小全局入口”替换 Codex 和 Pi 的 `AGENTS.md`。
   - 先保留 7 份旧 Codex Rule 文件；新入口不再引用它们，因此可以随时恢复旧 `AGENTS.md` 回滚。

6. 分别启动新的 Codex 和 Pi 会话做验收。
   - 小型单文件修改：不应加载 `engineering-workflow` 或专项 Skill。
   - 非平凡多步骤实现：应加载 `engineering-workflow`，并给出目标、风险和验证计划。
   - bug、公共 API、迁移、性能、分布式、可观测性、重构和深度 review：应由对应专项 Skill 主导，通用 Skill 不重复长检查表。
   - 架构、调用链和影响分析：有现成 CodeGraph 索引时走图工具；没有时退回 `rg`/读取，不自动建索引。
   - 库或 SDK 文档：由 `context7-mcp` 处理；业务逻辑和普通重构不得触发它。
   - todo 文档：有清晰分组和任务子项，完成项会被删除；普通聊天不得仅因是用户可见文本而加载 `shuorenhua`。
   - 项目内存在 `AGENTS.md` 时，仍能读取并遵守项目的构建、测试和完成标准。
   - Ponytail 默认不注入；显式调用仍可用。

7. 收尾或回滚。
   - 两个 agent 全部通过后，把 7 份旧 Codex Rule 文件移动到备份目录的 `retired/`，不要直接永久删除；保留一个审查周期后再决定是否清空备份。
   - 从本文删除整个 P0 迁移任务，只留下尚未审查的 Skills。
   - 任一验收失败：恢复备份中的两个 `AGENTS.md` 和 Ponytail 配置，保留已发布 Skills 但不依赖它们，记录失败样例后再修正。

### 验收标准

- Codex 和 Pi 各自只常驻一份短 `AGENTS.md`，正文没有外部 Markdown include。
- 两个 agent 通过 `skills` CLI 使用同一远端、同一版本的自有 Skills；没有手工复制或孤立符号链接。
- 通用 Skill 与专项 Skill 的触发边界通过正反样例；普通小任务没有额外流程负担。
- 审查、迁移和非平凡实施任务首次交付完整方案；“完成后报告下一项”不会再退化成逐步向用户索取决定。
- 验证结果只报告实际执行过的命令；项目 `AGENTS.md` 的约束没有丢失。
- Ponytail 默认关闭、显式能力保留；旧 Rules 和原配置可从备份恢复。

### 尚需单独审查的常驻插件

- [ ] `ponytail` 插件是否继续保留，以及 `ponytail-review/audit/debt` 与自有审查 Skills 的最终分工（`/Users/edison/.codex/plugins/cache/ponytail/ponytail/4.8.4/skills/ponytail/SKILL.md:1`）。
  - 已知材料：插件当前已启用，版本为 `4.8.4`；共享配置当前是 `defaultMode: lite`。
  - 本方案先把默认模式改为 `off`，原因是主 Skill 声明覆盖所有编码任务，并会额外约束实现和输出；显式 review/audit 能力不受影响。
  - 最终选择：后续根据专项 Skills 审查结果决定保留整个插件、只保留显式能力，或卸载。

## P1｜直接影响代码与交付

### 我们自己的 Skills

- [ ] `api-compatibility-review`（`/Users/edison/workspace/agent-skills/skills/api-compatibility-review/SKILL.md:1`）。
- [ ] `diagnose-and-fix-bugs`（`/Users/edison/workspace/agent-skills/skills/diagnose-and-fix-bugs/SKILL.md:1`）。
- [ ] `distributed-systems-reliability`（`/Users/edison/workspace/agent-skills/skills/distributed-systems-reliability/SKILL.md:1`）。
- [ ] `engineering-review`（`/Users/edison/workspace/agent-skills/skills/engineering-review/SKILL.md:1`）。
- [ ] `migration-safety`（`/Users/edison/workspace/agent-skills/skills/migration-safety/SKILL.md:1`）。
- [ ] `observability-readiness`（`/Users/edison/workspace/agent-skills/skills/observability-readiness/SKILL.md:1`）。
- [ ] `performance-engineering`（`/Users/edison/workspace/agent-skills/skills/performance-engineering/SKILL.md:1`）。
- [ ] `project-agents-bootstrap`（`/Users/edison/workspace/agent-skills/skills/project-agents-bootstrap/SKILL.md:1`）。
- [ ] `refactor-safety`（`/Users/edison/workspace/agent-skills/skills/refactor-safety/SKILL.md:1`）。

### OpenAI

- [ ] `gh-address-comments`：消除重复安装（`/Users/edison/.agents/skills/gh-address-comments/SKILL.md:1`）。
- [ ] `gh-fix-ci`：消除重复安装（`/Users/edison/.agents/skills/gh-fix-ci/SKILL.md:1`）。
- [ ] `security-best-practices`：触发范围和安全覆盖（`/Users/edison/.agents/skills/security-best-practices/SKILL.md:1`）。
- [ ] Codex 内置 `review-agent`：与现有审查 Skills 的分工（`/Users/edison/.codex/skills/.system/review-agent/SKILL.md:1`）。

### Ponytail

- [ ] `ponytail-review`（`/Users/edison/.codex/plugins/cache/ponytail/ponytail/4.8.4/skills/ponytail-review/SKILL.md:1`）。
- [ ] `ponytail-audit`（`/Users/edison/.codex/plugins/cache/ponytail/ponytail/4.8.4/skills/ponytail-audit/SKILL.md:1`）。
- [ ] `ponytail-debt`（`/Users/edison/.codex/plugins/cache/ponytail/ponytail/4.8.4/skills/ponytail-debt/SKILL.md:1`）。

### Matt Pocock

- [ ] `implement`：与全局工程规则是否重复（`/Users/edison/.agents/skills/implement/SKILL.md:1`）。
- [ ] `prototype`：一次性代码边界和验证效率（`/Users/edison/.agents/skills/prototype/SKILL.md:1`）。
- [ ] `resolving-merge-conflicts`（`/Users/edison/.agents/skills/resolving-merge-conflicts/SKILL.md:1`）。
- [ ] `tdd`：触发准确性和流程成本（`/Users/edison/.agents/skills/tdd/SKILL.md:1`）。

### Wondelai

- [ ] `clean-code`：可执行性及与全局编码规则的重复（`/Users/edison/.agents/skills/clean-code/SKILL.md:1`）。
- [ ] `refactoring-patterns`：与自研 `refactor-safety` 的分工（`/Users/edison/.agents/skills/refactoring-patterns/SKILL.md:1`）。

### 其他来源

- [ ] `cherry-pick-release-pr`：外部副作用和使用边界（`/Users/edison/.agents/skills/cherry-pick-release-pr/SKILL.md:1`）。
- [ ] `ci-diagnose`：与 `gh-fix-ci` 的分工（`/Users/edison/.agents/skills/ci-diagnose/SKILL.md:1`）。

## P2｜设计、规划与元能力

### OpenAI

- [ ] Codex 内置 `openai-docs`（`/Users/edison/.codex/skills/.system/openai-docs/SKILL.md:1`）。
- [ ] Codex 内置 `plugin-creator`（`/Users/edison/.codex/skills/.system/plugin-creator/SKILL.md:1`）。

### Ponytail

- [ ] `ponytail-gain`：是否有实际决策价值（`/Users/edison/.codex/plugins/cache/ponytail/ponytail/4.8.4/skills/ponytail-gain/SKILL.md:1`）。
- [ ] `ponytail-help`：是否值得进入 Skill 集合（`/Users/edison/.codex/plugins/cache/ponytail/ponytail/4.8.4/skills/ponytail-help/SKILL.md:1`）。

### Matt Pocock

- [ ] `ask-matt`：路由收益和上下文成本（`/Users/edison/.agents/skills/ask-matt/SKILL.md:1`）。
- [ ] `codebase-design`（`/Users/edison/.agents/skills/codebase-design/SKILL.md:1`）。
- [ ] `domain-modeling`（`/Users/edison/.agents/skills/domain-modeling/SKILL.md:1`）。
- [ ] `grill-with-docs`：与自研文档 Skill 的重叠（`/Users/edison/.agents/skills/grill-with-docs/SKILL.md:1`）。
- [ ] `improve-codebase-architecture`（`/Users/edison/.agents/skills/improve-codebase-architecture/SKILL.md:1`）。
- [ ] `to-issues`（`/Users/edison/.agents/skills/to-issues/SKILL.md:1`）。
- [ ] `to-prd`（`/Users/edison/.agents/skills/to-prd/SKILL.md:1`）。
- [ ] `triage`（`/Users/edison/.agents/skills/triage/SKILL.md:1`）。
- [ ] `handoff`（`/Users/edison/.agents/skills/handoff/SKILL.md:1`）。
- [ ] `setup-matt-pocock-skills`：是否仍有安装价值（`/Users/edison/.agents/skills/setup-matt-pocock-skills/SKILL.md:1`）。

### Wondelai

- [ ] `clean-architecture`（`/Users/edison/.agents/skills/clean-architecture/SKILL.md:1`）。
- [ ] `pragmatic-programmer`（`/Users/edison/.agents/skills/pragmatic-programmer/SKILL.md:1`）。
- [ ] `system-design`（`/Users/edison/.agents/skills/system-design/SKILL.md:1`）。

### 工具集成

- [ ] `context7-mcp`：可用性及与工具路由规则的关系（`/Users/edison/.agents/skills/context7-mcp/SKILL.md:1`）。
