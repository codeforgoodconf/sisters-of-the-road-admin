import React, { Component } from 'react';
import AccountSummary from './AccountSummary';


class ReviewPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            account
        } = this.props;

        return (
            <div class="ReviewPage">
                <AccountSummary account={account} switchView={this.props.switchView}/>
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <div class="total"><p class='f1'>Review Your Order</p>
                        {account.lastAdded > 0 &&
                            <h2 class="tl">Amount to add: ${(account.lastAdded / 100).toFixed(2)}</h2>
                        }
                        {account.lastAdded < 0 &&
                            <h2 class="tl">Amount to spend: ${((account.lastAdded * -1) / 100).toFixed(2)}</h2>
                        }

                        <h2 class="tl">New balance: ${(account.currentCredit / 100).toFixed(2)}</h2>
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
