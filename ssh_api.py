import paramiko


def change_esr(username,
               passw,
               hostname,
               mac,
               esr,
               core_at,
               output_handler
               ):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        output_handler(f"Выполняется подключение по SSH к {username}@{hostname}")
        client.connect(username=username, password=passw, hostname=hostname)
        output_handler(f"Отправка команды на перенос ТД ({mac}) на {esr}, кластер {core_at}")
        output_handler(f"Время выполнения может занимать до нескольких минут...")
        stdin, stdout, stderr = client.exec_command(
            f'''cd /opt/wifihs-dcbox-awx/; source .venv/bin/activate; ansible-playbook /opt/wifihs-dcbox-awx/playbooks/kea_fixed_underlay_by_mac.yml -e"{{'clustername': {esr}, 'mac': {mac}, 'core_at': {core_at}}}"''')
        out = '\n'.join(stdout.readlines())
        err = '\n'.join(stderr.readlines())
        output_handler(f"Результат переноса:\n {err} \n {out}")
    except Exception as e:
         output_handler(f"Процесс завершил работу с ошибкой:\n {e}")
    finally:
        client.close()



