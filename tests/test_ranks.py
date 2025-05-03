"""Tests for ranking logic."""

import os

from dotenv import load_dotenv

from src.rankgun.main import Client

load_dotenv()


TOKEN = os.environ["RANKGUN_TOKEN"]
WID = os.environ["WORKSPACE_ID"]
TESTINGUSERID = os.environ["TESTING_USER_ID"]

client = Client(wid=WID, token=TOKEN)


def test_set_rank_one():
    """Sets the rank of a test user."""
    assert client.setRank(TESTINGUSERID, 3).user == f"users/{TESTINGUSERID}"


def test_promotion():
    """Promote a test user."""
    assert client.promote(TESTINGUSERID).user == f"users/{TESTINGUSERID}"


def test_demotion():
    """Demote a test user."""
    assert client.demote(TESTINGUSERID).user == f"users/{TESTINGUSERID}"


def test_set_rank_two():
    """Sets the rank of a test user."""
    assert client.setRank(TESTINGUSERID, 2).user == f"users/{TESTINGUSERID}"
