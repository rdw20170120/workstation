# HowTo use Dorothy
REF: https://github.com/bevry/dorothy

I first removed my Homebrew installation
along with everything installed by it.

Dorothy requires XCode on Apple macOS,
installed via `xcode-select --install`.
I already had that.

Dorothy also requires these:
* bash - native to macOS
* curl - native to macOS
* grep - native to macOS
* git - installed with XCode
* awk - native with macOS

Dorothy cloned the Git repository
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
since I had yet to install anything via Homebrew.

I can install utilities using `setup-utils`
and find the right command using `get-installer`.

I installed more utilities via:
~~~
setup-util-bash
setup-util-emacs
setup-util-git
~~~
