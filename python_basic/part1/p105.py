import platform

print(f"os      = {platform.system()}")
print(f"Ver     = {platform.release()}")
print(f"端末    = {platform.platform()}")
print(f"タイプ  = {platform.machine()}")

"""
platform
    実行中のOSに関する情報を表示できるモジュール
"""