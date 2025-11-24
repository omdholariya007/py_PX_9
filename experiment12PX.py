import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
f1 = 5
f2 = 10
signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)
combined_signal = signal1+signal2
plt.figure(figsize=(12, 6))
plt.plot(t, combined_signal, label='combined')
plt.title('sin')
plt.xlabel('seconds')
plt.ylabel('amplitude')
plt.grid(True)
plt.legend()
plt.show()

#2
#using some content from above  code

signal2 = np.cos(2 * np.pi * 10 * t)
multiplied_signal = signal1* signal2
plt.figure(figsize=(12, 6))
plt.plot(t, multiplied_signal, label='multiply')
plt.title('signal Multiplication')
plt.xlabel('second')
plt.ylabel('amplitude')
plt.grid(True)
plt.legend()
plt.show()

#3
fs3 = 500
t3 = np.linspace(0, 1, fs3, endpoint=False)
sine = np.sin(2 * np.pi * 5 * t3)
shift = np.sin(2 * np.pi * 5 * (t3 - 0.1))

plt.figure(figsize=(12, 4))
plt.plot(t3, sine, label='sin')
plt.plot(t3, shift, label='shifted 5')
plt.title('time shifted')
plt.xlabel('Time ')
plt.ylabel('amplitude')
plt.legend()
plt.grid(True)
plt.show()

#4
f4 = 500
t4 = np.linspace(0, 1, f4, endpoint=False)
sine= np.sin(2 * np.pi * 10 * t4)
scaled = 3 * sine
plt.figure(figsize=(12, 4))
plt.plot(t4, sine, label='sine')
plt.plot(t4, scaled, label='scaled ')
plt.title('scaled sine wave')
plt.xlabel('time ')
plt.ylabel('amplitude')
plt.legend()
plt.grid(True)
plt.show()

#5
f5 = 500
t5 = np.linspace(0, 1, f5, endpoint=False)
sine = np.sin(2 * np.pi * 5 * t5)
rev = sine[::-1]
plt.figure(figsize=(12, 4))
plt.plot(t5, sine, label='sine')
plt.plot(t5, rev, label='reversed')
plt.title('sin wave')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.legend()
plt.grid(True)
plt.show()
