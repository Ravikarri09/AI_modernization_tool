import os

def scan_files(root_dir):
    files = []
    for root, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith((".py", ".java", ".php", ".js", ".ts")):
                files.append(os.path.join(root, file))
    return files
