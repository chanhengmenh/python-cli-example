# tests/test_main.py

from click.testing import CliRunner
from blkpy.main import main

def test_main_command():
    runner = CliRunner()
    result = runner.invoke(main, ['sda'])

    assert result.exit_code == 0
    assert "Device: sda" in result.output
    assert "Verbose: False" in result.output
    # The run_lsblk output will be a JSON string, so we can check for basic structure
    assert "name" in result.output
    assert "type" in result.output
