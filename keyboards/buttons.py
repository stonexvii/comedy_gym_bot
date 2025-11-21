class KeyboardButton:
    def __init__(self, text: str, callback=None, url: str | None = None, **kwargs):
        self.text = text
        if callback:
            self.callback_data = callback(
                **kwargs,
            )
        if url:
            self.url = url

    def as_kwargs(self):
        return self.__dict__
