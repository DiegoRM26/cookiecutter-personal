import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing git repository...{RESET_ALL}")

subprocess.run(["git", "init"])
subprocess.run(["git", "add", "*"])
subprocess.run(["git", "commit", "-m", "Initial commit"])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")