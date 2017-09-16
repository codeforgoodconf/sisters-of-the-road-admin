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
            <div className="AccountPage">
                <div className="header col-sm-12 centered">
                    <h1>{account.name}</h1>
                    <h3>Last worked: {account.lastCredit}</h3>
                    <h3>Last purchase: {account.lastMeal}</h3>
                </div>
                <div id="credits" className="centered">
                    Barter Credits: ${(account.currentCredit / 100).toFixed(2)}
                </div>
                <div className="buttons row center-block">
                    <button className="btn btn-info col-sm-offset-1"
                            onClick={() => this.props.switchView('buymealpage', account)}>
                        Buy Meal
                    </button>
                    <button className="btn btn-success col-sm-offset-1"
                            onClick={() => this.props.switchView('addcreditpage', account)}>
                        Add Credit
                    </button>
                </div>
                <div className="text-center row"
                    onClick={() => this.props.switchView('searchpage')}>
                    <button className="btn btn-lg btn-danger col-sm-offset-5 center-block">Back to Search</button>
                </div>
            </div>
         );
    }
}

export default AccountPage;
