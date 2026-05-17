# FeiShuSkill

> **一键安装 Feishu MCP，通过 MCP 控制飞书**
>
> 集成飞书（Feishu/Lark）服务的 AI Skill，让 AI 能够操作多维表格、文档、消息、群组等功能

## 📋 目录

- [项目简介](#-项目简介)
- [功能特性](#-功能特性)
- [环境要求](#-环境要求)
- [安装](#-安装)
- [配置飞书凭证与权限](#-配置飞书凭证与权限)
- [快速开始](#-快速开始)
- [用法示例](#-用法示例)
- [高级配置（OAuth）](#-高级配置oauth)
- [故障排查](#-故障排查)
- [开发与贡献](#-开发与贡献)
- [许可证](#-许可证)

## 🌟 项目简介

FeiShuSkill 是一个基于 [MCP（Model Context Protocol）](https://modelcontextprotocol.io/) 的 AI Skill，通过飞书官方 MCP 服务（`@larksuiteoapi/lark-mcp`）将 AI 与飞书开放平台连接，让你可以用自然语言直接控制飞书——查表格、发消息、搜文档、管群组，一句话搞定。

**核心流程：**
```
你的自然语言指令 → AI（Claude 等） → Feishu MCP 服务 → 飞书开放平台 API
```

## ✨ 功能特性

- **多维表格操作**：创建表格、查询/新增/修改/删除记录
- **消息收发**：发送文本、富文本消息到群组或个人
- **文档管理**：搜索文档、获取内容（需 OAuth）
- **群组管理**：创建群组、管理成员、获取群信息
- **权限控制**：添加协作者、设置访问权限
- **联系人管理**：通过邮箱/手机号获取用户信息
- **知识库操作**：搜索 Wiki、获取节点信息（需 OAuth）

## 🖥️ 环境要求

| 依赖 | 说明 |
|------|------|
| **Node.js ≥ 18**（含 `npx`） | 用于运行飞书 MCP 服务 |
| **支持 MCP 的 AI 客户端** | Claude Desktop、Claude Code 等 |
| **飞书企业账号** | 需有权限创建企业自建应用 |

> 无需本地克隆本仓库——Skill 安装只需一条命令，MCP 服务通过 `npx` 自动拉取。

## 📦 安装

### 一键安装（推荐）

使用 [OpenSkills](https://github.com/openskills/openskills) 一键完成 Skill 安装：

```bash
npm i -g openskills
openskills install whatevertogo/FeiShuSkill
```

按照提示填写你的飞书 `App ID` 和 `App Secret`，安装程序会自动写入 MCP 配置。

---

### 手动安装：Claude Desktop

1. 在 Claude Desktop 配置文件中添加 MCP 服务器（详见[配置章节](#-配置飞书凭证与权限)）。

2. 将本项目的 `lark-mcp/SKILL.md` 复制到 skills 文件夹：
   - macOS：`~/Library/Application Support/Claude/skills/`
   - Windows：`%APPDATA%\Claude\skills\`
   - Linux：`~/.config/Claude/skills/`

3. 重启 Claude Desktop。

---

### 手动安装：Claude Code

```bash
# 复制 Skill 文档
cp lark-mcp/SKILL.md ~/.claude/skills/lark-mcp.md
```

然后按[配置章节](#-配置飞书凭证与权限)完成 MCP 服务器配置。

## ⚙️ 配置飞书凭证与权限

### 第一步：获取飞书应用凭证

1. 访问 [飞书开放平台](https://open.feishu.cn/app)
2. 创建一个**企业自建应用**
3. 在「凭证与基础信息」中获取：
   - `App ID`（以 `cli_` 开头）
   - `App Secret`

### 第二步：添加应用权限

在「权限管理」中开启所需权限（按需添加）：

| 权限标识 | 用途 |
|----------|------|
| `bitable:app` | 多维表格读写 |
| `im:message:send_as_bot` | 发送消息 |
| `im:chat` | 群组管理 |
| `docx:document` | 文档读写 |
| `drive:drive` | 云空间 |
| `contact:user.id:readonly` | 查询用户 ID |
| `wiki:wiki:readonly` | 知识库查询 |

### 第三步：配置 MCP 服务器

在你的 AI 客户端配置文件中（如 Claude Desktop 的 `claude_desktop_config.json`）添加：

```json
{
  "mcpServers": {
    "lark-mcp": {
      "command": "npx",
      "args": [
        "-y", "@larksuiteoapi/lark-mcp", "mcp",
        "-a", "<your_app_id>",
        "-s", "<your_app_secret>"
      ]
    }
  }
}
```

将 `<your_app_id>` 和 `<your_app_secret>` 替换为实际值。

> 💡 如需搜索文档或知识库，请参阅[高级配置（OAuth）](#-高级配置oauth)章节。

## 🚀 快速开始

配置完成后，直接向 AI 发出自然语言指令，AI 会自动调用相应的飞书 MCP 工具：

**查询多维表格：**
```
请查询飞书多维表格 appXXXXX 中，状态为"进行中"的所有记录
```

**发送群消息：**
```
向"项目通知群"发送消息："本周任务已更新，请查收"
```

**搜索文档：**
```
搜索包含"Q4 季度报告"的飞书文档
```

### 创建项目管理表格

```
创建一个项目管理表格，包含任务名称、负责人、状态、截止日期字段
```

AI 将调用 `bitable_v1_app_create` → `bitable_v1_appTable_create` → `bitable_v1_appTableField_create`，并使用 `useUAT: true`（用户身份）确保你可以直接访问。

### 批量更新记录

```
将表格 tblXXXXX 中状态为"待处理"的记录更新为"进行中"
```

AI 先调用 `bitable_v1_appTableRecord_search` 查询符合条件的记录，再逐条调用 `bitable_v1_appTableRecord_update` 批量更新。

### 生成周报并发送

```
查询本周已完成的任务，整理成报告发送到项目群 oc_XXXXX
```

AI 查询记录 → 整理数据 → 调用 `im_v1_message_create` 发送富文本消息。

### 获取各类 ID

从 URL 直接读取是最快的方式：

```
多维表格：https://xxx.feishu.cn/base/appXXXXX?table=tblXXXXX
                                    ↑app_token      ↑table_id

文档：    https://xxx.feishu.cn/docx/doxcXXXXX
                                      ↑document_id
```

或让 AI 帮你查询：
```
列出我有权限访问的所有多维表格
列出我所在的所有群组
```

## 🔐 高级配置（OAuth）

搜索文档（`docx_builtin_search`）和搜索知识库（`wiki_v1_node_search`）需要用户令牌，必须同时配置 `--oauth` 和 `--token-mode user_access_token`：

**1. 登录获取用户令牌：**
```bash
npx -y @larksuiteoapi/lark-mcp login -a <your_app_id> -s <your_app_secret>
```

**2. 更新 MCP 配置：**
```json
{
  "mcpServers": {
    "lark-mcp": {
      "command": "npx",
      "args": [
        "-y", "@larksuiteoapi/lark-mcp", "mcp",
        "-a", "<your_app_id>",
        "-s", "<your_app_secret>",
        "--oauth",
        "--token-mode", "user_access_token"
      ]
    }
  }
}
```

**3. 在飞书开放平台配置重定向 URL：**

「应用」→「安全设置」→「重定向 URL」中添加：
```
http://localhost:3000/callback
```

**4. 重启 AI 客户端。**

| 场景 | 无 OAuth | 有 OAuth |
|------|:-------:|:-------:|
| 多维表格操作 | ✅ | ✅ |
| 发送消息 | ✅ | ✅ |
| 搜索文档/知识库 | ❌ | ✅ |
| 资源创建者为当前用户 | ❌ | ✅ |

## ❓ 故障排查

### AI 提示"工具未找到"

- MCP 服务未启动——检查配置文件中的 `mcpServers` 是否正确
- 是否mcp配置中加入了-t等，他会限制工具数目和内容
- 重启 AI 客户端

### 错误码 99991663

仅配置 `--oauth` 不够，必须同时加 `--token-mode user_access_token`，详见[高级配置](#-高级配置oauth)。

### `redirect_uri_mismatch` 错误

在飞书开放平台的应用安全设置中添加重定向 URL：`http://localhost:3000/callback`

### 权限不足（403）

检查飞书应用的「权限管理」，确认已开启对应权限并发布版本。

### 创建的资源无法访问

使用租户身份（`useUAT: false`，默认）创建的资源，创建者为应用而非用户。告知 AI"请使用用户身份（useUAT: true）创建"。

### 消息发送失败

- 确认机器人已加入目标群组
- 群组用 `receive_id_type: chat_id`，个人用 `open_id`

更多错误码参考 [lark-mcp/reference/troubleshooting.md](lark-mcp/reference/troubleshooting.md)。

## 🤝 开发与贡献

欢迎提交 Issue 反馈问题，或通过 Pull Request 改进文档与示例：

1. Fork 本仓库
2. 创建分支：`git checkout -b feat/your-feature`
3. 提交修改：`git commit -m 'feat: 描述你的改动'`
4. 推送并发起 PR

**文档结构：**

| 文件 | 说明 |
|------|------|
| `lark-mcp/SKILL.md` | Skill 核心技术文档（工具列表、参数、工作流） |
| `lark-mcp/plugin.json` | MCP 服务器配置模板 |
| `lark-mcp/reference/` | 各功能参考文档 |
| `lark-mcp/examples/` | 多维表格查询、消息格式示例 |

## 📄 许可证

[MIT License](LICENSE) © 2026 whatevertogo

## 🙏 致谢

- [飞书开放平台](https://open.feishu.cn/)
- [@larksuiteoapi/lark-mcp](https://www.npmjs.com/package/@larksuiteoapi/lark-mcp)
- [MCP 协议](https://modelcontextprotocol.io/)
