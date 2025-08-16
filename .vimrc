" Gerenciamento de plugins com vim-plug
call plug#begin('~/.vim/plugged')
Plug 'tomasr/molokai'     " Plugin do tema Molokai
call plug#end()

" Ativa suporte a 24-bit colors (cores verdadeiras) - importante para Molokai
if has('termguicolors')
  set termguicolors
endif

" Usa as cores originais do Molokai, que incluem suporte a itálico
let g:molokai_original = 1

" Aparência e comportamento do Vim
set number                   " Mostra números nas linhas
syntax enable               " Ativa destaque de sintaxe
set background=dark         " Fundo escuro
colorscheme molokai         " Aplica o tema Molokai

" Destaca a linha do cursor e parênteses pareados para conforto
set cursorline              
set showmatch               

" Menu de autocomplete no modo comando
set wildmenu                

" Comentários em cinza, sem itálico
highlight Comment cterm=NONE gui=NONE ctermfg=Grey guifg=#808080

" Strings (aspas) em amarelo mais forte
highlight String ctermfg=Yellow guifg=#ffff88

" Nomes de variáveis e identificadores em tom vinho escuro
highlight Identifier ctermfg=DarkMagenta guifg=#800080

" Palavras-chave continuam em ciano
highlight Keyword ctermfg=Cyan guifg=#00ffff

" Mapeia Ctrl+A para copiar todo o conteúdo do arquivo para o clipboard
nnoremap <C-a> ggVG"+y
" Copiar seleção atual com Ctrl+C no modo visual
vnoremap <C-c> "+y

inoremap <silent> !main <C-G>upublic static void main(String[] args)
inoremap <silent> !syso System.out.println();<Left><Left>
call plug#begin('~/.vim/plugged')

" Plugin de fechamento automático de pares
Plug 'jiangmiao/auto-pairs'

call plug#end()

" Indentação menor e mais compacta
set tabstop=4      " largura da tabulação
set shiftwidth=4    " largura da indentação automática "
" Auto inserir template quando criar novo arquivo .cpp
autocmd BufNewFile *.cpp 0r ~/.vim/cpp_template.cpp
autocmd BufNewFile *.py 0r ~/.vim/py_template.py


