import platform
import psutil
import socket
import time
import subprocess
import os

def get_os_info():
    try:
        os_name = platform.system()
        os_version = platform.version()
        return os_name, os_version
    except Exception as e:
        return "Error retrieving OS info:", str(e)

def get_processor_info():
    try:
        processor_info = platform.processor()
        return processor_info
    except Exception as e:
        return "Error retrieving processor info:", str(e)

def get_memory_info():
    try:
        memory_info = psutil.virtual_memory()
        total_memory_gb = round(memory_info.total / (1024 ** 3), 2)
        return total_memory_gb
    except Exception as e:
        return "Error retrieving memory info:", str(e)

def get_disk_space_info():
    try:
        disk_info = psutil.disk_usage('/')
        available_disk_gb = round(disk_info.free / (1024 ** 3), 2)
        return available_disk_gb
    except Exception as e:
        return "Error retrieving disk space info:", str(e)

def get_current_user():
    try:
        current_user = platform.node()
        return current_user
    except Exception as e:
        return "Error retrieving current user:", str(e)

def get_ip_address():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address
    except Exception as e:
        return "Error retrieving IP address:", str(e)

def get_system_uptime():
    try:
        uptime_seconds = time.time() - psutil.boot_time()
        return uptime_seconds
    except Exception as e:
        return "Error retrieving system uptime:", str(e)

def get_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage
    except Exception as e:
        return "Error retrieving CPU usage:", str(e)

def get_running_processes():
    try:
        running_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            pid = proc.info.get('pid')
            name = proc.info.get('name')
            memory_percent = proc.info.get('memory_percent')
            if pid and name and memory_percent is not None:
                running_processes.append((pid, name, round(memory_percent, 2)))
        return running_processes
    except Exception as e:
        return "Error retrieving running processes:", str(e)


def get_disk_partitions():
    try:
        disk_partitions = psutil.disk_partitions()
        return disk_partitions
    except Exception as e:
        return "Error retrieving disk partitions:", str(e)

def get_system_architecture():
    try:
        system_architecture = platform.architecture()[0]
        return system_architecture
    except Exception as e:
        return "Error retrieving system architecture:", str(e)

def get_environment_variables():
    try:
        environment_variables = os.environ
        return environment_variables
    except Exception as e:
        return "Error retrieving environment variables:", str(e)

if __name__ == "__main__":
    os_name, os_version = get_os_info()
    processor_info = get_processor_info()
    total_memory_gb = get_memory_info()
    available_disk_gb = get_disk_space_info()
    current_user = get_current_user()
    ip_address = get_ip_address()
    system_uptime = get_system_uptime()
    cpu_usage = get_cpu_usage()
    running_processes = get_running_processes()
    disk_partitions = get_disk_partitions()
    system_architecture = get_system_architecture()
    environment_variables = get_environment_variables()

    print("== OS Parameters ==")
    print("OS Name:", os_name)
    print("OS Version:", os_version)
    print("Processor Information:", processor_info)
    print("Memory (GB):", total_memory_gb)
    print("Available Disk Space (GB):", available_disk_gb)
    print("Current User:", current_user)
    print("IP Address:", ip_address)
    print("System Uptime (seconds):", system_uptime)
    print("CPU Usage (%):", cpu_usage)
    print("Running Processes:", running_processes)
    print("Disk Partitions:", disk_partitions)
    print("System Architecture:", system_architecture)
    print("Environment Variables:",environment_variables)
