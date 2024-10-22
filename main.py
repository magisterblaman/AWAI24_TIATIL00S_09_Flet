import time
import flet

def main(page: flet.Page):
    countdown_input = flet.TextField()
    countdown_text = flet.Text("100")

    def start_countdown(e):
        seconds = int(countdown_input.value)
        for s in range(seconds, -1, -1):
            countdown_text.value = str(s) + "s"
            countdown_text.update()
            time.sleep(1)

    countdown_start_button = flet.TextButton("Start",
                                             on_click=start_countdown)
    page.add(countdown_input)
    page.add(countdown_start_button)
    page.add(countdown_text)

flet.app(main)