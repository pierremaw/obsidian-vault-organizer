```
//@version=5

/// Most recent ok version is 511 (standard color palette)

indicator(title='FSX 3.11', shorttitle='FSX 3.11')

  

/// Components for signal generator

bar_source = hlc3

n1 = input(10, 'Channel Length (>1)')

n2 = input(21, 'Stochastic Ratio Length (>1)')

crossover_sma_len = input(2, 'Crossover Lag (>1)')

obLevel = input(75, 'Overbought (Red)')

osLevel = -obLevel

obMildLevel = 2 * obLevel / 3

osMildLevel = -obMildLevel

obEmbedLevel = input(88, 'Embedded (White)')

osEmbedLevel = -obEmbedLevel

obExtremeLevel = input(100, 'Extreme Overbought (Pink)')

osExtremeLevel = -obExtremeLevel

crossSeparation = input(3, 'Embed Separation')

ribbonLineWidth = input(5, 'Row Width')

  

/// Initialize data for stochastic

stochasticTrend(ap, n_channel, n_average, timeMultiplier) =>

    esa = ta.ema(ap, n_channel * timeMultiplier)

    d = ta.ema(math.abs(ap - esa), n_channel * timeMultiplier)

    ci = 100 * (ap - esa) / d

    tci = ta.ema(ci, n_average * timeMultiplier)

    wtA = tci

    wtB = ta.sma(wtA, crossover_sma_len * timeMultiplier)

    wtDiff = wtA - wtB

    [wtA, wtB, wtDiff]

[wta_1, wtb_1, wtdiff_1] = stochasticTrend(bar_source, n1, n2, 1)

[wta_2, wtb_2, wtdiff_2] = stochasticTrend(bar_source, n1, n2, 2)

[wta_4, wtb_4, wtdiff_4] = stochasticTrend(bar_source, n1, n2, 4)

[wta_8, wtb_8, wtdiff_8] = stochasticTrend(bar_source, n1, n2, 8)

[wta_16, wtb_16, wtdiff_16] = stochasticTrend(bar_source, n1, n2, 16)

[wta_32, wtb_32, wtdiff_32] = stochasticTrend(bar_source, n1, n2, 32)

[wta_64, wtb_64, wtdiff_64] = stochasticTrend(bar_source, n1, n2, 64)

[wta_128, wtb_128, wtdiff_128] = stochasticTrend(bar_source, n1, n2, 128)

  

/// Scan for embeddings in higher timeframes

overbought_2 = wta_2 > obEmbedLevel and wtdiff_2 > crossSeparation

overbought_4 = wta_4 > obEmbedLevel and wtdiff_4 > crossSeparation

overbought_8 = wta_8 > obEmbedLevel and wtdiff_8 > crossSeparation

overbought_16 = wta_16 > obEmbedLevel and wtdiff_16 > crossSeparation

overbought_32 = wta_32 > obEmbedLevel and wtdiff_32 > crossSeparation

overbought_64 = wta_64 > obEmbedLevel and wtdiff_64 > crossSeparation

oversold_2 = wta_2 < osEmbedLevel and wtdiff_2 < -crossSeparation

oversold_4 = wta_4 < osEmbedLevel and wtdiff_4 < -crossSeparation

oversold_8 = wta_8 < osEmbedLevel and wtdiff_8 < -crossSeparation

oversold_16 = wta_16 < osEmbedLevel and wtdiff_16 < -crossSeparation

oversold_32 = wta_32 < osEmbedLevel and wtdiff_32 < -crossSeparation

oversold_64 = wta_64 < osEmbedLevel and wtdiff_64 < -crossSeparation

  

/// Evaluation logic for overbought or oversold

highest_overbought = overbought_64 ? 6 : overbought_32 ? 5 : overbought_16 ? 4 : overbought_8 ? 3 : overbought_4 ? 2 : overbought_2 ? 1 : 0

highest_oversold = oversold_64 ? 6 : oversold_32 ? 5 : oversold_16 ? 4 : oversold_8 ? 3 : oversold_4 ? 2 : oversold_2 ? 1 : 0

  

/// Set color properties for ribbons

color_extremeSell = #f72585

color_sell = #b5179e  

color_midSell = #7209b7  

color_weakSell = #560bad  

color_neutralSell = #480ca8

color_underMidSell = #3a0ca3

color_underSell = #3f37c9

color_underExtremeSell = #4361ee

color_extremeBuy = #d8f3dc

color_buy = #b7e4c7

color_midBuy = #95d5b2

color_weakBuy = #74c69d  

color_neutralBuy = #52b788  

color_underMidBuy = #40916c

color_underBuy = #2d6a4f  

color_underExtremeBuy = #1b4332

  

/// Evaluation logic for ribbon colors

wtColor(a, b) =>

    na(a) ? color.blue : a < b ? a >= obExtremeLevel ? color_extremeSell : a >= obLevel ? color_sell : a >= obMildLevel ? color_midSell : a >= 0 ? color_weakSell : a >= osMildLevel ? color_neutralSell : a >= osLevel ? color_underMidSell : a >= osExtremeLevel ? color_underSell : color_underExtremeSell : a <= osExtremeLevel ? color_extremeBuy : a <= osLevel ? color_buy : a <= osMildLevel ? color_midBuy : a <= 0 ? color_weakBuy : a <= obMildLevel ? color_neutralBuy : a <= obLevel ? color_underMidBuy : a <= obExtremeLevel ? color_underBuy : color_underExtremeBuy

wt_color1 = wtColor(wta_1, wtb_1)

wt_color2 = wtColor(wta_2, wtb_2)

wt_color4 = wtColor(wta_4, wtb_4)

wt_color8 = wtColor(wta_8, wtb_8)

wt_color16 = wtColor(wta_16, wtb_16)

wt_color32 = wtColor(wta_32, wtb_32)

wt_color64 = wtColor(wta_64, wtb_64)

wt_color128 = wtColor(wta_128, wtb_128)

  

/// Evaluation logic for block Colors

wtBlockColor(layer_2exponent, a, b, a_x2, b_x2, highest_overbought_layer, highest_oversold_layer, wt_color) =>

    a < b and (a_x2 > obExtremeLevel and a_x2 > b_x2 or layer_2exponent <= highest_overbought_layer - 1) or a > b and (a_x2 < osExtremeLevel and a_x2 < b_x2 or layer_2exponent <= highest_oversold_layer - 1) ? color.white : wt_color

wt_block1 = wtBlockColor(0, wta_1, wtb_1, wta_2, wtb_2, highest_overbought, highest_oversold, wt_color1)

wt_block2 = wtBlockColor(1, wta_2, wtb_2, wta_4, wtb_4, highest_overbought, highest_oversold, wt_color2)

wt_block4 = wtBlockColor(2, wta_4, wtb_4, wta_8, wtb_8, highest_overbought, highest_oversold, wt_color4)

wt_block8 = wtBlockColor(3, wta_8, wtb_8, wta_16, wtb_16, highest_overbought, highest_oversold, wt_color8)

wt_block16 = wtBlockColor(4, wta_16, wtb_16, wta_32, wtb_32, highest_overbought, highest_oversold, wt_color16)

wt_block32 = wtBlockColor(5, wta_32, wtb_32, wta_64, wtb_64, highest_overbought, highest_oversold, wt_color32)

wt_block64 = wtBlockColor(6, wta_64, wtb_64, wta_128, wtb_128, highest_overbought, highest_oversold, wt_color64)

wt_block128 = wt_color128

  

/// Factory for plotting ribbons based on prior logic

hline(8 * ribbonLineWidth, color=color.blue)

plot(-ribbonLineWidth, color=wt_color1, style=plot.style_line, title='WT1', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 2, color=wt_block1, style=plot.style_line, title='WT1', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 3, color=wt_color2, style=plot.style_line, title='WT2', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 4, color=wt_block2, style=plot.style_line, title='WT2', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 5, color=wt_color4, style=plot.style_line, title='WT4', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 6, color=wt_block4, style=plot.style_line, title='WT4', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 7, color=wt_color8, style=plot.style_line, title='WT8', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 8, color=wt_block8, style=plot.style_line, title='WT8', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 9, color=wt_color16, style=plot.style_line, title='WT16', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 10, color=wt_block16, style=plot.style_line, title='WT16', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 11, color=wt_color32, style=plot.style_line, title='WT32', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 12, color=wt_block32, style=plot.style_line, title='WT32', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 13, color=wt_color64, style=plot.style_line, title='WT64', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 14, color=wt_block64, style=plot.style_line, title='WT64', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 15, color=wt_color128, style=plot.style_line, title='WT128', linewidth=ribbonLineWidth)

plot(-ribbonLineWidth * 16, color=wt_block128, style=plot.style_line, title='WT128', linewidth=ribbonLineWidth)

  

/// Evaluation logic for 1D WT

a = array.new_color()

wta_1_1D = request.security(syminfo.tickerid, '1D', wta_1)

wtb_1_1D = request.security(syminfo.tickerid, '1D', wtb_1)

array.push(a, request.security(syminfo.tickerid, '1D', wt_color1[0]))

array.push(a, request.security(syminfo.tickerid, '1D', wt_color1[1]))

array.push(a, request.security(syminfo.tickerid, '1D', wt_color1[2]))

array.push(a, request.security(syminfo.tickerid, '1D', wt_color1[3]))

array.push(a, request.security(syminfo.tickerid, '1D', wt_color1[4]))

array.push(a, request.security(syminfo.tickerid, '1D', wt_color1[5]))

array.push(a, request.security(syminfo.tickerid, '1D', wt_color1[6]))

recent_sig_x_1D = false

int i = 0

while i < array.size(a)

    if (array.get(a, i) == color_extremeBuy or array.get(a, i) == color_buy or array.get(a, i) == color_extremeSell or array.get(a, i) == color_sell)

        recent_sig_x_1D := true

    i += 1

wt1_1D_state = ""

if (wta_1_1D > wtb_1_1D)

    if (recent_sig_x_1D == true) and wta_1_1D <= -75

        wt1_1D_state := "A+ long"

    else if wta_1_1D <= -75

        wt1_1D_state := "A long"

    else if (recent_sig_x_1D == true) and wta_1_1D <= -50

        wt1_1D_state := "B+ long"

    else if wta_1_1D <= -50

        wt1_1D_state := "B long"

    else if wta_1_1D <= 0

        wt1_1D_state := "C long"

    else if wta_1_1D > 0

        wt1_1D_state := "D long"

else if (wta_1_1D <= wtb_1_1D)

    if (recent_sig_x_1D == true) and wta_1_1D >= 75

        wt1_1D_state := "A+ short"

    else if wta_1_1D >= 75

        wt1_1D_state := "A short"

    else if (recent_sig_x_1D == true) and wta_1_1D >= 50

        wt1_1D_state := "B+ short"

    else if wta_1_1D >= 50

        wt1_1D_state := "B short"

    else if wta_1_1D >= 0

        wt1_1D_state := "C short"

    else if wta_1_1D < 0

        wt1_1D_state := "D short"

  

/// Evaluation logic for 1W WT

b = array.new_color()

wta_1_1W = request.security(syminfo.tickerid, '1W', wta_1)

wtb_1_1W = request.security(syminfo.tickerid, '1W', wtb_1)

array.push(b, request.security(syminfo.tickerid, '1W', wt_color1[0]))

array.push(b, request.security(syminfo.tickerid, '1W', wt_color1[1]))

array.push(b, request.security(syminfo.tickerid, '1W', wt_color1[2]))

array.push(b, request.security(syminfo.tickerid, '1W', wt_color1[3]))

array.push(b, request.security(syminfo.tickerid, '1W', wt_color1[4]))

array.push(b, request.security(syminfo.tickerid, '1W', wt_color1[5]))

array.push(b, request.security(syminfo.tickerid, '1W', wt_color1[6]))

recent_sig_x_1W = false

i:=0

while i < array.size(b)

    if (array.get(b, i) == color_extremeBuy or array.get(b, i) == color_buy or array.get(b, i) == color_extremeSell or array.get(b, i) == color_sell)

        recent_sig_x_1W := true

    i += 1

wt1_1W_state = ""

if (wta_1_1W > wtb_1_1W)

    if (recent_sig_x_1W == true) and wta_1_1W <= -75

        wt1_1W_state := "A+ long"

    else if wta_1_1W <= -50

        wt1_1W_state := "A long"

    else if (recent_sig_x_1W == true) and wta_1_1W <= -50

        wt1_1W_state := "B+ long"

    else if wta_1_1W <= -50

        wt1_1W_state := "B long"

    else if wta_1_1W <= 0

        wt1_1W_state := "C long"

    else if wta_1_1W > 0

        wt1_1W_state := "D long"

else if (wta_1_1W <= wtb_1_1W)

    if (recent_sig_x_1W == true) and wta_1_1W >= 75

        wt1_1W_state := "A+ short"

    else if wta_1_1W >= 75

        wt1_1W_state := "A short"

    else if (recent_sig_x_1W == true) and wta_1_1W >= 50

        wt1_1W_state := "B+ short"

    else if wta_1_1W >= 50

        wt1_1W_state := "B short"

    else if wta_1_1W >= 0

        wt1_1W_state := "C short"

    else if wta_1_1W < 0

        wt1_1W_state := "D short"

  

/// Calculate WT state for the 1D and 1W

EP_1D_1W_long = timeframe.period == '60' and ((wt1_1D_state == 'A+ long' or wt1_1D_state == 'A long' or wt1_1D_state == 'B+ long' or wt1_1D_state == 'B long') and (wt1_1W_state == 'A+ long' or wt1_1W_state == 'A long' or wt1_1W_state == 'B+ long' or wt1_1W_state == 'B long'))

EP_1D_1W_short = timeframe.period == '60' and ((wt1_1D_state == 'A+ short' or wt1_1D_state == 'A short' or wt1_1D_state == 'B+ short' or wt1_1D_state == 'B short') and (wt1_1W_state == 'A+ short' or wt1_1W_state == 'A short' or wt1_1W_state == 'B+ short' or wt1_1W_state == 'B short'))

  

/// Get the present time frame, then increase it using these factors, 2x, 4x, and 6x

present_time_frame = str.tonumber(timeframe.period)

present_time_frame_2 = present_time_frame * 2

present_time_frame_4 = present_time_frame * 4

present_time_frame_6 = present_time_frame * 6

present_time_frame_2_string = str.tostring(present_time_frame_2)

present_time_frame_4_string = str.tostring(present_time_frame_4)

present_time_frame_6_string = str.tostring(present_time_frame_6)

  

/// Reformulate HTF

wta_256 = request.security(syminfo.tickerid, present_time_frame_2_string, wta_128[0])

wtb_256 = request.security(syminfo.tickerid, present_time_frame_2_string, wtb_128[0])

wta_512 = request.security(syminfo.tickerid, present_time_frame_4_string, wta_128[0])

wtb_512 = request.security(syminfo.tickerid, present_time_frame_4_string, wtb_128[0])

wta_768 = request.security(syminfo.tickerid, present_time_frame_6_string, wta_128[0])

wtb_768 = request.security(syminfo.tickerid, present_time_frame_6_string, wtb_128[0])

  

/// Evaluation logic for sandwich pattern longs (active timeframe)

sandwich_pattern_long = (((wta_1 > wtb_1 and wta_1 <= -21) and (wta_2 > wtb_2 and wta_2 <= -50) and (wta_4 > wtb_4 and wta_4 <= -50)) and ((wta_64 > wtb_64 and wta_64 <= 21) and (wta_128 > wtb_128 and wta_128 <= 21)))

  

/// Evaluation logic for sandwich pattern shorts (active timeframe)

sandwich_pattern_short = (((wta_1 < wtb_1 and wta_1 >= 21) and (wta_2 < wtb_2 and wta_2 >= 50) and (wta_4 < wtb_4 and wta_4 >= 50)) and ((wta_64 < wtb_64 and wta_64 >= -21) and (wta_128 < wtb_128 and wta_128 >= -21)))

  

/// Evaluation logic for sandwich pattern longs (active timeframe increased 2x)

sandwich_pattern_long_htf_x_2 = (((wta_2 > wtb_2 and wta_2 <= -21) and (wta_4 > wtb_4 and wta_4 <= -50) and (wta_8 > wtb_8 and wta_8 <= -50)) and ((wta_128 > wtb_128 and wta_128 <= 21) and (wta_256 > wtb_256 and wta_256 <= 21)))

  

/// Evaluation logic for sandwich pattern shorts (active timeframe increased 2x)

sandwich_pattern_short_htf_x_2 = (((wta_2 < wtb_2 and wta_2 >= 21) and (wta_4 < wtb_4 and wta_4 >= 50) and (wta_8 < wtb_8 and wta_8 >= 50)) and ((wta_128 < wtb_128 and wta_128 >= -21) and (wta_256 < wtb_256 and wta_256 >= -21)))

  

/// Evaluation logic for sandwich pattern longs (active timeframe increased 4x)

sandwich_pattern_long_htf_x_4 = (((wta_4 > wtb_4 and wta_4 <= -21) and (wta_8 > wtb_8 and wta_8 <= -50) and (wta_16 > wtb_16 and wta_16 <= -50)) and ((wta_256 > wtb_256 and wta_256 <= 21) and (wta_512 > wtb_512 and wta_512 <= 21)))

  

/// Evaluation logic for sandwich pattern short (active timeframe increased 4x)

sandwich_pattern_short_htf_x_4 = (((wta_4 < wtb_4 and wta_4 >= 21) and (wta_8 < wtb_8 and wta_8 >= 50) and (wta_16 < wtb_16 and wta_16 >= 50)) and ((wta_256 < wtb_256 and wta_256 >= -21) and (wta_512 < wtb_512 and wta_512 >= -21)))

  

/// Setup signals for Sandwiches

/// Setup signals for Sandwiches 2x

/// Setup signals for Sandwiches 4x

/// Setup signals for 1D & 1W EP setups

/// Setup signals for present timeframe. Sandwich pattern long & Sandwich pattern short

if sandwich_pattern_long

    alert(message='{"PATTERN": "sandwich [TIGHT]",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + timeframe.period + '",\n"BIAS": "long",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#00db91, 0), style = line.style_solid, width = 3)

if sandwich_pattern_short

    alert(message='{"PATTERN": "sandwich [TIGHT]",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + timeframe.period + '",\n"BIAS": "short",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#e10053, 0), style = line.style_solid, width = 3)

  

/// Setup signals for present timeframe adjusted 2x. Sandwich pattern long & Sandwich pattern short

if sandwich_pattern_long_htf_x_2

    alert(message='{"PATTERN": "sandwich [TIGHT]",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + str.tostring(present_time_frame_2) + '",\n"BIAS": "long",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#00db91, 0), style = line.style_solid, width = 3)

if sandwich_pattern_short_htf_x_2

    alert(message='{"PATTERN": "sandwich [TIGHT]",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + str.tostring(present_time_frame_2) + '",\n"BIAS": "short",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#e10053, 0), style = line.style_solid, width = 3)

  

/// Setup signals for present timeframe adjusted 4x. Sandwich pattern long & Sandwich pattern short

if sandwich_pattern_long_htf_x_4

    alert(message='{"PATTERN": "sandwich [TIGHT]",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + str.tostring(present_time_frame_4) + '",\n"BIAS": "long",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#00db91, 0), style = line.style_solid, width = 3)

if sandwich_pattern_short_htf_x_4

    alert(message='{"PATTERN": "sandwich [TIGHT]",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + str.tostring(present_time_frame_4) + '",\n"BIAS": "short",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#e10053, 0), style = line.style_solid, width = 3)

  

/// Setup signals for 1D & 1W EP setups

if EP_1D_1W_long

    alert(message='{"PATTERN": "ep - 1D & 1W are aligned setup",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + timeframe.period + '",\n"BIAS": "long",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)    

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#ffa603, 0), style = line.style_solid, width = 3)

else if EP_1D_1W_short

    alert(message='{"PATTERN": "ep - 1D & 1W are aligned setup",\n"TICKER": "' + syminfo.ticker + '",\n"TIME FRAME": "' + timeframe.period + '",\n"BIAS": "short",\n"1D WT": "' + wt1_1D_state + '",\n"1W WT": "' + wt1_1W_state + '"}', freq=alert.freq_once_per_bar)

    line.new(bar_index, 0, bar_index, -80, extend = extend.none, color = color.new(#ffa603, 0), style = line.style_solid, width = 3)
```