import  '../css/font-awesome.min.css';
import '../css/main.sass';
var  render_exchange_price_chart = require('../js/dapps/dapps_detail_page/exchange_price_charts.js');

class app{
    constructor(){
        console.log('this is a es6 class');
        this.say_hello('hello');
        render_exchange_price_chart();
    }

    say_hello(message) {
        console.log('hello');

    }
}

new app();

