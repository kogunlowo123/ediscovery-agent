"""eDiscovery Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_initiate_hold():
    """Test Initiate legal hold and notify custodians."""
    tools = AgentTools()
    result = await tools.initiate_hold(matter_id="test", custodians="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_collect_documents():
    """Test Collect documents from specified data sources."""
    tools = AgentTools()
    result = await tools.collect_documents(matter_id="test", sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_run_tar():
    """Test Run technology-assisted review on document collection."""
    tools = AgentTools()
    result = await tools.run_tar(matter_id="test", seed_set="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_custodian_compliance():
    """Test Track custodian acknowledgment and compliance with legal hold."""
    tools = AgentTools()
    result = await tools.track_custodian_compliance(matter_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ediscovery_agent_agent import EdiscoveryAgentAgent
    agent = EdiscoveryAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
