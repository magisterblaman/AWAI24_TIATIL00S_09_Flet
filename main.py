import time
import flet

def main(page: flet.Page):
    countdown_input = flet.TextField()
    countdown_text = flet.Text("100")
    alarm_sound = flet.Audio(src="alarm_done.mp3")

    is_counting_down=False

    def start_countdown(e):
        nonlocal is_counting_down
        if not is_counting_down:
            is_counting_down=True
            seconds = int(countdown_input.value)
            for s in range(seconds, -1, -1):
                countdown_text.value = str(s) + "s"
                countdown_text.update()
                time.sleep(1)
            alarm_sound.play()
            is_counting_down=False

    countdown_start_button = flet.TextButton("Start",
                                             on_click=start_countdown)

    page.overlay.append(alarm_sound)

    page.add(countdown_input)
    page.add(countdown_start_button)
    page.add(countdown_text)

flet.app(main)