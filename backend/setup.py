import subprocess, os, sys, time

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


def setup_django_server():
    os.system("clear||cls")
    print("Please Ensure You have a stable Internet connection to download required packages")
    print("Setup will start in the next 10 seconds")
    count= 10
    while count > 0:
        count= count - 1
        print(count)
        time.sleep(1)
    run_command("pip install --upgrade pip")
    run_command("pip install -r requirements.txt")
    run_command("py manage.py runserver 0.0.0.0:8000")

if __name__ == "__main__":
    setup_django_server()