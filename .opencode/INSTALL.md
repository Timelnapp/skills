# Timeln Skills — OpenCode Installation

## Install

Add the plugin to your `opencode.json`:

```json
{
  "plugins": [
    {
      "name": "timeln-skills",
      "source": "https://github.com/Timelnapp/skills",
      "path": ".opencode/plugins/timeln-skills.js"
    }
  ]
}
```

## MCP Server

You also need the hosted Timeln MCP. Add to your MCP config:

```json
{
  "mcpServers": {
    "timeln": {
      "url": "https://timeln-mcp-production.up.railway.app/mcp",
      "headers": {
        "Authorization": "Bearer tln_YOUR_TOKEN_HERE"
      }
    }
  }
}
```

Get your token at [app.timeln.app](https://app.timeln.app) → Settings → API Tokens → Create.

## Updating

Pull the latest version of the plugin source and restart OpenCode.

## Troubleshooting

- **Skills not loading**: Confirm the plugin path points to `.opencode/plugins/timeln-skills.js`
- **MCP tools unavailable**: Check your token is valid with the `whoami` tool
- **Windows**: Ensure Node.js is installed and `node` is on your PATH
