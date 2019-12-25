class Growth:
    def get_growth(self, start_price, end_price):
        return round(((end_price / start_price) - 1) * 100, 2)
