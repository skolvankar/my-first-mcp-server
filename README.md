# MyFirstMCPServer

A small [MCP](https://modelcontextprotocol.io) server built with [FastMCP](https://gofastmcp.com) 4.1.4. It exposes arithmetic tools that a client such as Cursor can call.

## Tools

| Tool | Arguments | Result |
| --- | --- | --- |
| `add` | `a`, `b` | `a + b` |
| `subtract` | `a`, `b` | `a - b` |
| `divide` | `a`, `b` | `a / b`. Raises an error when `b` is `0`. |
| `power` | `a`, `b` | `a ** b` |
| `fraction` | `number` | `1 / number`. `12.5` returns `0.08`. Raises an error when `number` is `0`. |

Every argument and return value is a float. `multiply` is present in `mcp_server_01.py` but commented out, so it is not registered.

## Setup

Python 3.10 or newer is required.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install .
```

Install inside this virtual environment. Installing FastMCP into the global Python interpreter upgrades shared packages and can conflict with other projects.

## Run

Two commands start the same server on different transports.

**stdio.** This is what Cursor and `fastmcp run` use. The process waits for an MCP client on stdin. The terminal stays quiet after the banner.

```powershell
fastmcp run mcp_server_01.py
```

**SSE.** This runs only when Python executes the file directly. The server listens at `http://127.0.0.1:8000/sse`.

```powershell
python mcp_server_01.py
```

`fastmcp run` imports the file, so the `if __name__ == "__main__"` block does not run. That command stays on stdio unless you pass a transport:

```powershell
fastmcp run mcp_server_01.py --transport sse --host 127.0.0.1 --port 8000
```

## Use it from Cursor

Add this to `mcp.json` under `mcpServers`. Use the full path of the script. A `cwd` entry is not applied, and a relative filename is resolved from your home folder.

```json
{
  "mcpServers": {
    "my-first-server": {
      "command": "C:\\Users\\skolvankar\\Downloads\\[Day20]Multi Agent Collaborative Systems Part 1\\CodingDay\\.venv\\Scripts\\fastmcp.exe",
      "args": [
        "run",
        "C:\\Users\\skolvankar\\Downloads\\[Day20]Multi Agent Collaborative Systems Part 1\\CodingDay\\mcp_server_01.py"
      ]
    }
  }
}
```

Refresh **my-first-server** in **Cursor Settings → Tools & MCP** after any change to `mcp_server_01.py`. Then ask the agent to call a tool, for example: "Use my-first-server to add 3 and 5."

You can also call the tools in a browser with the MCP Inspector:

```powershell
fastmcp dev inspector mcp_server_01.py
```
