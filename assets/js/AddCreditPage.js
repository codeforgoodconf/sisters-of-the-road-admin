import React, { Component } from 'react';
import axios from 'axios';
import DollarInput from './DollarInput';
import AccountSummary from './AccountSummary';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


class AddCreditPage extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
    }

    validateAmount(amount) {
        const currentCredit = this.props.account.currentCredit; // amount in cents, $8 = 800
        amount = Number(amount.value) * 100; // amount in cents
        if ((currentCredit + amount) > 5000) {
            console.log('balance can\'t exceed $50')
            document.getElementById('error-msg').innerHTML="Balance can't go above $50";
         } else if ( amount % 25 != 0){
            console.log('invalid amount')
            document.getElementById('error-msg').innerHTML=
                "Please enter an amount in increment of $.25";
         } else {
            this.props.updateTransactionAmount(amount/100);
            this.props.switchView('reviewpage', this.props.account);         
         }
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
                <AccountSummary account={account} switchView={this.props.switchView}/>
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <h1>Add Credit</h1>
                    <label class="fl f4 mt2 red" id="error-msg"></label> 
                    <DollarInput updateAmount={(amount) => this.updateAmount(amount)} />
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={() => this.props.switchView('accountpage', account)}>
                        <i class="fas fa-times pr2"></i>Cancel
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-green"
                            onClick={() => this.validateAmount(amount)}>
                        <i class="fas fa-plus pr2"></i>Continue
                    </button>
                </div>
            </div>
         );
    }
}

export default AddCreditPage;
