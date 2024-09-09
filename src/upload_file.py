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


# �R�}���h���C����������t�@�C���p�X���擾
file_path = sys.argv[1]
path_openmx_viewer_opener = sys.argv[2]
print(path_openmx_viewer_opener)

# �u���E�U���N��
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# �w���URL�ɃA�N�Z�X
url = "https://www.openmx-square.org/viewer/"
driver.get(url)

# �h���b�O�A���h�h���b�v�Ώۂ̗v�f��������
drop_area = driver.find_element(By.ID, 'cvarea')

# �t�@�C���̐�΃p�X���擾
abs_file_path = os.path.abspath(file_path)

# �t�@�C���̓��e��ǂݎ����Base64�G���R�[�h
with open(abs_file_path, 'rb') as file:
    file_content = base64.b64encode(file.read()).decode('utf-8')

# JavaScript�Ńh���b�O�A���h�h���b�v���V�~�����[�g����X�N���v�g
file_path_drop = path_openmx_viewer_opener + r"\src\drop_file.js"
with open(file_path_drop, 'r') as js_file:
    drag_and_drop_script = js_file.read()

print(f"upload a structure file")
# JavaScript�����s���ăt�@�C�����h���b�v
driver.execute_script(drag_and_drop_script, drop_area, file_content, os.path.basename(abs_file_path))


# omxv.config�̓��e��ǂݎ����Base64�G���R�[�h
abs_file_path_config = path_openmx_viewer_opener + r"\src\omxv.config"
with open(abs_file_path_config, 'rb') as file:
    file_content = base64.b64encode(file.read()).decode('utf-8')

# JavaScript�Ńh���b�O�A���h�h���b�v���V�~�����[�g����X�N���v�g
with open(file_path_drop, 'r') as js_file:
    drag_and_drop_script = js_file.read()

print(f"upload a config file")
# JavaScript�����s���ăt�@�C�����h���b�v
driver.execute_script(drag_and_drop_script, drop_area, file_content, os.path.basename(abs_file_path_config))


time_to_wait = 100000  # 3600�b�i1���ԁj�ҋ@
time.sleep(time_to_wait)

