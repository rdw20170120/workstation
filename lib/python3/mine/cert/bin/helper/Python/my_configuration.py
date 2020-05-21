import os


def get_cluster_user_pass():
    return os.environ['CB_Cluster_PassSuper']

def get_cluster_user_name():
    return os.environ['CB_Cluster_UserSuper']

def get_directory_answer():
    return os.environ['CB_All_DirAnswer']

def get_directory_data():
    return os.environ['CB_Cluster_DirData']

def get_directory_dataset():
    return os.environ['CB_Client_DirDataset']

def get_directory_index():
    return os.environ['CB_Cluster_DirIndex']

def get_directory_output():
    return os.environ['CB_Client_DirOutput']

def get_directory_package():
    return os.environ['CB_Client_DirPackage']

def get_exam_id():
    return os.environ['CB_ExamId']

def get_file_package_server():
    return os.environ['CB_PackageServer']

def get_file_ssh_key():
    return os.environ['CB_All_FileSshKey']

def get_group_a_name():
    return os.environ['CB_GroupA_Name']

def get_group_b_name():
    return os.environ['CB_GroupB_Name']

def get_host_client():
    return os.environ['CB_HostClient']

def get_hosts_server():
    return os.environ['CB_HostsServer']

def get_machine_username():
    return os.environ['CB_All_UserExaminee']

def get_port_web_ui():
    return int(os.environ['CB_Cluster_PortWebUi'])

def get_project_name():
    return os.environ['BO_ProjectName']

def get_project_version():
    return os.environ['CB_Version']

def get_session_id():
    return os.environ['CB_SessionId']

def get_sleep_in_seconds():
    return int(os.environ['CB_SleepSeconds'])

def get_task_count_init():
    return int(os.environ['CB_ExamTasksInit'])

def get_task_count_main():
    return int(os.environ['CB_ExamTasksMain'])

""" Disabled content
"""

