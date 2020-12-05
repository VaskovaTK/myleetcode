import sys
from subprocess import Popen, PIPE

def runFile(filePath, timeout):
    process = Popen(['python', filePath], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = process.communicate(timeout=60)

    for line in iter(process.stdout.readline, b''):
        # sys.stdout.write(line)
        sys.stdout.buffer.write(b"output: ")
        sys.stdout.buffer.write(line)

    for line in iter(process.stderr.readline, b''):
        # sys.stdout.write(line)
        sys.stdout.buffer.write(b"error: ")
        sys.stdout.buffer.write(line)