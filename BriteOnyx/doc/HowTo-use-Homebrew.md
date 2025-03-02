# HowTo use Homebrew

REF: https://brew.sh/

NOTE: Please use the `homebrew-*` scripts
in the `workstation` repository.
They capture the relevant functionality
as needed to support my projects.

## Install
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

## Update
`brew update`

## Upgrade installed packages
`brew upgrade`

## List installed packages after initial install
`brew list`
```
==> Formulae
```

## Install desired packages
`brew install hyper iterm2 neovim`

## List installed packages again
`brew list`
```
==> Formulae
gettext		libuv		luajit		msgpack		tree-sitter
libtermkey	libvterm	luv		neovim		unibilium

==> Casks
hyper
iterm2
mambaforge
```

## Uninstall Homebrew
~~~
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
~~~

