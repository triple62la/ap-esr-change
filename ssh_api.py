import paramiko


def change_esr(username, passw, hostname, mac, esr, core_at):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(username=username, password=passw, hostname=hostname)
    stdin, stdout, stderr = client.exec_command(
        f'''cd /opt/wifihs-dcbox-awx/; source .venv/bin/activate; ansible-playbook /opt/wifihs-dcbox-awx/playbooks/kea_fixed_underlay_by_mac.yml -e"{{'clustername': {esr}, 'mac': {mac}, 'core_at': {core_at}}}"''')
    out = stdout.readlines()
    err = stderr.readlines()
    client.close()
    return out, err


