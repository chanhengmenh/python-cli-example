# tests/test_util.py

from blkpy.util import run_lsblk

def test_run_lsblk():
    output = run_lsblk('sda')  # Replace 'sda' with a mock or test-safe device name
    assert isinstance(output, str)
    assert "sda" in output or "NAME" in output  # Loose check
