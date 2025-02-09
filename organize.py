import unreal
import os

#instance of unreal classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

#hardcoded folder path
folder_path = "/Game/Assets"

#get selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
cleaned = 0

if num_assets > 0:
    asset_path = editor_util.get_path_name_from_object(selected_assets[0])
    folder_path = os.path.dirname(asset_path)

for asset in selected_assets:
    #get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    #assemble new path and relocate asset
    try:
        new_path = os.path.join(folder_path, class_name, asset_name)
        editor_asset_lib.rename_loaded_asset(asset, new_path)
        cleaned += 1
    except Exception as e:
        unreal.log_warning(f"Failed to rename asset {asset_name}: {str(e)}")

unreal.log(f"Finished organizing {cleaned} assets")