import unreal
import os

#instance of unral classes
system_lib = unreal.SystemLibrary()
editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

#get selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
deleted_count = 0

#instant delete or move to trash folder
instant_delete = False
trash_folder = os.path.join(os.sep, "Game", "Trash")

to_be_deleted = []

for asset in selected_assets:
    #get the full path of the asset
    asset_name = asset.get_fname()
    asset_path = asset.get_path_name()

    #get list of references to the asset
    asset_ref = editor_asset_lib.find_package_referencers_for_asset(asset_path)

    #if the asset is not referenced by any other asset, add it to the list of assets to be deleted
    if len(asset_ref) == 0:
        to_be_deleted.append(asset)

for asset in to_be_deleted:
    asset_name = asset.get_fname()
    
    #instant delete
    if instant_delete:
        deleted = editor_asset_lib.delete_loaded_asset(asset)
        if not deleted:
            unreal.log_warning(f"Failed to delete {asset_name}")
            continue
        deleted_count += 1

    #move to trash folder
    else:
        source_path = asset.get_path_name()
        folder_name = str(asset_name)
        new_path = f"{trash_folder}/{folder_name}"
        
        moved = editor_asset_lib.rename_asset(source_path, new_path)
        if not moved:
            unreal.log_warning(f"Failed to move {asset_name} to trash folder")
            continue
        deleted_count += 1

output_test = "deleted" if instant_delete else "moved to trash folder"
unreal.log(f"Selected {num_assets} assets, {output_test} {deleted_count} unused assets")
