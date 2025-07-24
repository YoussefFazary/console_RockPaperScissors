from fabric import Connection, task

# Define your remote server's hostname/IP
# In a real scenario, you'd likely get this from a configuration file or environment variable
HOSTNAME = 'your_remote_server_ip_or_hostname'
USERNAME = 'your_username'

@task
def deploy(c):
    """
    Deploys a simple web application.
    """
    with Connection(host=HOSTNAME, user=USERNAME) as conn:
        print(f"Connecting to {conn.host}...")
        conn.run('sudo apt update')
        conn.run('sudo apt install -y nginx')
        conn.put('index.html', '/var/www/html/index.html', sudo=True) # Upload a local index.html
        conn.run('sudo systemctl restart nginx')
        print("Deployment complete!")

@task
def check_nginx_status(c):
    """
    Checks the status of the Nginx service.
    """
    with Connection(host=HOSTNAME, user=USERNAME) as conn:
        print(f"Checking Nginx status on {conn.host}...")
        result = conn.run('systemctl status nginx', warn=True) # warn=True to not abort on non-zero exit code
        print(result.stdout)
        if result.failed:
            print("Nginx service is not running or encountered an error.")
        else:
            print("Nginx service is running.")

@task
def cleanup(c):
    """
    Removes the deployed files and Nginx.
    """
    with Connection(host=HOSTNAME, user=USERNAME) as conn:
        print(f"Cleaning up on {conn.host}...")
        conn.run('sudo rm /var/www/html/index.html')
        conn.run('sudo apt remove -y nginx')
        conn.run('sudo apt autoremove -y')
        print("Cleanup complete.")

# To deploy the application
fab deploy

# To check Nginx status
fab check_nginx_status

# To clean up
fab cleanup
