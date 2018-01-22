import  '../css/font-awesome.min.css';
import '../css/main.sass';


class app{
    constructor(){
        console.log('this is a es6 class');
        this.say_hello('hello');
    }

    say_hello(message) {
        console.log('hello');

    }
}

new app();

