```
//@version=5

  

indicator(title='WT', shorttitle='WT')

stratMultiplier = input(defval=1, title='Timescale Multiplier')

  

n1 = input(10, 'Channel Length')

n2 = input(21, 'Stochastic Ratio Filter')

crossoverSMALen = input(2, 'Crossover Lag (>1)')

  

obLevel = input(75, 'Overbought %')

osLevel = -obLevel

obExtremeLevel = input(100, 'Extreme Overbought %')

osExtremeLevel = -obExtremeLevel

  

waveTrend(ap, n_channel, n_average, timeMultiplier) =>

    esa = ta.ema(ap, n_channel * timeMultiplier)

    d = ta.ema(math.abs(ap - esa), n_channel * timeMultiplier)

    ci = 100 * (ap - esa) / d

    tci = ta.ema(ci, n_average * timeMultiplier)

    wtA = tci

    wtB = ta.sma(wtA, crossoverSMALen * timeMultiplier)

    wtDiff = wtA - wtB

    [wtA, wtB, wtDiff]

  

[wta, wtb, wtdiff] = waveTrend(hlc3, n1, n2, stratMultiplier)

  

plot(obExtremeLevel, title="obE", color=color.new(#7e57c2, 0), style=plot.style_line, linewidth = 1)

plot(obLevel, title="ob", color=color.new(#7e57c2, 0), style=plot.style_line, linewidth = 1)

plot(osExtremeLevel, title="osE", color=color.new(#00db91, 0), style=plot.style_line, linewidth = 1)

plot(osLevel, title="os", color=color.new(#00db91, 0), style=plot.style_line, linewidth = 1)

wtColor = wtb - wta > 0 ? color.new(#7e57c2, 0) : color.new(#00db91, 0)

plot(wta, color=wtColor)

plot(wtb, color=wtColor)

extremeX = (wta > obExtremeLevel or wta < osExtremeLevel) and ta.cross(wta, wtb)

significantX = (wta > obLevel or wta < osLevel) and ta.cross(wta, wtb)

plot(significantX ? wta : na, color=color.new(#ffa600, 0), style=plot.style_circles, linewidth=4)

plot(extremeX ? wta : na, color=color.new(#ffa600, 0), style=plot.style_circles, linewidth=4)

xCircleColor = wtb - wta > 0 ? color.new(#7e57c2, 0) : color.new(#00db91, 0)

plot(ta.cross(wta, wtb) ? wtb : na, color=xCircleColor, style=plot.style_circles, linewidth=2)

  

/// 1D WT

a = array.new_float()

array.push(a, request.security(syminfo.tickerid, '1D', wta[0]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[0]))

array.push(a, request.security(syminfo.tickerid, '1D', wta[1]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[1]))

array.push(a, request.security(syminfo.tickerid, '1D', wta[2]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[2]))

array.push(a, request.security(syminfo.tickerid, '1D', wta[3]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[3]))

array.push(a, request.security(syminfo.tickerid, '1D', wta[4]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[4]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[5]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[5]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[6]))

array.push(a, request.security(syminfo.tickerid, '1D', wtb[6]))

wta1D =  array.get(a, 0)

wtb1D = array.get(a, 1)

bullish_sig_x_1D = false

bearish_sig_x_1D = false

int i = 0

while i < array.size(a)

    wta_temp = array.get(a, i)

    wtb_temp = array.get(a, i+1)

    if wta_temp <= -75 and wta_temp > wtb_temp

        bullish_sig_x_1D := true

    else if wta_temp >= 75 and wta_temp < wtb_temp

        bearish_sig_x_1D := true

    i += 2

wt_1D_state = ""

if (wta1D > wtb1D)

    if (bullish_sig_x_1D == true) or wta1D <= -75

        wt_1D_state := "[A] long x"

    else if wta1D <= -50

        wt_1D_state := "[B] long x"

    else if wta1D <= -21

        wt_1D_state := "[C] long x"

    else

        wt_1D_state := "[D] long x"

else if (wta1D <= wtb1D)

    if (bearish_sig_x_1D == true) or wta1D >= 75

        wt_1D_state := "[A] short x"

    else if wta1D >= 50

        wt_1D_state := "[B] short x"

    else if wta1D >= 21

        wt_1D_state := "[C] short x"

    else

        wt_1D_state := "[D] short x"

  

/// 1W WT

HTF_Shade = ""

wt_1W_state = ""

b = array.new_float()

array.push(b, request.security(syminfo.tickerid, '1W', wta[0]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[0]))

array.push(b, request.security(syminfo.tickerid, '1W', wta[1]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[1]))

array.push(b, request.security(syminfo.tickerid, '1W', wta[2]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[2]))

array.push(b, request.security(syminfo.tickerid, '1W', wta[3]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[3]))

array.push(b, request.security(syminfo.tickerid, '1W', wta[4]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[4]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[5]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[5]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[6]))

array.push(b, request.security(syminfo.tickerid, '1W', wtb[6]))

wta_1W = array.get(b, 0)

wtb_1W = array.get(b, 1)

bullish_sig_x_1W = false

bearish_sig_x_1W = false

i := 0

while i < array.size(b)

    wta_temp = array.get(b, i)

    wtb_temp = array.get(b, i+1)

    if wta_temp <= -75 and wta_temp > wtb_temp

        bullish_sig_x_1W := true

    else if wta_temp >= 75 and wta_temp < wtb_temp

        bearish_sig_x_1W := true

    i += 2

if (wta_1W > wtb_1W)

    if (bullish_sig_x_1W == true) or wta_1W <= -75

        wt_1W_state := "[A] long x"

    else if wta_1W <= -50

        wt_1W_state := "[B] long x"

    else if wta_1W <= -21

        wt_1W_state := "[C] long x"

    else

        wt_1W_state := "[D] long x"

else if (wta_1W <= wtb_1W)

    if (bearish_sig_x_1W == true) or wta_1W >= 75

        wt_1W_state := "[A] short x"

    else if wta_1W >= 50

        wt_1W_state := "[B] short x"

    else if wta_1W >= 21

        wt_1W_state := "[C] short x"

    else

        wt_1W_state := "[D] short x"

  

/// Setup array

c = array.new_float()

array.push(c, request.security(syminfo.tickerid, '1W', wta[0]))

array.push(c, request.security(syminfo.tickerid, '1W', wtb[0]))

array.push(c, request.security(syminfo.tickerid, '1D', wta[0]))

array.push(c, request.security(syminfo.tickerid, '1D', wtb[0]))

array.push(c, request.security(syminfo.tickerid, '480', wta[0]))

array.push(c, request.security(syminfo.tickerid, '480', wtb[0]))

array.push(c, request.security(syminfo.tickerid, '240', wta[0]))

array.push(c, request.security(syminfo.tickerid, '240', wtb[0]))

array.push(c, request.security(syminfo.tickerid, '120', wta[0]))

array.push(c, request.security(syminfo.tickerid, '120', wtb[0]))

array.push(c, request.security(syminfo.tickerid, '60', wta[0]))

array.push(c, request.security(syminfo.tickerid, '60', wtb[0]))

  

/// Get sig x count from timeframes

sigLongXCount = 0

sigShortXCount = 0

i := 0

while i < array.size(c)

    wta_temp = array.get(c, i)

    wtb_temp = array.get(c, i+1)

    if wta_temp <= -75 and wta_temp > wtb_temp

        sigLongXCount += 1

    else if wta_temp >= 75 and wta_temp < wtb_temp

        sigShortXCount += 1

    i += 2

  

/// Signal evaluation logic for specific x's

sig_x_long = wta < -75 and ta.crossover(wta, wtb)

if sig_x_long

    alert(message='{"PATTERN": "sig x",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + timeframe.period + '",\n"DIRECTION": "long",\n"HTF Shade": "' + HTF_Shade + '",\n"SIG LONG X COUNT": "' + str.tostring(sigLongXCount) + '",\n"SIG SHORT X COUNT": "' + str.tostring(sigShortXCount) + '",\n"1D WT": "' + wt_1D_state + '",\n"1W WT": "' + wt_1W_state + '"}', freq=alert.freq_once_per_bar)

sig_x_short = wta > 75 and ta.crossunder(wta, wtb)    

if sig_x_short

    alert(message='{"PATTERN": "sig x",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + timeframe.period + '",\n"DIRECTION": "short",\n"HTF Shade": "' + HTF_Shade + '",\n"SIG LONG X COUNT": "' + str.tostring(sigLongXCount) + '",\n"SIG SHORT X COUNT": "' + str.tostring(sigShortXCount) + '",\n"1D WT": "' + wt_1D_state + '",\n"1W WT": "' + wt_1W_state + '"}', freq=alert.freq_once_per_bar)
```