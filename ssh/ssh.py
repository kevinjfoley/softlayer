import paramiko


def run_cmd(ip, cmd):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username='root',
                key_filename="/root/.ssh/id_rsa")
    return ssh.exec_command(cmd)


def wait_cmds_complete(results):
    """
    Wait for a list of command results tuples (stdin, stdout, stderr)
 to complete.
    """

    e_stats = [result[1].channel.recv_exit_status() for result in results]
    return e_stats


def run_cmds(ips, cmds):

    results_list = []
    for ip, cmd in zip(ips, cmds):
        results_list.append(run_cmd(ip, cmd))

    return results_list
