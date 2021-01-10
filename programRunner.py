import sys
from subprocess import Popen, PIPE

class ProgramRunner():

    def runFile(self, filePath: str, timeout: int):
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