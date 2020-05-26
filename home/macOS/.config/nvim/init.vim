" Rob Williams' Neovim initialization

call plug#begin('~/.vim/plugged')
Plug 'junegunn/vim-plug'

Plug 'https://github.com/lifepillar/vim-solarized8'

" Plug 'junegunn/vim-easy-align'

" Plug 'tpope/vim-sensible'

" Plug 'SirVer/ultisnips'
" Plug 'honza/vim-snippets'

call plug#end()

" https://github.com/junegunn/vim-plug
" To manage these plugins:
" :PlugUpgrade
" :PlugInstall
" :PlugUpdate
" :UpdateRemotePlugins
" :PlugClean
" :PlugStatus
" :PlugDiff
" :PlugSnapshot

set termguicolors
set background=dark
colorscheme solarized8

