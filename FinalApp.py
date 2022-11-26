import tkinter
from tkinter import END
import tkinter.messagebox
import customtkinter

import googletrans
from googletrans import Translator

from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.title("Google Translator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


        # ============ Left Frame ============
        # Configure Grid Layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        # =========================== Button Images ===================================
        self.home_image = self.load_image("/test_images/home.png", 20)
        self.settings_image = self.load_image("/test_images/settings2.png", 20)
        self.bell_image = self.load_image("/test_images/bell.png", 20)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Google Translator App",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Home",
                                                image=self.home_image,
                                                compound="right")
        self.button_2.grid(row=2, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Settings",
                                               image=self.settings_image,
                                               compound="right")
        self.button_3.grid(row=3, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Notifications",
                                                image=self.bell_image,
                                                compound="right")
        self.button_4.grid(row=4, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============================ First Right Frame ======================================

        # Configure Grid Layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=1, rowspan=8, pady=30, padx=20, sticky="nsew")


        language = googletrans.LANGUAGES
        languageV = list(language.values())
        lang1 = language.keys()

        self.label_mode = customtkinter.CTkLabel(master=self.frame_right, text="From:")
        self.label_mode.grid(row=0, column=0, pady=0, padx=0, sticky="nwe")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=languageV)
        self.combobox_1.grid(row=0, column=0, columnspan=1, pady=30, padx=30, sticky="we")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=200,
                                            placeholder_text="Type text to Translate...")
        self.entry.grid(row=3, column=0, columnspan=1, pady=10, padx=30, sticky="we")



        # ============================ Second Right Frame ======================================

        self.frame_info1 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info1.grid(row=0, column=1, columnspan=1, rowspan=8, pady=30, padx=20, sticky="nsew")

        self.label_mode1 = customtkinter.CTkLabel(master=self.frame_right, text="To:")
        self.label_mode1.grid(row=0, column=1, pady=0, padx=0, sticky="nwe")

        self.combobox_2 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=languageV)
        self.combobox_2.grid(row=0, column=1, columnspan=1, pady=30, padx=30, sticky="we")

        self.entry1 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=200,
                                            placeholder_text="Translation")
        self.entry1.grid(row=3, column=1, columnspan=1, pady=10, padx=30, sticky="we")


        self.button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                command=self.translate_now)
        self.button_1.grid(row=5, column=0, pady=10, padx=30)

        # Set Default Values
        self.combobox_1.set("English")
        self.combobox_2.set("Select Language")
        self.button_1.configure(text="Translate")

    def translate_now(self):
        text_ = self.entry.get()
        t1 = Translator()
        trans_text = t1.translate(text_, src=self.combobox_1.get(), dest=self.combobox_2.get())
        trans_text = trans_text.text

        self.entry1.delete("0", END)
        self.entry1.insert(END, trans_text)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def load_image(self, path, image_size):
        """ load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

if __name__ == "__main__":
    app = App()
    app.mainloop()