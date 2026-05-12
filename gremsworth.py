"""
╔══════════════════════════════════════════════╗
║   KOKO  — Desktop Monkey Pet v8              ║
║   Ultimate Productivity Companion Update!    ║
╚══════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import Menu, simpledialog, messagebox
import random, time, threading, math
import psutil
from datetime import datetime
import os, subprocess, urllib.request, urllib.parse, ctypes, webbrowser, shutil
import ctypes.wintypes

# ══════════════════════════════════════════════
#  COLOUR PALETTE
# ══════════════════════════════════════════════
_  = None
TRANS = "#010203"  # Windows transparent key colour
O  = "#2d1b10" # Outline
F1 = "#6d4c41" # Dark fur
F2 = "#8d6e63" # Light fur
S1 = "#ffe0b2" # Skin light (face)
S2 = "#ffb74d" # Skin dark (hands/feet)
E  = "#000000" # Eye black / text
W  = "#ffffff" # Eye white / book pages
P  = "#ff8a80" # Pink (blush/mouth)
BC = "#1e88e5" # Book cover (Blue)

# ══════════════════════════════════════════════
#  PIXEL FRAMES  (14 cols × 14 rows)
# ══════════════════════════════════════════════
FRAMES = {
  "idle": [
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_],
      [_,O ,S2,O ,F2,F2,F2,F2,O ,S2,O ,O ,_],
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_],
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,_,_,_],
      [_,_,O ,S2,F2,F2,F2,F2,S2,O ,O ,O ,_,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,F1,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_],
    ]
  ],

  "walk": [
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,O ,S2,O ,F2,F2,F2,F2,O ,_,_,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,O ,S2,O ,O ,_,_], 
      [_,_,O ,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,O ,S2,O ,_,_,_,O ,S2,O ,_,_,_,_],
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,F2,F2,F2,F2,S2,O ,O ,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_],
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,_,O ,O ], 
      [_,_,O ,S2,O ,F2,F2,F2,F2,O ,S2,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,O ,_,_,_],
      [_,_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_],
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,F2,F2,F2,F2,S2,O ,O ,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_],
    ],
  ],

  "focus": [
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,E ,W ,S1,S1,W ,E ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,S1,S1,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,BC,BC,BC,BC,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,W ,W ,W ,W ,S2,O ,_,_,O ,_], 
      [_,_,O ,S2,W ,E ,W ,E ,S2,F1,O ,O ,_,_], 
      [_,_,O ,O ,BC,BC,BC,BC,O ,O ,O ,_,_,_], 
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ]
  ],

  "sleep": [
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,O ,O ,S1,S1,O ,O ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,S1,S1,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,F2,F2,F2,F2,S2,O ,_,_,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,O ,O ,S1,S1,O ,O ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,S1,S1,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,F2,F2,F2,F2,S2,O ,_,_,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ]
  ],

  "excited": [
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F2,F2,F2,F2,F2,F2,O ,_,_,_,_],
      [_,O ,S2,S2,F2,F2,F2,F2,S2,S2,O ,_,_,_],
      [_,O ,S2,O ,F2,F2,F2,F2,O ,S2,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,E ,W ,S1,S1,W ,E ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,W ,W ,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F2,F2,F2,F2,O ,_,_,O ,O ,_], 
      [_,O ,S2,S1,S1,S1,S1,S1,S2,O ,_,O ,_], 
      [_,_,O ,F2,S1,S1,S1,S1,F2,F2,O ,O ,_,_], 
      [_,_,O ,F2,F2,F2,F2,F2,F2,F2,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F2,F2,F2,F2,F2,F2,O ,_,_,_,_],
      [_,O ,S2,S2,F2,F2,F2,F2,S2,S2,O ,_,_,_],
      [_,O ,S2,O ,F2,F2,F2,F2,O ,S2,O ,_,_,_],
      [_,_,O ,S1,S1,S1,S1,S1,S1,O ,_,_,_,_],
      [_,O ,S1,E ,W ,S1,S1,W ,E ,S1,O ,_,_,_],
      [_,O ,S1,S1,S1,P ,P ,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,W ,W ,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F2,F2,F2,F2,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,S1,S1,S1,S1,S2,O ,_,O ,_], 
      [_,_,O ,F2,S1,S1,S1,S1,F2,F2,O ,O ,_,_], 
      [_,_,O ,F2,F2,F2,F2,F2,F2,F2,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ]
  ],

  "angry": [
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,O ,S1,S1,S1,S1,O ,O ,_,_,_,_],
      [_,O ,S1,O ,W ,S1,S1,W ,O ,S1,O ,_,_,_],
      [_,O ,S1,P ,P ,P ,P ,P ,P ,S1,O ,_,_,_],
      [_,_,O ,P ,P ,E ,E ,P ,P ,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,F2,F2,F2,F2,S2,O ,_,_,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,O ,S1,S1,S1,S1,O ,O ,_,_,_,_],
      [_,O ,S1,O ,W ,S1,S1,W ,O ,S1,O ,_,_,_],
      [_,O ,S1,P ,P ,P ,P ,P ,P ,S1,O ,_,_,_],
      [_,_,O ,P ,P ,E ,E ,P ,P ,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,_,O ,S2,F2,F2,F2,F2,S2,O ,_,_,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ]
  ],

  "shocked": [
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,W ,S1,S1,W ,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_], 
      [_,O ,S1,S1,S1,S1,S1,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,O ,O ,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,O ,S2,O ,F2,F2,F2,F2,O ,S2,O ,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ],
    [
      [_,_,_,_,_,_,_,_,_,_,_,_,_,_],
      [_,_,_,O ,O ,O ,O ,O ,O ,_,_,_,_,_],
      [_,_,O ,F1,F1,F1,F1,F1,F1,O ,_,_,_,_],
      [_,O ,S1,S1,F1,F1,F1,F1,S1,S1,O ,_,_,_],
      [_,O ,S1,O ,F1,F1,F1,F1,O ,S1,O ,_,_,_],
      [_,_,O ,S1,W ,S1,S1,W ,S1,O ,_,_,_,_],
      [_,O ,S1,W ,E ,S1,S1,E ,W ,S1,O ,_,_,_], 
      [_,O ,S1,S1,S1,S1,S1,S1,S1,S1,O ,_,_,_],
      [_,_,O ,S1,S1,O ,O ,S1,S1,O ,_,_,_,_],
      [_,_,_,O ,F1,F1,F1,F1,O ,_,_,O ,O ,_], 
      [_,O ,S2,O ,F2,F2,F2,F2,O ,S2,O ,O ,_], 
      [_,_,O ,F1,F2,F2,F2,F2,F1,F1,O ,O ,_,_], 
      [_,_,O ,F1,F1,F1,F1,F1,F1,F1,O ,_,_,_],
      [_,_,_,O ,S2,O ,_,O ,S2,O ,_,_,_,_], 
    ]
  ],
}

FRAME_MS = {
    "idle":    650,
    "walk":    160,
    "sleep":   950,
    "excited": 130,
    "angry":   110,
    "shocked": 190,
    "focus":   1000,
    "dance":   100,
}

# ══════════════════════════════════════════════
#  DIALOGUE
# ══════════════════════════════════════════════
IDLE_ROASTS = [
    "Just monkeying around?",
    "Idle for {min} min. Bananas.",
    "Ooo ooo ah ah! (Do some work!)",
    "Did you fall asleep? Oh. You didn't.",
    "Tasks won't finish themselves.",
    "Blink twice if you need a banana.",
]
CLICK_LINES = [
    "Eeeek! Personal space!",
    "Ow. Rude.",
    "Ooo ooo?",
    "Yes yes, adorable. Back to work.",
    "Stop poking the monkey.",
    "Fine. Hello. Happy? Shoo.",
]
HIGH_CPU_LINES = [
    "CPU at {pct}%! Hotter than a jungle in here!",
    "Your laptop is sweating. 🐒",
]
HIGH_RAM_LINES = [
    "RAM at {pct}%. Too many tabs!",
    "Memory: catastrophic. Eeeek!",
]
LATE_NIGHT_LINES = [
    "It's {hour}am. Monkeys sleep at night.",
    "Normal people sleep now.",
]
MORNING_LINES = [
    "Morning! Time for bananas! 🍌",
    "Another day. Another jungle.",
]
FEED_LINES = [
    "Ooo ooo! 🍌 Delicious!",
    "Mmm. Tastes like a virtual banana.",
    "I'll throw less poop today.",
]
POKE_LINES = [
    "EEEEK! STOP THAT.",
    "I will throw things at you.",
    "You absolute menace. 🐒",
]

# ══════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════
PIXEL      = 6     # Smaller, less intrusive size
COLS, ROWS = 14, 14
GOBLIN_W   = COLS * PIXEL
GOBLIN_H   = ROWS * PIXEL
WIN_W      = 200   
WIN_H      = 160

class GremsworthApp:
    def __init__(self):
        self.root = tk.Tk()
        self._build_window()
        self._build_canvas()
        self._build_menu()
        self._init_state()
        self._start_threads()
        self._tick()
        self._particle_tick()
        self._movement_tick()
        self.root.mainloop()

    # ── window ────────────────────────────────

    def _build_window(self):
        self.root.title("Koko Monkey Pet")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", TRANS)
        self.root.configure(bg=TRANS)
        
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        
        self.x = self.sw - WIN_W - 20
        self.y = self.sh - WIN_H - 60
        self.root.geometry(f"{WIN_W}x{WIN_H}+{int(self.x)}+{int(self.y)}")
        
        self.root.bind("<ButtonPress-1>",   self._drag_start)
        self.root.bind("<B1-Motion>",       self._drag_motion)
        self.root.bind("<ButtonRelease-1>", self._on_release)
        self.root.bind("<Button-3>",        self._show_menu)

    # ── canvas ────────────────────────────────

    def _build_canvas(self):
        self.canvas = tk.Canvas(
            self.root,
            width=WIN_W,
            height=WIN_H,
            bg=TRANS,
            highlightthickness=0
        )
        self.canvas.pack()
        
        self.goblin_ox = (WIN_W - GOBLIN_W) // 2
        self.goblin_oy = WIN_H - GOBLIN_H - 10
        
        self._cells = [
            [
                self.canvas.create_rectangle(
                    self.goblin_ox + c * PIXEL, self.goblin_oy + r * PIXEL,
                    self.goblin_ox + c * PIXEL + PIXEL, self.goblin_oy + r * PIXEL + PIXEL,
                    fill=TRANS, outline="", width=0,
                )
                for c in range(COLS)
            ]
            for r in range(ROWS)
        ]
        
        self.bubble_bg = self.canvas.create_rectangle(0,0,0,0, fill="#22222a", outline="#ffb74d", width=2, state="hidden")
        self.speech_text = self.canvas.create_text(
            WIN_W//2, 35, text="", fill="#ffffff",
            font=("Segoe UI", 9, "bold"), justify="center", width=180, state="hidden"
        )
        
        self.particles = []

    def _build_menu(self):
        self.menu = Menu(self.root, tearoff=0,
                         bg="#111827", fg="#ffcc80",
                         activebackground="#ffcc80",
                         activeforeground="#111",
                         font=("Segoe UI", 9, "bold"))
        self.menu.add_command(label="🍅 Focus Mode (25m)", command=self._start_focus)
        self.menu.add_command(label="🔍 Quick Search", command=self._quick_search)
        
        # Timesheet Tracker
        self.time_menu = Menu(self.menu, tearoff=0, bg="#111827", fg="#ffcc80",
                              activebackground="#ffcc80", activeforeground="#111", font=("Segoe UI", 9, "bold"))
        self.menu.add_cascade(label="⏱️ Time Tracker", menu=self.time_menu)
        self.time_menu.add_command(label="▶️ Start Project...", command=self._start_project)
        self.time_menu.add_command(label="⏹️ Stop Tracking", command=self._stop_project)
        self.time_menu.add_command(label="📊 View Summary", command=self._view_timesheet)
        
        # Interactive To-Do List
        self.task_menu = Menu(self.menu, tearoff=0, bg="#111827", fg="#ffcc80",
                              activebackground="#ffcc80", activeforeground="#111", font=("Segoe UI", 9, "bold"))
        self.menu.add_cascade(label="📋 Tasks", menu=self.task_menu)
        
        # Music Dancer & Media Controller
        self.media_menu = Menu(self.menu, tearoff=0, bg="#111827", fg="#ffcc80",
                               activebackground="#ffcc80", activeforeground="#111", font=("Segoe UI", 9, "bold"))
        self.menu.add_cascade(label="🎵 Media", menu=self.media_menu)
        self.media_menu.add_command(label="⏯ Play / Pause", command=lambda: ctypes.windll.user32.keybd_event(0xB3, 0, 0, 0))
        self.media_menu.add_command(label="⏭ Next Track", command=lambda: ctypes.windll.user32.keybd_event(0xB0, 0, 0, 0))
        self.media_menu.add_command(label="⏮ Prev Track", command=lambda: ctypes.windll.user32.keybd_event(0xB1, 0, 0, 0))
        self.media_menu.add_separator()
        self.media_menu.add_command(label="🕺 Dance!", command=self._dance)
        
        self.menu.add_command(label="📝 Open Notepad", command=self._open_notepad)
        self.menu.add_separator()
        self.menu.add_command(label="🐾 Follow Mouse", command=self._toggle_follow)
        self.menu.add_command(label="🎾 Play Fetch", command=self._play_fetch)
        self.menu.add_command(label="🪟 Toggle Window Perch", command=self._toggle_perch)
        self.menu.add_command(label="📸 Take Screenshot", command=self._take_screenshot)
        self.menu.add_command(label="🧹 Clean PC Trash", command=self._clean_temp)
        self.menu.add_separator()
        self.menu.add_command(label="🍌 Feed Monkey", command=self._feed)
        self.menu.add_command(label="👉 Poke him",        command=self._poke)
        self.menu.add_separator()
        self.menu.add_command(label="❌ Quit",            command=self.root.destroy)

    # ── state ─────────────────────────────────

    def _init_state(self):
        self.state           = "idle"
        self.frame_idx       = 0
        self.last_activity   = time.time()
        self.speech_clear_at = 0.0
        self._drag_x         = 0
        self._drag_y         = 0
        self._drag_moved     = False
        self._next_frame_at  = 0.0
        
        # Rogue-like movement state
        self.direction       = 1    
        self.vy              = 0.0  
        self.hold_timer      = 0.0
        self.climb_timer     = 0.0
        self.is_dragging     = False
        
        # Productive states
        self.focus_end_time    = 0.0
        self.tasks             = []
        self.last_hydrate_time = time.time()
        self.uncommitted_since = time.time()
        self.internet_down     = False
        
        self.current_project   = None
        self.project_start_time = 0.0
        self.timesheet         = {}
        
        self.is_following      = False
        self.is_fetching       = False
        self.window_perch      = False
        self.window_rects      = []
        
        self._update_task_menu()

    # ── main tick (tkinter thread-safe) ───────

    def _tick(self):
        now = time.time()
        if now >= self._next_frame_at:
            frames = FRAMES.get(self.state)
            if not frames:
                if self.state == "hold":
                    frames = FRAMES["angry"]
                elif self.state == "fall":
                    frames = FRAMES["shocked"]
                elif self.state == "climb":
                    frames = FRAMES["walk"]
                elif self.state == "dance":
                    frames = FRAMES["excited"]
                else:
                    frames = FRAMES["idle"]

            self.frame_idx = (self.frame_idx + 1) % len(frames)
            self._draw_frame(frames[self.frame_idx])
            
            ms = FRAME_MS.get(self.state, 600)
            if self.state == "hold": ms = FRAME_MS["angry"]
            elif self.state == "fall": ms = FRAME_MS["shocked"]
            elif self.state == "climb": ms = 140
            self._next_frame_at = now + ms / 1000.0
            
            if self.state == "sleep" and self.frame_idx == 0:
                self._spawn_particle("Zzz", "#4488ff")
            elif self.state == "angry" and self.frame_idx == 0:
                self._spawn_particle("🗯️", "#ff2200")
            elif self.state == "excited" and self.frame_idx == 0:
                self._spawn_particle("✨", "#ffe066")

        if self.speech_clear_at and now > self.speech_clear_at:
            self.canvas.itemconfig(self.bubble_bg, state="hidden")
            self.canvas.itemconfig(self.speech_text, state="hidden")
            self.speech_clear_at = 0.0
            
        self.root.after(40, self._tick)

    def _draw_frame(self, frame):
        # Determine mouse position for dynamic eyes!
        mx = self.root.winfo_pointerx()
        cx = self.x + WIN_W // 2
        if mx < cx - 100: eye_dir = -1
        elif mx > cx + 100: eye_dir = 1
        else: eye_dir = 0
        
        is_falling = (self.state == "fall")
        if is_falling:
            frame = frame[::-1]

        for r, row in enumerate(frame):
            for c, colour in enumerate(row):
                fill = colour if colour else TRANS
                
                # Interactive Eyes
                if not is_falling and self.state in ["idle", "walk", "excited", "dance"]:
                    if r == 6 and fill in (W, E):
                        # Eyes are in cols 3, 4 (left eye) and 7, 8 (right eye)
                        if eye_dir == -1: # look left
                            if c in (3, 7): fill = E
                            if c in (4, 8): fill = W
                        elif eye_dir == 1: # look right
                            if c in (3, 7): fill = W
                            if c in (4, 8): fill = E
                        else: # Look center
                            if c in (3, 8): fill = W
                            if c in (4, 7): fill = E

                self.canvas.itemconfig(self._cells[r][c], fill=fill)

    # ── appealing mechanics ───────────────────
    
    def _particle_tick(self):
        alive_particles = []
        for p in self.particles:
            canvas_id, px, py, life = p
            py -= 1  
            life -= 1
            if life <= 0:
                self.canvas.delete(canvas_id)
            else:
                self.canvas.coords(canvas_id, px, py)
                alive_particles.append((canvas_id, px, py, life))
        self.particles = alive_particles
        self.root.after(50, self._particle_tick)

    def _spawn_particle(self, text, color):
        px = self.goblin_ox + GOBLIN_W//2 + random.randint(-20, 20)
        py = self.goblin_oy + random.randint(0, 10)
        canvas_id = self.canvas.create_text(
            px, py, text=text, fill=color, font=("Segoe UI", 12, "bold")
        )
        self.particles.append((canvas_id, px, py, 40)) 

    def _movement_tick(self):
        if not self.is_dragging:
            
            # DYNAMIC FLOOR CALCULATION (Window Perch)
            base_floor = self.sh - WIN_H - 10
            highest_floor = base_floor
            
            if getattr(self, "window_perch", False) and getattr(self, "window_rects", None):
                wx = self.x + WIN_W//2
                wy = self.y + WIN_H - 10
                for (l, t, r, b) in self.window_rects:
                    if l < wx < r and t >= wy - 30:
                        f = t - WIN_H + 10
                        if f < highest_floor:
                            highest_floor = f
            floor_y = highest_floor
            
            # BALL PHYSICS (for Fetch!)
            if hasattr(self, "ball") and self.ball and self.ball.winfo_exists():
                if getattr(self.ball, "is_dragging", False) == False:
                    self.ball.vy += 1.5
                    self.ball.x += self.ball.vx
                    self.ball.y += self.ball.vy
                    
                    if self.ball.x < 0:
                        self.ball.x = 0; self.ball.vx *= -0.7
                    elif self.ball.x > self.sw - 24:
                        self.ball.x = self.sw - 24; self.ball.vx *= -0.7
                        
                    # Calculate dynamic floor for the BALL!
                    ball_floor = self.sh - 50
                    if getattr(self, "window_perch", False) and getattr(self, "window_rects", None):
                        bx = self.ball.x + 12
                        by = self.ball.y + 24
                        for (l, t, r, b) in self.window_rects:
                            if l < bx < r and t >= by - 50:
                                f = t - 24
                                if f < ball_floor:
                                    ball_floor = f

                    if self.ball.y > ball_floor:
                        self.ball.y = ball_floor
                        self.ball.vy *= -0.6
                        self.ball.vx *= 0.8
                    self.ball.geometry(f"+{int(self.ball.x)}+{int(self.ball.y)}")
            
            # 0. FETCH MOUSE OR BALL
            if self.is_following or (self.is_fetching and hasattr(self, "ball") and self.ball.winfo_exists()):
                if self.is_following:
                    tx = self.root.winfo_pointerx() - GOBLIN_W//2
                    ty = self.root.winfo_pointery() - GOBLIN_H - 10
                    
                    dx = tx - self.x
                    dy = ty - self.y
                    dist = math.hypot(dx, dy)
                    
                    if dist > 30:
                        speed = 6.0
                        self.x += (dx / dist) * speed
                        self.y += (dy / dist) * speed
                        if dx > 0: self.direction = 1
                        elif dx < 0: self.direction = -1
                        
                        if abs(dy) > abs(dx) + 20: self._set_state("climb")
                        else: self._set_state("walk")
                    else:
                        self._set_state("idle")
                        
                else: # FETCHING THE BALL!
                    tx = self.ball.x - GOBLIN_W//2
                    ty = self.ball.y - GOBLIN_H
                    dx = tx - self.x
                    
                    # He runs along the floor to get under the ball
                    if self.y < floor_y - 5:
                        self._set_state("fall")
                        self.vy += 1.2
                        self.y += self.vy
                    else:
                        self.y = floor_y
                        self.vy = 0.0
                        if abs(dx) > 15:
                            speed = 5.0
                            self.x += speed if dx > 0 else -speed
                            self.direction = 1 if dx > 0 else -1
                            self._set_state("walk")
                        else:
                            self._set_state("idle")
                            
                    # Can he catch it? Allow some leniency if it's right under him
                    dy = ty - self.y
                    dist = math.hypot(dx, dy)
                    is_held = getattr(self.ball, "is_dragging", False)
                    
                    if (dist <= 40 or (abs(dx) < 30 and abs(dy) < 80)) and not is_held:
                        self.ball.destroy()
                        self.is_fetching = False
                        self._speak("Got it! 🎾", "excited", 3.0)
                        self._set_state("excited")
                    
                self.root.geometry(f"+{int(self.x)}+{int(self.y)}")
                self.root.after(30, self._movement_tick)
                return
            
            # 1. WALK: Move horizontally until screen edge
            if self.state == "walk":
                if self.y < floor_y - 5: # Walked off a ledge
                    self._set_state("fall")
                    self.vy = 0
                else:
                    self.y = floor_y # Snap to current dynamic floor
                    speed = 4.0
                    self.x += speed * self.direction
                    
                    offset_x = (WIN_W - GOBLIN_W) // 2
                    right_bound = self.sw - WIN_W + offset_x
                    left_bound = -offset_x
                    
                    if self.direction > 0 and self.x >= right_bound:
                        self.x = right_bound
                        self._set_state("climb")
                        self.climb_timer = time.time() + random.uniform(1.0, 3.5)
                    elif self.direction < 0 and self.x <= left_bound:
                        self.x = left_bound
                        self._set_state("climb")
                        self.climb_timer = time.time() + random.uniform(1.0, 3.5)
                        
                self.root.geometry(f"+{int(self.x)}+{int(self.y)}")
                
            # 2. CLIMB: Scale the wall upwards!
            elif self.state == "climb":
                speed = 3.0
                self.y -= speed
                
                ceiling_y = -30
                if self.y <= ceiling_y or time.time() > self.climb_timer:
                    if self.y < ceiling_y: self.y = ceiling_y
                    self._set_state("hold")
                    self.hold_timer = time.time() + 1.5
                    
                self.root.geometry(f"+{int(self.x)}+{int(self.y)}")
                
            # 3. HOLD: Stick to wall briefly
            elif self.state == "hold":
                if time.time() > self.hold_timer:
                    self._set_state("fall")
                    self.vy = 0.0
                    if random.random() < 0.3:
                        self._speak("EEEEK!", "shocked", 1.5)
                    
            # 4. FALL: Gravity takes over
            elif self.state == "fall":
                gravity = 1.2
                self.vy += gravity
                self.y += self.vy
                
                if self.y >= floor_y:
                    self.y = floor_y
                    self.vy = 0.0
                    self.direction *= -1 
                    if random.random() < 0.6:
                        self._set_state("walk")
                    else:
                        self._set_state("idle")
                self.root.geometry(f"+{int(self.x)}+{int(self.y)}")
                
            # 5. DANCE: Jump and wiggle
            elif self.state == "dance":
                if random.random() < 0.1:
                    self.vy = -12.0 # High jump!
                self.vy += 1.5 # Gravity
                self.y += self.vy
                
                # Wiggle horizontal
                if random.random() < 0.3:
                    self.x += random.choice([-8, 8])
                    
                if self.y >= floor_y:
                    self.y = floor_y
                    self.vy = 0.0
                    
                self.root.geometry(f"+{int(self.x)}+{int(self.y)}")
                
        self.root.after(30, self._movement_tick)

    # ── background threads ────────────────────

    def _start_threads(self):
        threading.Thread(target=self._behavior_loop, daemon=True).start()
        threading.Thread(target=self._system_watch,  daemon=True).start()
        
    def _update_window_rects(self):
        rects = []
        def callback(hwnd, extra):
            if ctypes.windll.user32.IsWindowVisible(hwnd) and not ctypes.windll.user32.IsIconic(hwnd):
                length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                if length > 0:
                    rect = ctypes.wintypes.RECT()
                    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
                    w = rect.right - rect.left
                    h = rect.bottom - rect.top
                    # Ignore full screen and tiny windows
                    if 200 < w < self.sw - 10 and 100 < h < self.sh - 10:
                        rects.append((rect.left, rect.top, rect.right, rect.bottom))
            return True
        WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL, ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)
        ctypes.windll.user32.EnumWindows(WNDENUMPROC(callback), 0)
        self.window_rects = rects

    def _system_watch(self):
        time.sleep(2)
        sys_tick = 0
        while True:
            sys_tick += 1
            
            # Window Perch 🪟 Check (Every second)
            if getattr(self, "window_perch", False):
                self._update_window_rects()
            
            # 2. Distraction Yeller (Focus Mode Check) - Every 5s
            if sys_tick % 5 == 0 and self.state == "focus":
                try:
                    hwnd = ctypes.windll.user32.GetForegroundWindow()
                    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                    buf = ctypes.create_unicode_buffer(length + 1)
                    ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                    title = buf.value.lower()
                    distractions = ["youtube", "twitter", "facebook", "reddit", "instagram", "tiktok", "game", "netflix"]
                    if any(d in title for d in distractions):
                        self._speak(f"Get off that window! Focus!", "angry", 4.0)
                except Exception:
                    pass
            
            # 8. Wi-Fi & Internet Monitor - Every 10s
            if sys_tick % 10 == 0:
                try:
                    urllib.request.urlopen('http://1.1.1.1', timeout=2)
                    self.internet_down = False
                except:
                    if not self.internet_down:
                        self.internet_down = True
                        self._speak("Internet disconnected! We are stranded!", "shocked", 8.0)
                        
            # Desktop Cleanup Monitor (Every 60s)
            if sys_tick % 60 == 0:
                try:
                    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
                    if os.path.exists(desktop):
                        items = len([name for name in os.listdir(desktop) if not name.startswith('.')])
                        if items > 25 and random.random() < 0.4:
                            self._speak(f"Your desktop is a mess!\n{items} items! Clean it up!", "angry", 6.0)
                except Exception:
                    pass
                        
            # Battery, CPU, RAM, and Git - Every 30s
            if sys_tick % 30 == 0:
                try:
                    cpu = psutil.cpu_percent()
                    ram = psutil.virtual_memory().percent
                    if cpu > 80 and random.random() < 0.3:
                        self._speak(random.choice(HIGH_CPU_LINES).format(pct=int(cpu)), "shocked")
                    elif ram > 85 and random.random() < 0.3:
                        self._speak(random.choice(HIGH_RAM_LINES).format(pct=int(ram)), "angry")
                        
                    # 5. Battery/Power Panic
                    if hasattr(psutil, "sensors_battery"):
                        batt = psutil.sensors_battery()
                        if batt and not batt.power_plugged and batt.percent < 15:
                            if random.random() < 0.5:
                                self._speak(f"Battery {batt.percent}%! I'm dying! Plug me in!", "shocked", 5.0)
                                
                    # 7. Git / Code Commit Nagging
                    if os.path.exists(".git"):
                        status = subprocess.check_output(["git", "status", "--porcelain"], text=True, stderr=subprocess.DEVNULL)
                        if status.strip():
                            if time.time() - self.uncommitted_since > 3600: # 1 hour
                                if random.random() < 0.4:
                                    self._speak("You have uncommitted code! What if it crashes?!", "angry", 6.0)
                        else:
                            self.uncommitted_since = time.time()
                except Exception:
                    pass
                    
            time.sleep(1)

    def _behavior_loop(self):
        time.sleep(4)
        while True:
            # Check Focus Mode
            if self.state == "focus":
                if time.time() > self.focus_end_time:
                    self._set_state("excited")
                    self._speak("TIME'S UP! Take a break! 🍌", "excited", 10.0)
                else:
                    rem = int((self.focus_end_time - time.time()) / 60)
                    if rem in [20, 15, 10, 5] and random.random() < 0.2:
                        self._speak(f"Keep it up! {rem} mins left.", "focus", 4.0)
                time.sleep(15)
                continue
                
            # 1. Hydration & Posture Coach
            if time.time() - self.last_hydrate_time > 45 * 60:
                self.last_hydrate_time = time.time()
                self._speak("Posture check! Sit up straight and drink water! 💧", "excited", 8.0)
                time.sleep(15)
                continue

            idle = time.time() - self.last_activity
            hour = datetime.now().hour
            
            if self.is_dragging:
                time.sleep(2)
                continue

            if hour == 8 and random.random() < 0.05:
                self._speak(random.choice(MORNING_LINES), "excited")
            elif 1 <= hour < 5 and random.random() < 0.08:
                self._speak(random.choice(LATE_NIGHT_LINES).format(hour=hour), "angry")
            elif idle > 300 and self.tasks and random.random() < 0.2:
                # 4. Interactive To-Do List Reminder
                self._speak(f"Don't forget to: {self.tasks[0]}", "idle", 5.0)
            elif idle > 400 and self.current_project and random.random() < 0.2:
                mins = int((time.time() - self.project_start_time) // 60)
                self._speak(f"Working on {self.current_project}\nfor {mins} mins.", "idle", 5.0)
            elif idle > 600 and random.random() < 0.15:
                self._speak(random.choice(IDLE_ROASTS).format(min=int(idle // 60)), "idle")
            elif idle > 1200:
                self._set_state("sleep")
            elif self.state == "sleep" and idle < 1200:
                self._set_state("idle")
            elif self.state == "idle" and random.random() < 0.2:
                self.direction = random.choice([-1, 1])
                self._set_state("walk")
            time.sleep(15)

    # ── interactions ──────────────────────────
    
    def _add_task(self):
        task = simpledialog.askstring("Add Task", "What needs to be done?", parent=self.root)
        if task:
            self.tasks.append(task)
            self._update_task_menu()
            self._speak("Task added! Let's get to work.", "excited", 3.0)

    def _complete_task(self, idx):
        if idx < len(self.tasks):
            task = self.tasks.pop(idx)
            self._update_task_menu()
            self._speak(f"Finished: {task}!\nGreat job!", "excited", 5.0)

    def _update_task_menu(self):
        self.task_menu.delete(0, 'end')
        self.task_menu.add_command(label="➕ Add Task...", command=self._add_task)
        self.task_menu.add_separator()
        for i, t in enumerate(self.tasks):
            self.task_menu.add_command(label=f"✅ Complete: {t}", command=lambda idx=i: self._complete_task(idx))

    def _dance(self):
        self.last_activity = time.time()
        self._set_state("dance")
        self._speak("Grooving! 🎵", "excited", 6.0)
        def _stop():
            time.sleep(6)
            if self.state == "dance":
                self._set_state("idle")
        threading.Thread(target=_stop, daemon=True).start()

    def _start_focus(self):
        self.last_activity = time.time()
        self._set_state("focus")
        self._speak("Focus mode on! I'll hold this book.", "focus", 4.0)
        self.focus_end_time = time.time() + 25 * 60

    def _open_notepad(self):
        self.last_activity = time.time()
        self._speak("Opening notes...", "excited", 2.0)
        try:
            subprocess.Popen("notepad.exe")
        except:
            pass

    def _quick_search(self):
        self.last_activity = time.time()
        query = simpledialog.askstring("Quick Search", "What are you looking for?", parent=self.root)
        if query:
            # If it's a direct website link, open it directly
            if query.startswith("http") or ("." in query and " " not in query):
                url = query if query.startswith("http") else "https://" + query
                self._speak("Opening website!", "excited", 3.0)
            # If it's a programming question, search StackOverflow
            elif "error" in query.lower() or "how to" in query.lower() or "python" in query.lower():
                url = f"https://stackoverflow.com/search?q={urllib.parse.quote(query)}"
                self._speak("Searching StackOverflow!", "excited", 3.0)
            # Otherwise, skip Google results and go DIRECTLY to the first result
            else:
                url = f"https://duckduckgo.com/?q=!ducky+{urllib.parse.quote(query)}"
                self._speak("Taking you directly there!", "excited", 3.0)
            webbrowser.open_new_tab(url)

    def _start_project(self):
        if self.current_project:
            self._stop_project()
        project = simpledialog.askstring("Start Project", "Enter project name:", parent=self.root)
        if project:
            self.current_project = project
            self.project_start_time = time.time()
            if project not in self.timesheet:
                self.timesheet[project] = 0
            self._speak(f"Tracking time for:\n{project}", "excited", 4.0)

    def _stop_project(self):
        if self.current_project:
            elapsed = time.time() - self.project_start_time
            self.timesheet[self.current_project] += elapsed
            self._speak(f"Stopped tracking.\nLogged {int(elapsed//60)} mins.", "idle", 4.0)
            self.current_project = None
        else:
            self._speak("I'm not tracking anything right now.", "idle", 3.0)

    def _view_timesheet(self):
        if self.current_project:
            elapsed = time.time() - self.project_start_time
            self.timesheet[self.current_project] += elapsed
            self.project_start_time = time.time()
            
        if not self.timesheet:
            self._speak("Timesheet is empty!", "idle", 3.0)
            return
            
        summary = "Timesheet Summary:\n\n"
        for proj, seconds in self.timesheet.items():
            mins = int(seconds // 60)
            hours = mins // 60
            mins = mins % 60
            summary += f"• {proj}: {hours}h {mins}m\n"
            
        self._speak("Here is your time log!", "excited", 3.0)
        messagebox.showinfo("Project Timesheet", summary, parent=self.root)

    def _toggle_follow(self):
        self.is_following = not getattr(self, "is_following", False)
        if self.is_following:
            self.last_activity = time.time()
            self._speak("Chasing the pointer! 🐾", "excited", 3.0)
        else:
            self._speak("Phew, I'm tired.", "idle", 3.0)
            self._set_state("fall")
            self.vy = 0
            
    def _play_fetch(self):
        if hasattr(self, "ball") and self.ball and self.ball.winfo_exists():
            self.ball.destroy()
        
        self.last_activity = time.time()
        self._speak("Fetch! Throw the ball! 🎾", "excited", 3.0)
        
        self.ball = tk.Toplevel(self.root)
        self.ball.overrideredirect(True)
        self.ball.attributes("-topmost", True)
        self.ball.attributes("-transparentcolor", TRANS)
        self.ball.configure(bg=TRANS)
        # Spawn the ball safely in the middle of the screen so user can grab it!
        bx, by = self.sw // 2, self.sh // 2 - 100
        self.ball.geometry(f"24x24+{int(bx)}+{int(by)}")
        c = tk.Canvas(self.ball, width=24, height=24, bg=TRANS, highlightthickness=0)
        c.pack()
        c.create_oval(4,4,20,20, fill="#ff3333", outline="#ffffff", width=2)
        
        self.ball.x = bx
        self.ball.y = by
        self.ball.vx = 0.0
        self.ball.vy = 0.0
        self.ball.is_dragging = False
        self.ball.drag_x = 0
        self.ball.drag_y = 0
        
        def on_press(e):
            self.ball.is_dragging = True
            self.ball.drag_x = e.x_root
            self.ball.drag_y = e.y_root
            self.ball.vx = 0
            self.ball.vy = 0
            
        def on_drag(e):
            dx = e.x_root - self.ball.drag_x
            dy = e.y_root - self.ball.drag_y
            self.ball.x += dx
            self.ball.y += dy
            self.ball.geometry(f"+{int(self.ball.x)}+{int(self.ball.y)}")
            self.ball.vx = dx * 0.5
            self.ball.vy = dy * 0.5
            self.ball.drag_x = e.x_root
            self.ball.drag_y = e.y_root
            
        def on_release(e):
            self.ball.is_dragging = False
            self.ball.vx = max(-30, min(30, self.ball.vx))
            self.ball.vy = max(-30, min(30, self.ball.vy))
            
        self.ball.bind("<ButtonPress-1>", on_press)
        self.ball.bind("<B1-Motion>", on_drag)
        self.ball.bind("<ButtonRelease-1>", on_release)
        
        self.is_fetching = True
        self.is_following = False
        self._set_state("idle")

    def _toggle_perch(self):
        self.window_perch = not getattr(self, "window_perch", False)
        if self.window_perch:
            self._speak("Window walking enabled! 🪟", "excited", 3.0)
            self._set_state("fall")
        else:
            self._speak("Back to the floor.", "idle", 3.0)
            self._set_state("fall")

    def _take_screenshot(self):
        self.last_activity = time.time()
        def capture():
            self._speak("Screenshot in 3...", "excited", 1.0)
            time.sleep(1)
            self._speak("2...", "excited", 1.0)
            time.sleep(1)
            self._speak("1...", "excited", 1.0)
            time.sleep(1)
            self._speak("Cheese! 📸\n(Saved to clipboard)", "excited", 3.0)
            ctypes.windll.user32.keybd_event(0x2C, 0, 0, 0)
            time.sleep(0.1)
            ctypes.windll.user32.keybd_event(0x2C, 0, 2, 0)
        threading.Thread(target=capture, daemon=True).start()

    def _clean_temp(self):
        self.last_activity = time.time()
        self._speak("Cleaning PC trash! 🧹", "angry", 3.0)
        def worker():
            paths = [os.environ.get('TEMP'), os.environ.get('TMP'), r"C:\Windows\Temp"]
            freed = 0
            for p in paths:
                if not p or not os.path.exists(p): continue
                for item in os.listdir(p):
                    ipath = os.path.join(p, item)
                    try:
                        size = 0
                        if os.path.isfile(ipath):
                            size = os.path.getsize(ipath)
                            os.remove(ipath)
                        elif os.path.isdir(ipath):
                            for dp, _, fns in os.walk(ipath):
                                for f in fns:
                                    fp = os.path.join(dp, f)
                                    if not os.path.islink(fp) and os.path.isfile(fp):
                                        size += os.path.getsize(fp)
                            shutil.rmtree(ipath)
                        freed += size
                    except Exception:
                        pass
            mb = freed / (1024*1024)
            time.sleep(1.5)
            self._speak(f"Done! Swept {mb:.1f} MB\nof garbage! 🍌", "excited", 5.0)
        threading.Thread(target=worker, daemon=True).start()

    def _on_release(self, event):
        self.is_dragging = False
        if not self._drag_moved:
            self.last_activity = time.time()
            if self.state == "sleep":
                self._set_state("shocked")
                self._speak("WHO AWOKE THE MONKEY?", "angry", duration=3.0)
            elif self.state not in ["focus", "dance"]:
                self._speak(random.choice(CLICK_LINES), "excited")
        else:
            base_floor = self.sh - WIN_H - 10
            highest_floor = base_floor
            if getattr(self, "window_perch", False) and getattr(self, "window_rects", None):
                wx = self.x + WIN_W//2
                wy = self.y + WIN_H - 10
                for (l, t, r, b) in self.window_rects:
                    if l < wx < r and t >= wy - 30:
                        f = t - WIN_H + 10
                        if f < highest_floor:
                            highest_floor = f
            floor_y = highest_floor

            if self.y < floor_y - 30:
                self._set_state("fall")
                if random.random() < 0.5:
                    self._speak("EEEEK!", "shocked", 1.5)
            else:
                self._set_state("idle")

    def _feed(self):
        self.last_activity = time.time()
        if self.state == "focus":
            self.focus_end_time = 0 # Cancel focus
        self._speak(random.choice(FEED_LINES), "excited")

    def _poke(self):
        if self.state == "focus":
            self.focus_end_time = 0
            self._speak("Focus interrupted!", "shocked", 3.0)
        else:
            self._speak(random.choice(POKE_LINES), "angry")

    def _speak(self, text, state=None, duration=5.0):
        self.canvas.itemconfig(self.speech_text, text=text, state="normal")
        bbox = self.canvas.bbox(self.speech_text)
        if bbox:
            pad_x = 12
            pad_y = 8
            self.canvas.coords(self.bubble_bg, bbox[0]-pad_x, bbox[1]-pad_y, bbox[2]+pad_x, bbox[3]+pad_y)
            self.canvas.itemconfig(self.bubble_bg, state="normal")
            
        self.speech_clear_at = time.time() + duration
        if state:
            self._set_state(state)
            def _revert():
                time.sleep(duration)
                if self.state == state and self.state not in ["focus", "dance"]:
                    self._set_state("idle")
            threading.Thread(target=_revert, daemon=True).start()

    def _set_state(self, state):
        if self.state != state:
            self.state          = state
            self.frame_idx      = 0
            self._next_frame_at = 0

    # ── drag ──────────────────────────────────

    def _drag_start(self, event):
        self._drag_x     = event.x
        self._drag_y     = event.y
        self._drag_moved = False
        self.is_dragging = True
        self.vy          = 0.0 
        
        if getattr(self, "is_following", False):
            self.is_following = False
            self._speak("Gotcha! I'll stop chasing.", "idle", 3.0)
            self._set_state("shocked")
            return
            
        if self.state == "focus":
            self.focus_end_time = 0
            self._speak("Focus interrupted!", "shocked", 2.0)
        else:
            self._set_state("shocked") 

    def _drag_motion(self, event):
        dx = event.x - self._drag_x
        dy = event.y - self._drag_y
        if abs(dx) > 4 or abs(dy) > 4:
            self._drag_moved = True
        self.x += dx
        self.y += dy
        self.root.geometry(f"+{int(self.x)}+{int(self.y)}")

    def _show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

if __name__ == "__main__":
    GremsworthApp()
