





class Order:
    side: int # 0 - ask, 1 - bid
    order_id: int
    price: int
    qty: int
    timestamp: int # for price time priority
    prev_id: int
    next_id: int
    
   


class OrderBook:

    def __init__(self):
        pass



    def add(self):
        pass

    def cancel(self):
        pass

    def execute(self):
        pass
    def get_volume_at_limit(self):
        pass
    def get_best_bid(self):
        pass
    def get_best_offer(self):
        pass

