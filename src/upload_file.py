# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



import time
import base64
import sys
import os


# コマンドライン引数からファイルパスを取得
file_path = sys.argv[1]
path_openmx_viewer_opener = sys.argv[2]
print(path_openmx_viewer_opener)

# ブラウザを起動
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# 指定のURLにアクセス
url = "https://www.openmx-square.org/viewer/"
driver.get(url)

# ドラッグアンドドロップ対象の要素を見つける
drop_area = driver.find_element(By.ID, 'cvarea')

# ファイルの絶対パスを取得
abs_file_path = os.path.abspath(file_path)

# ファイルの内容を読み取ってBase64エンコード
with open(abs_file_path, 'rb') as file:
    file_content = base64.b64encode(file.read()).decode('utf-8')

# JavaScriptでドラッグアンドドロップをシミュレートするスクリプト
file_path_drop = path_openmx_viewer_opener + r"\src\drop_file.js"
with open(file_path_drop, 'r') as js_file:
    drag_and_drop_script = js_file.read()

print(f"upload a structure file")
# JavaScriptを実行してファイルをドロップ
driver.execute_script(drag_and_drop_script, drop_area, file_content, os.path.basename(abs_file_path))


# omxv.configの内容を読み取ってBase64エンコード
abs_file_path_config = path_openmx_viewer_opener + r"\src\omxv.config"
with open(abs_file_path_config, 'rb') as file:
    file_content = base64.b64encode(file.read()).decode('utf-8')

# JavaScriptでドラッグアンドドロップをシミュレートするスクリプト
with open(file_path_drop, 'r') as js_file:
    drag_and_drop_script = js_file.read()

print(f"upload a config file")
# JavaScriptを実行してファイルをドロップ
driver.execute_script(drag_and_drop_script, drop_area, file_content, os.path.basename(abs_file_path_config))


time_to_wait = 100000  # 3600秒（1時間）待機
time.sleep(time_to_wait)

