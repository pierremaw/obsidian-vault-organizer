```
//@version=5

indicator(title="10/20 EMA", shorttitle="10/20 EMA", overlay=true, timeframe="", timeframe_gaps=true)

  

len = input.int(10, minval=1, title="Length", group="EMA 1")

src = input(hlc3, title="Source", group="EMA 1")

offset = input.int(title="Offset", defval=0, minval=-500, maxval=500, group="EMA 1")

out = ta.ema(src, len)

plot(out, title="EMA", color=color.new(#FF69B4, 0), offset=offset)

  

ma(source, length, type) =>

    switch type

        "SMA" => ta.sma(source, length)

        "EMA" => ta.ema(source, length)

        "SMMA (RMA)" => ta.rma(source, length)

        "WMA" => ta.wma(source, length)

        "VWMA" => ta.vwma(source, length)

  

typeMA = input.string(title = "Method", defval = "SMA", options=["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="EMA 1 — Smoothing")

smoothingLength = input.int(title = "Length", defval = 5, minval = 1, maxval = 100, group="EMA 1 — Smoothing")

  

smoothingLine = ma(out, smoothingLength, typeMA)

plot(smoothingLine, title="Smoothing Line", color=#f37f20, offset=offset, display=display.none)

  
  

len1 = input.int(20, minval=1, title="Length", group="EMA 2")

src1 = input(hlc3, title="Source", group="EMA 2")

offset1 = input.int(title="Offset", defval=0, minval=-500, maxval=500, group="EMA 2")

out1 = ta.ema(src1, len1)

plot(out1, title="EMA", color=color.new(#fff59d, 0), offset=offset)

  

ma1(source, length, type) =>

    switch type

        "SMA" => ta.sma(source, length)

        "EMA" => ta.ema(source, length)

        "SMMA (RMA)" => ta.rma(source, length)

        "WMA" => ta.wma(source, length)

        "VWMA" => ta.vwma(source, length)

  

typeMA1 = input.string(title = "Method", defval = "SMA", options=["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="EMA 2 — Smoothing")

smoothingLength1 = input.int(title = "Length", defval = 5, minval = 1, maxval = 100, group="EMA 2 — Smoothing")

  

smoothingLine1 = ma1(out1, smoothingLength1, typeMA1)

plot(smoothingLine1, title="Smoothing Line", color=#f37f20, offset=offset, display=display.none)

  
  

len2 = input.int(65, minval=1, title="Length", group="EMA 3")

src2 = input(hlc3, title="Source", group="EMA 3")

offset2 = input.int(title="Offset", defval=0, minval=-500, maxval=500, group="EMA 3")

out2 = ta.ema(src2, len2)

plot(out2, title="EMA", color=color.new(color.orange, 0), offset=offset)

  

ma2(source, length, type) =>

    switch type

        "SMA" => ta.sma(source, length)

        "EMA" => ta.ema(source, length)

        "SMMA (RMA)" => ta.rma(source, length)

        "WMA" => ta.wma(source, length)

        "VWMA" => ta.vwma(source, length)

  

typeMA2 = input.string(title = "Method", defval = "SMA", options=["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="EMA 3 — Smoothing")

smoothingLength2 = input.int(title = "Length", defval = 5, minval = 1, maxval = 100, group="EMA 3 — Smoothing")

  

smoothingLine2 = ma1(out1, smoothingLength1, typeMA2)

plot(smoothingLine2, title="Smoothing Line", color=#f37f20, offset=offset, display=display.none)
```