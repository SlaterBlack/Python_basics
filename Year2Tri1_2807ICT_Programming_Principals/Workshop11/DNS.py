class DSN:
    def __init__(self):
        self._database = {}

    def update(self, domain_name, ipa):
        self.database.add([domain_name,ipa])

    def lookup(self, domain_name):
        if domain_name in self.database:
            return domain_name
        else:
            return None