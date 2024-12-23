import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import segno
import io
from PIL import Image, ImageTk
import sys
from collections import namedtuple

class AppleStyleQRGenerator:
    GeneratedImage = namedtuple('GeneratedImage', ['image'])

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        self.root.geometry("1200x800")

        # Set background color based on system (darker for macOS)
        self.is_macos = sys.platform == "darwin"
        self.bg_color = "#f5f5f7"  # Apple's light gray
        self.accent_color = "#0071e3"  # Apple's blue
        self.root.configure(bg=self.bg_color)

        # Configure styles
        self.setup_styles()

        # Variables
        self.data_var = tk.StringVar()
        self.ecc_var = tk.StringVar(value="M")
        self.version_var = tk.StringVar(value="Auto")
        self.fg_var = tk.StringVar(value="#000000")
        self.bg_var = tk.StringVar(value="#FFFFFF")
        self.logo_var = tk.StringVar()
        self.scale_var = tk.IntVar(value=10)
        self.border_var = tk.IntVar(value=4)

        # Image holder
        self.generated_img_holder = self.GeneratedImage(image=None)
        self.create_ui()

    def setup_styles(self):
        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')
        # Configure common styles
        self.style.configure("Main.TFrame", background=self.bg_color)
        self.style.configure("Card.TFrame", background="white", relief="flat")

        # Labels
        self.style.configure(
            "Title.TLabel",
            font=("SF Pro Display", 28, "bold"),
            background=self.bg_color,
            foreground="#1d1d1f"
        )
        self.style.configure(
            "Subtitle.TLabel",
            font=("SF Pro Text", 14),
            background=self.bg_color,
            foreground="#86868b"
        )
        self.style.configure(
            "Section.TLabel",
            font=("SF Pro Text", 16, "bold"),
            background="white",
            foreground="#1d1d1f"
        )
        self.style.configure(
            "Info.TLabel",
            font=("SF Pro Text", 12),
            background="white",
            foreground="#86868b"
        )

        # Entry
        self.style.configure(
            "App.TEntry",
            fieldbackground="#f5f5f7",
            borderwidth=0,
            relief="flat"
        )

        # Buttons
        self.style.configure(
            "Primary.TButton",
            font=("SF Pro Text", 13),
            background=self.accent_color,
            foreground="white",
            borderwidth=0,
            relief="flat",
            padding=(20, 10)
        )
        self.style.configure(
            "Secondary.TButton",
            font=("SF Pro Text", 13),
            background="#e8e8ed",
            foreground="#1d1d1f",
            borderwidth=0,
            relief="flat",
            padding=(20, 10)
        )

        # Combobox
        self.style.configure(
            "App.TCombobox",
            background="white",
            fieldbackground="#f5f5f7",
            arrowcolor=self.accent_color
        )

    def create_ui(self):
        # Main container with padding
        main_container = ttk.Frame(self.root, style="Main.TFrame", padding="40")
        main_container.grid(row=0, column=0, sticky="nsew")

        # Header
        self.create_header(main_container)

        # Content container
        content = ttk.Frame(main_container, style="Main.TFrame")
        content.grid(row=2, column=0, sticky="nsew", pady=(40, 0))

        # Create and arrange the main sections
        settings_card = self.create_settings_card(content)
        preview_card = self.create_preview_card(content)
        settings_card.grid(row=0, column=0, sticky="nw", padx=(0, 40))
        preview_card.grid(row=0, column=1, sticky="nsew")

        # Configure weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=3)

    def create_header(self, parent):
        # Title
        title = ttk.Label(
            parent,
            text="QR Code Generator",
            style="Title.TLabel"
        )
        title.grid(row=0, column=0, sticky="w")

        # Subtitle
        subtitle = ttk.Label(
            parent,
            text="Create beautiful QR codes for your digital and print materials",
            style="Subtitle.TLabel"
        )
        subtitle.grid(row=1, column=0, sticky="w", pady=(10, 0))

    def create_settings_card(self, parent):
        # Main card frame with white background and rounded corners
        card = ttk.Frame(parent, style="Card.TFrame", padding="30")

        # Content section
        self.create_section_label(card, "Content", 0)
        entry_frame = ttk.Frame(card, style="Card.TFrame")
        entry_frame.grid(row=1, column=0, sticky="ew", pady=(15, 30))
        data_entry = ttk.Entry(
            entry_frame,
            textvariable=self.data_var,
            style="App.TEntry",
            width=35,
            font=("SF Pro Text", 13)
        )
        data_entry.grid(row=0, column=0, sticky="ew")

        # QR Properties section
        self.create_section_label(card, "Properties", 2)
        properties_frame = ttk.Frame(card, style="Card.TFrame")
        properties_frame.grid(row=3, column=0, sticky="ew", pady=(15, 30))

        # Error correction
        ttk.Label(
            properties_frame,
            text="Error Correction",
            style="Info.TLabel"
        ).grid(row=0, column=0, sticky="w")
        ecc_box = ttk.Combobox(
            properties_frame,
            textvariable=self.ecc_var,
            values=["L", "M", "Q", "H"],
            state="readonly",
            style="App.TCombobox",
            width=5
        )
        ecc_box.grid(row=1, column=0, sticky="w", pady=(5, 0))

        # Version
        ttk.Label(
            properties_frame,
            text="Version",
            style="Info.TLabel"
        ).grid(row=0, column=1, sticky="w", padx=(30, 0))
        version_box = ttk.Combobox(
            properties_frame,
            textvariable=self.version_var,
            values=["Auto"] + [str(i) for i in range(1, 41)],
            state="readonly",
            style="App.TCombobox",
            width=5
        )
        version_box.grid(row=1, column=1, sticky="w", padx=(30, 0), pady=(5, 0))

        # Colors section
        self.create_section_label(card, "Colors", 4)
        colors_frame = ttk.Frame(card, style="Card.TFrame")
        colors_frame.grid(row=5, column=0, sticky="ew", pady=(15, 30))

        # Color buttons
        fg_button = ttk.Button(
            colors_frame,
            text="Foreground Color",
            command=self.pick_fg_color,
            style="Secondary.TButton"
        )
        fg_button.grid(row=0, column=0, sticky="w")
        bg_button = ttk.Button(
            colors_frame,
            text="Background Color",
            command=self.pick_bg_color,
            style="Secondary.TButton"
        )
        bg_button.grid(row=0, column=1, sticky="w", padx=(10, 0))

        # Logo section
        self.create_section_label(card, "Logo", 6)
        logo_frame = ttk.Frame(card, style="Card.TFrame")
        logo_frame.grid(row=7, column=0, sticky="ew", pady=(15, 30))
        logo_button = ttk.Button(
            logo_frame,
            text="Upload Logo (Optional)",
            command=self.select_logo,
            style="Secondary.TButton"
        )
        logo_button.grid(row=0, column=0, sticky="ew")

        # Action buttons at the bottom
        actions_frame = ttk.Frame(card, style="Card.TFrame")
        actions_frame.grid(row=8, column=0, sticky="ew", pady=(20, 0))
        self.generate_button = ttk.Button(
            actions_frame,
            text="Generate QR Code",
            command=self.generate_qr,
            style="Primary.TButton"
        )
        self.generate_button.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        self.save_button = ttk.Button(
            actions_frame,
            text="Save QR Code",
            command=self.save_qr,
            state="disabled",
            style="Secondary.TButton"
        )
        self.save_button.grid(row=1, column=0, sticky="ew")
        return card

    def create_preview_card(self, parent):
        card = ttk.Frame(parent, style="Card.TFrame", padding="30")
        # Preview title
        self.create_section_label(card, "Preview", 0)
        # Preview area
        preview_area = ttk.Frame(card, style="Card.TFrame")
        preview_area.grid(row=1, column=0, sticky="nsew", pady=(20, 0))
        self.preview_label = ttk.Label(
            preview_area,
            text="Your QR code will appear here",
            background="white",
            font=("SF Pro Text", 13),
            foreground="#86868b"
        )
        self.preview_label.grid(row=0, column=0, sticky="nsew")
        card.columnconfigure(0, weight=1)
        card.rowconfigure(1, weight=1)
        preview_area.columnconfigure(0, weight=1)
        preview_area.rowconfigure(0, weight=1)
        return card

    def create_section_label(self, parent, text, row):
        ttk.Label(
            parent,
            text=text,
            style="Section.TLabel"
        ).grid(row=row, column=0, sticky="w")

    def generate_qr(self):
        text_data = self.data_var.get().strip()
        if not text_data:
            messagebox.showerror("Error", "Please provide some text or URL to encode.")
            return
        try:
            ecc = self.ecc_var.get()
            version_setting = self.version_var.get()
            fg_color = self.fg_var.get()
            bg_color = self.bg_var.get()
            scale_val = self.scale_var.get()
            border_val = self.border_var.get()

            if version_setting == "Auto":
                qr_code = segno.make_qr(text_data, error=ecc)
            else:
                qr_code = segno.make_qr(text_data, error=ecc, version=int(version_setting))

            with io.BytesIO() as buffer:
                qr_code.save(
                    buffer,
                    kind="png",
                    scale=scale_val,
                    dark=fg_color,
                    light=bg_color,
                    border=border_val
                )
                buffer.seek(0)
                self.generated_img_holder = self.GeneratedImage(image=Image.open(buffer))

            if self.logo_var.get():
                try:
                    logo_img = Image.open(self.logo_var.get()).convert("RGBA")
                    qr_width, qr_height = self.generated_img_holder.image.size
                    logo_size = int(qr_width * 0.3)
                    logo_img = logo_img.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
                    pos_x = (qr_width - logo_size) // 2
                    pos_y = (qr_height - logo_size) // 2
                    self.generated_img_holder.image.paste(logo_img, (pos_x, pos_y), logo_img)
                except Exception as err:
                    messagebox.showerror("Error", f"Failed to embed logo: {err}")

            preview = ImageTk.PhotoImage(self.generated_img_holder.image)
            self.preview_label.config(image=preview)
            self.preview_label.image = preview
            self.save_button.config(state="normal")
        except Exception as err:
            messagebox.showerror("Error", f"Failed to generate QR code: {err}")

    def select_logo(self):
        file_path = filedialog.askopenfilename(
            title="Choose a logo",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if file_path:
            self.logo_var.set(file_path)

    def pick_fg_color(self):
        chosen_color = colorchooser.askcolor(
            title="Select foreground color",
            color=self.fg_var.get()
        )
        if chosen_color and chosen_color[1]:
            self.fg_var.set(chosen_color[1])

    def pick_bg_color(self):
        chosen_color = colorchooser.askcolor(
            title="Select background color",
            color=self.bg_var.get()
        )
        if chosen_color and chosen_color[1]:
            self.bg_var.set(chosen_color[1])

    def save_qr(self):
        if self.generated_img_holder.image is None:
            messagebox.showerror("Error", "No QR code has been generated.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")],
            title="Save QR Code"
        )

        if file_path:
            try:
                self.generated_img_holder.image.save(file_path)
                messagebox.showinfo("Success", f"QR code saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save the file: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AppleStyleQRGenerator()
    app.run()
