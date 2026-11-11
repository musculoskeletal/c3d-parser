
from PyInstaller.utils.hooks import collect_data_files, copy_metadata

datas = collect_data_files("opensim_model_creator") + copy_metadata("opensim-model-creator")
