import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def run_cmd(ip, cmd, user=None):

    if user is None:
        user = 'root'
    ssh.connect(ip, username=user,
                key_filename="/home/kevin/.ssh/softlayer")
    return ssh.exec_command(cmd)


def wait_cmds_complete(results):
    """
    Wait for a list of command results tuples (stdin, stdout, stderr)
 to complete.
    """

    e_stats = [result[1].channel.recv_exit_status() for result in results]
    return e_stats


def run_cmds(ips, cmds, user=None):

    results_list = []
    for ip, cmd in zip(ips, cmds):
        results_list.append(run_cmd(ip, cmd, user))

    return results_list


def copy_file(ip, local_file, dest_file):

    ssh.connect(ip, username='root',
                key_filename="/home/kevin/.ssh/softlayer")
    sftp = ssh.open_sftp()
    result = sftp.put(local_file, dest_file)
    return result


def copy_files(ips, local_files, dest_files):

    results_list = []
    for ip, local_file, dest_file in zip(ips, local_files, dest_files):
        results_list.append(copy_file(ip, local_file, dest_file))

    return results_list
