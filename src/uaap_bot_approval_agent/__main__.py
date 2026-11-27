"""Serve this bot, and only this bot, as an MCP server over stdio: `python -m uaap_bot_approval_agent`."""

import asyncio

from uaap.bots.mcp_server import serve

raise SystemExit(asyncio.run(serve(["approval-agent"])))
