
from PyInstaller.utils.hooks import collect_data_files, copy_metadata

datas = collect_data_files("articulated_ssm_both_sides") + copy_metadata("articulated-ssm")
