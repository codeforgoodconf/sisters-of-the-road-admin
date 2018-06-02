import React, { Component } from 'react';
import AccountSummary from './AccountSummary';


class AccountPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            account
        } = this.props;
        return (
            <div class="AccountPage pa4">
                <AccountSummary account={account} switchView={this.props.switchView}/>

                <div class="mv4 fr w-50">
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h4 w-30 white bg-purple"
                            onClick={() => this.props.switchView('buycardpage', account)}>
                        Buy Card
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h4 w-30 white bg-purple"
                            onClick={() => this.props.switchView('buymealpage', account)}>
                        Buy Meal
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h4 w-30 white bg-green"
                            onClick={() => this.props.switchView('addcreditpage', account)}>
                        Add Credit
                    </button>
                </div>
            </div>
         );
    }
}

export default AccountPage;
