





class Order:
    side: int # 0 - ask, 1 - bid
    order_id: int
    price: int
    qty: int
    timestamp: int # for price time priority
    prev_id: int
    next_id: int
    
   


class OrderBook:

    def __init__(self, max_price: int, min_price: int, tick_size: int = 1):
        self.min_price = min_price
        self.max_price = max_price
        numlevels = (max_price - min_price) // tick_size + 1
        self.tick_size = tick_size
        self.levels = [None for _ in range(numlevels)] 

        self.order_map = {} # map of order ids to their position node
    
    def get_index(self, price: float) -> int:
        return (price - self.min_price) // self.tick_size 




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

