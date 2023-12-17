import cv2
import tkinter as tk
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Betrayal Project")

        self.root.configure(bg="#696969") # #2b2b2b => dark gray

        self.root.resizable(False, False)

        self.frame_counter = 0

        # Set project label
        self.project_label = tk.Label(self.root, text="Betrayal Project", font=("Helvetica", 20), bg='#696969', fg='white')
        self.project_label.pack(pady=20, fill='y', expand=True)

        # Set project advisiors label
        self.project_advisiors_label = tk.Label(self.root, text="Project Advisiors:\nDr\\ Hussein Alshafie\nDr\\ Mousa Elkhadr", font=("Helvetica", 16), bg='#696969', fg='white')
        self.project_advisiors_label.pack(padx=(10, 0), pady=(20, 10), anchor='w', fill='y', expand=True)

        # Set project developers label
        self.project_developers_label = tk.Label(self.root, text="Project Developers:\nEng\\ Mohamed Khlawy\nEng\\ Waleed Elassar", font=("Helvetica", 16), bg='#696969', fg='white')
        self.project_developers_label.pack(padx=(0, 10), pady=(20, 10), anchor='e', fill='y', expand=True)

        # Set initial dimensions for the Canvas
        self.screen_width = 1000  # Adjust as needed
        self.screen_height = 250  # Adjust as needed
        
        self.character1_width = 250  # Adjust as needed
        self.character1_height = 250  # Adjust as needed

        self.character2_width = 250  # Adjust as needed
        self.character2_height = 250  # Adjust as needed

        self.arch_width = 50
        self.arch_height = 50

        self.whole_width = 1000  # Adjust as needed
        self.whole_height = 250  # Adjust as needed

        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, bg="#696969") # #2b2b2b => dark gray
        self.canvas.pack(fill='y', expand=True)

        self.btn_quit = tk.Button(self.root, text="Individual Scenes", font='Helvetica 12 bold', command=self.individual)
        self.btn_quit.pack(pady=5, fill='y', expand=True)
        
        self.btn_quit = tk.Button(self.root, text="Whole Scene", font='Helvetica 12 bold', command=self.whole)
        self.btn_quit.pack(pady=5, fill='y', expand=True)

        self.btn_restart = tk.Button(self.root, text="Restart GUI", font='Helvetica 12 bold', command=self.restart)
        self.btn_restart.pack(pady=5, fill='y', expand=True)

        self.btn_quit = tk.Button(self.root, text="Quit", font='Helvetica 12 bold', command=self.quit)
        self.btn_quit.pack(pady=5, fill='y', expand=True)

        self.delay1 = 150
        #self.delay2 = 150

    def run(self):
        self.root.mainloop()

    def display_first_frame_of_video_whole(self):
        ret, frame = self.cap_whole.read()

        if ret:
            frame = cv2.resize(frame, (self.whole_width, self.whole_height))

            self.photo3 = self.convert_to_photo(frame)
            
            x = 0  # Adjust as needed
            y = 0  # Adjust as needed

            self.canvas_image2 = self.canvas.create_image(x, y, anchor=tk.NW, image=self.photo3)

    def display_first_frame_of_video2(self):
        ret, frame = self.cap_2.read()

        if ret:
            frame = cv2.resize(frame, (self.character2_width, self.character2_height))

            self.photo2 = self.convert_to_photo(frame)
            
            x = 750  # Adjust as needed
            y = 0  # Adjust as needed

            self.canvas_image2 = self.canvas.create_image(x, y, anchor=tk.NW, image=self.photo2)

    def update1(self):
        ret, frame = self.cap_1.read()

        if self.frame_counter == 15:
            #self.cap_1.release()  # Release the first video capture

            self.display_moving_arch()

            self.update2()

            #return

        if ret:
            frame = cv2.resize(frame, (self.character1_width, self.character1_height))
            self.photo1 = self.convert_to_photo(frame)

            self.frame_counter += 1

            x = 0  # Adjust as needed
            y = 0  # Adjust as needed

            self.canvas.create_image(x, y, anchor=tk.NW, image=self.photo1)

            self.root.after(self.delay1, self.update1)

        else:
            #print (f"number of frame in first video = {self.frame_counter}")

            self.cap_1.release()  # Release the first video capture

            #self.display_moving_arch()

            self.update2()

    def update2(self):
        ret, frame = self.cap_2.read()

        if ret:
            frame = cv2.resize(frame, (self.character2_width, self.character2_height))

            self.photo2 = self.convert_to_photo(frame)
            
            x = 750  # Adjust as needed
            y = 0  # Adjust as needed

            self.canvas_image2 = self.canvas.create_image(x, y, anchor=tk.NW, image=self.photo2)

            self.root.after(self.delay1, self.update2)
        else:
            # Video has reached the end
            self.video_finished2 = True
            self.cap_2.release()  # Release the second video capture

    def display_moving_arch(self):
        self.arch = tk.PhotoImage(file="final_arch1.png")
        #self.arch = cv2.resize(self.arch, (50, 50))
        x = 250
        self.dx = 50
        self.canvas.create_image(x, 100, image=self.arch, tags="arch")
        while True:
            self.canvas.move("arch", self.dx, 0)
            self.canvas.after(100)
            self.canvas.update()
            if x < 800:
                x += self.dx
            else:
                self.canvas.delete("arch")
                break

    def update3(self):
        ret, frame = self.cap_whole.read()

        if ret:
            frame = cv2.resize(frame, (self.whole_width, self.whole_height))

            self.photo3 = self.convert_to_photo(frame)

            self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo3)

            self.root.after(25, self.update3)

    def convert_to_photo(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        self.photo = ImageTk.PhotoImage(image=image)  # Update the reference
        return self.photo

    def quit(self):
        #self.cap_1.release()
        #self.cap_2.release()
        self.root.destroy()

    def individual(self):
        self.video_source1 = "video 1_low 1.mp4"
        self.cap_1 = cv2.VideoCapture(self.video_source1)
        self.video_source2 = "video 2_low 1.mp4"
        self.cap_2 = cv2.VideoCapture(self.video_source2)
        self.video_source_whole = "whole_scene.mp4"
        self.cap_whole = cv2.VideoCapture(self.video_source_whole)
        
        self.display_first_frame_of_video_whole()
        self.display_first_frame_of_video2()
        self.update1()
        
    def whole(self):
        self.video_source_whole = "whole_scene.mp4"
        self.cap_whole = cv2.VideoCapture(self.video_source_whole)

        self.update3()

    def restart(self):
        self.root.destroy()
        video_player = VideoPlayer()
        video_player.run()


if __name__ == "__main__":
    video_player = VideoPlayer()
    video_player.run()