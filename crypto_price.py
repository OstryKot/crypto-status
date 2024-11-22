# pylint: disable=C0111,R0903
"""Module that displays content from status file
"""
import core.widget
import core.module

class Module(core.module.Module):
    def __init__(self, config, theme):
        self.widget = core.widget.Widget("status")
        super().__init__(config=config, theme=theme, widgets=self.widget)
        self.status_file = "/tmp/crypto_prices.txt"
        self.interval = 60

    def update(self):
        try:
            with open(self.status_file, 'r', encoding='utf-8') as f:
                status = f.read().strip()
                self.widget.full_text(status)
        except Exception as e:
            self.widget.full_text(f"Error: {str(e)}")

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
