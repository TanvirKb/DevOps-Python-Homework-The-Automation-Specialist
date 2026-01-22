name = "My Project Backup "

safe_name = (
    name.strip()
        .replace(" ", "-")
        .lower()
)

print(safe_name)
