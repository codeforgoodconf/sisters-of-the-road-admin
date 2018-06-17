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
                    <div class="total">
                        {account.lastAdded > 0 &&
                            <h2 class="tl">Amount added: ${(account.lastAdded / 100).toFixed(2)}</h2>
                        }
                        {account.lastAdded < 0 &&
                            <h2 class="tl">Amount spent: ${((account.lastAdded * -1) / 100).toFixed(2)}</h2>
                        }

                        <h2 class="tl">New balance: ${(account.currentCredit / 100).toFixed(2)}</h2>
                    </div>
                </div>
            </div>
         );
    }
}

export default ConfirmationPage;
