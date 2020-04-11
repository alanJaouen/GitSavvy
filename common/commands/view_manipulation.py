from sublime_plugin import TextCommand
from ...core.settings import GitSavvySettings


class gs_handle_vintageous(TextCommand):

    """
    Set the vintageous_friendly view setting if needed.
    Enter insert mode if vintageous_enter_insert_mode option is enabled.
    """

    def run(self, edit):
        savvy_settings = GitSavvySettings()
        if savvy_settings.get("vintageous_friendly", False) is True:
            self.view.settings().set("git_savvy.vintageous_friendly", True)
            if savvy_settings.get("vintageous_enter_insert_mode", False) is True:
                self.view.settings().set("vintageous_reset_mode_when_switching_tabs", False)
                self.view.run_command("_enter_insert_mode")


class gs_handle_arrow_keys(TextCommand):

    """
    Set the arrow_keys_navigation view setting if needed.
    It allows navigation by using arrow keys.
    """

    def run(self, edit):
        savvy_settings = GitSavvySettings()
        if savvy_settings.get("arrow_keys_navigation", False) is True:
            self.view.settings().set("git_savvy.arrow_keys_navigation", True)
