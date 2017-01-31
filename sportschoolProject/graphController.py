import pygal

def createLineGraph(data1, data2, data3, data4, data5):
    '''Maakt een .svg grafiek bestand
    data1 = List object met alle data
    data2 = List object met alle data
    data3 = List object met alle data
    data4 = List object met alle data
    data5 = List object met alle data'''
    custom_style = pygal.style.Style(
                    background="#2C2230",
                    plot_background="#3F3145",
                    foreground = 'rgba(255, 255, 255, 0.9)',
                    foreground_strong = 'rgba(255, 255, 255, 0.9)',
                    foreground_subtle = 'rgba(255, 255 , 255, 0.5)',
                    colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'),
                    font_family='googlefont:Rubik')

    bar_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=custom_style)
    bar_chart.add('A', data1)
    bar_chart.add('B', data2)
    bar_chart.add('C', data3)
    bar_chart.add('D', data4)
    bar_chart.add('E', data5)
    bar_chart.render_to_file("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/charts/chart.svg")

def createUserDataGraph(UREN1, UREN2, UREN3, UREN4, UREN5, CAL1, CAL2, CAL3, CAL4, CAL5):
    '''Maakt een .svg grafiek bestand
    data1 = List object met alle data
    data2 = List object met alle data
    data3 = List object met alle data
    data4 = List object met alle data
    data5 = List object met alle data'''
    totaleUren = UREN1 + UREN2 + UREN3 + UREN4 + UREN5
    totaleCalorieen = CAL1 + CAL2 + CAL3 + CAL4 + CAL5
    custom_style = pygal.style.Style(
        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'),
        font_family='googlefont:Rubik')
    gauge = pygal.SolidGauge(
        half_pie=True, inner_radius=0.50,
        style=custom_style)
    if totaleUren is not 0 and totaleCalorieen is not 0:
        gauge.add('Uren Gesport', [{'value': totaleUren, 'max_value': totaleUren}])
        gauge.add('Crosstrainer', [{'value': UREN1, 'max_value': totaleUren}])
        gauge.add('Hometrainer', [{'value': UREN2, 'max_value': totaleUren}])
        gauge.add('Loopband', [{'value': UREN3, 'max_value': totaleUren}])
        gauge.add('Roeitrainer', [{'value': UREN4, 'max_value': totaleUren}])
        gauge.add('Krachtstation', [{'value': UREN5, 'max_value': totaleUren}])
        gauge.add('Totale Calorieen', [{'value': totaleCalorieen, 'max_value': totaleCalorieen}])
        gauge.add('Crosstrainer', [{'value': CAL1, 'max_value': totaleCalorieen}])
        gauge.add('Hometrainer', [{'value': CAL2, 'max_value': totaleCalorieen}])
        gauge.add('Loopband', [{'value': CAL3, 'max_value': totaleCalorieen}])
        gauge.add('Roeitrainer', [{'value': CAL4, 'max_value': totaleCalorieen}])
        gauge.add('Krachtstation', [{'value': CAL5, 'max_value': totaleCalorieen}])
    else:
        gauge.add('Uren Gesport', [{'value': totaleUren}])
        gauge.add('Crosstrainer', [{'value': UREN1}])
        gauge.add('Hometrainer', [{'value': UREN2}])
        gauge.add('Loopband', [{'value': UREN3}])
        gauge.add('Roeitrainer', [{'value': UREN4}])
        gauge.add('Krachtstation', [{'value': UREN5}])
        gauge.add('Totale Calorieen', [{'value': totaleCalorieen}])
        gauge.add('Crosstrainer', [{'value': CAL1}])
        gauge.add('Hometrainer', [{'value': CAL2}])
        gauge.add('Loopband', [{'value': CAL3}])
        gauge.add('Roeitrainer', [{'value': CAL4}])
        gauge.add('Krachtstation', [{'value': CAL5}])
    gauge.render_to_file("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/charts/chart.svg")

def createAdminDataGraph(TOTAAL, KLANTENAMSTERDAM, KLANTENUTRECHT, KLANTENDENHAAG, KLANTENLELYSTAD, KLANTENAMERSFOORT):
    '''Maakt een .svg grafiek bestand
    data1 = List object met alle data
    data2 = List object met alle data
    data3 = List object met alle data
    data4 = List object met alle data
    data5 = List object met alle data'''
    custom_style = pygal.style.Style(
        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'),
        font_family='googlefont:Rubik')
    gauge = pygal.SolidGauge(
        half_pie=True, inner_radius=0.50,
        style=custom_style)
    gauge.add('Totaal', [{'value': TOTAAL, 'max_value': TOTAAL}])
    gauge.add('Amsterdam', [{'value': KLANTENAMSTERDAM, 'max_value': TOTAAL}])
    gauge.add('Utrecht', [{'value': KLANTENUTRECHT, 'max_value': TOTAAL}])
    gauge.add('Den Haag', [{'value': KLANTENDENHAAG, 'max_value': TOTAAL}])
    gauge.add('Lelystad', [{'value': KLANTENLELYSTAD, 'max_value': TOTAAL}])
    gauge.add('Amersfoort', [{'value': KLANTENAMERSFOORT, 'max_value': TOTAAL}])
    gauge.render_to_file("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/charts/adminChart.svg")