import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import os

script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, '..', 'Data', 'reviews.csv')
data = pd.read_csv(csv_path, parse_dates=["Timestamp"])
share = data.groupby(["Course Name"])["Rating"].count()



# Código conseguido de: https://www.highcharts.com/docs/chart-and-series-types/pie-chart
chart_def = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Número de ratings por curso'
    },
    plotOptions: {
        series: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'Nº de valoraciones:',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Nº de valoraciones:',
            colorByPoint: true,
            data: [
                {
                    name: 'Water',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.data = [{"name":v1, "y":v2} for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hc.data


    return wp

jp.justpy(app)