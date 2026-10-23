# 导出文件（txt）

全书 300 章，正文 66.5 万汉字。下列文件由 `chapters/` 下的分章 md 直接合并生成，内容与正文一致。

## 下载

| 文件 | 内容 | 适用 |
|---|---|---|
| [坟场之上_全本_300章.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_%E5%85%A8%E6%9C%AC_300%E7%AB%A0.txt) | 全本 300 章，UTF-8 带 BOM，2.6 MB | 手机阅读 App、微信读书导入、Windows 记事本 |
| [坟场之上_全本_300章_GBK.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_%E5%85%A8%E6%9C%AC_300%E7%AB%A0_GBK.txt) | 全本 300 章，GBK，1.8 MB | 老电纸书、车机、不认 UTF-8 的阅读器 |
| [坟场之上_01_坟场.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_01_%E5%9D%9F%E5%9C%BA.txt) | 卷一 1–40 章，274 KB | 按卷加载 |
| [坟场之上_02_红沙.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_02_%E7%BA%A2%E6%B2%99.txt) | 卷二 41–72 章，283 KB | 按卷加载 |
| [坟场之上_03_外环.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_03_%E5%A4%96%E7%8E%AF.txt) | 卷三 73–102 章，268 KB | 按卷加载 |
| [坟场之上_04_深空.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_04_%E6%B7%B1%E7%A9%BA.txt) | 卷四 103–149 章，418 KB | 按卷加载 |
| [坟场之上_05_主场.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_05_%E4%B8%BB%E5%9C%BA.txt) | 卷五 150–282 章，1.3 MB | 按卷加载 |
| [坟场之上_06_新历.txt](https://github.com/EraL-Jack/mynovel/raw/main/export/%E5%9D%9F%E5%9C%BA%E4%B9%8B%E4%B8%8A_06_%E6%96%B0%E5%8E%86.txt) | 尾声 283–300 章，158 KB | 按卷加载 |

点表格里的文件名即下载。若跳转到预览页，点右上角 Download raw file。

## 格式说明

- 开头：书名、作者、类型、完结状态、三行简介
- 分卷标记：`【卷一 坟场】`，多数阅读器可识别为目录层级
- 章标题：`第X章 标题`，一章一行，段间空一行
- 结尾：`— 全书完 —`

## 编码

- UTF-8 版带 BOM，Windows 记事本与主流手机阅读器直接打开
- 若打开是乱码，换 GBK 版

## 重新生成

正文改动后，用相同规则重新合并即可：按 `chNNN.md` 编号排序，取首行作章标题，去掉 `#`，其余作正文。
