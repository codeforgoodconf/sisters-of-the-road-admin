import React, { Component } from 'react';
import AccountSummary from './AccountSummary';


class ConfirmationPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            account
        } = this.props;

        return (
            <div class="ConfirmationPage">
                <AccountSummary account={account} switchView={this.props.switchView}/>
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <div class="total"><p class='f1'>Changes Saved!</p>
                        {account.lastAdded > 0 &&
                            <h2 class="tl">Amount added: ${account.lastAdded.toFixed(2)}</h2>
                        }
                        {account.lastAdded < 0 &&
                            <h2 class="tl">Amount spent: ${(account.lastAdded * -1).toFixed(2)}</h2>
                        }

                        <h2 class="tl">New balance: ${account.currentCredit.toFixed(2)}</h2>
                    </div>
                </div>
                <div class="mt5 fr w-50 h-50">
                    <button class="f3 br0 ph3 pv0 mb4 db h-25 w-80 white bg-purple"
                            onClick={() => this.props.switchView('accountpage', account)}>
                        <i class="far pr2"></i>Back to Account Summary 
                    </button>
                </div>
            </div>
         );
    }
}

export default ConfirmationPage;
