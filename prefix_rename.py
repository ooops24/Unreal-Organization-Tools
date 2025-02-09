import unreal

def prefix_rename_assets():
    #instance of unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    #prefix mapping
    prefix_mapping = {
        "Blueprint": "BP_",
        "StaticMesh": "SM_",
        "Texture2D": "T_",
        "Material": "M_",
        "MaterialInstanceConstant": "MI_",
        "SkeletalMesh": "SK_",
        "AnimBlueprint": "ABP_",
        "AnimSequence": "Anim_",
        "WidgetBlueprint": "WBP_",
        "ParticleSystem": "P_",
        "NiagaraSystem": "NS_",
        "SoundCue": "SC_",
        "SoundWave": "SW_",
        "World": "L_",
        "LevelSequence": "LS_",
        "DataTable": "DT_",
        "Enumeration": "E_",
    }

    #get selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    prefix_added = 0

    #loop through selected assets
    for asset in selected_assets:
        #get the class instance and the clear text name
        old_name = system_lib.get_object_name(asset)
        asset_class = asset.get_class()
        class_name = system_lib.get_class_display_name(asset_class)

        #get the prifix
        class_prefix = prefix_mapping.get(class_name, None)

        if class_prefix is None:
            unreal.log_warning(f"Class {class_name} is not supported")
            continue

        if not old_name.startswith(class_prefix):
            new_name = class_prefix + old_name
            editor_util.rename_asset(asset, new_name)
            prefix_added += 1
            unreal.log(f"Added prefix {class_prefix} to {old_name} to {new_name}")

        else:
            unreal.log(f"Asset {old_name} already has the correct prefix {class_prefix}")

    unreal.log(f"Finished adding prefix to {prefix_added} assets")



prefix_rename_assets()