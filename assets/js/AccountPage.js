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
                <div class="header col-sm-12 centered">
                    <h1>{account.name}</h1>
                    <h3>Last worked: {account.lastCredit}</h3>
                    <h3>Last purchase: {account.lastMeal}</h3>
                </div>
                <div id="credits" class="centered">
                    Barter Credits: ${(account.currentCredit / 100).toFixed(2)}
                </div>
                <div class="buttons row center-block">
                    <button class="btn btn-info col-sm-offset-1"
                            onClick={() => this.props.switchView('buymealpage', account)}>
                        Buy Meal
                    </button>
                    <button class="btn btn-success col-sm-offset-1"
                            onClick={() => this.props.switchView('addcreditpage', account)}>
                        Add Credit
                    </button>
                </div>
                <div class="text-center row"
                    onClick={() => this.props.switchView('searchpage')}>
                    <button class="btn btn-lg btn-danger col-sm-offset-5 center-block">Back to Search</button>
                </div>
            </div>
         );
    }
}

export default AccountPage;
