import click
from blkpy.util import run_lsblk
import json

@click.command()
@click.option('--verbose', '-v', is_flag=True)
@click.argument('device')
def main(device, verbose):
    print(f"Device: {device}")
    print(f"Verbose: {verbose}")
    
    result = run_lsblk(device)
    if result:
        print(json.dumps(result, indent=2))
    else:
        print(f"Device {device} not found")
        exit(1)
