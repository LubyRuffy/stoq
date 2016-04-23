from __future__ import absolute_import
from stoq.core import Stoq
from StoCelery.celery import app

stoq = Stoq()


class StoCeleryWorker(app.Task):

    abstract = True
    plugin = ""
    connector = "api-psql"

    def __init__(self):
        self.worker = stoq.load_plugin(self.plugin, "worker")
        self.worker.load_connector(self.connector)

    def run(self, payload, **kwargs):
        payload = payload.read()
        results, template_results = self.worker.start(payload=payload, **kwargs)

        if results:
            self.worker.connectors[self.connector].save(results)

        return results


class Yara(StoCeleryWorker):
    plugin = "yara"

class Exif(StoCeleryWorker):
    plugin = "exif"

class Peinfo(StoCeleryWorker):
    plugin = "peinfo"

class Clamav(StoCeleryWorker):
    plugin = "clamav"

class Trid(StoCeleryWorker):
    plugin = "trid"
