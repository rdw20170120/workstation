" Rob Williams' Vim initialization

call plug#begin('~/.vim/plugged')
Plug 'junegunn/vim-plug'
" To manage these plugins:
" :PlugUpgrade
" :PlugInstall
" :PlugUpdate
" :PlugClean
" :PlugStatus
" :PlugDiff
" :PlugSnapshot

" Plug 'SirVer/ultisnips'
" Plug 'honza/vim-snippets'
" Plug 'junegunn/vim-easy-align'
Plug 'airblade/vim-gitgutter'
Plug 'https://github.com/lifepillar/vim-solarized8'
Plug 'will133/vim-dirdiff'
call plug#end()

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

