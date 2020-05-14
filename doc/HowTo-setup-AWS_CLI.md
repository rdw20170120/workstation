HowTo setup the AWS CLI
=======================
This application relies upon the AWS CLI tool to manage a configuration for
accessing the Amazon cloud.  We create an AWS CLI profile for the application,
and you can optionally create other profiles such as for yourself.

**NOTE**: You must first have [setup the Python virtual environment][venv].

Obtain AWS credentials for the application
------------------------------------------
We have already created AWS credentials for the application, which are NOT
contained and should NEVER be contained within this project's repository.
Instead, those credentials must be obtained separately.  If necessary or
desired, one can use an IAM user with administrator privileges to create new
credentials for the application.  Below is the basic information for the
application's IAM user.

IAM user account for application
----------------------------------------------
* account name = TODO
* account id = TODO
* user name = TODO
* user ARN = arn:aws:iam::TODO

Configure AWS CLI
-----------------
The AWS CLI can manage named profiles, which are the best way to easily provide
AWS credentials to an application.  We must name the profile, but the name is
nothing more than a reference; pick a name that is convenient and meaningful.

The profile name must be provided to the application, which is accomplished
during [activation][activate].  The [activate.src](activate.src) script will
`source` the `context.src` script, if any.  You can create this script by
copying the [cfg/sample_context.src](cfg/sample_context.src) script.
**Note** that the copied script MUST NOT be checked into source control.

[Activate this project in a shell][activate].

**NOTE**: Do *NOT* configure a default profile, so that it cannot be used by
mistake!

~~~ bash
aws --profile $NameProfile configure
~~~

Which leads you through the following prompts:

    AWS Access Key ID [None]: ACCESS-KEY-ID
    AWS Secret Access Key [None]: ACCESS-KEY-SECRET
    Default region name [None]: REGION-NAME
    Default output format [None]: text

Now you can list those configuration settings.

~~~ bash
aws --profile $NameProfile configure list
~~~

Which outputs something like this:

          Name                    Value             Type    Location
          ----                    -----             ----    --------
       profile                     TODO           manual    --profile
    access_key     ****************TODO shared-credentials-file
    secret_key     ****************TODO shared-credentials-file
        region                     TODO       config-file   ~/.aws/config

Create AWS Access Key for yourself
----------------------------------
If you do not already have an Access Key for use with the AWS CLI, then let's
create one.

1. Browse to AWS Management Console
1. Login using credentials for the IAM user account to be inventoried
1. Browse https://console.aws.amazon.com/iam/
1. Create an Access Key
1. Save the new credential

Once you have created your own Access Key, you can repeat the steps above to
configure the AWS CLI with a profile for yourself.

Environment variables
---------------------
These are the shell environment variables used by the AWS CLI, which you
should check if you must troubleshoot the AWS CLI.

~~~ bash
$AWS\_ACCESS\_KEY\_ID
$AWS\_CA\_BUNDLE
$AWS\_CONFIG\_FILE
$AWS\_DEFAULT\_OUTPUT
$AWS\_DEFAULT\_REGION
$AWS\_PAGER
$AWS\_PROFILE
$AWS\_ROLE\_SESSION\_NAME
$AWS\_SECRET\_ACCESS\_KEY
$AWS\_SESSION\_TOKEN
$AWS\_SHARED\_CREDENTIALS\_FILE
~~~

Files
-----
These are the files used to configure the AWS CLI, which can likewise be used
for troubleshooting.

    ~/.aws/config
    ~/.aws/credentials

* See https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
* See https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

* **TODO**: Add command completion documented at https://pypi.org/project/awscli/

[activate]: doc/HowTo-activate_this_project.md "HowTo activate this project"
[application]: doc/HowTo-execute_application.md "HowTo execute application"
[AWS CLI]: doc/HowTo-setup-AWS_CLI.md "HowTo setup AWS CLI"
[clone]: doc/HowTo-setup-source_control.md "HowTo setup source control"
[initiation]: doc/project_initiation.md
  "How Rob initiated the project repository"
[license]: LICENSE "project license"
[ReadMe]: README.md "project ReadMe"
[test]: doc/HowTo-test.md "HowTo test"
[venv]: doc/HowTo-setup-Python_virtual_environment.md
  "HowTo setup Python virtual environment"
[workstation]: doc/HowTo-setup-workstation.md "HowTo setup workstation"

