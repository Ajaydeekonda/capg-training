import os

def get_current_directory():
    """Get the current working directory."""
    return os.getcwd()

def list_files_in_directory(path="."):
    """List all files and directories in a given directory."""
    return os.listdir(path)

def create_directory(directory_name):
    """Create a new directory."""
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

def remove_directory(directory_name):
    """Remove a directory (if empty)."""
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' removed successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")
    except OSError:
        print(f"Directory '{directory_name}' is not empty and cannot be removed.")

def rename_file(old_name, new_name):
    """Rename a file."""
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}'.")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")

def get_environment_variable(var_name):
    """Get the value of an environment variable."""
    return os.getenv(var_name, "Not Found")

def execute_system_command(command):
    """Execute a system command."""
    os.system(command)

def get_system_info():
    """Get system-related information."""
    return {
        "Operating System": os.name,
        "Current Working Directory": os.getcwd(),
        "User": os.getlogin(),
    }

# Example Usage
if __name__ == "__main__":
    print("Current Directory:", get_current_directory())
    
    print("\nFiles in Current Directory:")
    print(list_files_in_directory())

    create_directory("TestFolder")

    rename_file("old_file.txt", "new_file.txt")  # Ensure old_file.txt exists

    print("\nEnvironment Variable (PATH):")
    print(get_environment_variable("PATH"))

    print("\nSystem Information:")
    print(get_system_info())

    execute_system_command("echo Hello, OS Module!")  # Windows/Linux compatible command

    remove_directory("TestFolder")
