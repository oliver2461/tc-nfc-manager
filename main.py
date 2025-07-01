# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from db import init_db, get_description, add_tag, remove_tag

class NFCApp(App):
    def build(self):
        init_db()
        return Builder.load_file("ui.kv")

    def read_tag(self):
        tag_id = self.root.ids.tag_input.text.strip()
        desc = get_description(tag_id)
        if desc:
            self.root.ids.output_label.text = f"[{tag_id}] {desc}"
        else:
            self.root.ids.output_label.text = f"[{tag_id}] not found."

    def add_tag(self):
        tag_id = self.root.ids.tag_input.text.strip()
        desc = self.root.ids.desc_input.text.strip()
        if tag_id and desc:
            add_tag(tag_id, desc)
            self.root.ids.output_label.text = f"[{tag_id}] added."
        else:
            self.root.ids.output_label.text = "Enter both tag ID and description."

    def remove_tag(self):
        tag_id = self.root.ids.tag_input.text.strip()
        if tag_id:
            remove_tag(tag_id)
            self.root.ids.output_label.text = f"[{tag_id}] removed (if it existed)."
        else:
            self.root.ids.output_label.text = "Enter tag ID to remove."

if __name__ == "__main__":
    NFCApp().run()
