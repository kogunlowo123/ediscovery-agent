"""Test configuration for eDiscovery Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ediscovery-agent", "category": "Legal"}
