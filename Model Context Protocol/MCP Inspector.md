# MCP Inspector

[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is an **interactive developer tool** used for testing and debugging **MCP (Model Context Protocol) Servers**. It allows developers to **inspect, interact, and test MCP-compatible systems** without installing or deploying any full infrastructure.

---

### Why Use MCP Inspector?

- Requires **no setup or installation**
- Useful for **MCP server development, validation, and testing**
- Gives clear visibility into prompts, tools, metadata, and schemas exposed by your MCP server

---

### How to Run It

You can run MCP Inspector locally using `npx`:

```bash
npx @modelcontextprotocol/inspector <command>
```

Or, with arguments:

```bash
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

---

### Key Features

- **Metadata & Content View**  
  Displays server metadata and helps describe available content

- **Prompts Tab**  
  Shows all prompt templates exposed by the MCP server, making it easier to test interactions

- **Tools Tab**  
  Lists all available tools and their schemas.  
  Great for validating tools, input/output definitions, and testing them directly

---

MCP Inspector is a **must-have utility** for anyone building or integrating with MCP servers. It streamlines the development workflow and ensures your tools and prompts are easily testable and debuggable.
