"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """
    Basic represenation of video exporting codec.
    """

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""


    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec. """

    def prepare_export(self, video_data):
        print("Preparing video data for lessless export.")

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data in lossless format to {folder}.')


class H264VideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExport(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)"""

    def prepare_export(self, video_data):
        print('Preparing video data for H.264 (Hi422P) exprot.')
    
    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for H.264 (Hi422P) format to {folder}.')


class AudioExporter(ABC):
    """Basic represenation of audio exporting codec. """

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""
    
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder. """


class AACAudcioExporter(AudioExporter):
    """AAC audio exporting codec. """

    def prepare_export(self, audio_data):
        print("Prepares audio data for AAC export.")
    
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting the audio data to a {folder}")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Prepares audio data for WAV export.")
    
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting the audio data in WAV format to {folder}")



def main() -> None:
    """Main function."""
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")

        if export_quality in {'low', 'high', 'master'}:
            break
        
        print(f"Unknown iutput quality option: {export_quality}")

    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264Hi422PVideoExport()
        audio_exporter = AACAudcioExporter()
    elif export_quality == 'high':
        video_exporter = H264Hi422PVideoExport()
        audio_exporter = AACAudcioExporter()
    else:
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    
    # prepare the export

    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")
    
    folder = pathlib.Path("/usr/tmp/video")

    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()