import sys
import textwrap

module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))


"""
sys.builtin_module_names
    組み込みモジュールの一覧が見れる
textwrap
    長めのテキストを指定幅（文字数）で改行したり省略したりできる
"""