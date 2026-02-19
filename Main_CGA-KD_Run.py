import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

# -------------------- COLOR THEME --------------------
APP_BG = "#0F172A"          # Main background (dark blue)
HEADER_BG = "#1E293B"       # Header background
LEFT_BG = "#1D4ED8"         # Left panel background
RIGHT_BG = "#0F766E"        # Right panel background

TITLE_FG = "#38BDF8"        # Title text color
SUBTITLE_FG = "#E0F2FE"     # Subtitle text color
BTN_LEFT_BG = "#2563EB"     # Left buttons bg
BTN_LEFT_HOVER = "#3B82F6"  # Left hover
BTN_RIGHT_BG = "#14B8A6"    # Right buttons bg
BTN_RIGHT_HOVER = "#2DD4BF" # Right hover
BTN_FG = "white"            # Button text color
METRIC_TITLE_FG = "#FACC15" # Performance label color
# -----------------------------------------------------

def run_script(script_name, needs_dataset=False):
    try:
        if needs_dataset and not os.path.exists("selected_dataset.txt"):
            messagebox.showwarning("Dataset Missing", "Please select dataset first!")
            return

        script_path = os.path.join(os.getcwd(), script_name + ".py")

        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"{script_name}.py not found!")
            return

        subprocess.Popen([sys.executable, script_path])

    except Exception as e:
        messagebox.showerror("Execution Error", str(e))

def Adverse_Condition_Dataset():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="Select Dataset Folder", initialdir=os.getcwd())

    if folder_path:
        with open("selected_dataset.txt", "w") as f:
            f.write(folder_path)
        messagebox.showinfo("Success", "Dataset Folder Loaded Successfully!")
    else:
        messagebox.showwarning("Warning", "No folder selected.")

def Data_Acquasim(): run_script("Data_collection", True)
def Image_Preprocessing(): run_script("Physics_Preprocessing", True)
def FE(): run_script("Conditional_Generative_Adversarial_Networks_Feature_Extraction", True)
def Prediction(): run_script("Support_Vector_Machine_Student_Model", True)

def PSNR(): run_script("PSNR")
def TT(): run_script("Training_Time")
def PR(): run_script("Precision")
def RC(): run_script("Recall")
def ACC(): run_script("Accuracy")

root = tk.Tk()
root.title("Conditional Generative Adversarial Knowledge Distillation (CGA-KD)")
root.geometry("1366x768")
root.configure(bg=APP_BG)

TITLE_FONT = ("Segoe UI", 22, "bold")
BTN_FONT   = ("Segoe UI", 11, "bold")

# -------------------- HEADER --------------------
header = tk.Frame(root, bg=HEADER_BG, pady=25)
header.pack(fill="x")

tk.Label(header,
         text="CONDITIONAL GENERATIVE ADVERSARIAL KNOWLEDGE DISTILLATION FOR ",
         bg=HEADER_BG,
         fg=TITLE_FG,
         font=TITLE_FONT).pack()

tk.Label(header,
         text="SYNTHETIC ADVERSE WEATHER SIMULATION ",
         bg=HEADER_BG,
         fg=SUBTITLE_FG,
         font=TITLE_FONT).pack(pady=5)

# -------------------- CONTENT --------------------
content = tk.Frame(root, bg=APP_BG)
content.pack(expand=True, fill="both")

left_frame = tk.Frame(content, bg=LEFT_BG, padx=40, pady=40)
left_frame.pack(side="left", expand=True, padx=60, pady=40)

right_frame = tk.Frame(content, bg=RIGHT_BG, padx=40, pady=40)
right_frame.pack(side="right", expand=True, padx=60, pady=40)

# -------------------- LEFT BUTTONS --------------------
left_buttons = [
    ("Adverse Condition Dataset", Adverse_Condition_Dataset),
    ("Data Collection", Data_Acquasim),
    ("Physics-based Pre-processing ", Image_Preprocessing),
    ("Conditional GAN based Feature Extraction", FE),
    ("SVM based knowledge Distillation", Prediction)
]

for text, cmd in left_buttons:
    btn = tk.Button(left_frame,
                    text=text,
                    command=cmd,
                    font=BTN_FONT,
                    bg=BTN_LEFT_BG,
                    fg=BTN_FG,
                    activebackground=BTN_LEFT_HOVER,
                    relief="flat",
                    width=35,
                    pady=10,
                    cursor="hand2")
    btn.pack(pady=12)

    btn.bind("<Enter>", lambda e: e.widget.config(bg=BTN_LEFT_HOVER))
    btn.bind("<Leave>", lambda e: e.widget.config(bg=BTN_LEFT_BG))

# -------------------- RIGHT SIDE --------------------
tk.Label(right_frame,
         text="Performance Metrics",
         bg=RIGHT_BG,
         fg=METRIC_TITLE_FG,
         font=("Segoe UI", 13, "bold")).pack(pady=(0, 20))

right_buttons = [
    ("PSNR (dB)", PSNR),
    ("Training time (sec)", TT),
    ("Precision", PR),
    ("Recall", RC),
    ("Accuracy", ACC)
]

for text, cmd in right_buttons:
    btn = tk.Button(right_frame,
                    text=text,
                    command=cmd,
                    font=BTN_FONT,
                    bg=BTN_RIGHT_BG,
                    fg=BTN_FG,
                    activebackground=BTN_RIGHT_HOVER,
                    relief="flat",
                    width=30,
                    pady=8,
                    cursor="hand2")
    btn.pack(pady=9)

    btn.bind("<Enter>", lambda e: e.widget.config(bg=BTN_RIGHT_HOVER))
    btn.bind("<Leave>", lambda e: e.widget.config(bg=BTN_RIGHT_BG))

root.mainloop()
