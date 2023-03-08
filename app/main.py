import subprocess
import sys


def main():

    command = sys.argv[3]
    args = sys.argv[4:]
    
    completed_process = subprocess.run(
        [command, *args], capture_output=False, stdout=sys.stdout, stderr=sys.stderr
    )


if __name__ == "__main__":
    main()
