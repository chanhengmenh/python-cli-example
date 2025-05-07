# tests/test_main.py

from click.testing import CliRunner
from blkpy.main import main

def test_main_command():
    runner = CliRunner()
    result = runner.invoke(main, ['sda'])

    assert result.exit_code == 0
    assert "Device: sda" in result.output
