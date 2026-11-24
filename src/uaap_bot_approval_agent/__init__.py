"""Approval Agent: a UAAP bot, packaged on its own. Installing it registers it with the UAAP kernel."""

from uaap.bots.catalog import BotSpec

SPEC = BotSpec(
    id="approval-agent",
    name="Approval Agent",
    version="0.1.0",
    kind="agent",
    module="uaap_bot_approval_agent.agent",
    class_name="ApprovalAgent",
    needs_model=True,
    needs_inbox=True,
    summary="Reads the approvals inbox; never approves or rejects.",
)
