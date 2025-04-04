import os
import subprocess
import pathlib
import threading
from PIL import Image

import customtkinter


class MenuButton(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.select_button = customtkinter.CTkButton(
            self, text="Select your image", command=master.get_image
        )
        self.scale_factor = customtkinter.CTkOptionMenu(self, values=["2x", "4x"])
        self.file_extension = customtkinter.CTkOptionMenu(
            self, values=["png", "jpg", "webp"]
        )
        self.scale_button = customtkinter.CTkButton(
            self,
            text="Upscale",
            command=lambda: threading.Thread(target=master.scale_image).start(),
        )
        self.select_button.grid(row=0, column=0, padx=2, pady=(0, 20), sticky="w")
        self.scale_button.grid(row=1, column=0, padx=2, pady=(0, 20), sticky="w")
        self.scale_factor.grid(row=2, column=0, padx=2, pady=(0, 20), sticky="w")
        self.file_extension.grid(row=3, column=0, padx=2, pady=(0, 20), sticky="w")

        # add widgets onto the frame, for example:


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.selected_image_path = ""
        self.progress = customtkinter.CTkProgressBar(
            self, orientation="horizontal", mode="indeterminate"
        )
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.menu_button_frame = MenuButton(master=self)
        self.file_extension = self.menu_button_frame.file_extension.get()
        self.menu_button_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    def get_image(self):
        self.selected_image_path = customtkinter.filedialog.askopenfilename()
        if len(self.selected_image_path) != 0:
            self.selected_image = customtkinter.CTkImage(
                light_image=Image.open(self.selected_image_path),
                dark_image=Image.open(self.selected_image_path),
                size=(350, 420),
            )
            self.selected_image_label = customtkinter.CTkLabel(
                self, text="", image=self.selected_image
            )
            self.selected_image_label.grid(row=0, column=1, pady=10)
            self.selected_image_label_path = customtkinter.CTkLabel(
                self, text=self.selected_image_path
            )
            self.selected_image_label_path.grid(row=1, column=1, pady=10)
        else:
            pass

    def scale_image(self):
        if len(self.selected_image_path) != 0:
            self.progress.grid(row=2, column=1)
            self.progress.start()
            file_extension = self.menu_button_frame.file_extension.get()
            waifu2xbin = f"{pathlib.Path.cwd()}/waifu2x-ncnn-vulkan-20220728-ubuntu/waifu2x-ncnn-vulkan"
            filename, old_ext = os.path.splitext(self.selected_image_path)
            filename = filename + "_upscaled" + f".{file_extension}"
            filename = os.path.basename(filename)
            try:
                command = [
                    waifu2xbin,
                    "-i",
                    self.selected_image_path,
                    "-o",
                    f"./{filename}",
                ]
                result = subprocess.run(
                    command, capture_output=True, text=True, check=True
                )
                self.progress.stop()
                self.progress.grid_forget()
            except subprocess.CalledProcessError as e:
                print(f"Image conversion failed: {e}")
                print("Standard Error:", e.stderr)
        else:
            pass


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
app = App()
app.title("Zoro")
app.mainloop()
