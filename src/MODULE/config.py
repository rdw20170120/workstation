#!/bin/false

from pathlib import Path
from sys     import maxsize

from utility import environment


class Config:
    @property
    def is_dry_run(self):
        """Return whether we are performing a dry-run execution.
        
        This setting is configured in each deployment by the absence or the
        value of the environment variable.  By default, the variable is
        undefined.  As a consequence, execution is NOT a dry-run.  If the
        variable is defined in the deployment with an appropriate value, then
        we execute as a dry-run in which no actual changes are made.  This
        provides an advantage during development and testing.
        """
        try:
            v = environment.get('Run')
            return v.lower() == 'dry'
        except KeyError:
            return False

    @property
    def is_forced_run(self):
        """Return whether we are performing a forced-run execution.
        
        This setting is configured in each deployment by the absence or the
        value of the environment variable.  By default, the variable is
        undefined.  As a consequence, execution is NOT a forced-run.  If the
        variable is defined in the deployment with an appropriate value, then
        we execute as a forced-run in which we overwrite computed data files
        instead of skipping them when they already exist.  This provides an
        advantage during development and testing.
        """
        try:
            v = environment.get('Run')
            return v.lower() == 'force'
        except KeyError:
            return False

    @property
    def log_directory(self):
        return self.project_directory / 'log'

    @property
    def log_file(self):
        return self.log_directory / 'MODULE.log'

    @property
    def quick_run_limit(self):
        """Return quick run file size limit, if any.
        
        This setting is configured in each deployment by the absence or the
        value of the environment variable.  By default, the variable is
        undefined.  As a consequence, execution is NOT limited to a quick run.
        If the variable is defined in the deployment with an appropriate value,
        then we execute as a quick run in which we process only existing data
        files whose size is under the limit specified by the environment
        variable value (integer bytes).  This provides an advantage during
        development and testing.
        """
        try:
            return int(environment.get('Quick'))
        except KeyError:
            return maxsize

    @property
    def pid_file(self):
        return self.project_directory / 'pipeline.pid'

    @property
    def project_directory(self):
        return Path(environment.get('BO_Project'))
    
    @property
    def should_fake_it(self):
        """Return whether we should fake the data processing during execution.
        
        This setting is configured in each deployment by the absence or
        presence of the environment variable.  By default, the variable is
        undefined.  As a consequence, execution performs real data processing.
        If the variable is defined in the deployment, then data processing is
        faked.  This provides an advantage during development and testing since
        the real data processing takes significant time.
        """
        try:
            environment.get('FakeIt')
            return True
        except KeyError:
            return False

    @property
    def temporary_directory(self):
        return Path(environment.get('TMPDIR'))

