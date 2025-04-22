import qrcode
from PIL import Image
import os
from pyzbar.pyzbar import decode
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
import unittest
import sys

class QRGenerator:
    @staticmethod
    def generate_basic_qr(data, filename="qrcode.png", fill_color="black", back_color="white", size=10, border=4):
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=size,
                border=border,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img.save(filename)
            print(f"QR code has been saved to: {os.path.abspath(filename)}")
            return img
        except Exception as e:
            raise ValueError(f"Generation failed: {e}")

    @staticmethod
    def generate_advanced_qr(data, filename="qrcode.png", logo_path=None, gradient=False, shape='square'):
        try:
            qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            if logo_path:
                logo = Image.open(logo_path)
                logo_size = min(img.size) // 4
                logo = logo.resize((logo_size, logo_size))
                pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
                img.paste(logo, pos)

            img.save(filename)
            return img
        except Exception as e:
            raise ValueError(f"Advanced generation failed: {e}")

    @staticmethod
    def read_qr_code(image_path):
        try:
            decoded_objects = decode(Image.open(image_path))
            results = []
            for obj in decoded_objects:
                results.append({
                    "content": obj.data.decode('utf-8'),
                    "type": obj.type
                })
            return results
        except Exception as e:
            raise ValueError(f"Decoding failed: {e}")

    @staticmethod
    def analyze_qr(image_path):
        try:
            img = Image.open(image_path)
            pixels = list(img.getdata())
            color_count = Counter(pixels)
            width, height = img.size
            return {
                "black_ratio": color_count[(0, 0, 0)] / len(pixels),
                "size": f"{width}x{height}",
                "total_pixels": len(pixels)
            }
        except Exception as e:
            raise ValueError(f"Analysis failed: {e}")


class QRGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI QRcode generator v2.0")
        self.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Content:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.content_entry = tk.Entry(self, width=40)
        self.content_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Save the file name:").grid(row=1, column=0, sticky='e')
        self.filename_entry = tk.Entry(self, width=40)
        self.filename_entry.insert(0, "qrcode.png")
        self.filename_entry.grid(row=1, column=1)

        tk.Label(self, text="Logo Path(Optional):").grid(row=2, column=0, sticky='e')
        self.logo_entry = tk.Entry(self, width=40)
        self.logo_entry.grid(row=2, column=1)
        tk.Button(self, text="Browse...", command=self.browse_logo).grid(row=2, column=2)

        tk.Button(self, text="Generate a QR code", command=self.generate_qr, bg='green', fg='white').grid(row=3, column=1,
                                                                                                  pady=10)
        tk.Button(self, text="Decode the QR code", command=self.decode_qr, bg='blue', fg='white').grid(row=4, column=1)

        self.result_label = tk.Label(self, text="", wraplength=400)
        self.result_label.grid(row=5, column=0, columnspan=3)

    def browse_logo(self):
        filename = filedialog.askopenfilename(title="Choose Logo Picture")
        if filename:
            self.logo_entry.delete(0, tk.END)
            self.logo_entry.insert(0, filename)

    def generate_qr(self):
        try:
            data = self.content_entry.get()
            if not data:
                messagebox.showerror("Error", "Please enter your content")
                return

            filename = self.filename_entry.get() or "qrcode.png"
            logo_path = self.logo_entry.get() if self.logo_entry.get() else None

            if logo_path:
                QRGenerator.generate_advanced_qr(data, filename, logo_path)
            else:
                QRGenerator.generate_basic_qr(data, filename)

            messagebox.showinfo("Success", f"The QR code has been generated: {os.path.abspath(filename)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decode_qr(self):
        filename = filedialog.askopenfilename(title="Select the QR code image")
        if filename:
            try:
                results = QRGenerator.read_qr_code(filename)
                if results:
                    text = "\n".join([f"Content: {r['content']}\nType: {r['type']}\n" for r in results])
                    self.result_label.config(text=text)
                else:
                    messagebox.showinfo("Result", "The QR code content is not recognized")
            except Exception as e:
                messagebox.showerror("Error", str(e))


class TestQRGenerator(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_qr.png"
        QRGenerator.generate_basic_qr("test", self.test_file)

    def test_generation(self):
        self.assertTrue(os.path.exists(self.test_file))

    def test_decoding(self):
        results = QRGenerator.read_qr_code(self.test_file)
        self.assertEqual(results[0]['content'], "test")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


def command_line_interface():
    print("\n=== AI QR code genertor===")
    print("1. Generate a QR code")
    print("2. Decode the QR code")
    print("3. Analyze QR codes")
    print("4. Launch the GUI interface")
    print("5. Exit")

    choice = input("Please select an action (1-5): ")

    if choice == "1":
        data = input("Please enter your content: ")
        filename = input("Save the file name (Default: qrcode.png): ") or "qrcode.png"
        QRGenerator.generate_basic_qr(data, filename)
    elif choice == "2":
        image_path = input("Please enter the QR code image path: ")
        results = QRGenerator.read_qr_code(image_path)
        for r in results:
            print(f"Content: {r['content']}\nType: {r['type']}\n")
    elif choice == "3":
        image_path = input("Please enter the QR code image path: ")
        analysis = QRGenerator.analyze_qr(image_path)
        print(f"Black pixel ratio: {analysis['black_ratio']:.2%}")
        print(f"Size: {analysis['size']}")
    elif choice == "4":
        app = QRGeneratorApp()
        app.mainloop()
    elif choice == "5":
        sys.exit()
    else:
        print("Invaild input")


if __name__ == "__main__":
    while True:
        try:
            command_line_interface()
        except KeyboardInterrupt:
            print("\nThe program has exited")
            break
        except Exception as e:
            print(f"An error has occurred: {e}")
