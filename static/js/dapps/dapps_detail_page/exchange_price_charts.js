var $ = require('jquery');
var Highcharts = require('highcharts/highstock');
function render_charts(){
        $.getJSON('https://data.jianshukeji.com/stock/history/000001', function (data) {
    if(data.code !== 1) {
        alert('读取数据失败！');
        return false;
    }
    data = data.data;

    Highcharts.each(data, function(d) {
        d.length = 2;
    });
    Highcharts.stockChart('bitfinex_price', {
        rangeSelector: {
            selected: 2
        },
        title: {
            text: 'BitFinex价格'
        },
        plotOptions: {
            series: {
                showInLegend: true
            }
        },
        tooltip: {
            split: false,
            shared: true
        },
        series: [{
            // type: 'line',
            id: '000001',
            name: 'btc',
            data: data
        }]
    });
});
}

module.exports =  render_charts;

