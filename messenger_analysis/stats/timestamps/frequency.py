'''Plot frequency of timestamps by intervals'''


import matplotlib.pyplot as plt
import math
import numpy as np
from datetime import datetime, time
from typing import List
from messenger_analysis.chat.chat import Chat
from messenger_analysis.cli.config import CONFIG
from messenger_analysis.util.lists import flatten


minutes_in_day = 60 * 24


def plot_timestamp_frequencies(chats: List[Chat]):
    timestamps = flatten([[x.timestamp for x in y.messages] for y in chats])
    timestamps = [datetime.fromtimestamp(x / 1000.0) for x in timestamps]
    timestamps = [x.hour * 60 + x.minute for x in timestamps]
    _produce_figure(timestamps)


def _produce_figure(timestamps: List[float]):
    interval_size = CONFIG.plotTimestamps
    number_of_bins = minutes_in_day // CONFIG.plotTimestamps
    bins = np.linspace(0, 2 * np.pi, number_of_bins)
    width = 2 * np.pi / number_of_bins

    ts = [0] * number_of_bins
    for t in timestamps:
        ts[math.floor(t // interval_size)] += 1

    plt.clf()
    plt.title(f'Frequency of messages by {interval_size} minute intervals')

    ax = plt.subplot(111, projection='polar', label='Frequency')
    ax.plot(bins, ts)

    # Place 00:00 at top, rotate clockwise
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2)

    # Circumference labels
    ax.set_xticks(bins)
    ax.set_xticklabels([f'{tt // 60:02}:{tt % 60:02}' for tt in range(0, minutes_in_day, interval_size)])
    plt.setp([x for i, x in enumerate(ax.get_xticklabels()) if i % (60 // interval_size) != 0], visible=False)

    # Radius labels
    plt.setp(ax.get_yticklabels(), visible=False)

    plt.tightfit()
    plt.savefig(CONFIG.get_output_filename(f'message_frequency_{interval_size}_minute_intervals.png'))
