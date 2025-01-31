import sys

def get_python_version():
    """Get the current Python version."""
    return sys.version

def get_command_line_arguments():
    """Retrieve command-line arguments."""
    return sys.argv  # First argument (sys.argv[0]) is the script name

def get_system_platform():
    """Get the platform information (OS)."""
    return sys.platform

def get_recursion_limit():
    """Get the current recursion limit."""
    return sys.getrecursionlimit()

def set_recursion_limit(new_limit):
    """Set a new recursion limit."""
    sys.setrecursionlimit(new_limit)
    print(f"Recursion limit set to {new_limit}")

def get_system_path():
    """Get the list of directories Python searches for modules."""
    return sys.path

def exit_program():
    """Exit the program with a status code."""
    print("Exiting the program...")
    sys.exit(0)  # Status code 0 means normal exit

# Example Usage
if __name__ == "__main__":
    print("Python Version:")
    print(get_python_version())

    print("\nCommand Line Arguments:")
    print(get_command_line_arguments())

    print("\nSystem Platform:")
    print(get_system_platform())

    print("\nRecursion Limit:")
    print(get_recursion_limit())

    print("\nSetting New Recursion Limit to 2000:")
    set_recursion_limit(2000)

    print("\nSystem Path Directories:")
    for path in get_system_path():
        print(path)


