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
            <div class="AccountPage">
                <AccountSummary account={account} switchView={this.props.switchView}/>

                <div class="mt5 fr w-50 h-50">
                    <button class="f3 br0 ph3 pv0 mb4 db h-25 w-80 white bg-purple"
                            onClick={() => this.props.switchView('buycardpage', account)}>
                        <i class="far fa-credit-card pr2"></i>Buy Card 
                    </button>
                    <button class="f3 br0 ph3 pv1 mb4 db h-25 w-80 white bg-purple"
                            onClick={() => this.props.switchView('buymealpage', account)}>
                        <i class="fas fa-utensils pr2"></i>Buy Meal
                    </button>
                    <button class="f3 br0 ph3 pv1 mb0 db h-25 w-80 white bg-green"
                            onClick={() => this.props.switchView('addcreditpage', account)}>
                        <i class="fas fa-plus pr2"></i>Add Credit
                    </button>
                </div>
            </div>
         );
    }
}

export default AccountPage;
