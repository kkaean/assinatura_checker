# main.py
import tkinter as tk
from view.view import AssinaturaView

def main():
    root = tk.Tk()
    app = AssinaturaView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
