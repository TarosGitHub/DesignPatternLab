@echo off
rem 当バッチファイルの第1引数(%1)にはDesignePatternLabフォルダの絶対ディレクトリパスを指定すること

rem java -jar <plantuml.jarのパス> -o <出力先ディレクトリ> <入力元パス>
java -jar %1\lib\plantuml.jar -o %1\images %1\uml\**.txt

rem 参考1: http://plantuml.com/command-line
rem 参考2: http://yohshiy.blog.fc2.com/blog-entry-152.html
