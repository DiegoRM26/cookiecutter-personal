import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}Error: Project slug '{project_slug}' is not allowed.{RESET_ALL}")
    sys.exit(1)
    
print(f"{MESSAGE_COLOR}Project slug '{project_slug}' is valid.{RESET_ALL}")
print(f"Creating project at {os.getcwd()}{RESET_ALL}")