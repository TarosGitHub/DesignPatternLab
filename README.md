# Design Pattern

## Visual Studio CodeでのPlantUMLの使い方

- プレビューを見る

    ```
    [Alt] + d
    ```

- UML定義ファイル(.pu)から画像ファイルを作成

    ```
    $ java -jar plantuml.jar ./uml/**.pu
    ```

    ■ 入力ファイル

    入力ファイルにはファイルまたはディレクトリー(フォルダー)を指定する。ディレクトリーを指定した場合にはディレクトリー内の以下の拡張子のファイルが対象となる。

    - txt
    - c, cpp, h
    - java
    - tex
    - html, htm

    ファイルのフィルターには通常の `?`, `*` だけではなく、パス区切りまで任意の文字とする(サブディレクトリ以下まで探す) `**` も使用できる。

    ```
    java -jar plantuml.jar <入力ファイル>
    ```

    ■ 出力ファイル

    出力ファイルはUMLの定義に書かれたファイル名で、**入力ファイルからの相対パス**の位置に出力される。

    ```
    @startuml <ファイル名>
    ```

- 参考

    - [Visual Studio Code で UML を描こう！](https://qiita.com/couzie/items/9dedb834c5aff09ea7b2)
    - [PlantUML の使い方](http://yohshiy.blog.fc2.com/blog-entry-152.html)

## Python

- テスト実施方法

    ```
    $ python python/testmng.py
    ```
