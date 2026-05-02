def copy_file(command: str) -> None:
    files = command.split(" ")
    if len(files) != 3 or files[0] != "cp":
        return
    file1 = files[1]
    file2 = files[2]
    if file1 != file2:
        try:
            with open(file1, "r") as f:
                content = f.read()
            with open(file2, "a") as g:
                g.write(content)
        except FileNotFoundError:
            pass
