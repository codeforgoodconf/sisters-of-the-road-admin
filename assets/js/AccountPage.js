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
                <div className="header col-sm-6 centered">
                    <h1>{account.name}</h1>
                    <h5>Last worked: {account.lastWorked}</h5>
                    <h5>Last meal: {account.lastMeal}</h5>
                </div>
                <div id="credits" className="centered">
                    Barter Credits: ${account.currentCredit}
                </div>
                <div className="buttons row text-center">
                    <button className="btn btn-info col-sm-offset-2 centered"
                            onClick={() => this.props.switchView('buymealpage', account)}>
                        Buy Meal
                    </button>
                    <button className="btn btn-success col-sm-offset-2 centered"
                            onClick={() => this.props.switchView('addcreditpage', account)}>
                        Add Credit
                    </button>
                </div>
                <div className="text-center row"
                    onClick={() => this.props.switchView('searchpage')}>
                    <button className="btn btn-danger col-sm-2 col-sm-offset-5">Back to Search</button>
                </div>
            </div>
         );
    }
}

export default AccountPage;
