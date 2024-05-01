from urllib.request import urlopen

import reflex as rx

from reflex_audio_capture import AudioRecorderPolyfill, get_codec, strip_codec_part

from scribe1.components.geminiComponent import scribeGenerator

REF = "myaudio"





class AudioState(rx.State):
    """The app state."""

    has_error: bool = False
    processing: bool = False
    transcript: list[str] = []
    timeslice: int = 10000
    device_id: str = ""
    use_mp3: bool = True
    newAudio: str = ""

    async def on_data_available(self, chunk: str):
        mime_type, _, codec = get_codec(chunk).partition(";")
        audio_type = mime_type.partition("/")[2]
        if audio_type == "mpeg":
            audio_type = "mp3"
        print(len(chunk), mime_type, codec, audio_type)
        with urlopen(strip_codec_part(chunk)) as audio_data:
            try:
                self.processing = True
                yield
                with open("convo_audio.mp3", "wb") as f:
                    f.write(audio_data.read())
                scribe_dictionary = scribeGenerator()
                print(scribe_dictionary)
                #TODO Populate the patient profile with the auto-generated dictionary


            except Exception as e:
                self.has_error = True
                yield capture.stop()
                raise
            finally:
                self.processing = False

    def set_timeslice(self, value):
        self.timeslice = value[0]

    def set_device_id(self, value):
        self.device_id = value
        yield capture.stop()

    def on_error(self, err):
        print(err)

    def on_load(self):
        # We can start the recording immediately when the page loads
        return capture.start()


capture = AudioRecorderPolyfill.create(
    id=REF,
    on_data_available=AudioState.on_data_available,
    on_error=AudioState.on_error,
    timeslice=AudioState.timeslice,
    device_id=AudioState.device_id,
    use_mp3=AudioState.use_mp3,
)


def input_device_select():
    return rx.select.root(
        rx.select.trigger(placeholder="Select Input Device"),
        rx.select.content(
            rx.foreach(
                capture.media_devices,
                lambda device: rx.cond(
                    device.deviceId & device.kind == "audioinput",
                    rx.select.item(device.label, value=device.deviceId),
                ),
            ),
        ),
        on_change=AudioState.set_device_id,
    )


def audioIndex() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.card(
                rx.cond(
                    capture.media_devices,
                    input_device_select(),
                ),
            ),
            capture,
            rx.text(f"Recorder Status: {capture.recorder_state}"),
            rx.cond(
                capture.is_recording,
                rx.button("Stop Recording", on_click=capture.stop()),
                rx.button(
                    "Start Recording",
                    on_click=capture.start(),
                ),
            ),
            style={"width": "100%", "> *": {"width": "100%"}},
        ),
        size="1",
        margin_y="2em",
    )