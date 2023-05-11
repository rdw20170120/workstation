#!/usr/bin/env false
"""Manage configuration."""
# Internal packages (absolute references, distributed with Python)
from sys import maxsize

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import environment
from utility.config import Config as BaseConfig

# Project modules   (relative references, NOT packaged, in project)


class Config(BaseConfig):
    @property
    def fake_suffix(self):
        return ".fake"

    @property
    def filesystem_to_watch(self):
        return self.temporary_directory

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
            v = environment.get("Run")
            return v.lower() == "dry"
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
            v = environment.get("Run")
            return v.lower() == "force"
        except KeyError:
            return False

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
            return int(environment.get("Quick"))
        except KeyError:
            return maxsize

    @property
    def reserved_disk_space_in_bytes(self):
        """Return disk space to reserve in bytes.

        In the absence of a defined value for the environment variable, we
        use the maximum integer value as a default.
        """
        try:
            return int(environment.get("ReservedDiskSpaceInBytes"))
        except KeyError:
            return maxsize

    @property
    def should_abort_upon_task_failure(self):
        return False

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
            environment.get("FakeIt")
            return True
        except KeyError:
            return False

    @property
    def should_leave_output_upon_task_failure(self):
        return False


"""DisabledContent
"""
