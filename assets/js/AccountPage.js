import React, { Component } from 'react';


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
                <div class="blue oswald pb4 fl w-50">
                    <h1 class='f1'>{account.name}</h1>
                    <span class='f2'> current balance:</span>
                    <span class='gray f2'>${(account.currentCredit / 100).toFixed(2)}</span>

                    <h3>Last worked: {account.lastCredit}</h3>
                    <h3>Last purchase: {account.lastMeal}</h3>
                </div>

                <div class="mv4 fr w-50">
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h4 w-30 white opensans bg-purple"
                            onClick={() => this.props.switchView('buycardpage', account)}>
                        Buy Card
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h4 w-30 white opensans bg-purple"
                            onClick={() => this.props.switchView('buymealpage', account)}>
                        Buy Meal
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h4 w-30 white opensans bg-green"
                            onClick={() => this.props.switchView('addcreditpage', account)}>
                        Add Credit
                    </button>
                </div>
                <div class=""
                    onClick={() => this.props.switchView('searchpage')}>
                    <button class="">Back to Search</button>
                </div>
            </div>
         );
    }
}

export default AccountPage;
