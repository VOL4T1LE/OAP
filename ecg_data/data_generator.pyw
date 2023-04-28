
#? NOTICE
#? This file uses the "Better Comments" extension for Visual Studio Code.



# Blah

import numpy as np

def generate_ecg_data(heart_rate, duration):
    # Calculate the number of heart beats in the duration
    num_beats = int(heart_rate * duration / 60)

    # Calculate the duration of each heart beat
    beat_duration = duration / num_beats

    # Generate the time array for the ECG signal
    t = np.linspace(0, duration, num_beats * 1000, endpoint=False)

    # Generate the ECG signal
    ecg = np.zeros_like(t)

    for i in range(num_beats):
        # Add P wave
        p_start = int(i * 1000 * beat_duration)
        p_end = int((i + 0.1) * 1000 * beat_duration)
        p = np.sin(np.linspace(0, np.pi, p_end - p_start)) * 0.1
        ecg[p_start:p_end] += p

        # Add QRS complex
        qrs_start = int((i + 0.1 + 0.05) * 1000 * beat_duration)
        qrs_end = int((i + 0.12 + 0.09) * 1000 * beat_duration)
        qrs = np.sin(np.linspace(-0.05, 0.75, qrs_end - qrs_start)) * 1.5
        ecg[qrs_start:qrs_end] += qrs

        # Add ST segment
        st_start = int((i + 0.12 + 0.1) * 1000 * beat_duration)
        st_end = int((i + 0.18 + 0.1) * 1000 * beat_duration)
        st = np.linspace(-0.2, 0.1, st_end - st_start)
        ecg[st_start:st_end] += st

        # Add T wave
        t_start = int((i + 0.16 + 0.1) * 1000 * beat_duration)
        t_end = int((i + 0.28 + 0.1) * 1000 * beat_duration)
        t = np.sin(np.linspace(0, np.pi, t_end - t_start)) * 0.3
        ecg[t_start:t_end] += t

    # Scale the ECG signal to be between -1 and 1
    ecg /= np.max(np.abs(ecg))

    # Invert the ECG signal
    ecg = -ecg

    return t, ecg
