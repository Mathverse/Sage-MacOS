#! /usr/bin/env python3
import platform
import subprocess
import json
import re

cpu = platform.machine()
output_file = 'hashes_%s.json'%cpu
version_file = 'Sage_framework/repo/sage/VERSION.txt'
version_re = re.compile('SageMath version ([0-9]\.[0-9]*)')
with open(version_file) as input_file:
    m = version_re.match(input_file.readline())
    sage_version = m.groups()[0]
dist_file = 'SageMath-%s_%s.dmg'%(sage_version, cpu)

def main():
    md5 = subprocess.run(
        ['md5', dist_file],
        capture_output=True).stdout.decode('ascii').split()[-1]
    sha256 = subprocess.run(
        ['shasum', '-b', '-a', '256', dist_file],
        capture_output=True).stdout.decode('ascii').split()[0]
    hashes = {'file': dist_file, 'md5': md5, 'sha256': sha256}
    with open(output_file, 'w') as output:
        output.write(json.dumps(hashes, sort_keys=True, indent=4))
        output.write('\n')
    
if __name__ == '__main__':
    main()
    
