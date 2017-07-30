import React, { Component } from 'react';
import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";



class AddCreditPage extends Component {
    constructor () {
        super();
    }

    addCredit (account, amount) {
        const {
            updateBalance,
            switchView
         } = this.props;
         amount = Number(amount);
         axios.post('/account/1/add', {amount: amount}).then(function(response) {
             if (response.data && response.data.result === 'ok') {
                updateBalance(amount);
                switchView('confirmationpage', account);
             } else {
                 // the account ID was not found - what to do?
                 console.log('no account!')
             }
         });
    }

    render () {
        const {
            account
        } = this.props;

        var amount;

        return (
            <div className="AddCreditPage">
                <div className="header col-sm-12 centered">
                    <h3>{account.name}</h3>
                    <h5>Last worked: {account.lastCredit}</h5>
                    <h5>Last meal: {account.lastMeal}</h5>
                </div>
                <div id="calculate" className="jumbotron row center-block">
                    <div className="total">
                        <h3 className="text-center">Amount to add:</h3>
                        <input id="amount"
                            className="numbers col-sm-offset-3 input-lg center-block text-center"
                            type="number"
                            min="0.00"
                            step="0.25"
                            max="2500"
                            onChange={(event) => amount = event.target.value} />
                    </div>
                </div>
                <div>
                    <button type="submit" className="btn btn-success col-sm-offset-5 center-block" onClick={() => this.addCredit(account, amount)}>
                        Add amount
                    </button>
                </div>
                <div>
                    <button className="btn btn-info col-sm-2 col-sm-offset-5" onClick={() => this.props.switchView('accountpage', account)}>
                        Cancel
                    </button>
                </div>
            </div>
         );
    }
}

export default AddCreditPage;
