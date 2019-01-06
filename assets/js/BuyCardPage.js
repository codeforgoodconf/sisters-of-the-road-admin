import React, {Component} from 'react';
import axios from 'axios';
import DollarInput from './DollarInput';
import AccountSummary from './AccountSummary';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


class BuyCardPage extends Component {
    constructor() {
        super();
        this.state = {
            amount: ''
        };
    }

    buyCard(account) {
        const {
            updateBalance,
            switchView
        } = this.props;
        let amount = Number(this.state.amount);
        axios.post(
            '/accounts/' + account.id + '/buy_card',
            {amount: amount}
        ).then(response => {
            console.log(response);
            updateBalance(-amount);
            switchView('confirmationpage', account);
        }).catch(error => {
            console.log(error.response);
            if (error.response.data.result === 'limit_error') {
                console.log(error.response.data.message);
                document.getElementById('error-msg').innerHTML = "Balance can't go below $0.00";
            } else if (error.response.data.result === 'input_error') {
                console.log(error.response.data.message);
                document.getElementById('error-msg').innerHTML =
                    "Please enter an amount above $0 in increment of $.25";
            } else if (error.response.status === 404) {
                console.log('Account not found');
                document.getElementById('error-msg').innerHTML = "That user account was not found"
            }
        });
    }

    updateAmount(amount) {
        this.setState({amount: amount});
    }

    render() {
        const {
            account
        } = this.props;

        return (
            <div class="BuyCardPage">
                <AccountSummary account={account} switchView={this.props.switchView}/>
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <h1>Buy Card</h1>
                    <DollarInput updateAmount={(amount) => this.updateAmount(amount)}/>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                            onClick={() => this.props.switchView('accountpage', account)}>
                        <i class="fas fa-times pr2"></i>Cancel
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-purple"
                            onClick={() => this.buyCard(account)}>
                        <i class="fas fa-minus pr2"></i>
                        Spend amount
                    </button>
                </div>
            </div>
        );
    }
}

export default BuyCardPage;
