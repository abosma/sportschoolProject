import pygal

def createGraph(data1, data2, data3, data4, data5):
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