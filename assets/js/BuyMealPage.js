import React, { Component } from 'react';
import axios from 'axios';
import DollarInput from './DollarInput'
import AccountSummary from './AccountSummary';

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
                document.getElementById('error-msg').innerHTML=
                    "Please enter an amount above $0 in increment of $.25";
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
                <AccountSummary account={account} switchView={this.props.switchView}/>

                <div id="calculate" class="fr w-50 mt5 ba bw2 pa2">
                    <div class="total dib">
                        <h1>Buy Meal</h1>
                        <h3> <span class="pull-right" id="error-msg" style="color: red"></span> </h3>
                        <h3 class="fl w-50">Meal Total:</h3>
                        <div class='fr w-50'>
                            <DollarInput updateAmount={(amount) => this.updateAmount(amount)} /> 
                        </div>
                    </div>
                    <div>
                        <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                            onClick={() => this.props.switchView('accountpage', account)}>
                            Cancel
                        </button>
                        <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-purple"
                            onClick={() => this.buyMeal(account)}>
                        Spend amount
                        </button>
                    </div>
                </div>

            </div>
         );
    }
}

export default BuyMealPage;
