import React, { Component } from 'react';
import AccountSummary from './AccountSummary';


class ReviewPage extends Component {
    constructor () {
        super();
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
                switchView('reviewpage', account);
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
    render () {
        const {
            account,
            pendingTransaction
        } = this.props;
       console.log(pendingTransaction, typeof(pendingTransaction))
        return (
            <div class="ReviewPage">
                <AccountSummary account={account} switchView={this.props.switchView} />
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <div class="total"><p class='f1'>Review Your Order</p>
                        {pendingTransaction > 0 &&
                            <h2 class="tl">Amount to add: ${(pendingTransaction).toFixed(2)}</h2>
                        }
                        {pendingTransaction == 0 &&
                            <h2 class="tl">Amount is zero!</h2>
                        }
                        {pendingTransaction < 0 &&
                            <h2 class="tl">Amount to spend: ${(pendingTransaction * -1).toFixed(2)}</h2>
                        }

                        <h2 class="tl">New balance: ${((account.currentCredit / 100) + pendingTransaction).toFixed(2)}</h2>
                    </div>
                </div>
                <div class="mt5 fr w-50 h-50">
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={() => this.props.switchView('accountpage', account)}>
                        <i class="fas fa-times pr2"></i>Cancel
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-green"
                            onClick={() => this.props.switchView('confirmationpage', account)}>
                        <i class="fas fa-plus pr2"></i>Confirm
                    </button>
                </div>
            </div>
         );
    }
}

export default ReviewPage;
