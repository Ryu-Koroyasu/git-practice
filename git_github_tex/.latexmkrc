# =====================================================================
# latexmk 設定（このフォルダ内の全冊子で共通）
#   ビルド: latexmk main_intro.tex   （エンジン指定は不要）
#   全冊 : latexmk
#   掃除 : latexmk -C
# 生成物は output/ にまとめ、ソースのフォルダを汚さない。
# =====================================================================

$pdf_mode  = 4;               # LuaLaTeX で PDF を生成する
$lualatex  = 'lualatex -interaction=nonstopmode -file-line-error %O %S';

$out_dir   = 'output';        # PDF の出力先
$aux_dir   = 'output/aux';    # .aux / .log / .toc などの中間ファイル置き場

# 引数なしで latexmk を実行したときに作る対象（main_*.tex のみ。
# preamble.tex や chapters/*.tex は単体でコンパイルしない）。
@default_files = glob('main_*.tex');

$clean_ext = 'synctex.gz run.xml';
