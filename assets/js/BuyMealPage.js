import React, { Component } from 'react';
import axios from 'axios';
import DollarInput from './DollarInput'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


class BuyMealPage extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
    }

    buyMeal (account) {
        const {
            updateBalance,
            switchView
         } = this.props;
         let amount = Number(this.state.amount) * 100;
         axios.post('/account/'+ account.id + '/subtract', {amount: amount}).then(function(response) {
             if (response.data && response.data.result === 'ok') {
                updateBalance(amount * -1);
                switchView('confirmationpage', account);
             } else {
                 // the account ID was not found - what to do?
                 console.log('no account!')
             }
         });
    }

    updateAmount (amount) {
        this.setState({amount: amount});
    }

    render () {
        const {
            account
        } = this.props;

        return (
            <div className="BuyMealPage">
                <div className="header col-sm-12 centered">
                    <h1>{account.name}</h1>
                    <h3>Last worked: {account.lastCredit}</h3>
                    <h3>Last purchase: {account.lastMeal}</h3>                      
                </div>
                
                <div id="calculate" className="jumbotron row center-block">
                    <div className="total" className="text-center">
                        <h3>Current Barter Credits: ${(account.currentCredit / 100).toFixed(2)}</h3>
                        <h3>Meal Total:</h3>
                        <DollarInput updateAmount={(amount) => this.updateAmount(amount)} /> 
                    </div>
                </div>
                <div>
                    <button className="btn btn-success col-sm-offset-5 center-block"
                            onClick={() => this.buyMeal(account)}>
                        Spend amount
                    </button>
                </div>
                
                <button className="btn btn-info col-sm-offset-5 center-block"
                        onClick={() => this.props.switchView('accountpage', account)}>
                    Cancel
                </button>
                
            </div>
         );
    }
}

export default BuyMealPage;
