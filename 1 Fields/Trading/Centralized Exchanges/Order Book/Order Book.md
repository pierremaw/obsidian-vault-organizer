All centralized exchanges have an order book at their core. An order book is just a database that stores all sell and buy orders that traders want to make.

**Orderbooks are used to match** **buy** and **sell** **orders**. When a buyer and seller agree on a price, their orders are matched and a trade is executed.

![[Order Book.png]]

Sure, here is a possible scheme for the database for a CEX orderbook:

```sql
CREATE TABLE `orderbook` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `symbol` VARCHAR(255) NOT NULL,
  `side` ENUM('buy', 'sell') NOT NULL,
  `price` DECIMAL(18,8) NOT NULL,
  `quantity` DECIMAL(18,8) NOT NULL,
  `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);
```

This table would store the following information for each order in the orderbook:

* The order ID
* The symbol of the asset being traded
* The side of the order (buy or sell)
* The price of the order
* The quantity of the order
* The timestamp of the order

This information can be used to track the state of the orderbook, to match buy and sell orders, and to calculate the current market price for the asset.

___
Type: #subtopic 
Topics: [[Trading]], [[Centralized Exchanges]]

