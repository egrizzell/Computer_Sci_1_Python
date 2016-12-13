#MusicBox
from simplewin import simplewin
import winsound
import time


class piano:

    def __init__(self):
        self.key = ''
        self.key_list = ["C.wav", "Cs.wav", "D.wav", "Ds.wav", "E.wav", "F.wav",
                         "Fs.wav", "G.wav", "Gs.wav", "A.wav", "As.wav", "B.wav",
                         "C2.wav"]
        self.key_dict = {'a':self.key_list[0],
                         'w':self.key_list[1],
                         's':self.key_list[2],
                         'e':self.key_list[3],
                         'd':self.key_list[4],
                         'f':self.key_list[5],
                         't':self.key_list[6],
                         'g':self.key_list[7],
                         'y':self.key_list[8],
                         'h':self.key_list[9],
                         'u':self.key_list[10],
                         'j':self.key_list[11],
                         'k':self.key_list[12]
                         }
        

    def play(self, key):
        note = key
        sound = winsound.PlaySound(self.key_dict[note], winsound.SND_FILENAME | winsound.SND_ASYNC)
        return sound
                
class app:
     def __init__(self):
         # the special keyword “None” indicates no object
         self.win = None
         self.record = None
         
     def run(self):
         self.win = simplewin()
         self.win.add_label("My Piano")
         self.win.add_button("Quit", self.quit_program)
         self.win.add_button("Record", self.begin_recording)
         self.win.add_button("Playback", self.begin_playback)
         self.win.add_key_handler(self.key_down)
         self.win.run()
         
     def key_down(self, event):
         if self.record != None:
             self.key_play = piano()
             self.key_play.play(event.keysym)
             self.record.record_key(event.keysym)
         else:
             self.key_play = piano()
             self.key_play.play(event.keysym)
    

     def begin_recording(self):
         self.record = recorder()
         times = timer()
         times.start_timer()
         print("Recording...")

     def begin_playback(self):
         self.play_b = recorder()
         self.p = piano()
         self.play_b.playback(self.record.notes)
         
     def quit_program(self):
         print("Goodbye!")
         self.win.quit()
"""
recorder class with stub methods. Note that "pass" must
be used for empty function bodies, will be removed when
you put real code in.
"""

class recorder:
  def __init__(self):
      """
      Default constructor, going to need some way to store notes.
      """
      self.notes = []
      self.note_t = 0.0

  def record_key(self, key_index):
      """
      Method to record that a particular key (by index) was struck.
      """
      self.keys = key_index
      self.notes.append(self.keys)
      
        
  def playback(self, notes):
      ender = timer()
      ender.stop_timer()
      play_obj = piano()
      for note in notes:
          print(note)
          time.sleep(1)
          play_obj.play(note)
      
class timer:
    def __init__(self):
        self.start_time = 0.0
        self.end_time =0.0
        self.now = 0.0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()
        self.time_elapsed()

    def time_elapsed(self):
        self.time_e = (self.start_time) - (self.end_time)
        print("Time Elapsed: {}".format(self.time_e))

    def note_time(self, note):
        self.note = note
        self.now_time = time.time()
        self.notes_time = (self.start_time) - (self.now_time)
        
        
    
        
app = app()
app.run()

