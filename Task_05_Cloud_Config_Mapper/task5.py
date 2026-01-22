vm = {
    "id": "vm-12345",
    "ip": "192.168.1.10",
    "status": "running",
    "region": "us-east-1"
}

vm["status"] = "stopped"

vm["instance_type"] = "t3.large"

print(vm)
