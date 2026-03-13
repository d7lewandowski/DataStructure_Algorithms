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

class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs
    The factory doesn't maintain any of the instances it creates.
    """

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instances."""
    
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance."""

class FastExporter(ExporterFactory):
    """
    Factory aimed at providing a high speed, lower quality export.
    """
    
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExport()
    
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudcioExporter()

class HighQualityExporter(ExporterFactory):
    """
    Factory aimed at providing a slower speed, high quality export.
    """
    
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExport()
    
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudcioExporter() 


class MasterQualityExporter(ExporterFactory):
    """
    Factory aimed at providing a low speed, master quality export.
    """
    
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()
    
    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter() 

def read_exporter() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference."""

    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }

    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")

        if export_quality in factories:
            return factories[export_quality]
        
        print(f"Unknown iutput quality option: {export_quality}")


def main(fac: ExporterFactory) -> None:
    """Main function."""

    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_video_exporter()
    
    # prepare the export

    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")
    
    folder = pathlib.Path("/usr/tmp/video")

    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    
    fac = read_exporter()
    main(fac)