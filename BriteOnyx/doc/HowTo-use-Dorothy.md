# HowTo use Dorothy
REF: https://github.com/bevry/dorothy

I first removed my previous Homebrew installation
along with everything installed by it.

Dorothy requires XCode on Apple macOS,
installed via `xcode-select --install`.
I already had that.

Dorothy also requires these:
* awk - native with macOS
* bash - native to macOS
* curl - native to macOS
* git - installed with XCode
* grep - native to macOS

Dorothy cloned its Git repository
to ~/.local/share/dorothy
to which `$DOROTHY` points.
I had to manually redirect
that repository's origin
to my own empty repository
on GitHub.

I executed `setup-system install`
to set up my system via Dorothy.
It prompted me,
starting with automatically installing Homebrew.
I then executed `brew update` to update Homebrew.
I executed `brew upgrade`,
but there was nothing to do
since I had yet to install anything
via this new Homebrew.

Dorothy installed Bash, Dash, Elvish, KSH, Nu, and Zsh shells.

I can install utilities using `setup-utils`
and find the right command using `get-installer`.

I installed more utilities:
~~~
setup-mac-brew
setup-util-bash
setup-util-emacs
setup-util-git
~~~
While installing `git`,
Homebrew prompted me to install `delta` (which I did).

I need to integrate my manually-installed tools
into the Dorothy automated installation scripts.

I want to use the `pkgx` installer,
so I invoked `brew install pkgx`.
Once `pkgx` was installed
I invoked `pkgx dev integrate`
which modified my Bash startup scripts.

Consider using these Dorothy commands:
~~~
checksum
echo-gnu-command
eject-all
fs-diff
fs_realpath
fs-speed
fs-structure
get-volumes
gravatar
icloud-helper
is-apple-silicon
is-ci
is-same
itunes-owners
open-app
secret
setup-mac-appstore
sparse-vault
ssh-helper
sudo-helper
what-is-using
~~~
