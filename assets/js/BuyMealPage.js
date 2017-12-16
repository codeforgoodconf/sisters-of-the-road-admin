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
         axios.post('/account/'+ account.id + '/buy_meal', {amount: amount}).then(function(response) {
            if (response.data && response.data.result === 'ok') {
            updateBalance(amount * -1);
            switchView('confirmationpage', account);
            } else if (response.data && response.data.result === 'limit_error'){
            console.log('balance can\'t go below $0');
            document.getElementById('error-msg').innerHTML="Balance can't go below $0";
            } else if (response.data && response.data.result === 'input_error'){
                console.log('amount can\'t be negative')
                document.getElementById('error-msg').innerHTML="Amount cannot be negative";
            } else {
                // the account ID was not found - what to do?
                console.log('no account!');
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
            <div class="BuyMealPage">
                <div class="header col-sm-12 centered">
                    <h3>{account.name}</h3>
                    <h5>Last worked: {account.lastCredit}</h5>
                    <h5>Last purchase: {account.lastMeal}</h5>
                </div>
                <div id="calculate" class="jumbotron row center-block">
                    <div class="total">
                        <h3>
                            Current Barter Credits: ${(account.currentCredit / 100).toFixed(2)}
                            <span class="pull-right" id="error-msg" style="color: red"></span>
                        </h3>
                        <h3 class="text-center">Meal Total:</h3>
                        <DollarInput updateAmount={(amount) => this.updateAmount(amount)} /> 
                    </div>
                </div>
                <div>
                    <button class="btn btn-success col-sm-offset-5 center-block"
                            onClick={() => this.buyMeal(account)}>
                        Spend amount
                    </button>
                </div>
                <button class="btn btn-info col-sm-offset-5 center-block"
                        onClick={() => this.props.switchView('accountpage', account)}>
                    Cancel
                </button>
            </div>
         );
    }
}

export default BuyMealPage;
