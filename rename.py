import unreal

def rename_assets(search_pattern, replace_pattern, use_case):
    #instance of unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    #get selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log(f"Selected {num_assets} assets")

    #loop through selected assets
    for asset in selected_assets:
        old_name = asset.get_fname()
        
        #check if the asset name contains the search pattern
        if string_lib.contains(old_name, search_pattern, use_case=use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            replaced_name = string_lib.replace(old_name, search_pattern, replace_pattern, search_case=search_case)
            editor_util.rename_asset(asset, replaced_name)

            replaced += 1
            unreal.log(f"Renamed {old_name} to {replaced_name}")
        else:
            unreal.log(f"Asset {old_name} does not contain {search_pattern}")
    unreal.log(f"Finished renaming {replaced} assets")

rename_assets()