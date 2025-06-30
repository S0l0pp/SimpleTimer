import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("☁️ Cloud Timer")
        self.root.geometry("560x400")  # Bigger window
        self.root.configure(bg="#e6f2ff")  # Soft sky blue
        self.root.resizable(False, False)

        self.time_left = 0
        self.running = False

        self.label = tk.Label(root, text="00:00", font=("Segoe UI", 64, "bold"), bg="#e6f2ff", fg="#4d4d4d")
        self.label.pack(pady=25)

        self.entry = tk.Entry(root, font=("Segoe UI", 20), justify='center',
                              bg="white", fg="#333333", relief="flat", bd=5)
        self.placeholder = "Enter seconds"
        self.entry.pack(pady=15, ipady=10, ipadx=14)
        self.entry.insert(0, self.placeholder)
        self.entry.config(fg='grey')

        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._add_placeholder)

        button_frame = tk.Frame(root, bg="#e6f2ff")
        button_frame.pack(pady=15)

        self.start_button = tk.Button(button_frame, text="▶ Start", command=self.start_timer,
                                      font=("Segoe UI", 16, "bold"),
                                      bg="#b3d9ff", fg="#003366", activebackground="#99ccff",
                                      relief="flat", padx=16, pady=8, width=10)
        self.start_button.grid(row=0, column=0, padx=8)

        self.pause_button = tk.Button(button_frame, text="⏸ Pause", command=self.pause_timer,
                                      font=("Segoe UI", 16, "bold"),
                                      bg="#ffd9b3", fg="#663300", activebackground="#ffc299",
                                      relief="flat", padx=16, pady=8, width=10)
        self.pause_button.grid(row=0, column=1, padx=8)

        self.reset_button = tk.Button(button_frame, text="🔄 Reset", command=self.reset_timer,
                                      font=("Segoe UI", 16, "bold"),
                                      bg="#ffcccc", fg="#660000", activebackground="#ffb3b3",
                                      relief="flat", padx=16, pady=8, width=10)
        self.reset_button.grid(row=0, column=2, padx=8)

    def _clear_placeholder(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, tk.END)
            self.entry.config(fg="#333333")

    def _add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg='grey')

    def start_timer(self):
        if not self.running:
            try:
                val = self.entry.get()
                if val == self.placeholder:
                    raise ValueError  # Prevent starting with placeholder text
                self.time_left = int(val)
                self.running = True
                self.update_timer()
            except ValueError:
                self.label.config(text="Invalid")

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.label.config(text="00:00")

    def update_timer(self):
        if self.running:
            if self.time_left >= 0:
                mins, secs = divmod(self.time_left, 60)
                time_str = f"{mins:02}:{secs:02}"
                self.label.config(text=time_str)
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.label.config(text="☁️ Done!")
                self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
