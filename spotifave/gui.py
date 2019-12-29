from typing import Dict

import squarify
from matplotlib import cm, pyplot

from spotifave.spotipy_service import Artist


class Gui:
    @staticmethod
    def display_chart(ordered_artist_counts: Dict[Artist, int]):
        cmap = cm.get_cmap("prism")
        colors = [cmap(i / len(ordered_artist_counts)) for i in range(len(ordered_artist_counts.values()))]

        squarify.plot(sizes=ordered_artist_counts.values(),
                      label=[artist.name for artist in ordered_artist_counts.keys()],
                      alpha=.7, color=colors)

        fig = pyplot.gcf()
        fig.canvas.set_window_title("Artist Treemap")

        pyplot.subplots_adjust(left=0, bottom=0, top=1, right=1)
        pyplot.axis('off')
        pyplot.show()
