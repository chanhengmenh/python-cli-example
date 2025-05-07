from blkpy import util
import subprocess
import json

def test_run_lsblk_mock(monkeypatch):
    mock_output = json.dumps({
        "blockdevices": [
            {
                "name": "sda", 
                "size": "100G", 
                "type": "disk", 
                "mountpoint": None,
                "children": [
                    {"name": "sda1", "size": "100G", "type": "part", "mountpoint": "/"}
                ]
            }
        ]
    }).encode('utf-8')

    def mock_check_output(cmd):
        assert 'lsblk' in cmd
        assert '-J' in cmd
        return mock_output

    monkeypatch.setattr(subprocess, "check_output", mock_check_output)

    result = util.run_lsblk('sda')
    assert result is not None
    assert result['name'] == 'sda'
    assert result['type'] == 'disk'
    assert result['size'] == '100G'
    assert result['mountpoint'] is None
    assert 'children' in result
    assert len(result['children']) == 1
    assert result['children'][0]['name'] == 'sda1'

