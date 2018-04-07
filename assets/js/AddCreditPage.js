import React, { Component } from 'react';
import axios from 'axios';
import DollarInput from './DollarInput';


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";



class AddCreditPage extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
    }

    addCredit (account) {
        const {
            updateBalance,
            switchView
         } = this.props;
         let amount = Number(this.state.amount) * 100;
         axios.post('/account/' + account.id + '/credit', {amount: amount}).then(function(response) {
             if (response.data && response.data.result === 'ok') {
                updateBalance(amount);
                switchView('confirmationpage', account);
             } else if (response.data && response.data.result === 'limit_error'){
                console.log('balance can\'t exceed $50')
                document.getElementById('error-msg').innerHTML="Balance can't go above $50";
             } else if (response.data && response.data.result === 'input_error'){
                console.log('invalid amount')
                document.getElementById('error-msg').innerHTML=
                    "Please enter an amount above $0 in increment of $.25";
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
            <div class="AddCreditPage">

                <div id="account-summary" class="blue oswald pb4 fl w-50">
                    <h1 class='f1'>{account.name}</h1>
                    <span class='f2'> current balance:</span>
                    <span class='gray f2'>${(account.currentCredit / 100).toFixed(2)}</span>

                    <h3>Last worked: {account.lastCredit}</h3>
                    <h3>Last purchase: {account.lastMeal}</h3>
                </div>

                <div id="calculate" class="fr w-50">
                    <div class="total">
                        <h3>
                            Current Barter Credits: ${(account.currentCredit / 100).toFixed(2)}
                            <span class="pull-right" id="error-msg" style="color: red"></span>
                        </h3>
                        <h3 class="tc">Amount to add:</h3>
                        <DollarInput updateAmount={(amount) => this.updateAmount(amount)} /> 
                    </div>
                    <button type="submit"
                            class="btn btn-success col-sm-offset-5 center-block"
                            onClick={() => this.addCredit(account)}>
                        Add amount
                    </button>
                </div>
                <div>
                    <button class=""
                            onClick={() => this.props.switchView('accountpage', account)}>
                        Cancel
                    </button>
                </div>
            </div>
         );
    }
}

export default AddCreditPage;
