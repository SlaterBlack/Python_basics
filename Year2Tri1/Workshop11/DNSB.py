from DNS import DNS

class DNSB(DNS):
    def __init__(self):
        DNS.__init__(self)
        self.blacklist = set()

    def update_blacklist(self, ipa):
        self.blacklist.add(ipa)

    def lookup(self, domain_name):
        if ((domain_name not in self.database) or (domain_name in self.blacklist)):
            return domain_name
        else:
            return None
