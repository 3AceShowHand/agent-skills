# 日常开发 Skills 规划与 Rules 迁移方案

目标已经确认：Codex 和 Pi 使用同一套远端安装的自有 Skills，通过覆盖日常开发主流程和高风险专项，提高编码质量与效率，尽量在实现和交付前发现问题，减少返工。全局 `AGENTS.md` 只保留每次任务都必须成立的安全与执行底线。

本文只保留尚待确认或执行的事项。确认一项填写 `回复：y`；有问题、条件或修改建议时直接写具体内容。

## P0 执行流程

方案确认后连续执行以下阶段。正常实施步骤不再逐项要求新的用户决定；只有范围、权限、外部副作用或不可逆结果出现真实阻塞时才暂停。

- [ ] 阶段 1：提交、推送并统一安装。
  - 审查 unstaged、staged、未跟踪文件和最终 diff；运行 `git diff --check`。
  - 固定顺序：commit → push → 核对远端 SHA → 使用 `skills` CLI 安装。
  - Codex 和 Pi 从同一远端、同一 commit 安装全部自有 Skills。
  - 任一安装或版本核对失败，都不切换全局入口。
  - 完成条件：两个 agent 的自有 Skill 名称、来源和内容 hash 一致。
  - 回复：

    > （待填写）

- [ ] 阶段 2：切换 Codex/Pi 常驻行为并用新会话验收。
  - 两个 agent 使用相同的短 `AGENTS.md`，只保留正确性、安全、范围、最小修改、验证诚实、项目规则归属和权限边界。
  - `AGENTS.md` 不再 include 外部 Markdown Rule 文件。
  - Ponytail 保持 `defaultMode: off`；验收期间不依赖其显式 review/audit 能力。
  - 旧 Rules 在新入口生效后停止使用；验收不通过时修正新入口和 Skills，不恢复旧架构。
  - 小型单文件修改不触发完整 feature 流程。
  - feature/enhancement 使用 `feature-development`；bug/debug、refactor 和 code review 分别由对应主 Skill 主导。
  - 根据改动风险补充并运行必要的高质量测试。
  - 不调用 Ponytail，仍能保持最小 diff、简单设计和交付前复杂度检查。
  - CodeGraph 不可用时正确回退到 `rg` 和精确读取；外部库文档由 `context7-mcp` 处理。
  - 项目内 `AGENTS.md` 的构建、测试和完成标准仍然有效。
  - 完成条件：常驻内容只包含每个任务都必须成立的底线；两个 agent 对相同场景选择一致的主流程，不重复加载宽泛 Skills。
  - 回复：

    > （待填写）

- [ ] 阶段 3：完成 P0。
  - 验收通过：卸载整个 Ponytail plugin，并确认 Codex 新会话不再加载其 Skills。
  - 验收通过：永久删除 7 份旧 Codex Rule 文件，不保留 `retired/` 或其他迁移副本。
  - 验收通过：从 `coding-skills-review.md` 删除整个已完成的 P0，只保留尚未审查的 Skills。
  - 验收不通过：修正新的 Skills 或 `AGENTS.md` 后重新验收，不恢复旧 Rules、Ponytail 默认模式或已卸载 Skills。
  - 完成条件：Codex/Pi 共享同一套自有 Skills，最小全局入口生效，旧 Rules 已删除，review 文档已缩短。
  - 回复：

    > （待填写）
