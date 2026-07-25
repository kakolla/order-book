





class Order:

    def __init__(self, side: int, order_id: int, price: int, qty: int, timestamp: int):
            self.side = side # ask =0, bid = 1
            self.order_id = order_id
            self.price = price
            self.qty = qty
            self.timestamp = timestamp
            self.prev: "Order | None " = None
            self.next: "Order | None " = None
        
   

class PriceLevel:
    def __init__(self, head: Order | None = None , tail: Order | None = None):
        self.head = head
        self.tail = tail


    

class OrderBook:

    def __init__(self, max_price: int, min_price: int, tick_size: int = 1):
        self.min_price = min_price
        self.max_price = max_price
        numlevels = (max_price - min_price) // tick_size + 1
        self.tick_size = tick_size
        self.levels: list[None | PriceLevel] = [None for _ in range(numlevels)] 

        self.order_map = {} # map of order ids to their position node
    
    def get_index(self, price: int) -> int:
        return (price - self.min_price) // self.tick_size 

    def add(self, order: Order):
        # add an order
        # find price level, add to tail
        idx = self.get_index(order.price)
        price_level = self.levels[idx]
        # price_level = self.levels[order.price]
        if price_level is None:
            price_level = PriceLevel()
            self.levels[idx] = price_level

        if price_level.head is None:
            price_level.head = order
            price_level.tail = order
        else:
            tailnode = price_level.tail
            assert tailnode is not None
            tailnode.next = order
            order.prev = tailnode
            price_level.tail = order


        self.order_map[order.order_id] = order

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

