import fabric
from fabric.api import env

class Host:
    def __init__(self, user, key, host):
        self.user = user
        self.key = key
        self.host = host

    def run(self, command, shell=True, pty=True, combine_stderr=None, quiet=False, 
        warn_only=False, stdout=None, stderr=None, timeout=None, shell_escape=None):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.api.run(command, shell, pty, combine_stderr, quiet, warn_only, 
        stdout, stderr, timeout, shell_escape)

    def get(self, remote_path, local_path=None):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.operations.get(remote_path, local_path)

    def local(self, command, capture=False, shell=None):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.operations.local(command, capture, shell)

    def open_shell(self, command=None):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.operations.open_shell(command)

    def prompt(self, text, key=None, default='', validate=None):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.operations.prompt(text, key, default, validate)

    def put(self, local_path=None, remote_path=None, use_sudo=False, mirror_local_mode=False, 
        mode=None, use_glob=True, temp_dir=''):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.operations.put(local_path, remote_path, use_sudo, mirror_local_mode, 
        mode, use_glob, temp_dir)

    def reboot(self, wait=120):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.operations.reboot(wait)
    
    def sudo(self, command, shell=True, pty=True, combine_stderr=None, user=None, quiet=False, 
        warn_only=False, stdout=None, stderr=None, group=None, timeout=None, shell_escape=None):
        env.user = self.user
        env.key_filename = self.key
        env.host_string = self.host
        return fabric.operations.sudo(command, shell, pty, combine_stderr, user, quiet, 
        warn_only, stdout, stderr, group, timeout, shell_escape)
