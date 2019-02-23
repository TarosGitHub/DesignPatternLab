@echo off

rem java -jar <plantuml.jarのパス> -o <出力先ディレクトリ> <入力元パス>
java -jar %~dp0plantuml.jar -o %~dp0uml %~dp0uml\**.txt

rem 参考1: http://plantuml.com/command-line
rem 参考2: http://yohshiy.blog.fc2.com/blog-entry-152.html
