import os
import paramiko
import requests
import socket
import sys


class CommandExecuteException(Exception):
    """Command execution failed exception."""
    pass


class GeneralException(Exception):
    """General exceptions."""
    pass


class HostException(Exception):
    """Host not reachable exception."""
    pass


def check_count(json_response, bucket_name, some_key, type):
    score = 0
    msg = (
        "{0} not deleted for the user:"
        " {1} in {2} bucket"
        .format(type, some_key, bucket_name)
    )
    if json_response.get('status') == 'success':
        if json_response.get('metrics').get('resultCount') == 0:
            score = 1
            msg = (
                "{0} deleted for the user:"
                " {1} in {2} bucket"
                .format(type, some_key, bucket_name)
            )
    else:
        msg = json_response.get('errors', {})
    return score, msg


def check_host(host, port=8091, timeout=5):
    """Checks the host readability at a particular port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    if result != 0:
        raise HostException('{0}:{1} : Host not reachable'.format(host, port))
    sock.close()


def check_operator(plan, bucket_name, primary_index):
    if isinstance(plan, dict):
        plan = [plan]
    if isinstance(plan, list):
        for p in plan:
            if p.get('#operator') == 'PrimaryScan' and \
               p.get('index') == primary_index and \
               p.get('keyspace') == bucket_name:
                return True
            return check_operator(
                p.get('~children'), bucket_name, primary_index
            )


def check_result_count(result, count=1):
    score = 0
    msg = "The document has incorrect result count"
    if result == count:
        score = 1
        msg = "The document has correct result count"
    return score, msg


def check_results(result, bucket_name, doc_type, doc_username):
    score = 0
    msg = 'The Document contains incorrect results'
    for bucket in result:
        if bucket_name in list(bucket.keys()):
            if bucket.get(bucket_name).get('username') == doc_username and \
               bucket.get(bucket_name).get('type') == doc_type:
                score = 1
                msg = 'The Document contains correct results'
                break
    return score, msg


def connect_ssh(host, username, file_ssh_key):
    """Connecting to a remote host."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connecting to host
    ssh.connect(host, username=username, key_filename=file_ssh_key)
    return ssh


def delete_output(ssh, output_file):
    """ Deleting target output file."""
    rm_cmd = 'rm -f {0}'.format(output_file)
    rm_status, stdout, stderr = execute_command(ssh, rm_cmd)
    if rm_status != 0:
        raise_exception(stdout, stderr)


def execute_command(ssh, command):
    """Executing a command in remote system."""
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    return exit_status, stdout, stderr


def execute_commands(ssh, commands):
    """Executing commands in remote system using SSH."""
    for command in commands:
        exit_status, stdout, stderr = execute_command(ssh, command)
        if exit_status != 0:
            raise_exception(stdout, stderr)


def execute_query(host, query, auth, timeout=None):
    """Executes N1QL query and returns the response."""
    query_url = (
        'http://{0}:{1}/query/service'
        .format(host, 8093)
    )
    data = {'statement': query}
    if timeout:
        data['timeout'] = timeout
    response = requests.post(
        query_url,
        auth=auth,
        data=data
    )
    return response


def generate_output(client, user, file_ssh_key, filename, content):
    """Create a output file in the node with the govent content."""
    directory = os.path.dirname(filename)
    ssh = connect_ssh(client, user, file_ssh_key)
    commands = [
        "mkdir -p {0}".format(directory),
        "echo '{0}' > {1}".format(content, filename)
    ]
    execute_commands(ssh, commands)
    ssh.close()


def get_cbcollect_info_file_name(task_identifier, cluster_name, tool_name):
    return "{0}-{1}-{2}.zip".format(task_identifier, cluster_name, tool_name)


def get_cmd_status(ssh, command, expected_value=None):
    """Executes the command in remote node.
       Returns True if expected_value in command output,
       Returns command output if expected_value is None and output not empty,
       Returns False in other cases.
    """
    exit_status, stdout, stderr = execute_command(ssh, command)
    if exit_status == 0:
        output = stdout.read().replace('\n', '')
        if expected_value:
            if expected_value in output:
                return True
        elif output:
            return output
    return False


def get_details(host, extra_path, auth, port=8091):
    """Getting the details from couchbase server."""
    url = 'http://{0}:{1}/{2}'.format(host, port, extra_path)
    response = None
    try:
        response = make_request(requests.get, url, auth=auth)
    except requests.exceptions.RequestException:
        return None
    print('DEBUG: get_details()\nDEBUG: url={0}\n'.format(url))
    print('DEBUG: status_code={0}\nDEBUG: response={1}\n'.format(
        response.status_code, response.text
    ))
    return response


def get_errors(file_data):
    if isinstance(file_data, dict):
        return file_data.get('errors', [])
    return file_data


def get_fqdn(address):
    """Returns the fqdn of a node."""
    return socket.getfqdn(address)


def get_fqdn_list(address_list):
    """Returns the list of fqdn of nodes."""
    fqdn_list = []
    for address in address_list:
        fqdn = get_fqdn(address)
        if fqdn:
            fqdn_list.append(fqdn)
    return fqdn_list


def get_ip(address):
    """Returns the ip adress of a node."""
    if address:
        try:
            socket.inet_aton(address)
            return address
        except socket.error:
            return socket.gethostbyname(address)


def get_ip_list(address_list):
    """Retruns the list of ip addresses of nodes."""
    ip_list = []
    for address in address_list:
        ip_address = get_ip(address)
        if ip_address:
            ip_list.append(ip_address)
    return ip_list


def get_results(file_data):
    if isinstance(file_data, dict):
        return file_data.get('results', [])
    return file_data


def grading_host_check(host, port=8091):
    """Checking the host a particular port."""
    try:
        check_host(host, port)
        return True
    except:
        return False


def make_request(request_method, url, data={}, auth=None):
    """Making an API request."""
    response = request_method(url, data, auth=auth)
    response.raise_for_status()
    return response


def raise_exception(stdout, stderr):
    """Raising exception to the failed commands"""
    exception = ''
    stdout = stdout.read()
    if stdout:
        exception = stdout.strip('\n')
    else:
        exception = stderr.read().strip('\n')
    raise GeneralException(exception)


def score_check(score, ck_num, msg):
    """Returns the score along with check number."""
    sys.stdout.write("SCORE = {0} : {1} = {2}\n".format(score, ck_num, msg))


def wait_for_task_completion(task_type, host, port, auth):
    """Waiting until the task is completed of particular type"""
    task_url = (
        'http://{0}:{1}/pools/default/tasks'
        .format(host, port)
    )
    task_status = True
    while task_status:
        response = make_request(
            requests.get, task_url, auth=auth
        )
        for task in response.json():
            if(task.get('type') == task_type and
               task.get('status') == 'running'):
                break
        else:
            task_status = False

