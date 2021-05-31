" Rob Williams' Neovim initialization

call plug#begin(stdpath('data') . '/plugged')
Plug 'junegunn/vim-plug'

Plug 'https://github.com/lifepillar/vim-solarized8'

" Plug 'junegunn/vim-easy-align'

" Plug 'tpope/vim-sensible'

" Plug 'SirVer/ultisnips'
" Plug 'honza/vim-snippets'
call plug#end()

" https://github.com/junegunn/vim-plug
" Install for Apple macOS (11.0.1)
" sh -c 'curl -fLo \
"     ~/.config/nvim/autoload/plug.vim \
"     --create-dirs \
"     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
" TODO: Install for Linux
" To manage these plugins:
" :PlugUpgrade
" :PlugInstall
" :PlugUpdate
" :UpdateRemotePlugins
" :PlugClean
" :PlugStatus
" :PlugDiff
" :PlugSnapshot

" Colors {{{
" let $NVIM_TUI_ENABLE_TRUE_COLOR=1
set termguicolors
set background=dark
colorscheme solarized8
set background=dark
syntax enable
" }}} Colors

" Spaces & Tabs {{{
set autoindent
set copyindent
set expandtab
set shiftwidth=4
set softtabstop=4
set tabstop=4
" }}} Spaces & Tabs

" UI Config {{{
" set hidden
set cursorline
set laststatus=2
set nobackup
set noswapfile
set number
set showcmd
" set showmatch
" set wildmenu
" let &colorcolumn="80,".join(range(119,999),",")
" }}} UI Config

" Search {{{
set hlsearch
" set ignorecase
" set incsearch
set smartcase
" }}} Search

