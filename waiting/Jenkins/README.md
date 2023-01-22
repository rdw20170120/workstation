# Jenkins
This project
can be executed as
a Jenkins job.

Here are
the essentials
of the job configuration.

## Job configuration
This is a `Pipeline` job.
Configure the following items.

- `General`
  - Check `Discard old builds`
    - `Max # of builds to keep` = 7
- `Pipeline`
  - `Definition` = `Pipeline script from SCM`
    - `SCM` = `Git`
    - `Repository URL` = `URL`
    - `Credentials` = `CREDENTIALS`
    - `Branch specifier` = `refs/heads/BRANCH`
    - `Script Path` = `Jenkins/Jenkinsfile`
    - Check `Lightweight checkout`

