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
             
         });
    }
    render () {
        const {
            account,
            pendingTransaction
        } = this.props;
        console.log('pendingTransaction', pendingTransaction);
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
                    <form>
                        <label class="f3 b dib tr">Customer Initials:</label>
                        <input id="initials"
                        class="ml2 pa2 f4 w-60 input-reset ba bg-transparent hover-bg-light-gray"
                        type="string"
                        // value={this.state.amount}
                        placeholder={"Enter your initials"}
                        // onChange={(event) => this.onAmountChange(event.target.value)} 
                        />
                    </form>
                    
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
