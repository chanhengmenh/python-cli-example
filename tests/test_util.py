from blkpy import util
import subprocess
import json

def test_run_lsblk_mock(monkeypatch):
    mock_output = json.dumps({
        "blockdevices": [
            {
                "name": "sda", "size": "100G", "type": "disk", "mountpoint": None,
                "children": [
                    {"name": "sda1", "size": "100G", "type": "part", "mountpoint": "/"}
                ]
            }
        ]
    }).encode('utf-8')

    def mock_check_output(cmd):
        return mock_output

    monkeypatch.setattr(subprocess, "check_output", mock_check_output)

    result = util.run_lsblk('sda')
    assert result['name'] == 'sda'
    assert result['type'] == 'disk'

