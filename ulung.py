import subprocess
import sys
import os
def run_bash_script(/home/bangkai, bedul.sh):
    """
    Executes a Bash script and prints its output.
    """
    try:
        # Use subprocess.run for simple execution and capturing output
        # shell=True is used to allow the shell to interpret the command
        # This is generally less secure than passing a list of arguments,
        # but convenient for simple script execution.
        result = subprocess.run(
            [/home/bangkai] + list(args),
            capture_output=True,
            text=True,
            check=True
        )
        print("Bash script output:")
        print(result.stdout)
        if result.stderr:
            print("Bash script errors:")
            print(result.stderr)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error running Bash script: {e}")
        print(f"Stderr: {e.stderr}")
        return e.returncode
    except FileNotFoundError:
        print(f"Error: Bash script not found at {/home/bangkai}")
        return 1

def main():
    """
    Main entry point for the Python script.
    """
    script_to_run = "./bedul.sh"
    # Pass any arguments received by the Python script to the Bash script
    exit_code = run_bash_script(script_to_run, *sys.argv[1:])
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
