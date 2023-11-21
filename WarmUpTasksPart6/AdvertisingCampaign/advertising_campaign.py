import json


# [campaign_id][vendor_id][event][date]
class Message:
    def __init__(self, campaign_id, vendor_id, date, event):
        self.campaign_id = campaign_id
        self.vendor_id = vendor_id
        self.date = date
        self.event = event


class AdvertisingCampaign:
    def __init__(self, storage):
        self.storage = storage

    # message = {'campaign_id': '1', 'vendor_id': '2', 'date': '2023-11-11 12:23:12', 'event': 'click/impression}
    def receive(self, message):
        rec = json.loads(message)
        campaign_id = rec["campaign_id"]
        vendor_id = rec["vendor_id"]
        date = rec["date"]
        event = rec["event"]
        self.storage.append(campaign_id, vendor_id, date, event)

    def get_clicks_number_by_campaign_id(self, campaign_id, date_start, date_end):
        pass

    def get_event_number_by_vendor_id(self, vendor_id, date_start, date_end, event):
        pass


if __name__ == '__main__':
    adv = AdvertisingCampaign(dict())

